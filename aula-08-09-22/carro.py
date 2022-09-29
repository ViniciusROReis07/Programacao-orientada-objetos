class Carro():
    def __init__(self):
        self.quantidade_combustivel = 0
        
    def adicionar_combustivel(self, combustivel):
        self.quantidade_combustivel += combustivel
    
    def andar(self, km):
        self.quantidade_combustivel -= km*0.2
        
    def obter_combustivel(self):
        return self.quantidade_combustivel 
    
meu_carro = Carro()
meu_carro.adicionar_combustivel(20)   
meu_carro.andar(80)                 
print('Litros de combustível no tanque:', meu_carro.obter_combustivel())
