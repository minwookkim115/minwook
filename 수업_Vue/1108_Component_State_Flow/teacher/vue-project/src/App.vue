<template>
	<div style="border: 1px solid black;">
    <h1>APP</h1>
    <input type="text" @input="changeAppdata">
    <p>Parent Data : {{ parentData }}</p>
    <p>Parent Child Data : {{ parentChildData }}</p>
    <!-- 자식 컴포넌트 -->
    <Parent
    :app-data="appData"
    @parent-data-changed="onParentDataChanged"
    @parent-child-data-changed="onParentChildDataChanged"/>
  </div>
</template>

<script setup>
import Parent from "@/components/Parent.vue"
import { ref } from 'vue'

const appData = ref('')
const parentData = ref('')
const parentChildData = ref('')

const changeAppdata = function (event) {
  appData.value = event.target.value
}

const onParentDataChanged = function (data) {
  parentData.value = data
}

const onParentChildDataChanged = function (data) {
  parentChildData.value = data
}
</script>

<style scoped>
div {
  text-align: center;
}
</style>
