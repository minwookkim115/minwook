<template>
	<div>
		<h1>UserView</h1>
		<!-- <h2>{{ $route.params.id }}번 User 페이지</h2> -->
		<h2>{{ userId }}번 User 페이지</h2>
		<button @click="goHome">홈으로</button>
		<button @click="routeUpdate">100번 유저 페이지</button>
	</div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter, onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router'

const route = useRoute()
const userId = ref(route.params.id)

// 프로그래밍 방식 네비게이션
const router = useRouter()
const goHome = function () {
	router.push({ name: 'home' })
	// 히스토리에 안남음 뒤로가기 안됨
	// router.replace({ name:'home' })
}

onBeforeRouteLeave((to, from) => {
	const answer = window.confirm('갈래말래')
	// 취소를 눌렀다면
	if (answer === false) {
		return false
	}
})

const routeUpdate = function() {
	router.push({ name: 'user', params: { id: 100 }})
}

onBeforeRouteUpdate((to, from) => {
	userId.value = to.params.id
})
</script>

<style scoped>

</style>