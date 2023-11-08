<template>
	<div style="border:1px solid red;">
		<h1>Parent Child</h1>
		<input type="text" @input="changeParentChildData">
		<p>App Data : {{ appData }}</p>
		<p>Parent Data : {{ parentData }}</p>
	</div>
</template>

<script setup>
import { ref } from 'vue'

defineProps({
	appData: String,
	parentData: String,
})

const emit = defineEmits(['parentChildDataChanaged'])

const changeParentChildData = function (event) {
	emit('parentChildDataChanaged', event.target.value)
}

</script>

<style scoped>

</style>