<script setup>
import HelloWorld from './components/HelloWorld.vue'
// import Index from '@/views/index.vue'  // 这两种方式导入 都是可以的 因为我做了 src路径映射了 
import Index from './views/index.vue'

</script>

<template>
  <Index />
  <!-- <HelloWorld msg="Vite + Vue" /> -->
</template>

<style scoped></style>
