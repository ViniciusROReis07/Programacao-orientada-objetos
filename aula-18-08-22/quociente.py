a = int(input("a? "))
b = int(input("b? "))
q = 0


while a>=b:
    a -=b
    q += 1

print(f"Quociente = {q}")