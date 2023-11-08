<template>
  <div>
    <p>{{ myMsg }}</p>
		<button @click="updateName">이름 변경</button>
  </div>
</template>

<script setup>
defineProps({
    myMsg: String,
})

// 'updateName'은 emit 이벤트 이름
const emit = defineEmits(['updateName'])
// updateName은 걍 이름
const updateName = function () {
	emit('updateName')
}
</script>

<style scoped>

</style>