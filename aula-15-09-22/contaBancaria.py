class ContaBancaria():
    def __init__(self, conta, titular, saldo):
        self.conta = conta
        self.titular = titular
        self.__saldo = saldo
        
    def __repr__(self):
        return (f"Numero da conta: {self.conta}\n"+
                f"Titular........: {self.titular}\n"+
                f"Saldo..........: {self.__saldo}\n")
        
    @property
    def saldo(self):
        senha = input("Senha? ")
        if senha == '123':
            return self.__saldo
        else:
            return None
        
    # def get_saldo(self, senha):
    #     if senha == '123':
    #         return self.__saldo
    #     else:
    #         return None
       
    @saldo.setter 
    def saldo(self, valor):
        if valor > 2 * self.__saldo:
            print("Atividade suspeita!")
        elif valor < 0.50*self.__saldo:
            print("Atividade suspeita!")
        else:
            self.__saldo = valor
    
    # def set_saldo(self, valor):
    #     if valor > 2 * self.__saldo:
    #         print("Atividade suspeita!")
    #     elif valor < 0.50*self.__saldo:
    #         print("Atividade suspeita!")
    #     else:
    #         self.__saldo = valor
        
# c1 = ContaBancaria(123, 'Ana', 7500)
# print(f'Saldo: R$ {c1._saldo:.2f}')
# c1._saldo = c1._saldo + 10*c1._saldo
# print(f'Saldo: R$ {c1._saldo:.2f}')
        
        
# c1 = ContaBancaria(123, 'Ana', 7500)
# print(f'Saldo: R$ {c1._ContaBancaria__saldo:.2f}')
# c1._ContaBancaria__saldo = c1._ContaBancaria__saldo + 10*c1._ContaBancaria__saldo
# print(f'Saldo: R$ {c1._ContaBancaria__saldo:.2f}')

        
c1 = ContaBancaria(123, 'Ana', 7500)

print(f'Saldo: R$ {c1.saldo:.2f}')
c1.saldo = 10*c1.saldo
print(f'Saldo: R$ {c1.saldo:.2f}')
# c1.set_saldo(c1.get_saldo(senha) + 10*c1.get_saldo(senha))
# c1.set_saldo(1.00)
# print(f'Saldo: R$ {c1.saldo:.2f}')
        