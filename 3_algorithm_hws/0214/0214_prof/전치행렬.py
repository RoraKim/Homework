
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(3):
    print(*arr[i])

print('='*30)
for i in range(3):
    for j in range(i+1, 3):
        arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

for i in range(3):
    print(*arr[i])