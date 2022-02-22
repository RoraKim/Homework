def fibo(n):
    global cnt
    print(memo)
    cnt += 1
    if n >=2 and memo[n] == 0:
        memo[n] = fibo(n - 1) + fibo(n - 2)
    return memo[n]

n = 100
memo = [0] * (n + 1)
memo[0] = 0
memo[1] = 1
cnt = 0
print(fibo(n))
print(cnt)