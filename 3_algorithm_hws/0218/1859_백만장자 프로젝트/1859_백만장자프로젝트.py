import sys; sys.stdin = open('1859_백만장자프로젝트.txt')

def sum(arr):
    add = 0
    for i in arr:
        add += i

    return add


t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    sol = 0
    mmax = lst[N - 1]
    for i in range(N - 2, -1, -1):
        if mmax < lst[i]:
            mmax = lst[i]
        else:
            sol += (mmax - lst[i])
    print(sol)


    # sol = s = maxI = 0
    # while s < N:
    #     maxI = s
    #     for i in range(s, N):
    #         if lst[maxI] < lst[i]:
    #             maxI = i
    #     for i in range(s, maxI):
    #         sol += lst[maxI] - lst[i]
    #     s = maxI + 1
    #
    # print(sol)

















    # count = 0
    # money = 0
    # profit = 0
    # for i in range(days):
    #     if price[i] <= price[i + 1]:
    #         count += 1
    #         money += price[i]
    #
    #     elif price[i] > price[i + 1]:
    #         profit += (price[i] * count) - money
    #         money = 0
    #         count = 0
    # print(f'#{tc}', profit)

