# HomeWork
### Vanilla JavaScript

 JavaScript에서 표준(standard)가 중요한 이유를 서술하시오.

자바 스크립트가 넷스케이프 브라우저 뿐만 아니라 다른 웹브라우저의 지원을 받기 시작하면서 표준 규격이 없어 여러 브라우저에서 독자적인 특성이 추가되었고 호환성 문제가 발생하기 시작했다. 때문에 다양한 웹 브라우저 에서 자바스크립트가 공통되게 잘 작동하기 위해 표준 규격이 필요해졌는데 이떄문에 ECMA 스탠다드가 만들어지게 되었다. 



파편화 되어있는 브라우저들이 각자 다른 api를 제공했다. 표준화가 제정된 이후 부터는 통일된 스크립트도 대부분의 브라우저에서 정상 작동하게 되었다.

### JavaScript T/F

아래의 설명을 읽고 T/F 여부를 작성하시오.

- DOM 에서 최상위 객체는 document다. 
  - False
  - window
- getElementById 메서드보다 querySelector 메서드가 좋은 이유는 선택자를 더 유연하게 사용할 수 있기 때문이다.
  - True
- querySelectorAll 메서드를 통해 선택한 NodeList는 forEach 메서드를 사용할 수 있다. 
  - True
- document.createElement 메서드를 통해 HTML 요소를 생성할 수 있다. 
  - True
- 부모 노드에서 자식 노드를 추가하는 유일한 방법은 append 메서드 뿐이다 
  - False
  - appendchild도 존재. append는 노드객체 이외에도 추가할 수 있게 해줌. append는 다수의 문자와 노드를 넣을 수 있고, appendchild는 단수의 노드만 가능.