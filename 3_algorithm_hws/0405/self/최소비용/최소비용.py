import sys; sys.stdin = open('최소비용.txt')

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(arr)

    result = 0
    for i in range(n):
        result



