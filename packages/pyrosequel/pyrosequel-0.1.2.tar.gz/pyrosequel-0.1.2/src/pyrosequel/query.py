from .column import Everything

class Query:
    def __init__(self, model):
        self.model = model
        self.clauses = []
    async def cast(self):
        raise NotImplementedError("Abstract Query cannot be casted")
    async def cast_one(self):
        raise NotImplementedError("Abstract Query cannot be casted")
    
    def where(self, expr):
        assert not any([isinstance(i, WhereClause) for i in self.clauses]), "WHERE clause can only appear once"
        self.clauses.append(WhereClause(expr))
        return self
    
    def left_join(self, table, expr):
        self.clauses.append(LeftJoinClause(table, expr))
        return self
    def inner_join(self, table, expr):
        self.clauses.append(InnerJoinClause(table, expr))
        return self
    
    def returning(self, *columns):
        assert not any([isinstance(i, ReturningClause) for i in self.clauses]), "RETURNING clause can only appear once"
        self.clauses.append(ReturningClause(columns))
        return self
    
    def order_by(self, what, how):
        if (idx := next(filter(lambda x: isinstance(x[1], OrderByClause), enumerate(self.clauses)), (None,))[0]) is not None:
            self.clauses[idx].orders.append((what, how.upper()))
            return self
        self.clauses.append(OrderByClause([(what, how.upper())]))
        return self
    def order_by_desc(self, what):
        return self.order_by(what, "DESC")
    def order_by_asc(self, what):
        return self.order_by(what, "ASC")

class Clause:
    pass

class ReturningClause(Clause):
    def __init__(self, columns):
        self.columns = columns
class LimitClause(Clause):
    def __init__(self, how_much):
        self.how_much = how_much
class OffsetClause(Clause):
    def __init__(self, how_much):
        self.how_much = how_much
class WhereClause(Clause):
    def __init__(self, expr):
        self.expr = expr
class HavingClause(Clause):
    def __init__(self, expr):
        self.expr = expr
class GroupByClause(Clause):
    def __init__(self, expr):
        self.expr = expr

class LeftJoinClause(Clause):
    def __init__(self, on, expr):
        self.on = on
        self.expr = expr
class InnerJoinClause(Clause):
    def __init__(self, on, expr):
        self.on = on
        self.expr = expr
class OrderByClause(Clause):
    def __init__(self, orders):
        self.orders = orders

class SetClause(Clause):
    def __init__(self, what, value):
        self.what = what
        self.value = value

class UnionClause(Clause):
    def __init__(self, other):
        self.other = other

class SelectQuery(Query):
    def __init__(self, model, selected):
        super().__init__(model)
        self.selected = selected
    
    async def cast(self):
        return await self.model.__database__.cast_select(self)
    
    def union(self, other):
        self.clauses.append(UnionClause(other))
        return self
    
    def limit(self, how_much):
        assert not any([isinstance(i, LimitClause) for i in self.clauses]), "LIMIT clause can only appear once"
        self.clauses.append(LimitClause(how_much))
        return self
    def offset(self, how_much):
        assert not any([isinstance(i, OffsetClause) for i in self.clauses]), "OFFSET clause can only appear once"
        self.clauses.append(OffsetClause(how_much))
        return self
    def paginate(self, page_size, page):
        assert not any([isinstance(i, (LimitClause, OffsetClause)) for i in self.clauses]), "Paginate can only appear once and with no LIMIT or OFFSET clauses present"
        self.clauses += [LimitClause(page_size), OffsetClause(page_size * page)]
        return self

class InsertQuery(Query):
    def __init__(self, model, inserting):
        super().__init__(model)

        self.inserting = inserting
        self.select_query = None

    async def cast(self):
        return await self.model.__database__.cast_insert(self)
    
    async def cast_one(self):
        return await (await self.model.__database__.cast_insert(self)).fetchone()

    async def select(self, select_query):
        assert self.select_query is None, "Only one SELECT query can be used in INSERT; use UNION instead"
        self.select_query = select_query
        return self

class UpdateQuery(Query):
    def __init__(self, model):
        super().__init__(model)

    async def cast(self):
        return await self.model.__database__.cast_update(self)
    
    async def cast_one(self):
        return await (await self.model.__database__.cast_update(self)).fetchone()

    def set(self, what, value):
        self.clauses.append(SetClause(what, value))
        return self
