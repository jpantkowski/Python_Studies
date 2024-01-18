import json


def load_pikachu():
    pika_file = open("pika.json")
    return json.load(pika_file)


pikachu_dictionary = load_pikachu()
# print(json.dumps(pikachu_dictionary, indent = 4))

"""
Przedstaw pokemona z pliku pika.json (name, weight, height)
"""

print(f"Cześć mam na imię {pikachu_dictionary['name'].capitalize()}, ważę {pikachu_dictionary['weight']} kg i mam {pikachu_dictionary['height']} m wzrostu")

"""
Utwórz listę nazw wszystkich movesetów pikachu
"""
list_of_moves = []
for i in range(len(pikachu_dictionary["moves"])):
    list_of_moves.append(pikachu_dictionary["moves"][i]["move"]["name"])
print(list_of_moves)

"""
Utwórz listę nieukrytych umiejętności Pikachu
"""
non_secret_moves = []
for i in pikachu_dictionary["abilities"]:
    if not i["is_hidden"]:
        non_secret_moves.append(i["ability"]["name"])
print(non_secret_moves)
