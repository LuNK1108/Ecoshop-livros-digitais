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
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM livro")
    livros = cursor.fetchall()
    cursor.close()
    return livros

#busca carrinho pelo id_usuario
def buscar_carrinho(id_usuario):
    cursor = conexao.cursor(dictionary=True)
    sql = ("SELECT id_carrinho FROM carrinho WHERE id_usuario = %s")
    cursor.execute(sql, (id_usuario,))
    id_carrinho = cursor.fetchone()
    cursor.close()
    return id_carrinho

#insere um livro no banco
def inserir_livro(id_autor, id_categoria, titulo, descricao, preco, arquivo, capa, paginas, ativo, data):
    cursor = conexao.cursor(dictionary=True)
    sql = """
    INSERT INTO livro 
    (id_autor, id_categoria, titulo, descricao, preco, arquivo_pdf, capa_url, paginas, ativo, data_publicacao)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    valores = (id_autor, id_categoria, titulo, descricao, preco, arquivo, capa, paginas, ativo, data)

    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()

#excluir um livro do banco
def excluir_livro(id_livro):
    cursor = conexao.cursor(dictionary=True)
    sql = "DELETE FROM livro WHERE id_livro = %s"
    cursor.execute(sql, (id_livro,))
    conexao.commit()
    cursor.close()

#validar um login
def validar_login(email, senha):
    cursor = conexao.cursor(dictionary=True)
    sql = "SELECT * FROM usuario WHERE email = %s AND senha = %s"
    cursor.execute(sql,(email, senha))
    usuario = cursor.fetchone()
    cursor.close()

    return usuario

#cadastra usuarios
def cadastro_usuario(nome, email, senha, telefone, tipo, data):
    cursor = conexao.cursor(dictionary=True)
    sql = """
    INSERT INTO usuario 
    (nome, email, senha, telefone, tipo_usuario, data_cadastro)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    valores = (nome, email, senha, telefone, tipo, data)
    usuario = cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()

    if usuario:
        return True
    else:
        return False

def adicionar_item_carrinho(id_carrinho, id_livro, quantidade):
    cursor = conexao.cursor()
    sql = "INSERT INTO item_carrinho (id_carrinho, id_livro, quantidade) VALUES (%s, %s, %s)"
    valores = (id_carrinho, id_livro, quantidade)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    
def buscar_itens_carrinho(id_carrinho):
    cursor = conexao.cursor(dictionary=True)

    sql = """ SELECT l.* FROM item_carrinho ic JOIN livro l ON ic.id_livro = l.id_livro WHERE ic.id_carrinho = %s
    """
    cursor.execute(sql, (id_carrinho,))
    itens = cursor.fetchall()
    cursor.close()
    return itens