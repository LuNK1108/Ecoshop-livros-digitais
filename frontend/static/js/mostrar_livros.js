fetch("/mostra/livro")
    .then(resposta => resposta.json())
    .then(livros => {
        const lista = document.getElementById("lista-livros");

        livros.forEach(livro => {
            lista.innerHTML += `
                <div class="card-livro">
                    <h2>${livro.titulo}</h2>
                    <p>${livro.descricao}</p>
                    <p>R$ ${livro.preco}</p>
                    <button>Comprar</button>
                </div>
            `;
        });
    })
    .catch(erro => {
        console.log("erro ao mostrar livros", erro);
    });