### 1. 모음은 몇 개나 있을까? 

##### 문자열을 전달 받아 해당 문자열의 모음 갯수를 반환하는 count_vowels 함수를 작성하시오. 단, .count() 메서드를 활용하여 작성하시오.



``` python
count_vowels('apple')
count_vowels('banana')
```

``` python
def count_vowels(a):
    result = a.count('a') + a.count('e') + a.count('i') + a.count('o') + a.count('u')
    return(a)
```

``` python
def count_vowels(word):
    result = 0
    for i in 'aeiou':
        result += word.count(i)
    return result
```



------



### 2. 문자열 조작

#####  다음 중, 문자열(string)을 조작하는 방법으로 옳지 않은 것을 고르시오.

```
(1) .find(x)는 x의 첫번째 위치를 반환한다. 없으면 -1을 반환한다. 

(2) .split([chars])은 특정 문자를 지정하면 문자열을 특정 문자를 기준으로 나누어 list로 반환한다. 특정 문자를 지정하지 않으면 공백을 기준으로 나눈다. 

(3) .replace(old, new[, count])는 바꿀 대상 문자를 새로운 문자로 바꿔서 반환한다. 

(4) .strip([chars])은 특정 문자를 지정하면, 양쪽에서 해당 문자를 찾아 제거한다. 특정 문자를 지정하지 않으면 오류가 발생한다.
```

``` 
(4)번 .strip([chars])는 특정 문자를 지정하지 않으면 공백을(개행문자)제거한다.
```



### 3. 정사각형만 만들기

#####  각각 너비와 높이의 값으로 이루어진 2개의 list를 전달 받아, 각각의 값들을 조합하여 만들 수 있는 정사각형만의 넓이를 담은 list를 반환하는 only_square_area 함수를 작성하시오.

``` python
only_square_area([32, 55, 63], [13, 32, 40, 55])
```

``` python
def only_square_area(a,b):
    my_list=[]
    for i in a:
        for j in b:
            if i == j:
                my_list.append(i*j)
    
    return my_list            
```

``` python
def only_square_area(widths,heights):
    #리스트 컴프리헨션 
    #리스트에 최종적으로 추가할 값 + 반복문 순서대로 + 조건
    comb = [width * height for width in widths for height in heights if width == height]
    
    return comb
```

``` python
#정사각형이란 건 결국 높이와 너비가 같다는 뜻 
#그 말은 두 리스트를 비교했을 때 중복되는 값만 찾으면 된다...
value = set(widths) & set(heights)
result = []
	for val in value:
        result.append(val**2)
return result
```

``` python
return[val**2 fir val in set(widths) & set(heights)]
```

