# HomeWork
### 한국어로 번역하기

#####  1-1. django 프로젝트를 한국어로 제공하기 위해 번역이 필요하다. 이 설정을 위해 settings.py에 어떤 변수 그리고 어떤 값을 할당해야 하는지 작성하시오. 



- LANGUAGE_CODE = 'ko_kr'



##### 1-2 추가로 settings.py에 ‘이 변수‘가 활성화인 상태여야 1-1번 변수를 설정할 수 있다고 한 다. ‘이 변수’는 무엇인가?’

- USE_I18N



---



### 경로 설정하기

#####  다음은 어떤 django 프로젝트의 urls.py의 모습이다. 주소 ’/ssafy’로 요청이 들어왔을 때 실 행되는 함수가 pages 앱의 views.py 파일 안 ssafy 함수라면, 요청에 응답하기 위해 빈칸 __(a)__에 추가되어야 할 코드를 작성하시오

```python
from django.contrib import admin
from djaingo.urls import path
from pages import views

urlpatterns = [
    path(__(a)___),
    path('admin/', admin,site,urls),
]
```

- `'ssafy/',views.ssafy, name='ssafy'`

---



### Django Template Language 

##### 아래 링크를 참고하여 각 문제들을 해결하기 위한 코드를 작성하시오. https://docs.djangoproject.com/en/3.2/ref/templates/builtins/



1. menu 리스트를 반복문으로 출력하시오
   - menu

```python
{% for __(a)__ in menus %}
	<p>{{ menu }}</p>
{% endfor %}
```



2. post  리스트를 반복문을 활용하여 0번 글 부터 출력하시오
   - forloop.counter0 - 0부터 출력
   - forloop.counter - 1부터 출력

```python
{% for post in posts %}
	<p>{{ __(a)__ }}번 글 : {{ post }}</p>
{% endfor %}
```



3. userlist가 비어있다면 현재 가입한 유저가 없습니다를 출력하시오 
   - empty

```python
{%for user in users %}
	<p>{{ user }}</p>
{%__(a)___%}
	<p>현재 가입한 유저가 없습니다.</p>
{% endfor %}
```



4. 첫번쨰 반복문일때와 아닐때를 조건문으로 분기처리하시오

```python
{%for ?? in ??? %}
 {% if forloop.first %}
	<p>첫번째 반복문입니다</p>
 {% else %}
	<p>첫번째 반복문이 아닙니다</p>
 {% endif %}
<% endfor %>
```



5. 출력된 결과가 주석과 같아지도록 하시오

```python
<!-- 5 -->
<p>{{ 'hello'|length}}</p>

<!--My Name Is Tom-->
<p>{{ 'my name is tom'|title}}</p>
```



6. 변수 today에 datetime 객체가 들어있을 때 출력된 결과가 주석과 같아지도록 작성하시오

`y년 m월 d일 (D) A h : i`

```python
<!-- 2020년 02월 02일 (sun) PM 02:02 -->
{{ today|data:"__(a)__" }}
```

---



## Form tag with Django

```django
<form action='/create' method='GET'>
<label for="title">title : </label>
<input type="text" name="title" id="title">
    
<label for="content">content : </label>
<input type="text" name="content" id="content">
    
<label for="my-site">my-site : </label>
<input type="text" name="my-site" id="my-site">
       
<input type="submit">       
</form>
```

1. action이 하는 일 

   - form 태그의 데이터를 보낼 위치를 지정한다.

2. 지문의 코드 중 method가 가질 수 있는 속성값을 작성하시오

   - GET, POST

3. `https://127.0.0.1:8000/create/?title=안녕하세요&content=반갑습니다&my-site=파이팅`

   