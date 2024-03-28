nome = "Diogo"
idade = 20
profissao = "Programador"
linguagem = "Python"
saldo = 45.3241

dados = {"nome": "Diogo", "idade": 20}

print("nome: %s idade: %d" %(nome, idade))
print("nome: {} idade: {}" .format(nome, idade))
print("nome: {0} idade: {1}" .format(nome, idade))
print("nome: {nome} idade: {idade}" .format(nome=nome, idade=idade))
print("nome: {nome} idade: {idade}" .format(**dados))
print(f"Nome:{nome} Idade:{idade} Saldo:{saldo:.2f}")


