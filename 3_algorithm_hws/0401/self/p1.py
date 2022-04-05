from pprint import pprint

def dfs(now):
    visited[now] = 1
    print(now, end=' ')

    for next in range(1, v+1):
        if arr[now][next] == 1 and not visited[next]:
            dfs(next)



v,e = map(int, input().split()) #v는 노드의 갯수, e는 간선의 수
data = list(map(int, input().split()))
print(data)
visited = [0] * (v+1)
arr = [[0 for _ in range(v+1)]for _ in range(v+1)]
for i in range(v + 1):
    arr[data[i * 2]][data[i * 2 + 1]] = 1
    arr[data[i * 2 + 1]][data[i * 2]] = 1

pprint(arr)
dfs(1)