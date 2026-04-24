function excluir(id_livro){fetch("/excluir_livro", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({ id: id_livro })
 
});
    location.reload();
}

