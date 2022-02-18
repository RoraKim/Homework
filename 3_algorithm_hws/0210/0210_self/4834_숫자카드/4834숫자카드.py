def max(arr):
    max_num = arr[0]
    for i in arr:
        if max_num <= i:
            max_num = i

    return max_num

def counting_sort(arr, n):
    #n은 들어갈 수 있는 원소의 범위
    counts = [0] * (n + 1)

    for i in range(len(arr)):
        counts[arr[i]] += 1

    return counts


import sys; sys.stdin = open('4834.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    input_arr = list(map(int, input()))

    counts = counting_sort(input_arr, 9)
    max_card = 0
    max_num = 0

    for i in range(10):
        if max_num <= counts[i]:
            max_num = counts[i]
            max_card = i

    print(f'#{tc}',max_card,max_num)

























# import sys
# sys.stdin = open('4834.txt')
# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())
#     input_arr = list(map(int, input()))
#     counting_arr = [0] * 10
#
#     # counting_arr에 arr내 원소의 빈도수 담기
#     for i in range(0, len(input_arr)):
#         counting_arr[input_arr[i]] += 1
#     # print(counting_arr)
#
#     # 누적 counting_arr 업데이트
#     for i in range(1, len(counting_arr)):
#         counting_arr[i] += counting_arr[i - 1]
#     # print(counting_arr)
#
#     #result arr 생성
#     result_arr = [-1] * len(input_arr)
#
#     # result_arr에 정렬하기(counting_arr을 참조)
#     for i in range(len(result_arr) -1, -1, -1):
#         counting_arr[input_arr[i]] -= 1
#         result_arr[counting_arr[input_arr[i]]] = input_arr[i]
#
#     print(f'{tc} {max(result_arr)} {input_arr.index(max(result_arr))}')
#
#
#
