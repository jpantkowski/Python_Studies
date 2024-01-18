"""
Weż poniższą listę i pociachaj ją na 4-elementowe kawałki
UWAGA: Ostatni kawałek będzie miał 3 elementy:
output = [[1, 2, 3, 4 ], [5, 6, 7, 8], [9, 10, 11]]
lub
output = [(1, 2, 3, 4 ), (5, 6, 7, 8), (9, 10, 11)]
"""

a = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
output = []
for i in range(0, len(a), 4):
    output.append(a[i:i + 4])
print(output)

from more_itertools import batched