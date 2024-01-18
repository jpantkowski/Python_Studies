with open("rozliczenie.csv", "r") as plik1:
    content = plik1.readlines()
print(content)
for i in range(len(content)):
    content[i] = content[i].split(",")
print(content)
print(content[3])
print(content[3][2])

#obliczanie średniej wypłaty
total = 0
cycles = 0
for line in content[1:]:
    total += int(line[1])
print(f"Średnia wypłata to {round(total/(len(content)-1 ), 2)} PLN ")

#obliczanie liczby kobiet na macierzyńskim
count = 0
for line in content[1:]:
    if line[3].lower() == "k" and line[4][0].lower() == "t":
        count += 1
print(f"{count} kobiet przebywa na macierzyńskim")

with open("newfile.txt", "a") as plik1: #w - napdpisz a - dopisz
    plik1.write("Text")