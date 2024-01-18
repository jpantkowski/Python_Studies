"""
1. Przemnóż wszystkie liczby z listy przez siebie.
2. Oblicz sumę cyfr z wyniku pkt 1
"""

#Podstawowe funkcjonalności

#1
a = [4, 2, 5, 7, 2, 3]

iloczyn = 1
for i in a:
    iloczyn *= i
print(iloczyn)

#2
suma = 0
for i in str(iloczyn):
    suma += int(i)
print(suma)

#Zadanie 1 - KRÓCEJ!

from functools import reduce

def multiply(x , y):
    return x * y

result = reduce(multiply, a)
print(result)

"""
result = multiply(a[0], a[1])
result = multiply(result, a[2])
result = multiply(result, a[3])
result = multiply(result, a[4])
...
"""

#Zadanie 1 - JEDNA LINIJKA - funkcja lambda
result = reduce(lambda x, y: x * y, a)
print(result)


#Zadanie 2 - list comprehention
final_result = sum([int(digit) for digit in str(result)])
print(final_result)

#Zadanie 2 - MAPA
final_result = sum(map(int, str(result)))
print(final_result)

#Zadanie 2 - Gigachad
print(sum(map(int, str(reduce(lambda x, y: x * y, a)))))