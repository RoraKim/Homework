import sys
sys.stdin = open("4828.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))

    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j + 1]:
                a[j], a[j+1] = a[j+1], a[j]

                result = a[-1] - a[0]
    print(f'#{tc} {result}')
