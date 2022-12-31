# todo: 2d list

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    x = ''
    for col in row:
        x += str(col)
    print(x)

print(matrix[0][1])
print(matrix[2])
