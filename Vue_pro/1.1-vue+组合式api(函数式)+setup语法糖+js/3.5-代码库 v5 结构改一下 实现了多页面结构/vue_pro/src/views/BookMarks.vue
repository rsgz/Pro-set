<template>
  <div>
    <!-- 独立的导航栏 -->
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
// 书签页面的逻辑
</script>

<style scoped>
/* 书签页面的样式 */
nav {
  background-color: #f0f0f0;
  padding: 10px;
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