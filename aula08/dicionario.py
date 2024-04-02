pessoa = {"nome": "Diogo", "idade": 20}

pessoa = dict(nome="Diogo",idade=20)

pessoa["telefone"] = "4002-8922"

for i in pessoa:
    print(i, pessoa[i])

pessoa["nome"] = "Gabriel"
pessoa["idade"] = 25
pessoa["telefone"] = "9898-1781"

print('############')

for i in pessoa:
    print(i, pessoa[i])