def podatek(zarobki, liczba_dzieci):
    podatek_do_zaplaty = zarobki * 0.2 - 100 * liczba_dzieci
    print(f"Twój podatek wynosi {podatek_do_zaplaty}")
    return podatek_do_zaplaty

podatek(4000, 3)

# funkcja przyjmuje wiek, wagę, samopoczucie i zwraca współczynnik zdrowia
# jeśli wspołczynnik zdrowia > 5,można przystąpić do ubezpieczenia

def insurance(wiek, waga, samopoczucie):
    health_factor = wiek * waga * samopoczucie / 3000
    print(f"Twój współczynnik zdrowia wynosi {health_factor}")
    if health_factor > 5:
        print("Możesz przystąpić do ubezpieczenia")
    else:
        print("Nie możesz się ubezpieczyć, Twój współczynnik zdrowia jest za niski")
    return health_factor

insurance(32, 80, 10)