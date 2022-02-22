
def paper(n):

    if n >= 2 and memo[n] == 0:
        if n % 2 == 0:
            memo[n] = paper(n - 2) * 4 - 1

        if n % 2 == 1:
            memo[n] = paper(n - 2) * 4 + 1
    # print(memo)
    return memo[n]

t = int(input())
for tc in range(1, t+1):
    n = int(input()) // 10
    memo = [0] * (n + 1)
    memo[1] = 1
    memo[2] = 3
    # print(memo)
    print(f'#{tc}',paper(n))

