<template>
  
  <!-- 导航栏 -->
    <nav>
      <h1>{{ appName }}</h1>
      <ul>
        <li v-for="item in menuItems" :key="item.name">
          <a @click="currentView = item.name">{{ item.name }}</a>
        </li>
      </ul>

      <!-- 使用原生的 a 标签来实现点击后在新标签页打开  这种写法 需要英文-->
      <a :href="resolveRoute('/')" target="_blank">主页</a> |
      <a :href="resolveRoute('/BookMarks')" target="_blank">书签</a> |
      <a :href="resolveRoute('/MeiTiChuangZuo')" target="_blank">媒体创作</a>

      <!-- 这种写法 是当前页面渲染 链接页面 而不是新页面 -->
      <!-- <router-link to="/">主页</router-link> |
      <router-link to="/BookMarks">书签</router-link> |
      <router-link to="/MeiTiChuangZuo">媒体创作</router-link> -->
  </nav>

  <router-view></router-view>

  <DaiMaKu />
</template>

<script setup>
// import ServerList from "./components/ServerList.vue";
// import DatabaseQuery from "./components/DatabaseQuery.vue";
import DaiMaKu from "./components/DaiMaKu.vue";

const appName = "我的应用";
const menuItems = [
  { name: '书签' },
  { name: '媒体创作' },
  { name: '工作记录' },
  { name: '代码库' },
  { name: '账单' },
  { name: '商业想法' },
  { name: 'GPT交互' },
  { name: '神评' },
  { name: '词库' },
  { name: '图片库' },
  { name: '声音库' },
  { name: '视频库' },
  { name: '账号' },
  { name: '软件' },
  { name: '依赖模块' },
];

import { useRouter } from 'vue-router';
const router = useRouter();

// 计算完整的URL路径
const resolveRoute = (path) => {
  return window.location.origin + router.resolve({ path }).href;
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

/* 添加一些基本样式 */
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
}

nav {
  margin-bottom: 20px;
}

a {
  margin: 0 10px;
  text-decoration: none;
  color: #42b983;
}

a:hover {
  text-decoration: underline;
}

nav {
  margin-bottom: 20px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline;
  margin: 0 10px;
}
</style>
