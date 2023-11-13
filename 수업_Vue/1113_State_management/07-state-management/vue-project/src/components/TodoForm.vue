<template>
	<div>
		<form @submit.prevent="createTodo()" ref="formElem">
			<input type="text" v-model="todoText">
			<input type="submit">
		</form>
	</div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { ref } from 'vue'

const todoText = ref('')
const formElem = ref(null)

const store = useCounterStore()

const createTodo = function () {
	store.addTodo(todoText.value)
	formElem.value.reset()
	// todoText.value = ''
}
</script>

<style scoped>

</style>