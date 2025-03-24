<template>
  <el-container style="height: 100vh;">
    <el-header>
      <h2>代码库管理</h2>
    </el-header>
    <el-main>
      <!-- 搜索框 -->
      <el-input v-model="searchQuery" placeholder="搜索代码库..." style="margin-bottom: 20px;" />

      <!-- 增加新条目的表单 -->
      <el-form @submit.prevent="addCodeRepo">
        <el-form-item label="标题">
          <el-input v-model="newRepo.title" required />
        </el-form-item>
        <el-form-item label="语言">
          <el-input v-model="newRepo.language" required />
        </el-form-item>
        <el-form-item label="内容">
          <!-- <mavon-editor v-model="newRepo.code_content" /> -->
          <!-- <el-input v-model="newRepo.code_content" /> -->
          <v-md-editor v-model="newRepo.code_content" />
        </el-form-item>
        <el-button type="primary" native-type="submit">添加</el-button>
      </el-form>

      <!-- 数据列表 -->
      <el-table :data="filteredRepos" style="width: 100%">
        <el-table-column prop="title" label="标题" width="180"></el-table-column>
        <el-table-column prop="language" label="语言" width="180"></el-table-column>
        <el-table-column prop="createdAt" label="创建时间">
          <template #default="scope">
            {{ new Date(scope.row.createdAt).toLocaleString() }}
          </template>
        </el-table-column>
        <el-table-column prop="visits" label="访问频率"></el-table-column>
        <el-table-column label="操作">
          <template #default="scope">
            <el-button @click="editRepo(scope.$index)">编辑</el-button>
            <el-button type="danger" @click="deleteRepo(scope.$index)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>

      <!-- 添加一个按钮用于清除 'repos' 数据 -->
      <el-button type="danger" @click="clearRepos" style="margin-top: 20px;">清除所有代码库</el-button>
    </el-main>

    <!-- 编辑对话框 -->
    <el-dialog v-model="dialogVisible" title="编辑代码库">
      <el-form>
        <el-form-item label="标题">
          <el-input v-model="editingRepo.title" />
        </el-form-item>
        <el-form-item label="语言">
          <el-input v-model="editingRepo.language" />
        </el-form-item>
        <el-form-item label="内容">
          <!-- <mavon-editor v-model="editingRepo.code_content" /> -->
          <!-- <el-input v-model="editingRepo.code_content" /> -->
          <v-md-editor v-model="editingRepo.code_content" />
        </el-form-item>
        <el-button type="primary" @click="saveEditedRepo">保存</el-button>
      </el-form>
    </el-dialog>
  </el-container>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { ElContainer, ElHeader, ElMain, ElInput, ElForm, ElFormItem, ElButton, ElTable, ElTableColumn, ElDialog } from 'element-plus'
// import { mavonEditor } from 'mavon-editor'
import { } from '@kangc/v-md-editor';

// 初始化数据
const searchQuery = ref('')
const newRepo = ref({ title: '', language: '', code_content: "", createdAt: new Date(), visits: 0 })
const repos = ref(JSON.parse(localStorage.getItem('repos')) || [])
const dialogVisible = ref(false)
const editingRepoIndex = ref(-1)
const editingRepo = ref({})

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
  newRepo.value = { title: '', language: '', code_content: "", createdAt: new Date(), visits: 0 };
}

// 编辑代码库
function editRepo(index) {
  editingRepoIndex.value = index;
  editingRepo.value = { ...repos.value[index] };
  dialogVisible.value = true;
}

// 删除代码库
function deleteRepo(index) {
  repos.value.splice(index, 1);
  saveRepos();
}

// 清除所有代码库
function clearRepos() {
  repos.value = [];
  localStorage.removeItem('repos');
}

// 保存到本地存储
function saveRepos() {
  localStorage.setItem('repos', JSON.stringify(repos.value));
}

// 保存编辑后的代码库
function saveEditedRepo() {
  repos.value[editingRepoIndex.value] = { ...editingRepo.value };
  saveRepos();
  dialogVisible.value = false;
}

// 页面加载时从本地存储中恢复数据
onMounted(() => {
  try {
    repos.value = JSON.parse(localStorage.getItem('repos')) || [];
  } catch (e) {
    console.error('Failed to parse localStorage data:', e);
    repos.value = [];
  }
});
</script>

<style scoped>
/* .el-header {
  background-color: #B3C0D1;
  color: #333;
  text-align: center;
  line-height: 60px;
} */
</style>