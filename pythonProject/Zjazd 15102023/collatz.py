# jeżeli licza jest parzysta: podziel ją na 2
# jeżeli liczba jest nieparzysta: pomnóż ją razy 3 i dodaj 1
# wykonuj tę operację w kółko, aż dostaniesz 1
# przykład:
# 3 -> 10 -> 5 -> 6 -> 8 -> 4 -> 2 -> 1

# zadanie: uruchom ten algorytm dla liczb od 2-100
# wyprinuj, która z liczb 2-100 zajęło najwięcej kroków by dotrzeć do 1

numbers = list(range(2,101))
kroki = []

for number in numbers:
    steps = 0
    while number != 1:
        if number % 2 == 0:
            number = number / 2
            steps += 1
        else:
            number = number * 3 + 1
            steps += 1
    kroki.append(steps)
print(kroki)
print(kroki.index(max(kroki)) + 2) # +2 bo indexowanie zaczyna się od 0, a my zaczynamy od 2
print(len(kroki))

