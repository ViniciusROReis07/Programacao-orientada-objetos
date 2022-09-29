class Livro:
    def __init__(self,titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas
        
        

    def exibe(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Numero de paginas: {self.num_paginas}")
        print()
        print("-"*10)
        print()


l1 = Livro("Harry Potter", "J K Rowling", 264)
l2 = Livro("1984", "George Orwell", 300)
l1.exibe()
l2.exibe()
