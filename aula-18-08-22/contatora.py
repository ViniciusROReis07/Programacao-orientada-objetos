cont = 0

while True:
    letra = input("letra: ")
    if letra == "F":
        break
    else:
      cont += 1

print(f"Letras lidas = {cont}")