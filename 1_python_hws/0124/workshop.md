### 1. 평균 점수 구하기

#####  key 값으로 과목명, value 값으로 점수를 가지는 dictionary를 전달 받아, 전체 과목의 평균 점수를 반환하는 함수 get_dict_avg 함수를 작성하시오.

``` python
get_dict_avg({
    'python' : 80,
    'algorithm' : 90,
    'django' : 89,
    'web' : 83,       
})
```

``` python
def get_dict_avg(a):
    add = 0
    count = 0
    for val in a.values():
        add += int(val)
        count += 1

    return add / count



get_dict_avg({
    'python' : 80,
    'algorithm' : 90,
    'django' : 89,
    'web' : 83,       
})
```













### 2. 혈액형 분류하기 

##### 여러 사람의 혈액형(A, B, AB, O)에 대한 정보가 담긴 list를 전달 받아, key는 혈액형의 종류, value는 사람 수인 dictionary를 반환하는 count_blood 함수를 작성하시오.

```python
count_blood([
    'A', 'B', 'A', 'O', 'AB', 'AB',
    'O', 'A', 'B', 'O', 'B', 'AB',
])
```

``` python
def count_blood(blood):
    li = []
    
    for i in blood :
        li.append(i)
        
    idx = list(set(li))
    
    cnt = {}
    for i in idx :
        cnt[i] = blood.count(i)
        
    return cnt   
```

``` python
def count_blood(bloods):
    blood_dict = {}
    for blood in bloods:
        #blood_dict['key'] - 에러 
        #blood_dict.get() - none
        if blood_dict.get(blood):
            blood_dict[blood] += 1
    
            
        else:
            blood_dict[blood] = 1
    return blood_dict
        
        
```

``` python
def count_blood(blood):
    #안에 있는 각 값들에 해당하는 
    #키를 가진 딕셔너리를 만들고
    #그 키에 해당하는 값들을 채워 나가야 한다. 
    result = {}
    #전체 리스트 반복문 돌려서 
    for val in blood:
        #만약에 result에 해당하는 키 값이 있다면 +1
        if result[val]#=> 대괄호 접근의 경우...
        	#값이 없더라도 키에러가 발생하지 않도록
            if result.get(val):
        	result[val] += 1
            #없으면? 최초로 할당
            else:
                result[val] = 1 #값을 뭘 넣어야 할까?
```

