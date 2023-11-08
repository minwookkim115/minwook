<template>
	<div style="border: 1px solid blue;">
		<h1>Parent</h1>
		<input type="text" @input="changeParentData">
		<p>App Data : {{ appData }}</p>
		<p>Parent Child Data : {{ parentChildData }}</p>
		<ParentChild
		:app-data="appData"
		:parent-data="parentData"
		@parent-child-data-chanaged="onParentChildDataChanged"/>
	</div>
</template>

<script setup>
import ParentChild from '@/components/ParentChild.vue'
import { ref } from 'vue'

defineProps({
	appData: String,
})

const emit = defineEmits(["parentDataChanged", "parentChildDataChanged"])

const parentData = ref('')
const parentChildData = ref('')

const changeParentData = function (event) {
	parentData.value = event.target.value
	emit("parentDataChanged", parentData.value)
}

const onParentChildDataChanged = function (data) {
	parentChildData.value = data
	emit("parentChildDataChanged", data)
}
</script>

<style scoped>

</style>