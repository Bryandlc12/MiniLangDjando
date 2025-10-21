from MiniLangVisitor import MiniLangVisitor

class EvalVisitor(MiniLangVisitor):
    def __init__(self):
        self.variables = {}
        self.outputs = []

    def visitProgram(self, ctx):
        for stmt in ctx.statement():  # ahora sí devuelve todos los statements
            self.visit(stmt)
        return None

    def visitAssing(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.variables[name] = value
        return value

    def visitPrintStmt(self, ctx):
        value = self.visit(ctx.expr())
        self.outputs.append(str(value))
        return value

    def visitExpr(self, ctx):
        if ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            return self.visit(ctx.getChild(1))

        if ctx.getChildCount() == 3:
            left = self.visit(ctx.getChild(0))
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.getChild(2))
            if op == '+': return left + right
            if op == '-': return left - right
            if op == '*': return left * right
            if op == '/': return left / right

        if ctx.INT(): return int(ctx.INT().getText())
        if ctx.ID(): return self.variables.get(ctx.ID().getText(), 0)

        return 0
