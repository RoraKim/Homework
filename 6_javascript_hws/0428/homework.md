# HomeWork

### JavaScript T/F

아래의 설명을 읽고 T/F 여부를 작성하시오.
- EventTarget.addEventListener(type, listener)에서 listener 위치에 콜백 함수를 정의한 다. 이때 콜백 함수의 첫 번째 매개변수에는 발생한 이벤트에 대한 정보를 담고 있는 Event 객체가 전달된다.
  - true
- event.preventDefault 메서드를 통해 이벤트의 기본 동작을 취소할 수 있다.
  - true



### Event

DOM Event에는 다양한 종류의 Event가 존재한다. 아래 제시된 Event들이 각각 어떤 시점에 발생하는지 다음 MDN 문서를 참고하여 간단하게 작성하시오.

```
click : 마우스가 눌렸다가 뗐을 때
mouseover : 마우스 포인터가 위로 이동했을 때 
mouseout : 마우스가 올려졌다가 사라졌을 때 
keydown : 키가 눌렸을 때 
keyup : 키가 떼졌을 때
load : 로직 완료 되었을 때
scroll : 스크롤 되었을 때
change : 변동 사항이 발생했을 때
input : 입력값이 들어갈 떄
```







### EventListener

다음은 버튼을 클릭했을 때, 콘솔창을 통해 메시지를 확인하는 코드이다. (a), (b), (c)에 들어갈 코드를 작성하시오.

```javascript
const button = document.__(a)__('button')

button.__(b)__(__(c)__, function () {
    console.log('Button clicked!')
})
```

a :  queryselector

b : addevenlistener

c : click

