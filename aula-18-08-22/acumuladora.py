soma = 0

while True:
    valor = float(input("Valor: "))

    if valor == 99.99:
        break;
    else:
        soma += valor

print(f"Soma {soma}")