nome = "gUilHermE"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "  Ola mundo  "

print(texto + ".")
print(texto.strip() + ".")
print(texto.lstrip() + ".")
print(texto.rstrip() + ".")

menu = "Python"

print(menu.center(14,"$"))
print(menu.center(14))
print("-".join(menu))

for espaco in menu:
    print(espaco, end="-")