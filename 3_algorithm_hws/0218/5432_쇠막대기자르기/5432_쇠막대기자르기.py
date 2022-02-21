import sys; sys.stdin = open('5432_쇠막대기자르기.txt')

t = int(input())
for i in range(1, t + 1):
    lst = input()

    sol = 0
    count = 0
    for i in range(len(lst)):
        if lst[i] == '(':
            count += 1
        else:
            if lst[i - 1] == '(':
                count -= 1
                sol += count
            else:
                count -= 1
                sol += 1

    print(sol)

