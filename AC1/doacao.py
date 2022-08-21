carteira_digital = 0
valor_doacao = 0

while True : 
    valor = float(input())
    if(valor == -1):
        break
    valor_doacao += valor

carteira_digital = valor_doacao*2.50

print(f'VC$ {valor_doacao:.2f}')
print(f'R$ {carteira_digital:.2f}')