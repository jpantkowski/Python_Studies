import random
import httpx
from pathlib import Path

def get_random_pokemon():
    pokemon_id = random.randint(1, 151)
    response = httpx.get( f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}" )
    pokemon_data = response.json()
    return pokemon_data

def download_png(url : str, filename: str):
    response = httpx.get(url)
    png_file = open(Path(__file__).parent / "pngs" / filename, "wb")
    png_file.write(response.content)

"""
Ściągnij .png losowego pokemona
"""

def download_png_of_random():
    data = get_random_pokemon()
    adres = data["sprites"]["other"]["official-artwork"]["front_default"]
    name = data["name"]
    download_png(adres, f"{name}.png")

download_png_of_random()
