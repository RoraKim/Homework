# from itertools import permutations
# n = 5
# permu = []
# for i in range(0, n):
#     permu.append(i)
#
# print(permu)
# permu_list = []
# for permu_item in map(list, permutations(permu, n)):
#     permu_list.append(permu_item)
# print(permu_list)
#
# #print(permu_list)
# for i in range(len(permu_list)):
#     print(permu_list[i])

#-=========================================================



# n : 현재 들어간 깊이  k : 합
def gongjang(n, k):
    global result
    # 만약에 현재 더한 합이 result보다 크면 가지치기
    if k >= result:
        return
    # 작은데 n == N이면 result 갱신 후 return
    elif n == N:
        result = k
        return
    # 둘 다 아니라면 재귀 들어감
    else:
        # N가지 경우의 수를 다 돌아야 함
        for i in range(N):
            # 만약에 check이 0이라면 방문 안했기 때문에 방문
            if check[i] == 0:
                check[i] = 1
                # 체크 한 후 재귀 들어감, 합에 product[제품(1, 2, 3)][깊이(각 공장)]을 더해줌
                gongjang(n+1, k + product[i][n])
                # 재귀에서 나오면 check 초기화
                check[i] = 0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    product = [list(map(int, input().split())) for _ in range(N)]
    # 조합을 만들 check 변수 생성
    check = [0] * N
    # 최소값을 저장해야 함
    result = 1500
    gongjang(0, 0)
    print(f'#{t} {result}')


    #======================================================

from itertools import permutations
from pprint import pprint

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # pprint(arr)

    permu = [x for x in range(n)]
    # print(permu)

    minn = 10e9
    for this_lst in permutations(permu, n):
        # print(this_lst)
        summ = 0
        row = 0
        for factory in this_lst:
            summ += arr[row][factory]
            if summ >= minn:
                break
            row += 1
            # print(summ)
        if summ < minn:
            minn = summ

    print(f'#{tc} {minn}')