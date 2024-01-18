"""
Napisz funkcję przyjmującą użytkownika (np. Remigiusz) i zwracającą stan konta.
"""

NAMES = {
    2356354: "eugeniusz",
    8936743: "tymoteusz",
    2389654: "remigiusz"
}

BALANCE = {
    2356354: 3200,
    8936743: 5100,
    2389654: 60
}

def ID(klient):
    for key in NAMES:
        if NAMES[key] == klient:
            return key

def balance(key):
    print(f"{key} has {BALANCE[ID(key)]} PLN")

balance("eugeniusz")
