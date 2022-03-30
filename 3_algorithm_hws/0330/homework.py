array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
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

print(array) #[5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
quick_sort(array, 0, len(array) - 1)
print(array) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
def quick_sort(array):
    #리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    #피벗은 첫번째 원소
    pivot = array[0]
    # 피벗을 제외한 리스트
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot] #분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] #분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(array)
print(quick_sort(array))