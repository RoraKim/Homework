import sys; sys.stdin = open('5209_최소생산비용.txt')
from itertools import permutations
from pprint import pprint



def dfs(n, summ): #n은 dfs의 깊이, summ은 계산될때 마다 넘겨받는 값
    global minn

    # 현재까지 넘겨받은 summ값이 이미 minn보다 크면 더 계산할 필요가 없음
    if summ >= minn:
        return
    # 현재의 summ값이 min보다 작은데, 최대 깊이까지 탐색한거라면?
    # 지금의 summ이 이게 현재summ 중 가장 작은 값임
    elif n == length:
        minn = summ
        return

    else: #위에서 가지치기 당하지 않았으나, 아직 최대 깊이까지 탐색되지 않은거라면
        #length 가지 경우의수를 다 돌아야함 (제품 1, 2, 3)
        #checklist의 모든 원소를 탐색
        for i in range(length):
            #그 중 0인 것이 있다면
            if not visited[i]:
                visited[i] = 1
                #arr[제품][공장]
                dfs(n + 1, summ + arr[i][n])
                visited[i] = 0


t = int(input())

for tc in range(1, t+1):
    length = int(input())
    arr = [list(map(int, input().split())) for _ in range(length)]
    # pprint(arr)
    minn = 1500
    visited = [0] * length
    dfs(0, 0)
    print(f'# {tc} {minn}')











































#     permu = []
#     for i in range(0, n):
#         permu.append(str(i))
#
#     # print(permu)
#
#     possible_list = list(map(''.join, permutations(permu, n)))
#
#
#     minn = 10e9
#     for i in range(len(possible_list)):
#         # print(possible_list[i])
#         summ = 0
#         for j in range(len(possible_list[i])):
#             # print(j)
#             x, y = j, int(possible_list[i][j])
#             # print(x, y)
#             summ += arr[x][y]
#             if summ >= minn:
#                 break
#             # print(summ)
#         if summ < minn:
#             minn = summ
#
#
#     print(f'#{tc} {minn}')
#     # print('=' * 30)

#[[0, 0, 0, 0],
#[0, 73, 21, 21],
#[0, 11, 59, 40],
# 0, 24, 31, 83]]


# n = 5
# permu = []
# for i in range(0, n):
#     permu.append(str(i))
#
# print(permu)
# permu_list = map(list, permutations(permu, n))
#
# # for i in len(permu_list):
# #     print(permu_list[i])
#
# for i in permu_list:
#     a = i
#     print(a[0])
#
#     # for j in len()
#     # print(i)