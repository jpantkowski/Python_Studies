"""
Napisz grę:
Jesteśmy w pokoju z pokemomanmi i mamy wielką walizkę, którą możemy unieść 2000 kg wagi.
Program pyta nas, czy chcemy wziąć kolejnego pokemona do walizki.
Jeśli tak, dostajemy informację, ile miejsca nam zostało.
Jeśli powiemy tak i skończy nam się miejsce w walizce to przegrywamy.
Jeśli powiemy nie, gra się kończy i printuje pokemony, które zabieramy ze sobą do domu :3
"""

import random
from dataclasses import dataclass

import httpx


@dataclass
class Pokemon:
    name: str
    weight: int


def get_random_pokemon() -> Pokemon:
    pokemon_id = random.randint(1, 151)
    response = httpx.get(
        f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    pokemon_data = response.json()
    return Pokemon(pokemon_data["name"], pokemon_data["weight"])

waliza = []
pojemnosc_walizy = 2000
pokemon = get_random_pokemon()
waliza.append(pokemon.name)
pojemnosc_walizy -= pokemon.weight
print(f"Pozostało Ci {pojemnosc_walizy}")
while True:
    if input("Grasz? Tak/Nie") == "Tak":
        pokemon = get_random_pokemon()
        waliza.append(pokemon.name)
        pojemnosc_walizy -= pokemon.weight
        if pojemnosc_walizy < 0:
            print("Niestety przegrałeś")
            break
        else:
            print(f"Pozostało Ci {pojemnosc_walizy} ")
    else:
        print(f"Pozostało Ci {pojemnosc_walizy} i zabrałeś ze sobą {len(waliza)} pokemonów czyli {waliza}")
        break
