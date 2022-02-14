import sys
sys.stdin = open('1209sum.txt')

t = 10
for i in range(1, t+1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    # print(arr)


    result = []
    my_sum = 0
    for i in range(100):
        for j in range(100):
            my_sum += arr[i][j]
        result.append(my_sum)
        my_sum = 0
    # print(result)

    for i in range(100):
        for j in range(100):
            my_sum += arr[j][i]
        result.append(my_sum)
        my_sum = 0
    # print(result)

    for i in range(100):
        for j in range(100):
            if i == j:
                my_sum += arr[i][j]
                # print(my_sum)
    result.append(my_sum)
    my_sum = 0
    # print(result)

    for i in range(100):
        my_sum += arr[i][99 - i]
    result.append(my_sum)
    # print(result)
    # print('='*30)
    # print(len(result))

    max_num = 0
    for i in result:
        if i > max_num:
            max_num = i

    print(f' #{tc} {max_num}')