# znajdź parę liczb w zadanej liście, której suma wynosi 62
a = [253, 12, -2, 9, 234, 123, -94, 7]

for number1 in a:
    for number2 in a:
        if number1 + number2 == 62 and number1 != number2:
            print("62 = " + str(number1) + " + " + str(number2))

# sprytne rozwiązanie
n = 62
for i in a:
    if n - i in a:
        print(f"{i} oraz {n-i} dają razem {n}")
        break

# prosto i zrozumiale
m = 62
for i in a:
    for j in a:
        if i + j == n:
            print(f"{i} oraz  {j} dają razem {m}")