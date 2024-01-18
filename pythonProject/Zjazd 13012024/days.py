"""
Wyprintuj datę która była 10000 dni temu.
"""
from datetime import datetime, timedelta

today = datetime.now().date()
past = timedelta(days = 10000)
the_guys_date = today - past
print(the_guys_date)

"""
Liczba numerologiczna
1991-09-14
1+9+9+1 + 0+9 + 1+4
34:
3+4
7
Policz liczbę numerologiczną dla gościa co urodził się 10000 dni temu
"""

number = int(str(the_guys_date).replace("-",""))

while len(str(number)) > 1:
    number = sum(map(int, list(str(number))))

print(number)


print(len(number))



