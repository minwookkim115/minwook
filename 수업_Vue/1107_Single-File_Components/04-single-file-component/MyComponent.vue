<template>
  <div class="greeting">{{ msg }}</div>
</template>

<script setup>
import { ref } from 'vue'

const msg = ref('Hello World')
</script>

<!-- scoped가 지정되면 CSS가 현재 컴포넌트에만 적용 -->
<style scoped>
.greeting {
    color: red;
}
</style>