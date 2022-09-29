produtos = {}

for _ in range(0,5):
    nome_produto = input()
    valor = float(input())
    produtos[nome_produto] = valor

print("-"*10)

for produto, valor in produtos.items():
    print(f"Produto: {produto} Valor: {valor:.2f}")

print("-"*10)

for produto, valor in produtos.items():
    if valor > 50:
        print(f"Produto superior a 50: {produto}")

