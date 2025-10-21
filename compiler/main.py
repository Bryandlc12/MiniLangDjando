from antlr4 import *
from MiniLangLexer import MiniLangLexer
from MiniLangParser import MiniLangParser
from EvalVisitor import EvalVisitor

variables = {}

def eval_line(line):
    input_stream = InputStream(line)
    lexer = MiniLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MiniLangParser(token_stream)

    # Intentamos detectar qué tipo de línea es
    if line.startswith("print(") and line.endswith(")"):
        tree = parser.print_()  # ANTLR renombra 'print' a print_
    elif "=" in line:
        tree = parser.assing()
    else:
        tree = parser.expr()

    visitor = EvalVisitor(variables)
    return visitor.visit(tree)

def ResulMiniLang():
    code_lines = [input(f"{i+1}: ") for i in range(6)]

    for line in code_lines:
        line = line.strip()
        if not line:
            continue
        eval_line(line)

if __name__ == "__main__":
    ResulMiniLang()
