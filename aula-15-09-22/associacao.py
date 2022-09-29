class Funcionario:
    def __init__(self, nome, data_nasc, sexo, salario, endereco):
        self.nome = nome
        self.data_nasc = data_nasc
        self.sexo = sexo
        self.salario = salario
        self.endereco = endereco
        
    def exibir_dados(self):
        print(f"Nome........: {self.nome}\n"+
              f"Nascimento..: {self.data_nasc}\n"+
              f"Sexo........: {self.sexo}\n"+
              f"Salario.....: R$ {self.salario:.2f}")
        self.endereco.exibir_dados()
        
class Endereco: 
    def __init__(self, rua, numero, bairro, cep, complemento):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cep = cep
        self.complemento = complemento
        
    def exibir_dados(self):
        print(f"Rua........: {self.rua}\n"+
                f"Numero..: {self.numero}\n"+
                f"Bairro........: {self.bairro}\n"+
                f"Complemento...: {self.complemento}\n"+
                f"Cep...........: {self.cep}")
        
f = Funcionario('Ana', '12/06/1995', 'F', 10000.00, Endereco('Rua dois', 2, 'Two', 'N/A','22222-222'))

f.exibir_dados()