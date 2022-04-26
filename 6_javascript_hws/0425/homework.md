# HomeWork
### JS T/F

아래의 설명을 읽고 T/F 여부를 작성하시오.

- let & const 키워드로 선언한 변수와 var 키워드로 선언한 변수의 유일한 차이점은 변수의 유효범위이다.

  - False

    ```
    let & const -> block scope
    var -> function scope
    
    var 는 재선언 재할당이 모두 가능하다.
    let 은 재할당은 가능하지만 재선언은 불가능하다.
    const 는 재선언 재할당 모두 불가능하다.
    ```

    

- “값이 없음”을 표현하는 값으로 null과 undefined 두 종류가 있으며, 둘 다 typeof 연산자에서 undefined가 반환된다.

  - False
  - null의 type은 object가 출력된다.

- for ... in 문은 배열의 요소를 직접 순회하므로 배열의 각 요소를 활용하는 경우에 주로 활용한다.

  - False
  - object인 경우, key를 
  - 배열인 경우, index 번호가 값으로 전달된다. (배열도 key와 value로 이루어진 object)
  - 그렇기 때문에, 순서를 보장하지 않으므로 배열 순회에는 권장하지 않는다.

- ‘==’ 연산자는 두 변수의 값과 타입이 같은지 비교하고 같다면 true 아니면 false를 반환한다.

  - False
  - `===` 연산자는 값과 타입이 모두 일치한지를 확인한다.
  - `==` 연산자는 형변환이 가능하다면 자동 형변환후의 값이 같은지 확인한다.



### for ... of

아래 같이 numbers 배열이 주어졌을 때, 아래 요구사항들에 맞도록 코드를 작성하시오.

```javascript
const numbers = [1, 2, 3, 4, 5]
```

- for … of 문을 사용하여 배열의 각 요소를 출력하시오.

  ```js
  for (let num of numbers ) {
      console.log(num)
  }
  ```

  

- for … of 문을 사용하여 배열의 각 요소에 10을 더한 요소들로 구성된 새로운 배열을 생성하시오.

  ```js
  const addNumbers = []
  for (const num of numbers) {
      addNumbers.push(num + 10)
  }
  console.log(addNumbers)
  ```

  

- for … of 문을 사용하여 배열의 각 요소들 중 홀수 요소 들로만 구성된 새로운 배열을 생성하시오.

  ```js
  const oddNumbers = []
  for (const num of numbers) {
      if (num % 2) {
          oddNumbers.push(num)
      }
  }
  console.log(oddNumbers)
  ```

  

- for … of 문을 사용하여 배열의 각 요소들을 모두 더한 값을 구하시오.

  ```js
  let total = 0
  for (const num of numbers) {
      total += num
  }
  console.log(total)
  ```

  