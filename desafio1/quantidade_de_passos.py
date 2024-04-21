quantidade_passos = int(input())

if quantidade_passos > 0:
    for passos in range(1,quantidade_passos+1):
        if passos == 1:
            print(f'Explorador: {passos} passo')
        else:
            print(f'Explorador: {passos} passos')
else:
    print('Nenhum passo dado na floresta.')