from .query import SelectQuery, InsertQuery, UpdateQuery
from .column import Field

class Model:
    @classmethod
    def get_fields(cls):
        fields = list(filter(lambda x: not (x.startswith("__") and x.endswith("__")) and isinstance(getattr(cls, x), Field), cls.__dict__))
        return zip(fields, map(lambda x: getattr(cls, x), fields))

    @classmethod
    def __registered__(cls, database, preferred_name):
        cls.__database__ = database
        cls.__tablename__ = preferred_name

        for field_name, field in cls.get_fields():
            if isinstance(field, Field):
                if field.table_name is None:
                    field.table_name = cls.__tablename__
                if field.field_name is None:
                    field.field_name = field_name

    @classmethod
    def select(cls, *selected):
        assert hasattr(cls, "__database__") and hasattr(cls, "__tablename__")
        return SelectQuery(cls, selected)
    
    @classmethod
    def update(cls):
        assert hasattr(cls, "__database__") and hasattr(cls, "__tablename__")
        return UpdateQuery(cls)
    
    @classmethod
    async def create_table(cls, if_not_exists=False):
        assert hasattr(cls, "__database__") and hasattr(cls, "__tablename__")
        await cls.__database__.cast_create_table(cls, if_not_exists)

    @classmethod
    async def drop_table(cls, if_exists=False):
        assert hasattr(cls, "__database__") and hasattr(cls, "__tablename__")
        await cls.__database__.cast_drop_table(cls, if_exists)
    
    @classmethod
    def insert(cls, *values):
        assert hasattr(cls, "__database__") and hasattr(cls, "__tablename__")
        return InsertQuery(cls, values)

    def __repr__(self):
        names = [f"{i}={repr(getattr(self, i))}" for i in dir(self) if not (i.startswith("__") and i.endswith("__"))]
        return f"{self.__class__.__name__}({', '.join(names)})"