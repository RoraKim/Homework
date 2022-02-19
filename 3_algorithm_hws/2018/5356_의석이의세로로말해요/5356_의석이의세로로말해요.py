import sys; sys.stdin = open('5356_의석이의세로로말해요.txt')

t = int(input())
for tc in range(1, t + 1):
    lst = [input() for _ in range(5)]
    arr = [['*'] * 15 for _ in range(15)]

    print(lst)
    for i in range(5):
        for j in range(len(arr[i])):

    # print(arr)
    # for i in range(5):
    #     for j in range(len(arr[i])):
    #         arr[i][j] = lst[i][j]