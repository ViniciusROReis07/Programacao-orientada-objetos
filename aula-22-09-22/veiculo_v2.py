from statistics import mode


class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

                
class VeiculoRegistrado(Veiculo):
    def __init__(self, marca, modelo, placa):
        super().__init__(marca, modelo)
        self.placa = placa
        
    def exibir(self):
        print("--------------------")
        print("Marca:", self.marca) 
        print("Modelo:", self.modelo) 
        print("Placa:", self.placa)

veiculo_registrado = VeiculoRegistrado("Ford", "KA", "ERF-455")
veiculo_registrado.exibir();

class Moto(VeiculoRegistrado):
    def __init__(self, marca, modelo, placa, guidao):
        super().__init__(marca, modelo, placa)
        self.guidao = guidao
        
        
    def exibir(self):
        print("--------------------")
        print("Marca:", self.marca) 
        print("Modelo:", self.modelo) 
        print("Placa:", self.placa)
        print("Guidao:", self.guidao)
        
moto = Moto("Honda", "XRE", "KRY-465", "898258547852354")
moto.exibir();
    
class Carro(VeiculoRegistrado):
    def __init__(self, marca, modelo, placa, portas):
        super().__init__(marca, modelo, placa) # Acionando o init da classe mae
        self.portas = portas
        
    def exibir(self):
        print("--------------------")
        print("Marca:", self.marca) 
        print("Modelo:", self.modelo) 
        print("Placa:", self.placa)
        print("portas:", self.portas)
    # def exibir(self):
    #     print("--------------------")
    #     print("Marca:", self.marca) 
    #     print("Modelo:", self.modelo) 
    #     print("Placa:", self.placa)
    #     print("Portas:", self.portas) 
carro = Carro("FIAT", "UNO", "KRPL-46895", 2)
carro.exibir();
        
class CarroCombustao(Carro):
    def __init__(self, marca, modelo, placa, portas, tanque):
        super().__init__(marca, modelo, placa, portas)
        self.tanque = tanque
        
    def exibir(self):
        print("--------------------")
        print("Marca:", self.marca) 
        print("Modelo:", self.modelo) 
        print("Placa:", self.placa)
        print("Portas:", self.portas)
        print("Tanque:", self.tanque)

carro_combustao = CarroCombustao("FIAT", "UNO", "KRPL-46895", 2, "20L")
carro_combustao.exibir();
        
class CarroEletrico(Carro):
    def __init__(self, marca, modelo, placa, portas, bateria):
        super().__init__(marca, modelo, placa, portas)
        super.bateria = bateria
        
    def exibir(self):
        print("--------------------")
        print("Marca:", self.marca) 
        print("Modelo:", self.modelo) 
        print("Placa:", self.placa)
        print("Portas:", self.portas)
        print("Bateria:", self.bateria)

carro_combustao = CarroCombustao("FIAT", "UNO", "KRPL-46895", 2, "100WP")
carro_combustao.exibir();

class VeiculoNaoRegistrado(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        
    def exibir(self):
        print("--------------------")
        print("Marca:", self.marca) 
        print("Modelo:", self.modelo) 

veiculo_nao_registrado = VeiculoNaoRegistrado("Mobilete", ";lkl")
veiculo_nao_registrado.exibir();        

class Bicicleta(VeiculoNaoRegistrado):
    def __init__(self, marca, modelo, material, marcha):
        super().__init__(marca, modelo)
        self.material = material
        self.marcha = marca
    
    def exibir(self):
        print("--------------------")
        print("Marca:", self.marca) 
        print("Modelo:", self.modelo) 
        print("Material:", self.material)
        print("Marcha:", self.marca)

bicicleta = Bicicleta("Kaloi", "85", "Aco", "8")
bicicleta.exibir()