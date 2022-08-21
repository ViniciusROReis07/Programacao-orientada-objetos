qtd_canais = int(input())

if 1<= qtd_canais <= 200:
    canais = []

    for _ in range(0,qtd_canais):
        canal = input()
        canal = canal.split(";")
        canais.append(canal)

    x = float(input())
    y = float(input())

    print("-----")
    print("BÔNUS")
    print("-----")
 

    for canal in canais:
        canal[3] = (canal[3] == "sim")
        canal[1] = int(canal[1])
        canal[2] = float(canal[2])

        bonus = 0

        if canal[3]:
            bonus =  ((canal[1]//1000) * x) + canal[2]
        else:
            bonus = ((canal[1]//1000) * y) + canal[2]

        print(f"{canal[0]}: R$ {bonus:.2f}")



