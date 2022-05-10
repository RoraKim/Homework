. 아래의 설명을 읽고 T/F 여부를 작성하시오. - Vue는 컴포넌트 간 양방향 데이터 흐름을 지향하기 때문에 부모, 자식 컴포넌트 간의 데이터 전달 및 수정이 자유롭다. - v-on 디렉티브는 해당 요소 또는 컴포넌트에서 특정 이벤트 발생 시 전달받은 함수를 실행한다. - 부모 컴포넌트는 props를 통해 자식 컴포넌트에게 이벤트를 보내고, 자식 컴포넌트는 emit을 통해 부모 컴포넌트에게 데이터를 전달한다.

Vue는 단방향 데이터 흐름을 지향하는 프론트엔드 프레임워크다. 공식문서를 참고하여 그 이유를 서술하시오

아래와 같은 Vue 프로젝트에서 2개의 버튼이 동작하는 것을 비교하여 .native 수식어의 역할을 작성하시오.

![image-20220510093937820](homework.assets/image-20220510093937820.png)





![image-20220510093953544](homework.assets/image-20220510093953544.png)





\4. 다음은 자식 컴포넌트에서 이벤트를 발생시켜 부모 컴포넌트의 함수를 실행하는 코드이다. 빈칸 (a), (b), (c)에 들어갈 코드를 작성하시오. • TodoListInput 컴포넌트의 버튼을 누르면 add-todo 이벤트가 발생한다. (이벤트 발생 시 data의 inputData 값도 함께 전달한다.) • TodoList 컴포넌트에서 add-todo 이벤트를 청취하면, onAddTodo 메서드를 실행한다. • onAddTodo 메서드에서는 TodoListInput 컴포넌트에서 전달받은 값을 console.log 함수를 통해 출력한다.

![image-20220510094015332](homework.assets/image-20220510094015332.png)



![image-20220510094032898](homework.assets/image-20220510094032898.png)