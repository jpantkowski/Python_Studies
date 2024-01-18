a = 5
b = 7.4
c = "Mama"
d_lista = [1, 2, 3, 5.5, "Mama", "54"]

print( a * c )
print( a * d_lista[5] )

if c == "Tata":
    print("Cześć Tata")
else:
    print("Cześć Mama")

for i in range(100, -1, -10):
    print(i)

while (a < 10):
    print(f"a wynosi {a}")
    a += 1

while True:
    wiek = int(input("Ile masz lat? "))
    if wiek >= 18:
        break
    else:
        print("Zły wiek, spróbuj jeszcze raz")
print("Dalsza część programu")

