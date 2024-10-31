import enum

class SQLExpr:
    def __eq__(self, value):
        return BinaryExpr(self, value, SQLBinaryOperator.EQ)
    def __ne__(self, value):
        return BinaryExpr(self, value, SQLBinaryOperator.NEQ)
    def __gt__(self, value):
        return BinaryExpr(self, value, SQLBinaryOperator.GT)
    def __ge__(self, value):
        return BinaryExpr(self, value, SQLBinaryOperator.GTE)
    def __lt__(self, value):
        return BinaryExpr(self, value, SQLBinaryOperator.LT)
    def __le__(self, value):
        return BinaryExpr(self, value, SQLBinaryOperator.LTE)
    
    def __add__(self, value):
        return BinaryExpr(self, value, SQLBinaryOperator.ADD)
    def __sub__(self, value):
        return BinaryExpr(self, value, SQLBinaryOperator.SUB)
    def __mul__(self, value):
        return BinaryExpr(self, value, SQLBinaryOperator.MUL)
    def __truediv__(self, value):
        return BinaryExpr(self, value, SQLBinaryOperator.DIV)
    def __mod__(self, value):
        return BinaryExpr(self, value, SQLBinaryOperator.MOD)

class COUNT(SQLExpr):
    def __init__(self, item):
        self.item = item

class SQLBinaryOperator(enum.Enum):
    EQ = 1
    NEQ = 2
    GT = 3
    GTE = 4
    LT = 5
    LTE = 6

    AND = 10
    OR = 11

    ADD = 30
    SUB = 31
    DIV = 32
    MUL = 33
    MOD = 34

class BinaryExpr(SQLExpr):
    def __init__(self, val1, val2, op):
        self.val1 = val1
        self.val2 = val2
        self.op = op