import sys; sys.stdin = open('5201_컨테이너운반.txt')

t = int(input())
# print(t)
for tc in range(1, t+1):
    n, m = map(int, input().split())

    #cons에 컨테이너를 넣어주고, 내림차순 정렬
    cons = list(map(int, input().split()))
    cons.sort(reverse=True)
    # print(con)

    #trucks에 트럭을 넣어주고 내림차순 정렬
    trucks = list(map(int, input().split()))
    trucks.sort(reverse=True)
    summ = 0

    # 트럭을 기준으로 컨테이너를 순회
    # 트럭 용량에맞는 con을 찾으면 summ에 더하고 다음 트럭으로 넘어감
    for truck in trucks:
        for con in cons:
            if truck >= con:
                summ += con
                #한번 실린 con은 제거
                cons.remove(con)
                #break로 다음 트럭 찾아감
                break
    print(f'#{t} {summ}')













    # print(truck)
    # print(con)
    # for i in truck:
    #     for j in con:
    #         if i >= j:
    #             summ += j
    #             truck.remove(i)
    #             con.remove(j)
    # print(summ)

















    # summ = 0
    # while len(con) or len(truck):
    #     while con[0] > truck[0]:
    #         #너무 큰 컨테이너 버림
    #         con.pop(0)
    #
    #         if con[0] <= truck[0]:
    #             break
    #
    #     if len(con) == 0 or len(truck) == 0:
    #         break
    #
    #     for j in con:
    #         if con[0] <= truck[0]:
    #             truck.pop(0)
    #             a = con.pop(0)
    #             summ += a
    #         if len(con) == 0 or len(truck) == 0:
    #             break
    #     # break



    # print(con)
    # print(truck)
    # print(summ)












    # if truck[0] < con[0]:
    #     print(f'{tc} 0')
    #
    # n = 0
    # summ = 0
    # while truck[n] >= con[n]:
    #     summ += con[n]







