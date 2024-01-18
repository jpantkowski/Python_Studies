# Napisz funkcję, która zwróci ilość powtarzających się już elementów.
# W poniższej liście są 3 powtórki - 2, 2 i 15, więc:
# Output = 3

a = [ 2, 4, 2, 2, 15, 16, 5, 15]

def recurring_numbers(liczby):
    duplikaty = []
    unikalne_liczby = set()
    for liczba in liczby:
        if liczba in unikalne_liczby:
            duplikaty.append(liczba)
        else:
            unikalne_liczby.add(liczba)
    return duplikaty

wynik = recurring_numbers(a)
print("Powtarzające się liczby:", wynik)

def czy_roznica(lista):
    zbior = set(lista)
    return len(lista) - len(zbior)

print(czy_roznica(a))
