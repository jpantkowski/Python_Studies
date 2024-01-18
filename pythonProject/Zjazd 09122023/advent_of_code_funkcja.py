"""
1. Znajdź pierwszą cyfrę od lewej i od prawej zadanego napisu
2. Połącz tak znalezione 2 cyfry w liczbę 2-cyfrową.
"""

string = "oinj3odbifh5oiugbdfn4865nv"

def two_digit(x):
    for i in x:
        if i.isnumeric():
            break
    for y in reversed(x):
        if y.isnumeric():
            break
    print(i + y)

two_digit(string)
