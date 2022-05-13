<template>
  <div id="app">
    <hello-world @child-click="onClick"></hello-world>  
    <hello-world @click.native="onClick"></hello-world>
    <todo-list></todo-list>
    <p @click="onClick">test</p>
    <hr>

    <h2>App</h2>
    <input type="text" v-model="appData">
    
    <p>parentData : {{ parentData }}</p>
    <p>childData : {{ childData }}</p>

    <app-parent
      :app-data="appData"
      :parent-data="parentData"
      :child-data="childData"
      @parent-input-change="onParentInputChange"
      @child-input-change="onChildInputChange"
    >
    </app-parent>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import TodoList from './components/TodoList.vue'

// 불러오기
import AppParent from './components/AppParent.vue'

export default {
  name: 'App',
  // 2. 등록하기
  components: {
    HelloWorld,
    TodoList,
    AppParent
  },
  // data function 형태로 만들어야 한다.
  data: function () {
    // return 값으로 처리한다.
    return {
      appData: null,
      parentData: null,
      childData: null,
    }
  },
  methods: {
    onClick() {
      console.log('Hello!')
    },
    onChildInputChange(childInputData) {
      this.childData = childInputData
    },
    onParentInputChange(parentInputData) {
      this.parentData = parentInputData
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
