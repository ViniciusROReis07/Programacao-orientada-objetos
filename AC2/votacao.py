# Crie um programa que solicite ao usuário o nome e
# o número de cinco candidatos que concorrerão à uma
# eleição, o número deve ser único para cada candidato e
# serão válidos apenas números naturais.
# Em seguida, peça os votos de cada pessoa para que possam
# ser contabilizados, o voto será mediante o número do
# candidato.
# Ao final, o programa deverá exibir o nome dos candidatos,
# e a quantidade de votos, inclusive os votos em branco.
# O programa também deverá exibir o vencedor da eleição.
# Obs.(1): O programa deve prever a situação em que o usuário
#          tente votar em um candidato inexistente, nesse caso
#          o voto será anulado. Uma mensagem deverá ser exibida
#          indicando o ocorrido.
# Obs.(2): Caso o usuário digite o número de voto -1, isso indicará
#          um voto em branco. Uma mensagem deverá ser exibida
#          indicando o ocorrido.
# Obs.(3): Após a confirmação de um voto válido, o programa deverá
#          exibir o nome do candidato que recebeu o voto.
# Obs.(4): O programa deve registrar os números dos candidatos, os
#          nomes e a quantidade de votos em um dicionário, isto é,
#          o número deverá ser a chave e o valor associado uma lista
#          em que o primeiro valor é o nome e o segundo a quantidade
#          de votos.
# Obs.(5): O seu código de resposta deve estar logo em seguida deste
#          enunciado, ou seja, faça o download deste arquivo, insira
#          o seu código abaixo e anexe novamente o arquivo como resposta.


candidatos = {
    -1:[
        "Voto(s) em branco",
        0
    ]
}

for _ in range(0,5):
    numero = 0
    while numero <= 0: 
        numero = int(input("Numero candidato: "))
        
            
    nome = input("Nome candidato: ")
    candidatos[numero] = [ nome, 0]
    
numero_votos = int(input("Números de votantes: "))
    
for _ in range(0,numero_votos):
        voto = int(input("Por favor informe o numero do candidato em que deseja votar: "))
        
        if  voto in candidatos:
            candidatos[voto][1] += 1
            
            if(voto == -1):
                print("*********************** VOTO EM BRANCO *********************")
            else:
                print(f"Obrigado por votar em {candidatos[voto][0]}")
        else:
            print("******************* VOTO ANULADO, RAZAO: CANDIDATO INVALIDO ********************")

vencedor = ['',0]

for numero, dados in sorted(candidatos.items()):
        if numero != -1:
            if dados[1] > vencedor[1]:
                vencedor = [dados[0], dados[1]]
            
        print("-"*10)
        print(f"{dados[0]}")
        print(f"Total de votos: {dados[1]}")
        print("-"*10)
        print()
   
        
print(f"🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳 O(a) vencedor(a) da eleicao e {vencedor[0]} com {vencedor[1]} votos 🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳")
    
        

    
    
    

    

    

            
    
    
    