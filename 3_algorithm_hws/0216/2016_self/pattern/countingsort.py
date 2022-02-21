def countingsort(input_arr, k):
    counting_arr = [0] * (k + 1)

    for i in input_arr:
        counting_arr[i] += 1
    print(counting_arr)

    for i in range(1, len(counting_arr)):
        counting_arr[i] += counting_arr[i - 1]

    print(counting_arr)

    result_arr = [-1] * len(input_arr)

    for i in input_arr:
        counting_arr[i] -= 1
        result_arr[counting_arr[i]] = i
    return result_arr

input_arr = [1, 3, 2, 5]
k = 9
print(countingsort(input_arr, k))
































# def countingsort(input_arr, k):
#     #k는 들어갈 수 있는 수의 범위
#     counting_arr = [0] * (k + 1)
#
#     for i in input_arr:
#         counting_arr[i] += 1
#
#
#
#     for i in range(1, len(counting_arr)):
#         counting_arr[i] += counting_arr[i - 1]
#
#     result_arr = [-1] * len(input_arr)
#
#     for i in input_arr:
#         counting_arr[i] -= 1
#         result_arr[counting_arr[i]] = i
#
#     return result_arr
#
#     print(counting_arr)
# input_arr = [1, 5, 4, 6, 7]
# print(countingsort(input_arr, 9))
