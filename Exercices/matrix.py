# two dimensional list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# return first element of first list, so 1
print(matrix[0][0])
print(matrix)

for row in matrix:
    for item in row:
        print(item)