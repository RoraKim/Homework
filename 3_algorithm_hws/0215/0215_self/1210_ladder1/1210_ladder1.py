import sys
sys.stdin = open('input.txt')

# 나는 좌, 우, 상만 확인 할 것이다.
# 단 위는 마지막에
dx = [0, 0, -1]
dy = [-1, 1, 0]

def ladder_search(x, y):
    # 처음 시작 위치 y 기록
    # 도착할 때 까지
    first_y = y
    while x != 0:
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 100 and 0 <= ny < 100 and arr[nx][ny] == 1:
                arr[x][y] = 0
                # 내 현재 위치 변경
                x, y = nx, ny
    return first_y
for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                # x, y 헷갈리지 말기
                x, y = i, j
    result = ladder_search(x, y)
    print(f'#{tc} {result}')



































#======================================================================================================

import sys; sys.stdin = open('1210_ladder1.txt')

# 도착점과 연결되어있는 출발점을 찾자
for tc in range(1, 11):
    N = int(input())
    #앞 뒤로 0을 추가해 범위를 벗어나지 않게 해줌
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]  # 일단 값을 받아오자

    #뒤에서부터 찾기
    #맨뒤의 값이 2인 지점의 인덱스를 찾아라
    finish_line_idx = arr[99].index(2)
    # print(finish_line_idx)

    #맨 마지막 줄에서 왼, 오를 탐색하고 왼, 오가 없으면 위로 가자
    # arr의 첫 줄에 도착할 때 까지

    last = 99
    finish_line = arr[last][finish_line_idx]

    #왼 오 위
    di = [0, 0, -1]
    dj = [-1, 1, 0]

    while last > 0:

    #지나온 길을 0으로 바꾸기
    #왼 위 있으면 왼
        if arr[last][finish_line_idx - 1] == 1 and arr[last -1][finish_line_idx] ==1:
            finish_line_idx += dj[0]
            arr[last][finish_line_idx] = 0
        #오 위 있으면 오
        if arr[last][finish_line_idx + 1] == 1 and arr[last -1][finish_line_idx] ==1:
            finish_line_idx += dj[1]
            arr[last][finish_line_idx] = 0

        #왼 있으면 왼
        if arr[last][finish_line_idx - 1] == 1:
            finish_line_idx += dj[0]
            arr[last][finish_line_idx] = 0

        #오 있으면 오
        if arr[last][finish_line_idx + 1] == 1:
            finish_line_idx += dj[1]
            arr[last][finish_line_idx] = 0

        #위 있으면 위
        if arr[last - 1][finish_line_idx] == 1:
            last += di[2]
            arr[last][finish_line_idx] = 0

    print(f'#{tc} {finish_line_idx - 1}')

