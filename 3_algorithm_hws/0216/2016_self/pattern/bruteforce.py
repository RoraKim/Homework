# arr = [[1,2,3], [4,5,6],[7,8,9]]
# arr = list(map(list, zip(*arr)))
# print(arr)

#
# arr = [3,4,5,6]
# n = len(arr)
#
# def bit(arr, n):
#     for i in range(1<<n):
#         for j in range(n):
#             if i & (1<<j):
#                 print()[j], end=' '
#         print()
#
# print(bit(arr, n))

#
#
# arr = [3, 6, 7, 1, 5, 4]
# def a(arr):
#     n = len(arr)  # n:원소의 개수
#     main_lst = []
#     for i in range(2**n):
#         sub_lst = []
#         for j in range(n):
#             if i & (2**j):
#                 sub_lst.append(arr[j])
#         main_lst.append(sub_lst)
#     return main_lst
# b = a(arr)
#
# print(b)

# [[], [3], [6], [3, 6], [7], [3, 7], [6, 7], [3, 6, 7], [1], [3, 1], [6, 1], [3, 6, 1], [7, 1], [3, 7, 1], [6, 7, 1], [3, 6, 7, 1], [5], [3, 5], [6, 5], [3, 6, 5], [7, 5], [3, 7, 5], [6, 7, 5], [3, 6, 7, 5], [1, 5], [3, 1, 5], [6, 1, 5], [3, 6, 1, 5], [7, 1, 5], [3, 7, 1, 5], [6, 7, 1, 5], [3, 6, 7, 1, 5], [4], [3, 4], [6, 4], [3, 6, 4], [7, 4], [3, 7, 4], [6, 7, 4], [3, 6, 7, 4], [1, 4], [3, 1, 4], [6, 1, 4], [3, 6, 1, 4], [7, 1, 4], [3, 7, 1, 4], [6, 7, 1, 4], [3, 6, 7, 1, 4], [5, 4], [3, 5, 4], [6, 5, 4], [3, 6, 5, 4], [7, 5, 4], [3, 7, 5, 4], [6, 7, 5, 4], [3, 6, 7, 5, 4], [1, 5, 4], [3, 1, 5, 4], [6, 1, 5, 4], [3, 6, 1, 5, 4], [7, 1, 5, 4], [3, 7, 1, 5, 4], [6, 7, 1, 5, 4], [3, 6, 7, 1, 5, 4]]
#
#
# arr = [3, 6, 7, 1, 5, 4]
# def setsetset(arr):
#     sub_set = [[]]
#     for i in arr:
#         len_ = len(sub_set)
#         for j in range(len_):
#             sub_set.append(sub_set[j] + [i])
#     return sub_set
#
# print(setsetset(arr))


# def binary(a, N, key):
#     start = 0
#     end = N - 1
#
#     while start <= end:
#         middle = (start + end) // 2
#         if a[middle] == key:
#             return True, middle
#         elif a[middle] > key:
#             end = middle - 1
#         else:
#             start = middle + 1
#     return False
#
# a = [1, 3, 5, 7, 9]
# N = 5
# key = 3
# print(binary(a, N, key))


#k번째로 작은 원소를 찾는 알고리즘
#1번부터 k번째까지 작은 원소들을 찾아 배열의 앞쪽으로 이동시키고, 배열의 k번째를 반환
def select(arr, k):
    # 아우터 루프가 한번 돌 때 마다 element하나의 최종위치가 확정
    for i in range(0, len(arr) -1): #0에서 k-1까지 비교하므로 오름차순으로 정렬되기 때문에
        minidx = i
        #이너 루프 가장 작은 숫자를 찾기 위해 순차적으로 이동
        #i는 이미 정렬되어 있는 원소의 갯수
        #len(arr)모든 엘리먼트를 다 봄
        for j in range(i + 1, len(arr)):
            if arr[minidx]>arr[j]:
                minidx = j
        arr[i],arr[minidx] = arr[minidx], arr[i]
    return arr, arr[k-1] #k-1번째 값이 k번째로 작은 값이 된다(인덱스조회는 0부터 해주므로)


arr = [5, 4, 3, 6, 2]
k = 2
print(select(arr, k))











# p = 'love' #찾을 패턴
# t = 'I love you' #주어진 텍스트
# m = len(p) #패턴의 길이
# n = len(t) #텍스트의 길이
#
#
# def bruteforce(p, t):
#     i = 0
#     j = 0
#     #i와 j가 각각 패턴과 전체 텍스트의 길이를 벗어나지 않는 동안
#     while j < m and i < n:
#         if p[j] != t[i]:
#              i = i - j
#              j = -1
#         i += 1
#         j += 1
#
#     if j == m:
#         return i - m
#
#     else:
#         return -1
#
#
# print(bruteforce(p,t))
#
#
# def bruteforce(p,t):
#     i = 0 #n - text길이
#     j = 0 #m - 패턴 길이
#     while j < m and i < n:
#         if p[j] != t[i]:
#             i = i - j
#             j = -1
#         i += 1
#         j += 1
#
#     if j == m:
#         return i - j
#
#     else:
#         return -1
#
#
#
#










# p = 'is' #찾을 패턴
# t = 'That is book' #전체 텍스트
# m = len(p) #찾을 패턴의 길이
# n = len(t) #전체 텍스트의 길이
#
# def Bruteforce(p, t):
#     i = 0
#     j = 0
#     #j와 i가 각각 패턴과 전체 텍스트의 길이를 벗어나지 않는 동안
#     while j < m and i < n:
#         # 패턴의 글자와 텍스트의 글자가 다르면
#         if p[j] != t[i]:
#             #패턴은 0으로 리셋, i는 다음글자로 가도록
#             i = i - j
#             #if를 빠져나가자 마자 j + 1로 인해 0이 됨
#             j = -1
#         #패턴과 텍스트가 일치하면 1씩 증가
#         i += 1
#         j += 1
#     #while문이 끝난 이유가 패턴의 끝에 도달했기 때문이라면
#     #어느 인덱스에서부터 패턴이 맞았는지 보여줌줌
#     f j == m:
#         return i - j
#
#     else:
#         return -1
#
#
#
# print(Bruteforce(p,t))
#
#

#     i = 0
#     j = 0
#     while j < m and i < n:
#         if t[i] != p[j]:
#             i = i - j
#             j = -1
#         i = i + 1
#         j = j + 1
#
#     if j == m:
#         return i - m
#     else:
#         return -1
#
# print(Bruteforce(p,t))