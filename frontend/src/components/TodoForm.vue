<template>
  <form @submit.prevent="formulario">
      <input 
        type="text" 
        class="form-control my-3"
        placeholder="Ingrese tarea"
        v-model.trim="texto">
  </form>
</template>

<script>
import { inject, ref, watchEffect } from 'vue'
export default {
    setup() {
        const todos = inject('todos')
        const texto = ref('')
        
        async function newTodo(todo) {

            await fetch('http://127.0.0.1:8000/api/todos/', {
                method: 'post',
                headers: {
                'Content-Type': 'application/json'
                },
                body: JSON.stringify(todo)
            });
            
            todo = {};

            loadData();
        }

        async function loadData() {
            const response = await fetch('http://127.0.0.1:8000/api/todos/');
            const data = await response.json();
            todos.value = data;
        }
        
        const formulario = () => {
            // console.log(texto.value)
            if (texto.value === '') {
                console.log('esta vacio')
                return
            }

            const todo = {
                texto: texto.value,
                estado: false,
                id: Date.now(),
            }

            newTodo(todo)

            texto.value = ''
        }

        return { formulario, texto, }
    }
}
</script>

<style>

</style>