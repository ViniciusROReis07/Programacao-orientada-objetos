class TV:
    def  __init__(self, tela, resolucao, fabricante, preco):
         self.tela = tela
         self.resolucao = resolucao
         self.fabricante = fabricante
         self.preco = preco
         
    def exibe(self): 
        print(f"Tamanho...: {self.tela}")
        print(f"resolucao...: {self.resolucao}")
        print(f"fabricante...: {self.fabricante}")
        print(f"preco...: {self.preco}")
        print("-"*15)


tv1 = TV(43, "Full HD","LG",1200.00)
tv2 = TV(65, "8k", "Sony", 6500.00)

print(tv1.exibe())
print(tv2.exibe())

tv2.preco = 0.92 * tv2.preco

print(tv2.exibe())