# WorkShop

### 무엇이 중복일까

문자열을 전달 받아 해당 문자열에서 중복해서 나타난 문자들을 담은 list를 반환하는
duplicated_letters 함수를 작성하시오.

```python
duplicated_letters('apple') # => ['p']
duplicated_letters('banana') # => ['a', 'n']
```

``` python
def duplicated_letters(a):
    new_lst = []
    for i in a:
        if a.count(i)>1:
            new_lst.append(i)
            result = list(set(new_lst))
                
    return result
```

``` python
def duplicated_letters(word):
    #중복되 글자들 찾아서
    #리스트에 담아서 반환
    result = []
    #중복된 글자?
    #넘겨받은 word에 두개 이상 출몰하는 글자 
    #count메서드 쓰면 몇개인지 확인 가능 
    for char in word:
        #각 알파벳이 단어에 2번 이상 있다면
        if word.count(char) >= 2:
            #추가 하기전에 또다른 조건을 생각해 내자 
            #이미 result에 있으면 안넣는다.
            #혹은 아직 없으면 넣는다. 
            if char not in result:
                result.append(char)
    return result
```

``` python
if 안의 if는 and or 사용해서
한번에 if쓸 수 있음
```



### 소대소대

문자열을 전달 받아 해당 문자열을 소문자와 대문자가 번갈아 나타나도록 변환하여
반환하는 low_and_up 함수를 작성하시오. 이때, 전달 받는 문자열은 알파벳으로만
구성된다.

```python
low_and_up('apple') # =>aPpLe
low_and_up('banana')  # => bAnAnA
```

``` python
def low_and_up(word):
    result = ''
    for idx in range(len(word)):
        #단어의 idx 번째에 해당하는 값을 소문자나 대문자로 바꿔서 더하기
        # result += word[idx].???
        result += word[idx]

    for idx, char in enumerate(word):
        print(idx, char)
        #만약에 idx % 2 == 1
        if idx % 2 == 1:
            result += char.upper()

        else:
            result += char.lower()
    return result
```

```python
result=[char.upper() if idx%2 else char.lower()for idx, char in enumerate(word)]
#값 
['a', 'P', 'p', 'L', 'e']
return ''.join(result)
```





### 솔로 천국 만들기

정수 0부터 9까지로 이루어진 list를 전달 받아, 연속적으로 나타나는 숫자는 하나만 남기고 제거한 list를 반환하는 lonely 함수를 작성하시오. 이때, 제거된 후 남은 수들이 담긴 list의 요소들은 기존의 순서를 유지해야 한다.

```python
lonely([1, 1, 3, 3, 0, 1, 1]) # => [1, 3, 0, 1]
lonely([4, 4, 4, 3, 3]) # => [4, 3]
```

``` python
def lonely(numbers):
    result=[numbers[0]]
    for number in numbers:
        if result[-1] != number:
            result.append(number)

    return result
```

