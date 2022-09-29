class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = salario
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter 
    def salario(self, valor):
        self.__salario = valor

    @nome.setter 
    def nome(self, nome):
        self.__nome = nome
        
    @cpf.setter 
    def cpf(self, cpf):
        self.__cpf = cpf
    

func1 = Funcionario("Pedro", "111222333-22", 1500.0)
func1.salario = 2000.0              # Altera salário
print("Nome:", func1.nome)
print("CPF:", func1.cpf)
print("Salário:", func1.salario)
