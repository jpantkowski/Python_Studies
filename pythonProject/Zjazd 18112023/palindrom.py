#program, który sprawdzi, czy dane wyrażenie jest palindromem
list_of_sentences = []
max_lenght = []
while True:
    phrase = str(input("Podaj słowo do sprawdzenia: "))
    list_of_sentences.append(phrase)

    print(f"Wprowadzono {phrase}")

    sentence = phrase.replace(" ","").replace(".","").replace(",","").lower()
    max_lenght.append(len(sentence))

    if sentence == sentence[::-1]:
        print(f"Wyrażenie {phrase} jest palindromem")
    else:
        print(f"Wyrażenie {phrase} nie jest palindromem")

    decision = input("Czy chcesz sprawdzić kolejne słowo? T/N")
    if decision.lower() == "n":
        break

print(f"Sprawdzono {len(list_of_sentences)} sentencji, najdłuższa z nich ma {max(max_lenght)} znaków. ")