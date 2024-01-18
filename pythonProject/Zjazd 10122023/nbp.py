"""
Używając https://api.nbp.pl/en.html
pobierz i wyprintuj ostatni kurs wybranej waluty
"""

import httpx

response = httpx.get("http://api.nbp.pl/api/cenyzlota")
resp = response.json()
print(f"Ostatnia data: {resp[0]['data']}, cena: {resp[0]['cena']} PLN" )

"""
Napisz funkcję, która dla zadanej daty i waluty wyprintuje kurs.
Przykładowy URL: https://api.nbp.pl/api/exchangerates/rates/a/jpy/2023-12-08/
"""

waluta = input("Jaka waluta Cię interesuje? (np. EUR, USD, JPY)")
data = input("Z kiedy chcesz kurs? (yyyy-mm-dd)")

response = httpx.get(f"https://api.nbp.pl/api/exchangerates/rates/a/{waluta}/{data}/")
rate_dict = response.json()["rates"][0]
print(f"Kurs: {rate_dict['mid']} PLN")

"""
Zadanie domowe:
przy response.json() zrób sekcję try: except:
złap odpowiedni wyjątek, i spróbuj httpx.get ponownie z datą poprzedzającą.
PROBLEMY :(  :
1. datetime - obliczenie daty poprzedzającej
2. rekurencja
"""





