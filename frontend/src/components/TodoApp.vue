<template>
  <div class="container">
    <h1>ToDos</h1>
    <todo-form />
    <todo-list />
  </div>
</template>

<script>
import { provide, ref, watchEffect } from 'vue'
import TodoForm from './TodoForm.vue'
import TodoList from './TodoList.vue'
export default {
  components: { TodoForm, TodoList },
  setup() {
      const todos = ref([])
      provide('todos', todos)

      async function loadData() {
        const response = await fetch('http://127.0.0.1:8000/api/todos/');
        const data = await response.json();
        todos.value = data;
      }

      watchEffect(() => {
          // console.log(todos.value.length)
          // console.log(todos.value)

          loadData();
      })
  }

}
</script>

<style>

</style>