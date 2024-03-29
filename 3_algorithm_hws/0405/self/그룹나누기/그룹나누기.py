import sys; sys.stdin = open('그룹나누기.txt')

# T = int(input())
#
# for tc in range(1, T + 1):
#     n, m = map(int, input().split())
#     arr = list(map(int, input().split()))
#     result = [[]for _ in range(n)]
#     print(result)
#     print(arr)
#     groups = []
#     for i in range(0, m * 2,2):
#         group = [arr[i], arr[i+1]]
#         groups.append(group)
#
#     print(groups)


def find(x):
    if p[x] == x:
        return x  # x가 루트라면 반환
    else:
        p[x] = find(p[x])  # 아니면 루트 찾아가면서 부모 정보 갱신해주기
        return p[x]


def union(x, y):
    parent_x, parent_y = find(x), find(y)  # 두개 부모찾아서
    if parent_x < parent_y:  # 숫자 작은걸 부모로 결합해주기
        p[parent_y] = parent_x
    elif parent_x > parent_y:
        p[parent_x] = parent_y


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    p = [x for x in range(N + 1)]
    print(p)

    for i in range(0, M * 2, 2):
        union(data[i], data[i + 1])  # 두개 결합하기

    print(p)

    for i in range(1, N + 1):
        find(i)  # 부모 노드 정보 갱신

    print(p)

    set_p = set(p[1:])
    print(set_p)
    print(f"#{tc} {len(set_p)}")