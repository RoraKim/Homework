import sys; sys.stdin = open('2001_파리퇴치.txt')

t = int(input())
for tc in range(1, t + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            cnt = 0
            sol = 0
            for ii in range(i, i + M):
                for jj in range(j, j + M):
                    cnt += arr[ii][jj]
            if sol < cnt:
                sol = cnt
    print(f'#{tc} {sol}')