capacidade_atual, aumento_percentual = map(int, input().split())

soma = capacidade_atual * (aumento_percentual / 100)
nova_capacidade = capacidade_atual + soma
print(int(nova_capacidade))