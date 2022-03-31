

def quick_sort(array, start, end):
    if start >= end: #원소가 한개라는 뜻
        return #함수 종료
    #첫번째 원소를 pivot으로 설정
    pivot = start
    #첫번째 원소를 제외하고 가장 왼쪽원소를 left
    left = start + 1
    #가장 오른쪽 원소를 right
    right = end
    #엇갈릴때까지 반복
    while(left <= right):
        #피벗보다 큰 데이터를 찾을때 까지 반복
        while(left<= end and array[left] <= array[pivot]):
            left += 1
        #피벗보다 작은 데이터를 찾을때 까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1

        if left > right: #엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]

        else: #엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[right], array[left] = array[left], array[right]

    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right -1)
    quick_sort(array, right +1, end)
    return arr

# print(array) #[5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
# quick_sort(array, 0, len(array) - 1)
# print(array) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    sorted_arr = quick_sort(arr, 0, len(arr) - 1)
    print(f'#{tc} {sorted_arr[n//2]}')




# def quick_sort(array):
#     #리스트가 하나 이하의 원소만을 담고 있다면 종료
#     if len(array) <= 1:
#         return array
#     #피벗은 첫번째 원소
#     pivot = array[0]
#     # 피벗을 제외한 리스트
#     tail = array[1:]
#
#     left_side = [x for x in tail if x <= pivot] #분할된 왼쪽 부분
#     right_side = [x for x in tail if x > pivot] #분할된 오른쪽 부분
#
#     # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고 전체 리스트 반환
#     return quick_sort(left_side) + [pivot] + quick_sort(right_side)
#
# # print(array)
# # print(quick_sort(array))
#
# t = int(input())
# for tc in range(1, t+1):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     sorted_arr = quick_sort(arr)
#     print(f'#{tc} {sorted_arr[n//2]}')



#============================================================

# import sys;
#
# sys.stdin = open('input.txt')
#
#
# def qSort(arr, s, e):
#     if s < e:
#         p = lomuto_partition(arr, s, e)
#         qSort(arr, s, p - 1)
#         qSort(arr, p + 1, e)
#
#
# def hoare_partition(arr, left, right):
#     pivot = arr[left]
#     i = left
#     j = right
#     while i <= j:
#         while i <= j and arr[i] <= pivot:
#             i += 1
#         while i <= j and arr[j] >= pivot:
#             j -= 1
#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[left], arr[j] = arr[j], arr[left]
#     print(arr)
#     return j
#
#
# def lomuto_partition(arr, left, right):
#     x = arr[right]
#     i = left - 1
#     for j in range(left, right):
#         if arr[j] <= x:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i + 1], arr[right] = arr[right], arr[i + 1]
#     print(arr)
#     return i + 1
#
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     arr = list(map(int, input().split()))
#     print(arr)
#     e = len(arr) - 1
#     s = 0
#     qSort(arr, s, e)


#==================================================================

#==================================================================================

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[-1]
        smaller, equal, larger = [], [], []
        for num in arr:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)

        return quicksort(smaller) + equal + quicksort(larger)


test_case = int(input())
for tc in range(1, test_case+1):
    n = int(input())
    unsorted_list = list(map(int, input().split()))
    print(f'#{tc} {quicksort(unsorted_list)[n//2]}')