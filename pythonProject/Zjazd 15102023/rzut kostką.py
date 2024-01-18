# Oblicz ekperymentalnie prawdopodobnieństwo wyrzucenia
# min 1 szóstki przy użyciu 3k6
import random

p = 0
for i in range(3):
    x = random.randint(1, 6)
    print(x)
    if x == 6:
        p += 1
if p > 0:
    print("Gratulacje! Wygrałeś")
else:
    print("Niestety, przegrałeś :(")
print("Prawdopodobieństwo wynosiło " + str(round(p / 3 * 100, 2)) + "%")

# inne rozwiązanie
counter_6 = 0
for i in range(3):
    if random.randint(1, 6) == 6:
        counter_6 += 1
# 5 sposobów na print ze zmienną
print(f"six rolled {counter_6} times")
print("six rolled {} times".format(counter_6))
print("six rolled", counter_6, "times")
print("six rolled " + str(counter_6) + " times") #dodawanie stringów plusikami jest niewydajne!
print(" ".join(["six rolled", str(counter_6), "times"])) #nieczytelne, w tym przypadku nieprzydatn