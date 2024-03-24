MAIOR_IDADE = 18
IDADE_ESPECIAL = 12
texto_maior_idade = "Maior de idade, pode tirar a CNH."
texto_else = "Ainda não pode tirar a CNH."

idade = int(input("Informe a sua idade: "))

if idade >= MAIOR_IDADE:
    print(f'{texto_maior_idade}')

if idade < MAIOR_IDADE:
    print(f'{texto_else}')

if idade >= MAIOR_IDADE:
    print(f'{texto_maior_idade}')
else:
    print(f'{texto_else}')

if idade >= MAIOR_IDADE:
    print(f'{texto_maior_idade}')
elif idade >= IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer as aulas prásticas")
else:
    print(f'{texto_else}')