# załóżmy, że pesel ma 4 cyfry
# stwórzmy zbiór NFZ – ludzie, w bazie pacjentów NFZ
# stwórzmy zbiór chorzy_rok – ludzie chorzy w ostatnim roku
# stwórzmy zbiór chorzy_miesiac – ludzie chorzy w ostatnim miesiącu
# stwórzmy zbiór bemowo – wszystkich ludzi mieszkających w centrum
# stwórzmy zbiór zoliborz – wszystkich ludzi mieszkających na krzykach



NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436])
chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
centrum = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
krzyki = {7648, 2345, 2356, 3987, 1234, 3476, 3254}
zbior_pusty = set()

# suma zbiorów ->          |
# częsc wspólna zbiorów -> &
# różnica zbiorów ->       -
# różnica symetryczna ->   ^

#ile osób chorowało w ostatnim roku w centrum
chorzy_centrum = chorzy_rok & centrum
print(f"{len(chorzy_centrum)} osób chorowało w ostatnim roku w centrum")

#ile osób z centrum chorowało w ostatnim roku?
centrum_chorzy = centrum & chorzy_rok
print(f"{len(chorzy_centrum)} osób z centrum chorowało w ostatnim roku") #działanie to jest przemienne

#poprawność danych
#każdy, kto chorował w ostatnim miesiącu, powinien jednocześnie chorować w ostatnim roku
if chorzy_miesiac == chorzy_miesiac & chorzy_rok:
    print("Dane się zgadzają")
else:
    print("Coś jest nie tak")

#nikt nie powiniem mieszkać jednocześnie w centrum i na krzykach
#jeśli są tacy, trzeba usunąć
if len(centrum & krzyki) == 0:
    print("Jest ok")
else:
    centrum -= krzyki

#każdy powinien być w bazie NFZ. Jeśli nie ma to trzeba go dopisać.
wszyscy = chorzy_rok | chorzy_miesiac | centrum | krzyki
if wszyscy == NFZ:
    print("Jest okej")
else:
    NFZ |= wszyscy

#pesele żeńskie mają ostatnią cyfrę parzystą, mięskie - nieparzystą
#zróbmy nowe zbiory, osobnme dla mężczyzn i kobiet
mezczyzni = set()
kobiety = set()
for i in wszyscy:
    if i % 2 == 0:
        kobiety.add(i)
    else:
        mezczyzni.add(i)
print(mezczyzni)
print(kobiety)

