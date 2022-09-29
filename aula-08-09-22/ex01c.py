class Livro:
    def __init__(self,titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas
        
        

    def __repr__(self):
        return f"Titulo: {self.titulo} \n" +\
        f"Autor: {self.autor} \n" +\
        f"Numero de paginas: {self.num_paginas} \n" +\
        "-"*10                                   
        
l1 = Livro("Harry Potter", "J K Rowling", 264)
l2 = Livro("1984", "George Orwell", 300)
print(l1)
print(l2)
