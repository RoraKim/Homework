![image-20220330141713328](homework.assets/image-20220330141713328.png)





### 퀵정렬 

-  기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법 
- 일반적인 상황에서 가장 많이 사용되는 알고리즘중 하나이다. 
- 병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘이다.
- 가장 기본적인 퀵 정렬은 첫번쨰 데이터를 기준 데이터(pivot)으로 설정합니다. 



![image-20220330131530564](homework.assets/image-20220330131530564.png)

5가 피벗, 왼쪽에서부터 5보다 큰 데이터를 선택 -> 7이 선택, 오른쪽에서 부터 5보다 작은 데이터를 선택 -> 4가 선택 

: 4와 7의 위치가 바뀜 

![image-20220330131646348](homework.assets/image-20220330131646348.png)



위치가 엇갈리는 경우 

피벗과 작은데이터의 위치를 서로 변경 

![image-20220330132214428](homework.assets/image-20220330132214428.png)



----

이렇게 되면 피벗을 기준으로 왼쪽에 있는 데이터는 모두 5보다 작고, 오른쪽에 있는 데이터는 모두 5보다 크다는 특징이 생김. 이렇게 피벗을 기준으로 데이터 묶음을 나누는 작업을 분할이라고 함.

![image-20220330132450858](homework.assets/image-20220330132450858.png)

다시 왼쪽에 있는 데이터를 상대로 퀵정렬 수행 

오른쪽 데이터 상대로 퀵정렬 수행 

재귀적으로 수행되며, 정렬될 때 마다 정렬되는 범위가 재귀적으로 점점 좁아지는 형태 

-----



### 퀵정렬 소스코드: 재귀 

```python
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
def quick_sort(array, start, end):
    if start >= end: #원소가 한개라는 뜻
        return #함수 종료
    pivot = start
    left = start + 1
    right = end
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
```

-----



### 퀵 정렬 소스코드 : pythonic

```python
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

print(quick_sort(array))
```

