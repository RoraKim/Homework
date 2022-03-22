import sys
sys.stdin = open('input.txt')

di = [-1, 1, 0, 0] #상, 하, 좌, 우
dj = [0, 0, -1, 1]


def check(x, y):
    #범위안에 있는지 체크
    if x>=0 and x<16 and y>=0 and y<16:
        return True
    return False


def maze(x, y): #맨 처음 넘겨받을 좌표는 시작점
    Q = []
    Q.append((x, y))
    #visited의 현재 좌표를 벽으로 변경함
    visited[x][y] = 2

    while Q: #Q의 모든 것이 pop되어서 더이상 탐색할 곳이 없기 전에는 멈추지 않음
        x, y = Q.pop(0) #Q의 맨앞 인덱스 값을 꺼내옴
        for i in range(4):
            nx = x + di[i]
            ny = y + dj[i]

            #nx, ny가 범위 안에 있을 때
            if check(nx, ny):
                #nx, ny의 위치가 벽이 아니고 visited에 방문한적이 없다면
                if arr[nx][ny] != 1 and visited[nx][ny] == 0:
                    #도착점을 찾았다면 visited에 표시해주고 1을 반환
                    if arr[nx][ny] == 3:
                        visited[nx][ny] = 3
                        return 1
                    #반환되지 않았다면, 아직 도착점을 찾지 못한것
                    #탐색할 Q에 nx,ny를 넣어주고 visited를 1로 변경
                    Q.append((nx, ny))
                    visited[nx][ny] = 1
                    
    #while안에서 return이 되지 않았다는 것은 되는 경우의 수가 없었다는 뜻               
    return 0


for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    # print(arr)
    visited = [[0]* 16 for _ in range(16)] #16 * 16 배열 생성
    for i in range(16):
        for j in range(16):
            #시작점의 좌표를 넘겨줌
            if arr[i][j] == 2:
                result = maze(i, j)
                break

    print(f'#{tc} {result}')
    print(visited)
