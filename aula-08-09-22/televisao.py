class Televisao():
     def __init__(self):
         self.volume = 0
         self.canal = None
         
     def aumentar_volume(self):
         self.volume += 1
     def diminuir_volume(self):
         self.volume -= 1
     def alterar_canal(self, canal):
         self.canal = canal
         
tv = Televisao()
tv.alterar_canal(6)
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.diminuir_volume()
