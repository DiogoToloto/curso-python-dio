contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "8614-8452"}
}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}

print(contatos)
print(copia)