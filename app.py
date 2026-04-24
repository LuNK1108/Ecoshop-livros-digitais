from flask import Flask, render_template, jsonify
from backend.database import mostrar_livros

app = Flask(
    __name__,
    template_folder="frontend/templates",
    static_folder="frontend/static"
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/mostra/livro")
def mostra_livro():
    livros = mostrar_livros()
    return jsonify(livros)

app.run(debug=True)