class Livro:
    def __init__(self,titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas
        
        

def exibe(L):
    print(f"Titulo: {L.titulo}")
    print(f"Autor: {L.autor}")
    print(f"Numero de paginas: {L.num_paginas}")
    print()
    print("-"*10)
    print()


l1 = Livro("Harry Potter", "J K Rowling", 264)
l2 = Livro("1984", "George Orwell", 300)
exibe(l1)
exibe(l2)
