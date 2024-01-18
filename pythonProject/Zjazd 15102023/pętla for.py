numbers = [24, 12, 67, 3, -1, 67, -23]

for number in numbers:
    print(number)

if number == -23:
    print("number still exists and is equal to -23")

i = 1
i = i + 1 # dodajemy 1 do istniejącej zmiennej i
i += 1    # taki sam efekt ma konstrukcja += 1
print(i)  # print zwróci 3

# policz liczby ujmne z listy poniżej
numbers = [24, 12, 67, 3, -1, 67, -23]

x = 0
for number in numbers:
    if number < 0:
        x += 1

print("Quantity of negative numbers is:")
print(x)

y = []     # definiujemy pustą listę
for number in numbers:
    if number < 0:         # jeżeli element jest ujemny
        y.append(number)   # element jest dodany do listy
print(len(y))              # printujemy długość powstałej listy

# list comprehention narzędzie do tworzenia zbioru wg warunków
negative_numbers = [number
                    for number in numbers
                    if number < 0]
print(len(negative_numbers))

