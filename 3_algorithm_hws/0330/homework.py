
import sys; sys.stdin = open('병합정렬.txt')

def merge(left, right):
    # 뉴 배열..
    result = []

    # 이미 정렬된 배열 두개 비교하면서 인덱스 옮겨서 넣기
    # i -> 왼쪽 확인할 인덱스, j -> 오른쪽 확인..
    i = j = 0

    # left[i] right[j] 얘네 두개 비교할거다!
    while i < len(left) or j < len(right):

        # left랑 right  둘 다 요소가 남아있을때만 가능 ..
        if i < len(left) and j < len(right):
            # 더 작은쪽 가져와서 append
            # 가져온 쪽 인덱스 +1 시켜준다..
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        else:
            # 비교할 요소가 없는 상황!!!!!!!!
            # 1. 왼쪽만 남아있음
            if i < len(left):
                result.append(left[i])
                i += 1
            else:
                # 2. 오른쪽만 남아있음
                result.append(right[j])
                j += 1

    #쪼개진 값들이 정렬된 상태로 넘어감
    return result


def merge_sort(list):

    global cnt

    #더이상 list를 쪼갤 수 없으면
    if len(list) <= 1:
        return list
    #중앙값
    mid = len(list) // 2
    #left, right로 쪼개주기
    leftList = list[:mid]
    rightList = list[mid:]

    #각 각 나눠서 merge_sort 실시
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)
    #반 나눈애들끼리 맨 오른쪽 요소 비교
    if leftList[-1] > rightList[-1]:
        cnt += 1
    return merge(leftList, rightList)



t = int(input())
for tc in range(1, t+1):
    n = int(input())
    array = list(map(int, input().split()))
    cnt = 0

    sorted_array = merge_sort(array)
    # print(sorted_array)
    print(f'#{tc} {sorted_array[n//2]}', end=' ')
    print(cnt)




