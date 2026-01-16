# Generated from grammar/MiniLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniLangParser import MiniLangParser
else:
    from MiniLangParser import MiniLangParser

# This class defines a complete listener for a parse tree produced by MiniLangParser.
class MiniLangListener(ParseTreeListener):

    # Enter a parse tree produced by MiniLangParser#program.
    def enterProgram(self, ctx:MiniLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniLangParser#program.
    def exitProgram(self, ctx:MiniLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniLangParser#statement.
    def enterStatement(self, ctx:MiniLangParser.StatementContext):
        pass

    # Exit a parse tree produced by MiniLangParser#statement.
    def exitStatement(self, ctx:MiniLangParser.StatementContext):
        pass


    # Enter a parse tree produced by MiniLangParser#ifStatement.
    def enterIfStatement(self, ctx:MiniLangParser.IfStatementContext):
        pass

    # Exit a parse tree produced by MiniLangParser#ifStatement.
    def exitIfStatement(self, ctx:MiniLangParser.IfStatementContext):
        pass


    # Enter a parse tree produced by MiniLangParser#forStatement.
    def enterForStatement(self, ctx:MiniLangParser.ForStatementContext):
        pass

    # Exit a parse tree produced by MiniLangParser#forStatement.
    def exitForStatement(self, ctx:MiniLangParser.ForStatementContext):
        pass


    # Enter a parse tree produced by MiniLangParser#condition.
    def enterCondition(self, ctx:MiniLangParser.ConditionContext):
        pass

    # Exit a parse tree produced by MiniLangParser#condition.
    def exitCondition(self, ctx:MiniLangParser.ConditionContext):
        pass


    # Enter a parse tree produced by MiniLangParser#comparisonOp.
    def enterComparisonOp(self, ctx:MiniLangParser.ComparisonOpContext):
        pass

    # Exit a parse tree produced by MiniLangParser#comparisonOp.
    def exitComparisonOp(self, ctx:MiniLangParser.ComparisonOpContext):
        pass


    # Enter a parse tree produced by MiniLangParser#expr.
    def enterExpr(self, ctx:MiniLangParser.ExprContext):
        pass

    # Exit a parse tree produced by MiniLangParser#expr.
    def exitExpr(self, ctx:MiniLangParser.ExprContext):
        pass



del MiniLangParser