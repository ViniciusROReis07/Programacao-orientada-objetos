qtd_primos = 0
cont = 2
numero = int(input("Numero: "))

while cont < numero:
    if numero%cont == 0:
      print("Nao e primo")
      break
    cont += 1
else:
    print("Primo")
