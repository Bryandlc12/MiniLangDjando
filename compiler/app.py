from flask import Flask, request, jsonify
from flask_cors import CORS
from antlr4 import InputStream, CommonTokenStream
from MiniLangLexer import MiniLangLexer
from MiniLangParser import MiniLangParser
from EvalVisitor import EvalVisitor

app = Flask(__name__)
CORS(app)

@app.route("/run", methods=["POST"])
def run_code():
    data = request.get_json()
    code = data.get("code", "")
    visitor = EvalVisitor()
    try:
        input_stream = InputStream(code)
        lexer = MiniLangLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = MiniLangParser(tokens)
        tree = parser.program()
        visitor.visit(tree)
        return jsonify({"outputs": visitor.outputs, "variables": visitor.variables})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
