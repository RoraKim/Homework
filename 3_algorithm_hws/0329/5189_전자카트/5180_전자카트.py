import sys; sys.stdin = open('5180_전자카트.txt')
import time
start = time.time()
from pprint import pprint

#permu 함수를 만들어서 1로 시작하는 result만 구한다
#해당 result값의 [j], [j+1] 인덱스를 이용해
# arr해당값의 합을 구한다.

return_arr = []
#return_arr에 [[1,2,3], [1, 3, 2]] 형식으로 담기게함
def permu(l):
    if l == r:
        if result[0] != 1 and result[0] != 0:
            pass

        elif result[0] == 1:
            copy_result = result[:]
            return_arr.append(copy_result)
            return return_arr

    else:
        for i in range(n):
            if result[0] != 1 and result[0] != 0:
                continue
            elif checklist[i] == 0:
                result[l] = permu_n[i]
                # if result[0] != 1 and result[0] != 0:
                #     break
                # print(result)
                checklist[i] = 1
                permu(l + 1)
                checklist[i] = 0

    return return_arr

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [[0]*(n+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
    permu_n = [i for i in range(1, n+1)]
    # print(permu_n)
    r = n
    result = [0] * r
    checklist = [0] * n
    permu(0)



    #arr의 값들 중 최소합을 구하기
    minn = 100000000000000000
    summ = 0
    for i in range(len(return_arr)):
        return_arr[i].append(1)
    # print(return_arr)
    for i in return_arr:
        for j in range(len(i) - 1):
            summ += arr[i[j]][i[j+1]]
        if summ < minn:
            minn = summ
        summ = 0

    print(f'#{tc} {minn}')
    print("time :", time.time() - start)
    return_arr = []






