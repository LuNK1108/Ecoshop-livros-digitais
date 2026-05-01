# EcoShop - Livros Digitais

Sistema web desenvolvido para gerenciamento e venda de livros digitais, com funcionalidades de autenticação, catálogo de produtos e carrinho de compras.

---

## Tecnologias Utilizadas

* Python
* Flask
* MySQL
* HTML
* CSS
* JavaScript (Fetch API)

---

## Funcionalidades

### Usuários

* Cadastro de usuário
* Login com validação
* Sessão de usuário

### Livros

* Listagem de livros via API
* Cadastro de novos livros
* Exclusão de livros

### Carrinho

* Um carrinho por usuário
* Adição de livros ao carrinho
* Visualização dos itens

---

## Estrutura do Banco de Dados

### Tabela `usuario`

* id_usuario
* nome
* email
* senha
* telefone
* tipo_usuario

### Tabela `livro`

* id_livro
* titulo
* descricao
* preco
* id_autor
* id_categoria

### Tabela `carrinho`

* id_carrinho
* id_usuario
* data_criacao

### Tabela `item_carrinho`

* id_item
* id_carrinho
* id_livro
* quantidade

---

## Estrutura do Projeto

```id="proj01"
Ecoshop-livros-digitais/
│
├── app.py
├── backend/
│   └── database.py
│
├── frontend/
│   ├── templates/
│   │   ├── index.html
│   │   ├── login.html
│   │   └── carrinho.html
│   │
│   └── static/
│       ├── css/
│       │   └── style.css
│       └── js/
│           ├── mostrar_livros.js
│           ├── excluir_livro.js
│           └── item_carrinho.js
```

---

## Como Executar o Projeto

### 1. Clonar o repositório

```bash id="proj02"
git clone https://github.com/LuNK1108/Ecoshop-livros-digitais.git
cd Ecoshop-livros-digitais
```

---

### 2. Criar ambiente virtual

```bash id="proj03"
python -m venv venv
venv\Scripts\activate
```

---

### 3. Instalar dependências

```bash id="proj04"
pip install flask mysql-connector-python
```

---

### 4. Configurar banco de dados

* Criar banco no MySQL
* Executar os scripts SQL do projeto

---

### 5. Rodar aplicação

```bash id="proj05"
python app.py
```

---

### 6. Acessar no navegador

```id="proj06"
http://127.0.0.1:5000
```

---

## Endpoints principais

| Método | Rota             | Descrição            |
| ------ | ---------------- | -------------------- |
| GET    | /mostra/livro    | Lista livros (JSON)  |
| POST   | /cadastrar_livro | Cadastra livro       |
| POST   | /excluir_livro   | Exclui livro         |
| POST   | /item_carrinho   | Adiciona ao carrinho |

---

## Aprendizados

Durante o desenvolvimento, foram praticados:

* Integração entre backend e frontend
* Manipulação de banco de dados
* Uso de API com Fetch
* Sessões em Flask
* Organização de projeto

---

## Melhorias Futuras

* Upload de imagens e arquivos PDF
* Sistema de pagamento
* Interface aprimorada
* Criptografia de senha
* Sistema de pedidos

---

## Autor

Lucas Oliveira
https://github.com/LuNK1108

---

## Projeto acadêmico

Desenvolvido com foco em aprendizado prático de desenvolvimento web com Flask.
