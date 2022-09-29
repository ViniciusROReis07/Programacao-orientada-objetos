class Filme():
    def __init__(self, titulo, genero):
        self.__titulo = titulo
        self.__genero = genero
        
    def __repr__(self):
        return (f"Genero: {self.__genero}\n"+
                f"Titulo: {self.__titulo}\n")
    
    def get_titulo(self):
        return self.__titulo
    
    def get_genero(self):
        return self.__genero
    
    def set_titulo(self, titulo):
        self.__titulo = titulo
    
    def set_genero(self, genero):
        self.__genero = genero
        
filmes = []

for _ in range(0,3):
    titulo = input("Titulo: ")
    genero = input("Genero: ")
    
    filmes.append(Filme(titulo, genero))
    
def exibe(filmes):
    print('\n'+'*'*20)
    for filme in filmes:
        print(filme)

exibe(filmes)
