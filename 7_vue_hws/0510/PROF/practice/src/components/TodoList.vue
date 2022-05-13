<template>
  <div>
    <todo-list-input @add-todo="onAddTodo"></todo-list-input> 
  </div>
</template>

<script>
import TodoListInput from '@/components/TodoListInput'

export default {
  name: 'TodoList',
  components: {
    TodoListInput,
  },
  methods: {
    onAddTodo(todo) {
      console.log(todo)
    }
  }
}
</script>

<style>

</style>