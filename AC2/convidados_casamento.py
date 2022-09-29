convidados_noivo = set()
convidados_noiva = set()


while True:
    convite = input()
    
    if convite == "ACABOU":
        break
    else:
        nome_convidado, quem_convidou = convite.split(";")
        
        if quem_convidou == "noiva":
            convidados_noiva.add(nome_convidado)
        elif quem_convidou == "noivo":
            convidados_noivo.add(nome_convidado)
        

print('--------------------')
print('LISTA FINAL')
print('--------------------')
for convidado in sorted(convidados_noiva|convidados_noivo):
    print(convidado)
print()

print('--------------------')
print('APENAS NOIVA')
print('--------------------')
for convidado in sorted(convidados_noiva-convidados_noivo):
    print(convidado)
print()

print('--------------------')
print('APENAS NOIVO')
print('--------------------')
for convidado in sorted(convidados_noivo-convidados_noiva):
    print(convidado)
print()

print('--------------------')
print('POR AMBOS')
print('--------------------')
for convidado in sorted(convidados_noiva&convidados_noivo):
    print(convidado)
print()


print('--------------------')
print('POR APENAS UM DELES')
print('--------------------')
for convidado in sorted(convidados_noiva^convidados_noivo):
    print(convidado)
