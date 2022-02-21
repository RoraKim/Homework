import sys; sys.stdin = open('5356_의석이의세로로말해요.txt')

t = int(input())
for tc in range(1, t + 1):
    arr = [input() for _ in range(5)]
    sols = []
    for j in range(15):
        for i in range(5):
            if j < len(arr[i]):
                sols.append(arr[i][j])

    print(f'#{tc} {"".join(sols)}')








    # # print(arr)
    # #
    # print(lst)
    # for i in range(5):
    #     for j in range(i):
    #         arr[i][j] = lst[i][j]
    #
    # print(arr)


