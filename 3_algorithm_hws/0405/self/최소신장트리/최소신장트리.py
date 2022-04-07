# import sys; sys.stdin = open('최소신장트리.txt')
#
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
#
#     #모든 간선을 담을 리스트와 최종 비용을 담을 변수
#     edges = []
#     result = 0
#     count = 0
#
#     #부모 테이블 상에서 부모를 자신으로 초기화 하기
#     for i in range(1, v+1):
#         parent[i] = i
#     print(f'parent {parent}')
#
#
#     #모든 간선에 대한 정보를 입력 받기
#     for i in range(e):
#         a, b, distance = map(int, input().split())
#         #거리 순으로 정렬하기 위해서 튜플의 첫번째 원소를 거리로 설정
#         edges.append((distance, a, b))
#     print(f'edges {edges}')
#
#     #간선을 거리 순으로 정렬
#     edges.sort()
#     print(f'edges {edges}')
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
#
#
#     print(f'#{tc} {result}')


#
# lst = ['a', 'b', 't', 'a', 'a', 'a', 'b', 'a', 'a']
# lst = list(set(lst))
#
# lst.sort()
# print(lst)
#
# [10, 9, 8, 7, 6, 6, 7, 8, 9, 10]
#
# def code(n):
#     if n == 5:
#         return
#
#     print(n)
#     code(n-1)
#     print(n)
#
#
# code(10)


lst = [[0] * 5 for _ in range(5)]
lst[2][3] = 1
print(lst)

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def bfs(x, y):
    for k in range(4):
        nx = x + di[k]
        ny = y + dj[k]

        if 0<= nx<6 and 0<= ny <6:
            lst[nx][ny] = lst[x][y] + 1

bfs(2, 3)
print(lst)