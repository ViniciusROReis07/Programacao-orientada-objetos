conjunto = set()
print(type(conjunto))

conjunto = {} #Cria um dicionario vazio

conjunto = {10,20,40,10,30}

print(len(conjunto))

conjunto.add(77)# Nao pode adicionar itens mudaveis

print(conjunto)

conjunto.add((21,31))

print(conjunto)


p = set("ana")
print(p)

p = set("banana")
print(p)

list(p)
L = list(p)
print(L)

L.sort()
print(L)

print(hash((10,20)))#Criptografia de mao unica

conjunto.update([100,200,300])#Pega o item por item no conjunto
print(conjunto)

conjunto.discard(300)# Se nao houver o valor nao avisara que o item nao exite

print(conjunto) 

conjunto.remove(100)# Se nao houver o item ira disparar uma execption

conjunto.pop()#Remove o ultimo item do conjunto

conjunto.clear()