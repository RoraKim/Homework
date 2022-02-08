## 1. CSS flex-direction

####  Flex box의 주축을 변경하는 flex-direction의 4가지 값과 각각의 특징을 작성하시오.

main axis의 기준 방향을 설정한다. 



1) row  : 주축을 가로로, 오른쪽 방향으로 
2) row_reverse : 주축을 가로로, 오른쪽에서 왼쪽 방향으로 
3) column : 주축을 세로로, 위쪽부터 아래쪽 방향으로 
4) column_reverse : 주축을 세로로, 아래에서 위로

``` html
<div class="flex_container flex direction : row">
    <div class="flex_item">1</div>
</div>
```

``` html
<div class="flex_container flex_direction : row_reverse">
    <div class="flex_item">1</div>
</div>
```

``` html
<div class="flex_container flex_direction: column">
    <div class="flex_item">1</div>
</div>
```

``` html
<div class="flex_container flex_direction: column_reverse">
    <div class="flex_item">1</div>
</div>
```







---



##  2. Bootstrap flex-direction

####  flex-direction의 4가지 요소와 대응하는 bootstrap 클래스를 작성하시오.

1) row  : flex-row
2) row_reverse  : flex-row-reverse
3) column : flex-column
4) column_reverse : flex-column-reverse

``` html
<article class="d-flex">
    <div class="d-flex flex-row"></div> 
    <div class="d-flex flex-row-reverse"></div> 
    <div class="d-flex flex-column"></div> 
    <div class="d-flex flex-column-reverse"></div> 
</article>
```

-----



## 3.  align-items

####  align-items 속성의 4가지 값과 각각의 특징을 작성하시오.

align-items와 align-content



align-content : 여러 줄들 사이의 간격을 지정(공간 나누기 개념)

align-items : 컨테이너 안에서 어떻게 모든 요소들이 정렬하는지를 지정(정렬 개념)



모든 아이템을 cross axis 기준으로 정렬

1. stretch : 부모 flex 컨테이너의 최대 높이로 설정 , 여러 줄을 컨테이너에 맞도록 늘임
2. flex-start : 교차축 방향의 시작선에 정렬, 여러줄들을 컨테이너의 꼭대기에 정렬
3. flex-end : 교차축 방향의 끝에 정렬, 여러 줄들을 컨테이너의 바닥에 정렬
4. center : 교차축의 중앙에 정렬 여러줄들을 세로선 상의 가운데에 정렬
5. space-between : 여러 줄들 사이에서 동일한 간격을 둔다
6. space-around : 여러 줄들 주위에 동일한 간격을 둔다  
7. baseline 

``` html
align-content: flex-start;
```



---



## 4. flex-flow

####  flex-flow 속성은 두가지 속성의 축약형이다. 올바르게 짝지어진 것을 고르시오

``` 
(1) flex-direction, flex-wrap
(2) flex-direction, align-items
(3) justify-content, flex-wrap
(4) justify-content, align-items
```

(1) flex-flow row, wrap

---





## 5. Bootstrap Grid System

####  하단 코드에 Bootstrap Grid System을 적용시키고자 할 때, __(a)__, __(b)__ 각각에 입력해야 할 클래스 이름을 작성하시오.

``` html
<div class="(a)">
  <div class="(b)">
      <div class="col-(c)-(d)"></div>
    </div>
</div>
```

(a) : container - 컴테이너를 통해 얻을 수 있는 것 브레이크 포인트 들어갈 수 있음

(b) : row

(c) : sm, md, lg, xl, xxl : 디바이스나 화면의 크기에 따라서 반응형으로 디자인 구현 가능하도록 하는 역할

(d) : 12 이하의 정수 : 공간을 12개로 나누어서 해당 요소가 몇칸을 차지할 것인지를 정의 