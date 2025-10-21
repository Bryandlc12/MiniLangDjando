# Generated from MiniLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniLangParser import MiniLangParser
else:
    from MiniLangParser import MiniLangParser

# This class defines a complete generic visitor for a parse tree produced by MiniLangParser.

class MiniLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniLangParser#program.
    def visitProgram(self, ctx:MiniLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#assing.
    def visitAssing(self, ctx:MiniLangParser.AssingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#printStmt.
    def visitPrintStmt(self, ctx:MiniLangParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#expr.
    def visitExpr(self, ctx:MiniLangParser.ExprContext):
        return self.visitChildren(ctx)



del MiniLangParser