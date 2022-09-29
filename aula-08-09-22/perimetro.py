class Perimetro():
     def __init__(self, lado_a, lado_b, lado_c):
         self.lado_a = lado_a
         self.lado_b = lado_b
         self.lado_c = lado_c
         
     def cacula_perimetro(self):
        return self.lado_a + self.lado_b + self.lado_c
         
lado_a = float(input("Lado a: "))
lado_b = float(input("Lado b: "))
lado_c = float(input("Lado c: "))

perimetro_a = Perimetro(lado_a, lado_b, lado_c)
valor_perimetro = perimetro_a.cacula_perimetro()
print(f"Perimetro: {valor_perimetro:.2f}")