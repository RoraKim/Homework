import sys
sys.stdin = open('4839_이진탐색.txt')
t = int(input())
for tc in range(1, t+1):
    p, a, b = map(int, input().split())
    # print(a, b)

    def bynarySearch(p, a)
    start = 0
    end = p - 1

    count_a = 0
    # while start <= end:
    #     middle = (start + end) // 2
    #     if middle == a:#중앙값이 내가 원하는 값이면 끝남
    #         count_a += 1
    #         break
    #
    #
    #     elif middle > a: #원하는 값이 아니고, 원하는 값이 중앙값 보다 앞에 위치
    #         count_a += 1
    #         end = middle - 1
    #
    #     else: #원하는 값이 중앙값 보다 뒤에 위치
    #         count_a += 1
    #         start = middle + 1

    count_b = 0
    while start <= end:
        middle = (start + end) // 2
        if middle == b:  # 중앙값이 내가 원하는 값이면 끝남
            count_b += 1
            print(count_b)
            break
        elif middle > b:  # 원하는 값이 아니고, 원하는 값이 중앙값 보다 앞에 위치
            count_b += 1
            end = middle - 1

        else:  # 원하는 값이 중앙값 보다 뒤에 위치
            count_b += 1
            start = middle + 1
