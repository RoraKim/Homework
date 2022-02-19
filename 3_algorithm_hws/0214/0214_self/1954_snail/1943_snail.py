import sys
sys.stdin = open("1943_snail.txt")

T = int(input())
di = [0, 1, 0, -1] # 우 하 좌 상
dj = [1, 0, -1, 0]
for tc in range(1, T+1):
    N = int(input()) # 달팽이의 크기
    arr = [[0] * N for _ in range(N)] # 달팽이의 크기만큼 0으로 채워진 행렬
    # print(arr)
    number = 1 # 1부터 숫자를 채워줌
    i, j = 0, -1 # (0,0)부터 시작이 아닌 (0,-1)부터 시작
    k = 0 # 방향의 idx
    while number <= N * N: # 달팽이의 크기만큼 반복
        ni, nj = i+di[k], j+dj[k] # 뱡향 이동
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0: # 범위안에 있으면서 해당 값이 0일때
            arr[ni][nj] = number # 숫자를 채워줌
            number += 1 # 숫자를 1 더해줌
            i, j = ni, nj # 인덱스값 변경
        else:
            k = (k+1) % 4 # 벽을 만나거나 범위에서 벗어난 경우 방향 전환

    print(f'#{tc}')
    for a in range(N):
        print(*arr[a])