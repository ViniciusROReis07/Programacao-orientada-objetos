class PosGraduacao():
    def __init__(self, instituicao, curso):
        self.instituicao = instituicao
        self.curso = curso
        
    def get_curso(self):
        return self.curso

class Doutorado(PosGraduacao):
    def __init__(self, instituicao, curso, tese = None):
        super().__init__(instituicao, curso)
        self.__tese = tese
        
    def get_curso(self):
        return f"doutorado em {super().get_curso()}"
        
    def set_tese(self, titulo):
        self.__tese = titulo
    
    def get_tese(self):
        return self.__tese
    

    
    
dr = Doutorado("USP", "Juris Docto")

print("Dados do Dr:")
print(f"Instituicao: {dr.instituicao}")
print(f"Curso: {dr.curso}")
print(f"Tese: {dr.get_tese()}")

print()
print("-"*20)
print()

dr.set_tese("Lava Jato")

print("Dados do Dr:")
print(f"Instituicao: {dr.instituicao}")
print(f"Curso: {dr.curso}")
print(f"Tese: {dr.get_tese()}")