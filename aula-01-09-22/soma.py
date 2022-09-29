def soma(*a):
     s = 0
     for item in a:
         s += item
     return s
 
a =  soma(10,10)
b = soma(10,10,10)
 
print(a)
print(b)