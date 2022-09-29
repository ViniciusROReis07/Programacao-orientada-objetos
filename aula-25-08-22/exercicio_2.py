alunos = {}

for _ in range(0,5):
    aluno = input("Informe o ra do aluno: ")
    notas = []
    for _ in range(0,3):
      nota = float(input("Informa a nota do aluno: "))
      notas.append(nota)
    alunos[aluno] = notas
    print("-"*10)

for aluno, notas in alunos.items():
    soma_notas = 0
    for nota in notas:
        soma_notas += nota
    
    media = soma_notas/len(notas)
    print(f"Media do {aluno} e : {media:.1f}")

   

