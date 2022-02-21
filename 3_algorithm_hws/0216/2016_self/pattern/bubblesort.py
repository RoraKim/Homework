# def bubblesort(arr, n):
#     for i in range(n-1, 0, -1):
#         for j in range(i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
# arr = [1, 3, 4, 2, 4]
# n = len(arr)
#
# print(bubblesort(arr, n))


# for i1 in range(1, 4):
#     for i2 in range(1, 4):
#         if i2 != i1:
#             for i3 in range(1, 4):
#                 if i3 != i1 and i3 != i2:
#                     print(i1, i2, i3)
#
#
# for i in range(n):
#     for j in range(m):
#         arr[i][j]
#
# for j in range(m):
#     for i in range(n):
#         arr[i][j]
#
# for i in range(n):
#     for j in range(m):
#         arr[i][j + (m-1 -)]
#
#
#
di = [0, 1, 0, -1]
dj = [ 1, 0, -1, 0]
N = 5
M = 5
arr = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                print(arr[ni][nj])



# for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
#     ni = i + di[k]
#     nj = j + dj[k]
#     if 0 <= ni < N and 0 <= nj < M:
#         arr[ni][nj]
#

