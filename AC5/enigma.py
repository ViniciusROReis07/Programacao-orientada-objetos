def enigma(L):
    d = {"?" : 0, "!": 0}
    c = set()
    for x in L:
        if "A" <=  x <= "Z":
            d["?"] += 1
        elif "0" <= x <= "9":
            d["!"] += 1
        else:
            c.add(x)
    return [d, c]
 

print(type(enigma("teste  T!")))


