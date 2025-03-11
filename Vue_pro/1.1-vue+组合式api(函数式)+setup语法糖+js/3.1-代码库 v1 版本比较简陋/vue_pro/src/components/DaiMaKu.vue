<template>
  <div>
    <!-- 搜索框 -->
    <input v-model="searchQuery" placeholder="搜索代码库..." />

    <!-- 增加新条目的表单 -->
    <form @submit.prevent="addCodeRepo">
      <label>标题：</label>
      <input v-model="newRepo.title" required />
      
      <label>语言：</label>
      <input v-model="newRepo.language" required />
      
      <button type="submit">添加</button>
    </form>

    <!-- 数据列表 -->
    <ul>
      <li v-for="(repo, index) in filteredRepos" :key="index">
        {{ repo.title }} - {{ repo.language }} - {{ new Date(repo.createdAt).toLocaleString() }} - 访问: {{ repo.visits }}
        <button @click="editRepo(index)">编辑</button>
        <button @click="deleteRepo(index)">删除</button>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';

// 初始化数据
const searchQuery = ref('');
const newRepo = ref({ title: '', language: '',createdAt: new Date(), visits: 0 });
const repos = ref(JSON.parse(localStorage.getItem('repos')) || []);

// 计算属性：过滤和排序后的仓库列表
const filteredRepos = computed(() => {
  let result = repos.value.filter(repo =>
    repo.title.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
    repo.language.toLowerCase().includes(searchQuery.value.toLowerCase())
  );
  return result.sort((a, b) => b.visits - a.visits);
});

// 添加新的代码库
function addCodeRepo() {
  repos.value.push({ ...newRepo.value });
  saveRepos();
  newRepo.value = { title: '', language: '', createdAt: new Date(), visits: 0 };
}

// 编辑代码库
function editRepo(index) {
  const updatedRepo = prompt("更新标题", repos.value[index].title);
  if (updatedRepo !== null) {
    repos.value[index].title = updatedRepo;
    saveRepos();
  }
}

// 删除代码库
function deleteRepo(index) {
  repos.value.splice(index, 1);
  saveRepos();
}

// 保存到本地存储
function saveRepos() {
  localStorage.setItem('repos', JSON.stringify(repos.value));
}

// 页面加载时从本地存储中恢复数据
onMounted(() => {
  repos.value = JSON.parse(localStorage.getItem('repos')) || [];
});
</script>

<style scoped>
/* 添加一些基本样式 */
input, button {
  margin: 5px;
}
</style>