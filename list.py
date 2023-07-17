array: list = [
    [1, 2, 3, 4, 0],
    [5, 6, 7, 8, 1],
    [9, 10, 11, 12, 2],
    [13, 14, 15, 16, 3],
    [17, 18, 19, 20, 4]
]

print(array)

x1, x2, y1, y2 = 1, 3, 2, 3

for row in array[x1 - 1:x2]:
    for index in range(len(row[y1:y2+1])):
        row[index + y1] = 1

print(array)