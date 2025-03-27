<template>
    <div>
      <nav>
        <router-link to="/Home">首页</router-link>
        <router-link to="/WenBenBiJiao">文本比较</router-link>
        <router-link to="/WenBenBiJiao">工具 2</router-link>
        // 添加更多导航
      </nav>
      <div>
        <button @click="$router.push('/WenBenBiJiao')">文本比较</button>
        <button @click="$router.push('/WenBenBiJiao')">打开工具 2</button>
        //添加更多按钮
      </div>
    </div>
  </template>

<script setup>
import { ref } from 'vue'


</script>

<style scoped>

</style>