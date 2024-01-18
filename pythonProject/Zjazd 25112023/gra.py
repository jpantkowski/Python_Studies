"""
Utwórz dwie klasy:
Player / Hero
- self.hp
- self.damage
- def attack

Monster / NPC / Attackable
- self.hp
- self.damage
- def attack

Zasymuluj walkę 2 obiektów
kiedy self.hp <= 0 oznacz obiekt jako martwy
Ogłoś zwycięzcę pojedynku.
"""

class Character:
    def __init__(self, name, hp : int, damage : int):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} can't attack because it's already dead")
        else:
            target.hp -= self.damage

    def is_alive(self) -> bool:
        return self.hp > 0

Asasyn = Character("Asasyn", 21, 3)
Szkielet = Character("Szkielet", 11, 2)

while Asasyn.hp > 0 and Szkielet.hp > 0:
    Asasyn.attack(Szkielet)
    Szkielet.attack(Asasyn)
    print(f"Asasyn ma {Asasyn.hp} HP , Szkielet ma {Szkielet.hp} HP")

if Asasyn.hp > 0:
    print("Zwycięzcą pojedynku jest Asasyn")
else:
    print("Zwyciężył Szkielet")


