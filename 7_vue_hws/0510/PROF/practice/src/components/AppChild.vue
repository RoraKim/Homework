<template>
  <div id="child">
    <h2>App Child</h2>
    <!-- #input이벤트가 발생된 input태그가 가지고 있는 값을 할당해서 넘겨줌 -->
    <input type="text" :value="childData" @input="onInput">
    <p>appData : {{ appData }}</p>
    <p>parentData : {{ parentData }}</p>
  </div>
</template>

<script>
export default {
  name: 'AppChild',
  props: {
    appData: {
      type: String
    },
    parentData: {
      type: String
    },
    childData: {
      type: String
    }
  },
  methods: {
    // #event가 발생했기 때문에 첫번째 인자는 event 
    onInput(event) {
      // 이 event가 가지고 있을 target이 가진 value 뽑아보기 
      // 그것이 event listner이니까
      // 값을 입력할 때 마다 콘솔이 변하는 것 확인
      // console.log(event.target.value)

      // event를 발생 시킬건데, child-input-change라는 이벤트가 발생하면 
      // event가 가지고 있을 target이 가진 value를 넘겨준다
      // 하위 컴포넌트인 AppChild는 무슨 값을 넘겨주고 있는가
      // 내가 input에 집어넣은 :value="childData"가 가지고 있는 값을 
      // 나를 부르고 있는 바로 상위 컴포넌트에 보낼 수 있게 된다.

      this.$emit('child-input-change', event.target.value)
    }
  }
}
</script>

<style>

</style>