### 1. List의 합 구하기

####  정수로만 이루어진 list를 전달 받아 해당 list의 모든 요소들의 합을 반환하는 list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오.

``` python
list_sum([1, 2, 3, 4, 5]) #=> 15
```

``` python
def list_sum(a):
    total = 0
    for num in a:
        total = total + num
    return total     

print(list_sum([1, 2, 3, 4, 5]))
```









### 2. Dictionary로 이루어진 List의 합 구하기

####  Dictionary로 이루어진 list를 전달 받아 모든 dictionary의 'age' key에 해당하는 value 들의 합을 반환하는 dict_list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오.

``` python
dict_list_sum([{'name' : 'kim', 'age' : 12},
               {'name' : 'lee', 'age' : 4}])  #=>16
```

``` python
def dict_list_sum(a):
    age = 0
    for i in a:
        age += i['age']
    return age
```





---



### 3. 2차원 List의 전체 합 구하기

####  정수로만 이루어진 2차원 list를 전달 받아 해당 list의 모든 요소들의 합을 반환하는 all_list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오.

``` python
all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]) #=>55

```

``` python
def all_list_sum(a):
    total = 0
    for i in a:
        for j in i:
            total += j
    return total         
```

