import sys; sys.stdin = open('5203_베이비진게임.txt')

# babugin이 완성되면 player번호를 return하는 함수
def babygin(arr, player):
    #counting 배열 활용
    counting = [0] * 10
    for i in arr:
        counting[i] += 1
    # print(counting)

    for j in range(10):
        #triplet일때의 조건
        if counting[j] !=0 and counting[j] % 3 == 0:
            return player
            break

    for k in range(8):
        #run일때의 조건
        if counting[k] >=1 and counting[k + 1] >=1 and counting[k + 2] >=1:
            return player
            break


t = int(input())
for tc in range(1, t+1):
    arr = list(map(int, input().split()))

    arr_1 = []
    arr_2 = []
    for i in range(0, 12, 2):
        arr_1.append(arr[i])
        arr_2.append(arr[i+1])


        # print(arr_1)
        # print(arr_2)
        #한개씩 증가하고 있는 arr_1, arr_2를
        #원소수가 3 이상일 때 부터 babygin()검증
        if len(arr_1) >=3:
            if babygin(arr_1, 1) == 1:
                print(f'#{tc} 1')
                break


        if len(arr_2) >=3:
            if babygin(arr_2, 2) == 2:
                print(f'#{tc} 2')
                break

    else:
        print(f'#{tc} 0')


# a = [1, 2, 3, 4, 4, 4]
# print(babygin(a, 1))


