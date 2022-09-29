class ContaBancaria:
    def __init__(self, numero, saldo, titular ):
        self.numero = numero
        self.__saldo = saldo #modificando a visibilidadde para privato
        # self._saldo = saldo #modificando a visibilidadde para protegido
        self.titular = titular
        
    def exibe(selft):
        print(f"Numero da conta: {selft.numero}")
        print(f"Saldo.........: R$ {selft.__saldo:.2f}")
        print(f"Titilar.......: {selft.titular}")
        print("-"*15)
        print()
        
    def deposito(self, valor):
        self.__saldo += valor
        
    def saque(self, valor):
        if(self.__saldo>=valor):
            self.__saldo -= valor
        
# def deposito(c, valor):
#     c._ContaBancaria__saldo += valor # Forcando uma alteracao no atr privado

        
c1 = ContaBancaria(123, 2000.00, "Joao")
c2 = ContaBancaria(456, 7000.00, "Maria")
c3 = ContaBancaria(789, 15000.00, "Jose")

c1.exibe()

valor = float(input("Valor? "))
# c1.saldo += valor
# deposito(c1, valor)
c1.deposito(valor)
c1.exibe()

valor = float(input("Valor? "))

c1.saque(valor)

c1.exibe()

