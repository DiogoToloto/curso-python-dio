contatos = {
    "diogogabril@gmail.com": {"nome": "Diogo", "telefone": "3333-4551"},
    "brunacaroline@gmail.com": {"nome": "Bruna", "telefone": "8764-6648"},
    "elainecristina@gmail.com": {"nome": "Elaine", "telefone": "1476-4462"},
    "giovannacristina@gmail.com": {"nome": "Giovanna", "telefone": "7445-2311"},
}

# for chave in contatos:
#     print(chave, contatos[chave])

# print("=" * 80)

for chave, valor in contatos.items():
    print(chave, valor)