
nota_trabalho = float(input())
nota_prova = float(input())

if (nota_trabalho+nota_prova)/2 >= 6:
    print('aprovado')
else:
    if (nota_trabalho+10)/2 >= 6:
        print('talvez com a sub')
    else :
        print('reprovado')