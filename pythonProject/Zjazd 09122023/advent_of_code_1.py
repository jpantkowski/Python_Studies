with open("advent_of_code.txt") as plik1:
    content = plik1.readlines()

lista = []
def two_digit(x):
    for i in x:
        if i.isnumeric():
            break
    for y in reversed(x):
        if y.isnumeric():
            break
    return int(i + y)

for rekord in content:
    lista.append(two_digit(rekord))

print(sum(lista))
