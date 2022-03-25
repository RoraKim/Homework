import sys
sys.stdin = open('input.txt')


def bfs(s, e):
    visited = [0] * (V + 1)
    queue = []
    queue.append(s)
    visited[s] = 0
    while queue:
        node = queue.pop(0)
        if node == e:
            return visited[node]
        for next_node in arr[node]:
            if visited[next_node] == 0:
                visited[next_node] = visited[node] + 1
                queue.append(next_node)
    return 0


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V + 1)]
    for i in range(E):
        first, second = map(int, input().split())
        arr[first].append(second)
        arr[first].append(second)
    # print(arr) #인덱스번호 : 정점의 번호, 각 인덱스의 값 : 연결된 정점의 번호

    s, e = map(int, input().split())
    result = bfs(s, e)
    print(f"#{tc} {result}")