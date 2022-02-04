## 1. HTML 정의 아래의 보기 (1) ~ (4) 중에서, HTML의 본딧말을 고르시오. 

``` 
(1) Hyperlinks and Text Markup Language 
(2) Home Tool Markup Language
(3) Hyper Text Markup Language
(4) Hyper Tool Markup Language
```

``` html
(3) Hyper Text Markup Language
HTML이란 Hyper Text Markup Language의 약자이다. 이는 웹페이지를 작성(구조화)하기 위한 언어이다. Hyper Text 란 기존의 선형적인 텍스트가 아닌 비선형적으로 이루어진 텍스트를 의미하며, 이는 인터넷의 등장과 함께 대두되었다. 기본적으로 Hyperlink를 통해 텍스트를 이동한다. 이러한 Hyper Text는 인간이 기억하는 방식까지 바꾸고 있는데 이를 컬럼비아대 뱃시 스패로 교수팀은 구글 효과라고 이름붙였다. 
```



### 2. HTML 개념

####  각 문항을 읽고 맞으면 T, 틀리면 F를 작성 하시오.

``` 
1) 웹 표준을 만드는 곳은 Mozilla 재단이다. F
W3C와 WHATWG가 만든다. 이제는 WHATWG에 주도권이 있다. 
WHATWG에서 HTML Living Standard를 만든다. 

2) 표(table) 을 만들 때에는 반드시 <th>태그를 사용해야 한다. F
반드시 th 태그를 사용할 필요는 없다. 

3) 제목(Heading) 태그는 제목 이외에는 사용하지 않는 것이 좋다. T 
시멘틱 웹의 의미를 살려서 제목 이외에는 사용하지 않는 것이 좋다. 검색엔진은 제목 태그를 중요한 의미로 받아들일 가능성이 크다. 

4) 리스트를 나열하기 위해서는 태그만 사용 할 수 있다. F
ol, ul 모두 사용할 수 있고 각 리스트 아이템들은 li 태그를 사용해서 나타낸다. 

5) HTML의 태그는 반드시 별도의 닫는 태그가 필요하다. F 
여는태그와 닫는태그가 한 쌍인 태그와, 별도의 닫는 태그가 필요 없는 태그도 있다. <br>, <p>
```







## 3. CSS 정의

####  아래의 보기 (1) ~ (4) 중에서, CSS의 본딧말을 고르시오

``` 
(1) Creative Style Sheets
(2) Cascading Style Sheets
(3) Computer Style Sheets
(4) Colorful Style Sheets
```

``` html
(2) Cascading Style Sheets 
스타일을 지정하기 위한 언어 
선택하고, 스타일을 지정한다
```





### 4. CSS 개념

####  각 문항을 읽고 맞으면 T, 틀리면 F를 작성 하시오.

```
1) HTML과 CSS는 각자 문법을 갖는 별개의 언어이다. T

2) 웹 브라우저는 내장 기본 스타일이 있어 CSS가 없어도 작동한다. T
- user agent stylesheets

3) 자식 요소 프로퍼티는 부모의 프로퍼티를 모두 상속 받는다. F
상속되는 것 : Text관련 요소(font, color, text-allign), opacity, visibility 등
상속되지 않는 것 : Box model 관련 요소(width, height, margin, padding, border, box-sizing, display), position 관련 요소(position, top/right/bottom/left,z-index)

4) 디바이스마다 화면의 크기가 다른 것을 고려하여 상대 단위인 %를 사용한다.F
vw vh등의 viewport에 따른 상대단위가 별도로 존재한다.

5) id 값은 유일해야 하므로 중복되어서는 안된다. T
```





## 5. CSS 우선순위

#### CSS는 우선 적용되는 순서가 존재 한다. 우선순위가 높은 순으로 나열 하시오.

``` 
요소 선택자, Inline style, 소스 순서, !important, id선택자, class 선택자
```

``` python
!important > Inline style > id > class 선택자 > 요소 선택자 > 소스 순서 
```

