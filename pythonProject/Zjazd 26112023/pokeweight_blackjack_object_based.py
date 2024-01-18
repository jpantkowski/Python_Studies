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

class PokeBlackJack:
    def __init__(self):
        self.capacity = 2000
        self.suitcase = []

    def get_pokemon(self):
        pokemon = get_random_pokemon()
        self.capacity -= pokemon.weight
        self.suitcase.append(pokemon.name)
        print(f"You found {pokemon.name}, it weights {pokemon.weight}")
        print(f"You have {self.capacity} left")

    @property
    def is_lost(self):
        return self.capacity < 0

game = PokeBlackJack()
game.get_pokemon()
while input("Do You want to take another Pokemon with You? (y/n)") == "y":
    game.get_pokemon()
    if game.is_lost:
        print("You lost :(")
        break
else:
    print(f"Congrats, You took {game.suitcase} with You :>")