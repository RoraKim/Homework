import sys; sys.stdin = open('최소이동거리.txt')



T = int(input())
for t in range(1, T+1):
    N, E = map(int, input().split())
    MAP = [[0] * (N+1) for _ in range(N+1)]
    # 거리를 최대값으로 만들어 놈
    D = [10000001] * (N+1)
    print(D)
    # 맵에 도로의 정보 추가
    for i in range(E):
        s, e, w = map(int, input().split())
        MAP[s][e] = w
    # 시작은 0으로 두고
    D[0] = 0
    # j - 목표 위치 k - MAP에서 목표 위치로 가는 경로 찾기
    for j in range(1, N+1):
        for k in range(N+1):
            # 만약에 MAP에 목표 위치로 가는 경로가 있다면
            if MAP[k][j] != 0:
                print(f'MAP[k][j] + D[k]: {MAP[k][j] + D[k]}')
                print(f'D[j]: {D[j]}')
                # 현재 저장되어있는 이동거리인 D[j]와 경로값 MAP[k][j], k까지 최소한으로 이동하는 거리 D[k]를 비교 후 갱신
                D[j] = min(D[j], MAP[k][j] + D[k])
    print(D)
    print(f'#{t} {D[-1]}')

























# #특정 원소가 속한 집합을 찾기
# def find_parent(parent, x):
#     #루트 노드를 찾을때 까지 재귀 호출
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#
#     return parent[x]
#
# #두 원소가 속한 집합을 합치기
# def union_parent(parent, a, b):
#     #루트노드를 찾음
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#
#     if a < b:
#         parent[b] = a
#
#     else:
#         parent[a] = b
#
# t = int(input())
# for tc in range(1, t+1):
#     #노드의 개수 v와 간선의 개수 e
#     v, e = map(int, input().split())
#     parent = [0] * (v + 1) #부모 테이블 초기화하기
#
#     #모든 간선을 담을 리스트와 최종 비용을 담을 변수
#     edges = []
#     result = 0
#     count = 0
#
#     #부모 테이블 상에서 부모를 자신으로 초기화 하기
#     for i in range(1, v+1):
#         parent[i] = i
#
#
#     #모든 간선에 대한 정보를 입력 받기
#     for i in range(e):
#         a, b, distance = map(int, input().split())
#         #거리 순으로 정렬하기 위해서 튜플의 첫번째 원소를 비용으로 설정
#         edges.append((distance, a, b))
#
#     #간선을 거리 순으로 정렬
#     edges.sort()
#     print(edges)
#
#     #간선을 하나씩 확인 하며
#     for edge in edges:
#         distance, a, b = edge
#
#         #사이클이 발생하지 않는 경우에만 집합에 포함
#         if find_parent(parent, a) != find_parent(parent, b):
#
#             #합치기 연산을 수행할 때 마다, 즉 노드가 이어질 때 마다
#             union_parent(parent, a, b)
#             result += distance
#             if b == v:
#                 break
#
#
#
#
#     print(result)