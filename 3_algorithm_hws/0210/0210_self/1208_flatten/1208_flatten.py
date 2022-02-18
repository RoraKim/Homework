import sys
sys.stdin = open('1208_flatten.txt')

def len(arr):
    counts = 0
    for i in arr:
        counts += 1
    return counts

def bubble_sort(arr, n):
    for i in range(n-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

for tc in range(1, 11):
    dump = int(input())
    boxs = list(map(int, input().split()))
    sorted_boxs = bubble_sort(boxs, len(boxs))
    while dump > 0:
        sorted_boxs[0] += 1
        sorted_boxs[-1] -= 1
        dump -= 1
        sorted_boxs = bubble_sort(boxs, len(boxs))
        if sorted_boxs[0] == sorted_boxs[-1] or abs(sorted_boxs[0] - sorted_boxs[-1]) == 1:
            # print(f'#{tc}', sorted_boxs[-1] - sorted_boxs[0])
            break

    print(f'#{tc}', sorted_boxs[-1] - sorted_boxs[0])















# def len(arr):
#     counts = 0
#     for i in arr:
#         counts += 1
#     return counts
#
# def bubble_sort(arr, n):
#     for i in range(n-1, 0, -1):
#         for j in range(i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
#     return arr
#
# for tc in range(1, 11):
#     dump = int(input())
#     boxs = list(map(int, input().split()))
#
#     while dump >= 0:
#         sorted_boxs = bubble_sort(boxs,len(boxs))
#         sorted_boxs[0] += 1
#         sorted_boxs[-1] -= 1
#         dump -= 1
#         if sorted_boxs[0] == sorted_boxs[-1] or abs(sorted_boxs[0] - sorted_boxs[-1]) == 1:
#             # print(f'#{tc}', sorted_boxs[-1] - sorted_boxs[0])
#             break
#
#
#     print(f'#{tc}',sorted_boxs[-1] - sorted_boxs[0] + 2)
#






















# import sys
# sys.stdin = open('1208_flatten.txt')
#
#
# for tc in range(1, 11):
#     dump_num = int(input())
#     box = list(map(int, input().split()))
#
#     max_box = 0
#     min_box = 101
#     for i in box:
#
#         if i > max_box:
#             max_box = i
#         if i < min_box:
#             min_box = i
#
#
#         if max_box != 101 and min_box != 0:
#             idx_max = box.index(max_box)
#             idx_min = box.index(min_box)
#             box[idx_max] = max_box-1
#             box[idx_min] = min_box + 1
#             dump_num -= 1
#
#
#
#         if max_box - min_box < 2:
#             print(max_box - min_box)
#
#         if dump_num == 0:
#             print(max_box - min_box)
#
#
#             -------------------------------------------------------------
#             h_cnt = [0] * 101
#             min_v = 101
#             max_v = 0
#
#             박스의 높이를 카운트 하면서 h_cnt 최고점과 최저점을 찾기
#             for i in range(100):
