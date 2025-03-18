<template>
  <div class="tou">
    <!-- 独立的导航栏 -->
    <HeadContent />

    <nav>
      <h1>书签页面</h1>
      <ul>
        <li><router-link to="/">返回主页</router-link></li>
        <li><router-link to="/MeiTiChuangZuo">媒体创作</router-link></li>
      </ul>
    </nav>

    <!-- 页面内容 -->
    <div>
      <h2>这是书签页面的内容</h2>
      <p>书签页面的具体内容...</p>
    </div>
  </div>
</template>

<script setup>
import HeadContent from "./HeadContent.vue";

// 书签页面的逻辑
</script>

<style scoped>
.tou {
  background-color: #303841;
}

/* #app {
  /* background-color: #303841; */
/* font-family: Avenir, Helvetica, Arial, sans-serif; */
/* -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center; */
/* color: #303841; */
/* color: #2c3e50; */
/* margin-top: 60px; */
/* }  */

/* 书签页面的样式 */
nav {
  /* background-color: #f0f0f0; */
  padding: 1px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline;
  margin: 0 10px;
}

a {
  text-decoration: none;
  color: #42b983;
}

a:hover {
  text-decoration: underline;
}
</style>

<!-- <style scoped>
.el-header {
  background-color: #B3C0D1;
  color: #333;
  text-align: center;
  line-height: 60px;
}
</style> -->