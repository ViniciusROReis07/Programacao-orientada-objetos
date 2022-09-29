class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = float(salario)
        
    def __repr__(self):
        return f"Nome: {self.nome}\n" +\
               f"Salario R$ {self.salario:.2f}\n"+\
               "-"*20
    
        
    def aumentar_salario(self, percentual):
        self.salario += self.salario*percentual/100
  
L = []

for i in range(2):  
    nome = input("Nome? ")
    salario = float(input("Salario? R$ ")) 
    L.append(Funcionario(nome, salario))
    

for i in range(2):  
    L[i].aumentar_salario(int(input("Aumento (%): ")))
    print(L[i])

