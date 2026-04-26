function item_carrinho(id_livro){fetch("/item_carrinho", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({ id: id_livro })
 
});
    
}

