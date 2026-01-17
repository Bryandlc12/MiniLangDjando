# views.py
from django.shortcuts import render
from antlr4 import *
from grammar.MiniLangLexer import MiniLangLexer
from grammar.MiniLangParser import MiniLangParser
from grammar.MiniLangVisitorExec import MiniLangInterpreter

def index(request):
    code = ""
    output = ""

    if request.method == "POST":
        code = request.POST.get("code", "")
        try:
            # Crear input stream
            input_stream = InputStream(code)
            
            # Lexer
            lexer = MiniLangLexer(input_stream)
            tokens = CommonTokenStream(lexer)
            
            # Parser
            parser = MiniLangParser(tokens)
            tree = parser.program()
            
            # Ejecutar con nuestro intérprete
            interpreter = MiniLangInterpreter()
            output = interpreter.execute(tree)
            
        except Exception as e:
            import traceback
            output = f"❌ Error: {e}\n\n{traceback.format_exc()}"

    return render(request, "core/index.html", {"code": code, "output": output})