class Crocodile:
    tail = True
    limbs = 4

    # dunder method (double underscore method)
    # to jest metoda - funkcja w klasie to metoda:
    def __init__(self, name, place_of_habitat):
        self.name = name
        self.place = place_of_habitat

    def eat(self):
        pass

    @staticmethod
    def get_population_count():
        return 921234

    @classmethod
    def get_population_limbs_count(cls):
        crocodile_count = cls.get_population_count()
        return crocodile_count * cls.limbs

# to jest funkcja:
def function():
    pass

andrzej = Crocodile("Andrzej", "ZOO in Wroclaw")
blazej = Crocodile("Blazej", "Amazon forest")
print("ok")
print(Crocodile.get_population_limbs_count())
