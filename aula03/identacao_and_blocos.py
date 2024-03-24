def sacar(valor):
    saldo = 200

    if saldo >= valor:
        print('valor sacado')
        print('Retire o seu valor na boca do caixa')
    else:
        print('Saldo insuficiente')

    print('Obrigado por ser nosso cliente, tenha um bom dia!')

def depositar(valor):
    saldo = 500
    saldo += valor

sacar(300)
