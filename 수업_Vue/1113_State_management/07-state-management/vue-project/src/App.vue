<template>
  <div>
    <h1>Todo Project</h1>
    <h2>완료된 Todo : {{ store.doneTodosCount }}</h2>
    <TodoList />
    <TodoForm />
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import TodoForm from '@/components/TodoForm.vue'
import TodoList from '@/components/TodoList.vue'

const store = useCounterStore()
</script>

<style scoped>
</style>
