qtd = int(input("Quantidade: "))
cont = 0
vogais = 0

while qtd > cont:
    letra = input("Letra: ")
    cont += 1
    if letra in "aeiou":
        vogais += 1
    
print(f"Quantidade de vogais: {vogais}")