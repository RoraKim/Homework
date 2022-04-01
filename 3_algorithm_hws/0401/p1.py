arr = list(map(int, input().split()))
n = 7
print(arr)

adj = [[] for _ in range(n + 1)]

for i in range(0, len(arr)-1, 2):
    adj[arr[i]].append(arr[i+1])
    adj[arr[i + 1]].append(arr[i])
#

print(adj)