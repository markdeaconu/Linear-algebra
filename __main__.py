from rowreduction2 import row_reduction
from determinant2 import determinant
from mcopy2 import mcopy
rows = int(input("how many rows in your matrix"))
columns = int(input("how many columns in your matrix"))
matrix = []
for i in range(rows):
    raw_row = list(input())
    new_row = []
    for columns in raw_row:
        new_row.append(int(columns))
    matrix.append(new_row)

print(row_reduction(mcopy(matrix)))

print(determinant(mcopy(matrix)))
