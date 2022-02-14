import sys
sys.stdin = open('1209sum.txt')

n = int(input())
arr = [list(map(int, input().split())) for _ in range(10)]
# print(arr)

result = []
my_sum = 0
for i in range(10):
    for j in range(10):
        # print(type(arr[i][j]))
        my_sum += arr[i][j]
        # print(my_sum)
    result.append(my_sum)
    my_sum = 0

print(result)
