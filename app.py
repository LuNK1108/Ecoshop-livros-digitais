from flask import Flask, render_template, jsonify, request, redirect
from backend.database import mostrar_livros, inserir_livro, excluir_livro

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

@app.route("/cadastrar_livro", methods=["POST"])
def cadastrar_livro():
    id_autor = int(request.form["id_autor"])
    id_categoria = int(request.form["id_categoria"])
    titulo = request.form["titulo"]
    descricao = request.form["descricao"]
    preco = float(request.form["preco"])
    arquivo = request.form["arquivo"]
    capa = request.form["capa"]
    paginas = int(request.form["paginas"])
    ativo = request.form["ativo"] == "true"
    data = request.form["data"]

    inserir_livro(id_autor,id_categoria,titulo,descricao,preco,arquivo,capa,paginas,ativo,data
    )

    return redirect("/")

@app.route("/excluir_livro", methods=["POST"])
def excluir_livros():
    data = request.get_json()
    id_livro = data["id"]
    excluir_livro(id_livro)
    return redirect("/")

app.run(debug=True)