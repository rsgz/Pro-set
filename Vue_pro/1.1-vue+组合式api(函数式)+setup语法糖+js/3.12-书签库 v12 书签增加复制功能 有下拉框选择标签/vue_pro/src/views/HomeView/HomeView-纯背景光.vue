<template>
  <div>
    <!-- 独立的导航栏 -->
    <nav>
      <!-- <h1>主页</h1> -->
      <ul class="ul_top">
        <li><router-link class="app-button-neon" to="/BookMarks">书签</router-link></li>
        <li><router-link class="app-button-neon" to="/MeiTiChuangZuo">媒体创作</router-link></li>
        <li><router-link class="app-button-neon" to="/DaiMaKu">代码库</router-link></li>
        <li><router-link class="app-button-neon" to="/CssKu">Css库</router-link></li>
        <li><router-link class="app-button-neon" to="/ToolSets">Tools6站在</router-link></li>
      </ul>
    </nav>

    <!-- 页面内容 -->
    <div>
      <h2>6666666666</h2>
      <p>22222222222</p>
    </div>
  </div>
</template>

<script setup>
// 主页的逻辑
</script>

<style scoped>
/* 主页的样式 */
/* nav { */
  /* background-color: #f0f0f0; */
  /* padding: 1px; */
/* } */
.ul_top{
  margin-top: 10px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline;
  margin: 0 3px;
}

a {
  text-decoration: none;
  color: #42b983;
}

a:hover {
  text-decoration: none;
}

.app-button-neon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 5px 5px;
  border-radius: 8px;
  background-color: #333;
  color: #64ffda;
  font-size: 16px;
  cursor: pointer;
  box-shadow: 0 0 10px #64ffda, 0 0 20px #64ffda, 0 0 30px #64ffda;
  transition: box-shadow 0.3s ease-in-out;
}
.app-button-neon:hover {
  box-shadow: 0 0 15px #0391f0, 0 0 30px #03c2f1, 0 0 45px #0fbbf0;
  border: #03c2f1 1px solid;
  color: #199af0;
}
.app-button-neon img {
  margin-right: 1px;
  width: 20px;
  height: 20px;
}
</style>