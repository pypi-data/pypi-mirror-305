import aiosqlite
from .model import Model
from .query import SelectQuery, WhereClause, LeftJoinClause, InnerJoinClause, UnionClause, InsertQuery, ReturningClause, LimitClause, OffsetClause, OrderByClause, UpdateQuery, SetClause
from .column import IntegerField, TextField, Everything, ForeignKeyField, Default, NotNull, PrimaryKey, Field, ColumnAttribute, Cascade
from .sqlfn import SQLExpr, COUNT, BinaryExpr, SQLBinaryOperator
from typing import Type, TypeVar

T = TypeVar('T', bound='Model')

class SQLiteDatabase:    
    database: aiosqlite.Connection
    models: dict[str, Model]

    @classmethod
    async def connect(cls, database, *args, **kwargs):
        db = cls()
        db.database = await aiosqlite.connect(database, *args, **kwargs)
        db.models = {}

        await db.database.execute("PRAGMA foreign_keys = ON;")

        return db
    
    def register_model(self, table_name=None):
        def inner(model_type: Type[T]) -> Type[T]:
            nonlocal table_name

            assert isinstance(model_type, type) and Model in model_type.__bases__, "Registered model is not a class or is not a subclass of Model"
            if table_name is None:
                table_name = model_type.__name__
            self.models[table_name] = model_type
            model_type.__registered__(self, table_name)
            return model_type
        return inner
    
    def register_models(self, *models):
        for model in models:
            self.register_model()(model)
    
    def _to_sql(self, obj):
        if obj is None:
            return "NULL"
        if isinstance(obj, str):
            self._sql_args.append(obj)
            return "?"
        if isinstance(obj, (str, int, float)):
            return str(obj)
        if isinstance(obj, LimitClause):
            return f" LIMIT {self._to_sql(obj.how_much)} "
        if isinstance(obj, OffsetClause):
            return f" OFFSET {self._to_sql(obj.how_much)} "
        if isinstance(obj, OrderByClause):
            return f" ORDER BY {', '.join(map(lambda x: self._to_sql(x[0]) + ' ' + x[1].upper(), obj.orders))} "
        if isinstance(obj, WhereClause):
            return f" WHERE {self._to_sql(obj.expr)} "
        if isinstance(obj, UnionClause):
            assert isinstance(obj.other, SelectQuery)
            return f" UNION {self._to_sql(obj.other)[1:-1]} "
        if isinstance(obj, LeftJoinClause):
            return f" LEFT JOIN {obj.on.__tablename__} ON {self._to_sql(obj.expr)} "
        if isinstance(obj, InnerJoinClause):
            return f" INNER JOIN {obj.on.__tablename__} ON {self._to_sql(obj.expr)} "
        if isinstance(obj, ReturningClause):
            return f" RETURNING {', '.join(map(self._to_sql, obj.columns))} "
        if isinstance(obj, Field):
            return f"{obj.table_name}.{obj.field_name}"
        if isinstance(obj, BinaryExpr):
            op = {
                SQLBinaryOperator.EQ: "=",
                SQLBinaryOperator.NEQ: "!=",
                SQLBinaryOperator.GT: ">",
                SQLBinaryOperator.GTE: ">=",
                SQLBinaryOperator.LT: "<",
                SQLBinaryOperator.LTE: "<=",

                SQLBinaryOperator.AND: "AND",
                SQLBinaryOperator.OR: "OR",

                SQLBinaryOperator.ADD: "+",
                SQLBinaryOperator.SUB: "-",
                SQLBinaryOperator.MUL: "*",
                SQLBinaryOperator.DIV: "/",
                SQLBinaryOperator.MOD: "%"
            }[obj.op]
            return f"{self._to_sql(obj.val1)} {op} {self._to_sql(obj.val2)}"
        if isinstance(obj, Cascade):
            return f"CASCADE"
        if isinstance(obj, COUNT):
            return f"COUNT({self._to_sql(obj.item)})"
        if isinstance(obj, SetClause):
            return f" SET {obj.what.field_name} = {self._to_sql(obj.value)}"
        if isinstance(obj, Everything):
            return f"*"
        if isinstance(obj, SelectQuery):
            query = "(SELECT "
            query += ", ".join(map(self._to_sql, obj.selected if len(obj.selected) > 0 else [Everything()]))
            query += " FROM "
            query += obj.model.__tablename__

            for clause in obj.clauses:
                query += self._to_sql(clause)
            query += ")"
            return query
        raise TypeError(f"SQLiteDatabase cannot convert object {obj} for an SQL query")
    
    async def cast_select(self, select_query: SelectQuery):
        self._sql_args = []
        c = await self.execute(self._to_sql(select_query)[1:-1] + ";", self._sql_args)
        return await c.fetchall()
    
    def _to_sql_type(self, field):
        if isinstance(field, IntegerField):
            return "INTEGER"
        if isinstance(field, TextField):
            return "TEXT"
        raise ValueError(f"Cannot convert {field} type")
    
    def _to_sql_fieldattr(self, attr: ColumnAttribute):
        if isinstance(attr, PrimaryKey):
            return "PRIMARY KEY"
        if isinstance(attr, NotNull):
            return "NOT NULL"
        if isinstance(attr, Default):
            self._sql_args.append(self._to_sql(attr.default))
            return "DEFAULT ?"
        raise ValueError(f"Cannot convert {attr} attribute")

    def _to_sql_type_def(self, field: Field):
        query = field.field_name + " "
        if isinstance(field, (ForeignKeyField)):
            query += self._to_sql_type(field.foreign_column)
            query += " REFERENCES "
            query += field.foreign_column.table_name
            query += f"({field.foreign_column.field_name})"
            if field.on_delete:
                query += f" ON DELETE {self._to_sql(field.on_delete)}"
            if field.on_update:
                query += f" ON UPDATE {self._to_sql(field.on_update)}"
        else:
            query += self._to_sql_type(field)
        if len(field.attributes) > 0:
            query += " " + " ".join(map(self._to_sql_fieldattr, field.attributes))
        return query

    async def cast_create_table(self, table: Model, if_not_exists: bool):
        self._sql_args = []

        query = "CREATE TABLE "
        if if_not_exists:
            query += "IF NOT EXISTS "
        query += table.__tablename__
        query += "("
        query += ", ".join(map(lambda x: self._to_sql_type_def(x[1]), table.get_fields()))
        query += ");"

        await self.execute(query, self._sql_args)

    async def cast_drop_table(self, table: Model, if_exists: bool):
        self._sql_args = []

        query = "DROP TABLE "
        if if_exists:
            query += "IF EXISTS "
        query += table.__tablename__
        query += ";"
        
        await self.execute(query, self._sql_args)

    async def cast_insert(self, insert_query: InsertQuery):
        self._sql_args = []

        assert len(insert_query.inserting) > 0
        if isinstance(insert_query.inserting[0], (list, tuple)):
            assert all(isinstance(x, (list, tuple)) for x in insert_query.inserting), "When doing named insertion, every field should be named."
            assert all(isinstance(t[0], Field) for t in insert_query.inserting), "Keys for named inserting should be fields"
            assert all(t[0].table_name == insert_query.model.__tablename__ for t in insert_query.inserting), "Cannot insert to foreign key"

            query = "INSERT INTO "
            query += insert_query.model.__tablename__
            query += "(" + ", ".join(map(lambda x: x[0].field_name, insert_query.inserting)) + ")"
            query += " VALUES "
            query += "(" + ", ".join(map(lambda x: self._to_sql(x[1]), insert_query.inserting)) + ") "

            for clause in insert_query.clauses:
                query += self._to_sql(clause)
            query += ";"

            return await self.execute(query, self._sql_args)
        elif isinstance(insert_query.inserting[0], Field):
            # from select
            assert all(isinstance(x, Field) for x in insert_query.inserting), "When doing select insertion, every value should be Field."
            assert all(x.table_name == insert_query.model.__tablename__ for x in insert_query.inserting), "Fields cannot be foreign."
            assert insert_query.select_query is not None, "Select insertion should not be None."

            query = "INSERT INTO "
            query += insert_query.model.__tablename__
            query += "(" + ", ".join(map(lambda x: x.field_name, insert_query.inserting)) + ") "
            query += self._to_sql(insert_query.select_query)[1:-1]
            
            for clause in insert_query.clauses:
                query += self._to_sql(clause)
            query += ";"

            return await self.execute(query, self._sql_args)
        else:
            query = "INSERT INTO "
            query += insert_query.model.__tablename__
            query += " VALUES "
            query += "(" + ", ".join(map(lambda x: self._to_sql(x), insert_query.inserting)) + ")"

            for clause in insert_query.clauses:
                query += self._to_sql(clause)
            query += ";"

            return await self.execute(query, self._sql_args)
    
    async def cast_update(self, update_query: UpdateQuery):
        self._sql_args = []

        query = "UPDATE "
        query += update_query.model.__tablename__
        query += " "
        for clause in update_query.clauses:
            query += self._to_sql(clause)
        query += ";"

        return await self.execute(query, self._sql_args)

    async def close(self):
        await self.database.close()

    async def execute(self, query, args):
        return await self.database.execute(query, args)