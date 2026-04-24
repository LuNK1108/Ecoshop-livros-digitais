import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",      # no XAMPP geralmente é vazio
    database="db_ecoshop_livros"
)

if conexao.cursor:
    cursor = conexao.cursor(dictionary=True)
    print("Banco conectado")

#retorna todos os livros no banco
def mostrar_livros():
    cursor.execute("SELECT * FROM livro")
    livros = cursor.fetchall()
    return livros

#insere um livro no banco
def inserir_livro(id_autor, id_categoria, titulo, descricao, preco, arquivo, capa, paginas, ativo, data):
    sql = """
    INSERT INTO livro 
    (id_autor, id_categoria, titulo, descricao, preco, arquivo_pdf, capa_url, paginas, ativo, data_publicacao)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    valores = (id_autor, id_categoria, titulo, descricao, preco, arquivo, capa, paginas, ativo, data)

    cursor.execute(sql, valores)
    conexao.commit()