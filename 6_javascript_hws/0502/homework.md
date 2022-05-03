# HomeWork

### AJAX T/F

아래의 설명을 읽고 T/F 여부를 작성하시오.

- JavaScript는 single threaded 언어로 한 번에 한 가지 일 밖에 처리하지 못한다.

  True

- setTimeout은 브라우저의 Web API를 사용하는 함수로, Web API에서 동작이
  완료되면 Call Stack에 바로 할당된다.

  False

  callstack -> webAPI -> task Queue -> event loop를 통해서 call stack이 비었을 때 선입 선출 되어 call 스택으로 할당



### asynchronous & synchronous

JavaScript에서 동기와 비동기 함수의 차이점을 서술하시오.

자바 스크립트는 싱글 스레드이기 때문에 한번에 하나의 작업 수행

따라서 a작업이 완료된 후 b작업을 진행하는 방식이 동기적 작동



비동기 함수

javascript는 비동기 함수를 싱해앟게 되면 web api에게 실행 주체를 넘겨준다

넘겨준 비동기 함수 처리가 끝나길 기다리는 게 아니라 본인이 해야할 다음 작업으로 넘어감 

### Axios

다음은 axios를 사용하여 API 서버로 요청을 보내고, 정상적으로 응답이 왔을 때 응답 데이터를 출력하는 코드이다. (a), (b), (c)에 들어갈 코드를 작성하시오.

```js
axios.__(a)__('https://api.example/com/data')
	.__(b)__(function (response) {
	    console.log(__(c)__)
	})
```

a : get

b : then

c :response.data
