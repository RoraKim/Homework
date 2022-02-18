import sys; sys.stdin = open('p1.txt')
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#델타를 이용해 주변값과의 차이 절댓값을 반환하는 함수
def search(x, y, N):

    #한 좌표당 절댓값의 합을 누적
    cnt = 0
    #처음부터 끝 좌표까지
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        #새 좌표가 범위를 벗어나지 않는다면
        if 0 <= nx < N and 0 <= ny < N:
            cnt += abs(arr[nx][ny] - arr[x][y])
    return cnt


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    result = 0
    for i in range(n):
        for j in range(n):
            result += search(i,j,n)
    print(result)
#


















# #n * m 배열
#
# di = [0, 1, 0, -1] #우 하 좌 상
# dj = [1, 0,-1, 0]
#
# for k in range(4):
#     ni = i + di[k]
#     nj = j + dj[k]
#     #이범위에서만 유효한 인덱스를 벗어나지 않는다
#     if 0 <= ni < n and 0 <= nj < m:
#         arr[ni][nj]

# arr = [[1,2,3],[4,5,6],[7,8,9]]
# n = 3
# for i in range(n):
#     for j in range(n):
#         for di, dj in [(0,1),(1,0),(0,-1),(-1,0)]:
#             ni = i + di
#             nj = j + dj
#             if 0 <= ni < n and 0 <= nj < n:
#                 print(i,j,arr[ni][nj])
#         print()