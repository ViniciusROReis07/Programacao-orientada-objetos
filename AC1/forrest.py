valores = []
media = 0
valores_abaixo_media = []

while True :
    valor = int(input())
    if valor > 0:
      valores.append(valor)
    else:
        break

tamanho_lista = len(valores)

if tamanho_lista >0:
    for valor in valores:
        media += valor


media /= tamanho_lista

print(f'MEDIA: {media:.2f}')

for valor in valores:
    if valor < media:
        print(valor)