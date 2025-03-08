<script setup>
import { ref } from 'vue'

const count = ref(0)
</script>

<template>
<div id="app">
  <button @click="count++" :disabled="false"> Count is: {{ count }}</button>
</div>
</template>

<style scoped>
/* 如果有样式需求可以在这里添加 */
</style>