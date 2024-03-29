#
#
# def counting_sort(input_arr, n):
# #     # n은 원소의 범위
# #     # input_arr는 정렬할 값
#
#     # 원소의 범위 만큼 인덱스를 담을 배열을 생성
#     counts = [0] * (n + 1)
#     # print(counts) #[0, 0, 0, 0, 0, 0]
#
#     # input_arr을 순회하며 횟수를 counts에 누적시킴
#     # range(len(input_arr)) : 결과적으로 인풋 index 처음부터 끝까지임
#     for i in range(len(input_arr)):
#         counts[input_arr[i]] += 1
#
#     # print(counts) #[1, 3, 1, 1, 2, 0]
#
#     #원소의 범위만큼 레인지를 정하면 맨 마지막 직전의 인덱스까지 감
#     #그 마지막 인덱스를 count i + 1이 채워줌
#     for i in range(n):
#         counts[i + 1] += counts[i]
#
#     # print(counts) #[1, 4, 5, 6, 8, 8]
#
#     #원래 input_arr를 재정렬해서 넣어줄 arr를 생성
#     #result_arr는 물론 input_arr와 같은 크기여야할 것이다.
#     result_arr = [-1] * len(input_arr)
#
#     for i in range(len(input_arr) - 1,-1, -1):
#         counts[input_arr[i]] -= 1
#         result_arr[counts[input_arr[i]]] = input_arr[i]
#
#     return result_arr
#     # print(counts)
#     # print(result_arr)
#
#
#
# a = [0, 4, 1, 3, 1, 2, 4, 1]
#
# print(counting_sort(a, 5)) # [0, 1, 1, 1, 2, 3, 4, 4]


def counting_sort(input_arr, k):
    """
    input_arr : 입력 배열(1 to k)
    counting_arr : 카운트 배열
    k는 데이터의 개수가 아닌 데이터 원소의 범위
    """

    counting_arr = [0] * (k+1)

    # 1. counting array에 arr내 원소의 빈도수 담기
    # for i in range(0, len(input_arr)):
    #     counting_arr[input_arr[i]] += 1
    for i in input_arr:
        counting_arr[i] += 1
    print(counting_arr)

    # 2. 누적(counting_arr 업데이트)
    for i in range(1, len(counting_arr)):
        counting_arr[i] += counting_arr[i - 1]

    print(counting_arr)
#
    # 3. result_arr 생성
    result_arr = [-1] * len(input_arr)
#
    # 4. result_arr에 정렬하기(counting_arr를 참조)
    # for i in range(len(result_arr) - 1, -1, -1):
    #     counting_arr[input_arr[i]] -= 1
    #     result_arr[counting_arr[input_arr[i]]] = input_arr[i]
    for i in input_arr:
        counting_arr[i] -= 1
        result_arr[counting_arr[i]] = i

    return result_arr


a = [0, 4, 1, 3, 1, 2, 4, 1]
print(a)

print(counting_sort(a, 5)) # [0, 1, 1, 1, 2, 3, 4, 4]