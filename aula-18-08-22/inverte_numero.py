n = int(input("n? "))

while n>0:
    print(n % 10, end="")
    n //= 10
print()