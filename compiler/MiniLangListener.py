# Generated from MiniLang.g4 by ANTLR 4.13.1
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


    # Enter a parse tree produced by MiniLangParser#assing.
    def enterAssing(self, ctx:MiniLangParser.AssingContext):
        pass

    # Exit a parse tree produced by MiniLangParser#assing.
    def exitAssing(self, ctx:MiniLangParser.AssingContext):
        pass


    # Enter a parse tree produced by MiniLangParser#printStmt.
    def enterPrintStmt(self, ctx:MiniLangParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by MiniLangParser#printStmt.
    def exitPrintStmt(self, ctx:MiniLangParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by MiniLangParser#expr.
    def enterExpr(self, ctx:MiniLangParser.ExprContext):
        pass

    # Exit a parse tree produced by MiniLangParser#expr.
    def exitExpr(self, ctx:MiniLangParser.ExprContext):
        pass



del MiniLangParser