import argparse


agenda = {
    "Maria": "(11)9456-6655",
    "Pedro": "(11)9431-6353",
    "Maria": "(11)9895-8756"
}

x = agenda.values()
print(x)

x = agenda.items()
print(x)

y = dict(x)
print(y)

print(agenda["Maria"])

d = {}
print(type(d))

d = dict()
print(type(d))

print(len(agenda))

d = {"ana": [190, 777],"bia":[192,193]}

print(d["ana"])

d["ana"] = 190

print(d["ana"])

x = d.pop("ana")

print(d)
print(x)

x = d.popitem()

print(d)

for item in agenda.items():
    print("Nome: ",item[0])
    print("Telefone: ",item[1])

for nome, telefone in agenda.items():
    print("Nome: ",nome)
    print("Telefone: ",telefone)