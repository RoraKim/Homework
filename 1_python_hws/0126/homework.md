### 1 . Type Class

####  Python은 객체 지향 프로그래밍 언어이다. Python에서 기본적으로 정의되어 있는 클래스를 최소 5가지 이상 작성하시오.

``` python
int, str, list, tuple, dict, float, complex, map, zip
```



----

### 2. Magic Method 

#### 아래에 제시된 매직 메서드들이 각각 어떠한 역할을 하는지 간단하게 작성하시오.

``` python
--init-- : 생성자(인스턴스가 생성될 때 실행)
--del-- : 소멸자(인스턴스가 소멸될 때 실행)
--str-- : 
    사람이 보기 좋게 출력
    str(Object),format(),print()에 의해서 호출되는 방식
--repr-- : 
    기계 혹은 개발자가 보기 좋게 출력
    디버깅에 사용되기 때문에, 조금 더 많은 정보를 담은 형태로 출력
```

### \__str__과 \_\_repr\_\_

``` python
from datetime import datetime
now = datetime.now()

print(str(now)) #2022-02-02 18:07:16.513325

print(repr(now)) #datetime.datetime(2022, 2, 2, 18, 7, 16, 513325)
```





### 3. Instance Method

####  .sort()와 같이 문자열, 리스트, 딕셔너리 등을 조작 할 때 사용하였던 것들은 클래스에 정의된 메서드들이었다. 이처럼 문자열, 리스트, 딕셔너리 등을 조작하는 메서드를 최소 3가지 이상 그 역할과 함께 작성하시오.



``` python
.index()
.update()
.replace(old, new)

list : append, pop, remove
str : split, join, power
dict : get, update
```





----

### 4. Module Import



``` python
#fibo.py

def fibo_recursion(n):
    if n < 2:
        return n 
    else:
        return fibo_recursion(n-1) + fibo_recursion(n-2)
```



#### 위와 같은 코드가 같은 폴더 안의 fibo.py 파일에 작성되어 있을 때, 아래와 같은 형태로 함수를 실행 할 수 있도록 하는 import 문을 빈칸 (a), (b), (c)를 채워 넣어 완성하시오.



``` python
from __(a)__ import __(b)__ as __(c)__

recursion(4)
```

``` py
from fibo import fibo_recursion as recursion
```
