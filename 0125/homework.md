# HomeWork

### Built-in 함수와 메서드

sorted()와 .sort()의 차이점을 코드의 실행 결과를 활용하여 설명하시오.

``` python
a= [10, 5, 6, 1, 8]
result = a.sort()
print(a, result)

#결과
[1, 5, 6, 8, 10] None - 원본이 변경됨 
```

``` python
a= [10, 5, 6, 1, 8]
result = sorted(a)
print(a, result)

#결과
[10, 5, 6, 1, 8] [1, 5, 6, 8, 10] - 원본이 변경되지 않음.result가 변경값 반환 
```



### .extend()와 .append()

.extend()와 .append()의 차이점을 코드의 실행 결과를 활용하여 설명하시오.

``` python
cafe = ['starbucks', 'hollys', 'toms']
print(cafe)
cafe.extend(['coffee'])
print(cafe)

#값
['starbucks', 'hollys', 'toms']
['starbucks', 'hollys', 'toms', 'coffee']
```

``` python
cafe = ['starbucks', 'hollys', 'toms']
print(cafe)
cafe += (['coffee'])
print(cafe)

#값
['starbucks', 'hollys', 'toms']
['starbucks', 'hollys', 'toms', 'coffee']
```

``` python
cafe = ['starbucks', 'hollys', 'toms']
print(cafe)
cafe.append('coffee')
print(cafe)

#값
['starbucks', 'hollys', 'toms']
['starbucks', 'hollys', 'toms', 'coffee']
```

``` python
cafe.append(['coffee'])
#['starbucks', 'hollys', 'toms', ['coffee']]

cafe.extend(['coffee'])
#['starbucks', 'hollys', 'toms', 'coffee']

cafe.append('coffee')
#['starbucks', 'hollys', 'toms', 'coffee']

cafe.extend('coffee')
#['starbucks', 'hollys', 'toms', 'c', 'o', 'f', 'f', 'e', 'e']
```



### 복사가 잘 된 건가?

아래의 코드를 실행 하였을 때, 변수 a와 b에 담긴 list의 요소가 같은지 혹은 다른지
여부를 판단하고 그 이유를 작성하시오.

```python
a = [1, 2, 3, 4, 5]
b = a

a[2] = 5

print(a)
print(b)
```

``` python
#값
[1, 2, 5, 4, 5]
[1, 2, 5, 4, 5]

대입 연산자 = 
해당 주소의 일부 값을 변경하는 경우 이를 참조하는 모든 변수에 영향
```

