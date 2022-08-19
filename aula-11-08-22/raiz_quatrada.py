a = int(input())

m1 = a // 100
m2 = a  % 100
s = m1 + m2
q =  s * s

if a == q:
    print("Sim")
else:
    print("Nao")