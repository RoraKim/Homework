# HomeWork

### Circle 인스턴스 만들기

아래와 같은 Circle 클래스가 있을 때, 반지름이 3이고 x, y좌표가 (2, 4)인 Circle 인스턴스를 만들어 넓이와 둘레를 출력하시오.

```python
class Circle:
    pi = 3.14
    
    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y
        
    def area(self):
        return self.pi * self.r * self.r
    
    def circumference(self):
        return 2 * self.pi * self.r
    
    def center(self):
        return (self.x, self.y)
```

``` python
C1 = Circle(3, 2, 4)
print(C1.area()) #28.259999999999998
print(C1.circumference()) #18.84
```



### Dog과 Bird는 Animal이다

다음과 같이 Animal 클래스가 주어질 때, 해당 클래스를 상속 받아 아래의 보기와 같이 동작하는 Dog 클래스와 Bird 클래스를 작성하시오.

```python
class Animal:
    def __init__(self, name):
        self.name = name
        
    def walk(self):
        print(f'{self.name}! 걷는다!')
        
    def eat(self):
        print(f'{self.name}! 먹는다!')
```

```python
dog = Dog('멍멍이')
dog.walk() # 멍멍이! 달린다!
dog.bark() # 멍멍이! 짖는다!

bird = Bird('구구')
bird.walk() # 구구! 걷는다!
bird.eat() # 구구! 먹는다!
bird.fly() # 구구! 푸드덕!
```

``` python
class Animal:
    def __init__(self, name):
        self.name = name
        
    def walk(self):
        print(f'{self.name}! 걷는다!')
        
    def eat(self):
        print(f'{self.name}! 먹는다!')


class Dog(Animal):

    def walk(self):
        print(f'{self.name}! 달린다!')

    def bark(self):
        print(f'{self.name}! 짖는다!')

class Bird(Animal):

    def fly(self):
        print(f'{self.name}! 푸드덕!')
```





### 오류의 종류

아래에 제시된 오류들이 각각 어떠한 경우에 발생하는지 간단하게 작성하시오.

```python
ZeroDivisionError: 0으로 나누려고 할 때
    
NameError: 정의 되지 않은 변수이름 사용
    
TypeError: 자료형에 대한 잘못된 사용 
    int('3') == 3
    int([123]) TypeError
    
IndexError: 인덱스 범위를 초과해서 조회하고자 할 때
KeyError: 딕셔너리에 없는 키를 조회하고자 할 때, 혹은 세트에 없는 값 삭제하거나 조회하려고 할 때
    
ModuleNotFoundError: 모듈을 찾을 수 없을 때 
    
ImportError: 모듈은 있는데 모듈에 없는 변수/클래스/함수를 찾고자 할 때
```

