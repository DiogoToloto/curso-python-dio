contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "8614-8452"}
}

# print(contatos["chave"])

print(contatos.get("chave"))
print(contatos.get("chave", {}))
print(contatos.get("guilherme@gmail.com", {}))