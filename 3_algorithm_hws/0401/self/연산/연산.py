import sys; sys.stdin = open('연산.txt')
from collections import deque

def cal(num, idx):
    if idx == 0:
        return num + 1

    if idx == 1:
        return num - 1

    if idx == 2:
        return num * 2

    if idx == 3:
        return num - 10

def bfs(n, m):
    #처음 주어진 n은 아직 연산 전이기 때문에 visited를 0으로 바꿔줌
    visited[n] = 0
    queue = deque()
    queue.append(n)

    while queue:
        #지금 조사 대상인  num을 찾아서
        num = queue.popleft()

        for i in range(4):
            #new_num이 cal함수를 통해 총 4개가 반환될 것임
            new_num = cal(num, i)
            #반환된 new_num이 m과 같다면, 직전까지의 연산 횟수 반환
            if new_num == m:
                return visited[num] + 1

            #반환된 new_num이 아직 최종값에 도달하지 않았는데, 방문한 적도 없다면
            elif 0< new_num < 1000000 and visited[new_num]== -1:
                visited[new_num] = visited[num] + 1
                queue.append(new_num)


t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    visited = [-1] * 1000001
    print(f'#{tc} {bfs(n, m)}')


























# def bfs(n, m):
#     visited[n] = 0
#     queue = deque()
#     queue.append(n)
#
#     while queue:
#         num = queue.popleft()
#         oper = [num + 1, num - 1, num * 2, num - 10]
#
#         for i in range(4):
#             if oper[i] == m:
#                 return visited[num]
#
#             if 0 < oper[i] <= 1000000:
#                 if visited[oper[i]] == -1:
#                     queue.append(i)
#                     visited[oper[i]] = visited[num] + 1








