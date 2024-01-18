from matplotlib import pyplot as plt


a = (0, 0)
b = (0, 3)
c = (2, 3)
d = (2, 4)
points = [a, b, c, d]

#ARGS

print(points)
print(*points)

print(list(zip(*points)))

#plt.scatter(*zip(*points))
#plt.plot(*zip(*points))
#plt.show()

def multyply(x, y):
    return x * y

numbers = [6, 5]
print(multyply(*numbers))

#KWARGS
def summarize_person(name: str = "Noname", pesel: str = "00000000000", age: int = 18):
    print(f"{name=}, {pesel=}, {age=}")

summarize_person(name = "Herbert", pesel = "92101004818", age = 31)

person = {
    "name" : "Halibut",
    "pesel" : "97112376925",
    "age" : 26
}

summarize_person(name = person["name"], pesel = person["pesel"], age = person["age"])
summarize_person(**person)


