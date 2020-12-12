<template>
  <li class="list-group-item d-flex justify-content-between align-items-center">
      <span 
          role="button" 
          @click="completado(todo)"
          :class="{'tachado': todo.estado}"
      >
          {{ todo.texto }}
      </span>
      <span role="button" @click="eliminar(todo.id)">
          <i class="fas fa-times"></i>
      </span>
  </li>
</template>

<script>
import { inject } from 'vue'
export default {
    props: {
        todo: {
            type: Object,
            required: true
        }
    },
    setup() {
        const todos = inject('todos')

        async function loadData() {
            const response = await fetch('http://127.0.0.1:8000/api/todos/');
            const data = await response.json();
            todos.value = data;
        }

        async function deleteItem(id) {
            await fetch(`http://127.0.0.1:8000/api/todos/${id}/`, {
                method: 'delete',
                headers: {
                'Content-Type': 'application/json'
                }
            });
         
            loadData();
        }

        async function editItem(todo) {
            const todoAux = {
                id: todo.id,
                estado: true,
                texto: todo.texto
            }

            await fetch(`http://127.0.0.1:8000/api/todos/${todo.id}/`, {
                method: 'put',
                headers: {
                'Content-Type': 'application/json'
                },
                body: JSON.stringify(todoAux)
            });
            
            loadData();
        }

        const eliminar = id => {
            deleteItem(id)
        }

        const completado = todo => {
            editItem(todo)
        }

        return { eliminar, completado }
    }
}
</script>

<style>
.tachado {
    text-decoration: line-through;
}
</style>