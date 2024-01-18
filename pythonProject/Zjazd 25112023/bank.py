"""
Mamy konta 3 osób:
Asi, Basi, i Pawła.
Każdy początkowo ma 100 PLN.
Napisz program obsługujący przelewy między tymi kontami.
Wykonaj 4 'przelewy', po czym wyprintuj stan konta każdej osoby:

asia has transferred 20 PLN to pawel
basia has transferred 50 PLN to pawel
pawel has transferred 60 PLN to asia
basia has transferred 30 PLN to asia
asia has 170 PLN
basia has 20 PLN
pawel has 110 PLN

(Można uprościć, że stan konta to int, olewamy istnienie groszy)
"""

bank = {
    "Asia" : 100 ,
    "Basia" : 100 ,
    "Pawel" : 100
}

def transfer(nadawca, odbiorca, kwota):
    bank[nadawca] -= kwota
    bank[odbiorca] += kwota
    print(f"{nadawca} has transferred {str(kwota)} PLN to {odbiorca}")

def status(jaki_bank):
    for i in jaki_bank:
        print(f"{i} has {jaki_bank[i]} PLN")

transfer("Asia", "Pawel", 20)
transfer("Basia", "Pawel", 50)
transfer("Pawel", "Asia", 60)
transfer("Basia", "Asia", 30)

status(bank)