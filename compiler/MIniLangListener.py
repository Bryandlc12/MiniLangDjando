# Generated from MIniLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MIniLangParser import MIniLangParser
else:
    from MIniLangParser import MIniLangParser

# This class defines a complete listener for a parse tree produced by MIniLangParser.
class MIniLangListener(ParseTreeListener):

    # Enter a parse tree produced by MIniLangParser#program.
    def enterProgram(self, ctx:MIniLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by MIniLangParser#program.
    def exitProgram(self, ctx:MIniLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by MIniLangParser#statement.
    def enterStatement(self, ctx:MIniLangParser.StatementContext):
        pass

    # Exit a parse tree produced by MIniLangParser#statement.
    def exitStatement(self, ctx:MIniLangParser.StatementContext):
        pass


    # Enter a parse tree produced by MIniLangParser#assing.
    def enterAssing(self, ctx:MIniLangParser.AssingContext):
        pass

    # Exit a parse tree produced by MIniLangParser#assing.
    def exitAssing(self, ctx:MIniLangParser.AssingContext):
        pass


    # Enter a parse tree produced by MIniLangParser#print.
    def enterPrint(self, ctx:MIniLangParser.PrintContext):
        pass

    # Exit a parse tree produced by MIniLangParser#print.
    def exitPrint(self, ctx:MIniLangParser.PrintContext):
        pass


    # Enter a parse tree produced by MIniLangParser#expr.
    def enterExpr(self, ctx:MIniLangParser.ExprContext):
        pass

    # Exit a parse tree produced by MIniLangParser#expr.
    def exitExpr(self, ctx:MIniLangParser.ExprContext):
        pass



del MIniLangParser