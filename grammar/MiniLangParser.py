# Generated from grammar/MiniLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,23,105,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,5,0,16,8,0,10,0,12,0,19,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,3,1,33,8,1,1,2,1,2,1,2,1,2,1,2,1,2,5,2,41,8,2,
        10,2,12,2,44,9,2,1,2,1,2,1,2,1,2,5,2,50,8,2,10,2,12,2,53,9,2,1,2,
        3,2,56,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,5,3,72,8,3,10,3,12,3,75,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,92,8,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,
        100,8,6,10,6,12,6,103,9,6,1,6,0,1,12,7,0,2,4,6,8,10,12,0,3,1,0,11,
        16,1,0,17,18,1,0,19,20,109,0,17,1,0,0,0,2,32,1,0,0,0,4,34,1,0,0,
        0,6,57,1,0,0,0,8,78,1,0,0,0,10,82,1,0,0,0,12,91,1,0,0,0,14,16,3,
        2,1,0,15,14,1,0,0,0,16,19,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,
        20,1,0,0,0,19,17,1,0,0,0,20,21,5,0,0,1,21,1,1,0,0,0,22,23,5,21,0,
        0,23,24,5,1,0,0,24,33,3,12,6,0,25,26,5,2,0,0,26,27,5,3,0,0,27,28,
        3,12,6,0,28,29,5,4,0,0,29,33,1,0,0,0,30,33,3,4,2,0,31,33,3,6,3,0,
        32,22,1,0,0,0,32,25,1,0,0,0,32,30,1,0,0,0,32,31,1,0,0,0,33,3,1,0,
        0,0,34,35,5,5,0,0,35,36,5,3,0,0,36,37,3,8,4,0,37,38,5,4,0,0,38,42,
        5,6,0,0,39,41,3,2,1,0,40,39,1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,
        42,43,1,0,0,0,43,45,1,0,0,0,44,42,1,0,0,0,45,55,5,7,0,0,46,47,5,
        8,0,0,47,51,5,6,0,0,48,50,3,2,1,0,49,48,1,0,0,0,50,53,1,0,0,0,51,
        49,1,0,0,0,51,52,1,0,0,0,52,54,1,0,0,0,53,51,1,0,0,0,54,56,5,7,0,
        0,55,46,1,0,0,0,55,56,1,0,0,0,56,5,1,0,0,0,57,58,5,9,0,0,58,59,5,
        3,0,0,59,60,5,21,0,0,60,61,5,1,0,0,61,62,3,12,6,0,62,63,5,10,0,0,
        63,64,3,8,4,0,64,65,5,10,0,0,65,66,5,21,0,0,66,67,5,1,0,0,67,68,
        3,12,6,0,68,69,5,4,0,0,69,73,5,6,0,0,70,72,3,2,1,0,71,70,1,0,0,0,
        72,75,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,76,1,0,0,0,75,73,1,
        0,0,0,76,77,5,7,0,0,77,7,1,0,0,0,78,79,3,12,6,0,79,80,3,10,5,0,80,
        81,3,12,6,0,81,9,1,0,0,0,82,83,7,0,0,0,83,11,1,0,0,0,84,85,6,6,-1,
        0,85,92,5,22,0,0,86,92,5,21,0,0,87,88,5,3,0,0,88,89,3,12,6,0,89,
        90,5,4,0,0,90,92,1,0,0,0,91,84,1,0,0,0,91,86,1,0,0,0,91,87,1,0,0,
        0,92,101,1,0,0,0,93,94,10,5,0,0,94,95,7,1,0,0,95,100,3,12,6,6,96,
        97,10,4,0,0,97,98,7,2,0,0,98,100,3,12,6,5,99,93,1,0,0,0,99,96,1,
        0,0,0,100,103,1,0,0,0,101,99,1,0,0,0,101,102,1,0,0,0,102,13,1,0,
        0,0,103,101,1,0,0,0,9,17,32,42,51,55,73,91,99,101
    ]

class MiniLangParser ( Parser ):

    grammarFileName = "MiniLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'print'", "'('", "')'", "'if'", 
                     "'{'", "'}'", "'else'", "'for'", "';'", "'=='", "'!='", 
                     "'<'", "'<='", "'>'", "'>='", "'*'", "'/'", "'+'", 
                     "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "INT", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_ifStatement = 2
    RULE_forStatement = 3
    RULE_condition = 4
    RULE_comparisonOp = 5
    RULE_expr = 6

    ruleNames =  [ "program", "statement", "ifStatement", "forStatement", 
                   "condition", "comparisonOp", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    ID=21
    INT=22
    WS=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniLangParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = MiniLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2097700) != 0):
                self.state = 14
                self.statement()
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 20
            self.match(MiniLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(MiniLangParser.IfStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(MiniLangParser.ForStatementContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = MiniLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.match(MiniLangParser.ID)
                self.state = 23
                self.match(MiniLangParser.T__0)
                self.state = 24
                self.expr(0)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.match(MiniLangParser.T__1)
                self.state = 26
                self.match(MiniLangParser.T__2)
                self.state = 27
                self.expr(0)
                self.state = 28
                self.match(MiniLangParser.T__3)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.ifStatement()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 31
                self.forStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(MiniLangParser.ConditionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniLangParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = MiniLangParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(MiniLangParser.T__4)
            self.state = 35
            self.match(MiniLangParser.T__2)
            self.state = 36
            self.condition()
            self.state = 37
            self.match(MiniLangParser.T__3)
            self.state = 38
            self.match(MiniLangParser.T__5)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2097700) != 0):
                self.state = 39
                self.statement()
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 45
            self.match(MiniLangParser.T__6)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 46
                self.match(MiniLangParser.T__7)
                self.state = 47
                self.match(MiniLangParser.T__5)
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2097700) != 0):
                    self.state = 48
                    self.statement()
                    self.state = 53
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 54
                self.match(MiniLangParser.T__6)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.ID)
            else:
                return self.getToken(MiniLangParser.ID, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)


        def condition(self):
            return self.getTypedRuleContext(MiniLangParser.ConditionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniLangParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)




    def forStatement(self):

        localctx = MiniLangParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(MiniLangParser.T__8)
            self.state = 58
            self.match(MiniLangParser.T__2)
            self.state = 59
            self.match(MiniLangParser.ID)
            self.state = 60
            self.match(MiniLangParser.T__0)
            self.state = 61
            self.expr(0)
            self.state = 62
            self.match(MiniLangParser.T__9)
            self.state = 63
            self.condition()
            self.state = 64
            self.match(MiniLangParser.T__9)
            self.state = 65
            self.match(MiniLangParser.ID)
            self.state = 66
            self.match(MiniLangParser.T__0)
            self.state = 67
            self.expr(0)
            self.state = 68
            self.match(MiniLangParser.T__3)
            self.state = 69
            self.match(MiniLangParser.T__5)
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2097700) != 0):
                self.state = 70
                self.statement()
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 76
            self.match(MiniLangParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)


        def comparisonOp(self):
            return self.getTypedRuleContext(MiniLangParser.ComparisonOpContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = MiniLangParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.expr(0)
            self.state = 79
            self.comparisonOp()
            self.state = 80
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniLangParser.RULE_comparisonOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonOp" ):
                listener.enterComparisonOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonOp" ):
                listener.exitComparisonOp(self)




    def comparisonOp(self):

        localctx = MiniLangParser.ComparisonOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_comparisonOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 129024) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def INT(self):
            return self.getToken(MiniLangParser.INT, 0)

        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)


        def getRuleIndex(self):
            return MiniLangParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.state = 85
                self.match(MiniLangParser.INT)
                pass
            elif token in [21]:
                self.state = 86
                self.match(MiniLangParser.ID)
                pass
            elif token in [3]:
                self.state = 87
                self.match(MiniLangParser.T__2)
                self.state = 88
                self.expr(0)
                self.state = 89
                self.match(MiniLangParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 101
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 99
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = MiniLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 93
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 94
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==17 or _la==18):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 95
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = MiniLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 96
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 97
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==19 or _la==20):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 98
                        self.expr(5)
                        pass

             
                self.state = 103
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




