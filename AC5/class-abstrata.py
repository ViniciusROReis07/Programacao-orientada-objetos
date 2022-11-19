from abc import ABC, abstractclassmethod

from matplotlib.pyplot import cla

class A(ABC):
    def metodo_m(self):
        pass
    
    @abstractclassmethod
    def metodo_n(self):
        pass
    
class B(A):
    def metodo_o():
        pass
    
    def metodo_n(self):
        pass
    
x = B()