<!-- npm install element-plus axios -->

<template>
  <el-container>
    <!-- 头部 -->
    <el-header>
      <h1>书签集合</h1>
    </el-header>

    <!-- 主体 -->
    <el-main>
      <!-- 搜索框 -->
      <el-row :gutter="20" style="margin-bottom: 20px;">
        <el-col :span="6">
          <el-input v-model="searchQuery.name" placeholder="名称" />
        </el-col>
        <el-col :span="6">
          <el-input v-model="searchQuery.source" placeholder="来源" />
        </el-col>
        <el-col :span="6">
          <el-input v-model="searchQuery.tag" placeholder="标签" />
        </el-col>
        <el-col :span="6">
          <el-button type="primary" @click="fetchBookMarks(1)">搜索</el-button>  
          <el-button type="success" @click="openDialog(0)">添加书签</el-button>
        </el-col>
      </el-row>

      <!-- 书签表格 -->
      <el-table :data="bookMarks" style="width: 100%; background-color: #303841; color: #3a4750;">
        <el-table-column prop="id" label="ID" />
        <el-table-column prop="name" label="名称" />
        <el-table-column prop="url" label="网址" />
        <el-table-column prop="source" label="来源" />
        <el-table-column prop="purpose" label="用途" />
        <el-table-column prop="tag" label="标签" />
        <el-table-column label="操作">
          <template #default="scope">
            <el-button type="primary" @click="editBookMark(scope.row)">编辑</el-button>
            <el-button type="danger" @click="deleteBookMark(scope.row.id)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>

      <!-- 分页 -->
      <el-pagination
        style="margin-top: 20px;"
        background
        layout="prev, pager, next"
        :total="total"
        :page-size="20"
        :current-page="currentPage"
        @current-change="handlePageChange"
      />

      <!-- 添加/编辑对话框 -->
      <el-dialog v-model="dialogVisible" :title="isEdit ? '编辑书签' : '添加书签'">
        <el-form :model="currentBookMark">
          <el-form-item label="ID">
            <el-input v-model="currentBookMark.id" />
          </el-form-item>
          <el-form-item label="名称">
            <el-input v-model="currentBookMark.name" />
          </el-form-item>
          <el-form-item label="网址">
            <el-input v-model="currentBookMark.url" />
          </el-form-item>
          <el-form-item label="来源">
            <el-input v-model="currentBookMark.source" />
          </el-form-item>
          <el-form-item label="用途">
            <el-input v-model="currentBookMark.purpose" />
          </el-form-item>
          <el-form-item label="标签">
            <el-input v-model="currentBookMark.tag" />
          </el-form-item>
        </el-form>
        <template #footer>
          <el-button @click="dialogVisible = false">取消</el-button>
          <el-button type="primary" @click="saveBookMark">保存</el-button>
        </template>
      </el-dialog>
    </el-main>
  </el-container>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

// const bookMarks = ref([]);   // 用于存储书签数据
const bookMarks = ref([]);   // 用于存储书签数据

const searchQuery = ref({ name: '', source: '', tag: '' });  // 搜索查询条件
const dialogVisible = ref(false);
const isEdit = ref(false);
const currentBookMark = ref({ id:'',name: '', url: '', source: '', purpose: '', tag: '' });
const loading = ref(false); // 加载状态

const currentPage = ref(1);  // 当前页码
const total = ref(0);        // 总记录数
// const items=ref([]);  // 当前页数据


// 获取书签数据   这种写法 是数据不为空的情况下 是可以的
// const fetchBookMarks = async (page = 1) => {
//   const response = await axios.get('/api/bookmarks', {
//     params: { ...searchQuery.value, page, limit: 100 },
//   });
//   bookMarks.value = response.data.data;
//   total.value = response.data.total;
// };

//  第二种写法 更加健壮 考虑到了 数据为空的情况   但是这种写法有点冗余
// 获取书签数据
// const fetchBookMarks = async (page = 1) => {
//   try {
//     loading.value = true; // 设置加载状态为 true

//     // 初始化或清空当前的书签数据
//     bookMarks.value = [];
//     total.value = 0;

//     const response = await axios.get('/api/bookmarks', {
//       params: { ...searchQuery.value, page, limit: 100 },
//     });

//     if (response.data && response.data.data !== undefined) {
//       bookMarks.value = response.data.data;
//       total.value = response.data.total || 0;
//     } else {
//       console.warn('从服务器 返回了 不期望的 数据格式');
//       bookMarks.value = []; // 确保数据为空数组
//       total.value = 0;
//     }
//   } catch (error) {
//     console.error('获取书签错误:', error);
//     // 可以在这里给用户提供友好的错误提示
//   } finally {
//     loading.value = false; // 请求结束，无论成功与否都设置加载状态为 false
//   }
// };

// 第三种写法
// 获取书签数据
const fetchBookMarks = async (page = 1) => {
  try {
    console.log("fetchBookMarks");
    loading.value = true; // 设置加载状态为 true
    const response = await axios.get('/api/bookmarks', {
      params: { ...searchQuery.value, page, limit: 20 },
    });
    console.log('Axios 请求 URL:', response.config.url);
    console.log('Axios 请求数据:', response.data);

    bookMarks.value = response.data.data || [];
    console.log("bookMarks.value",bookMarks.value);
    total.value = response.data.total || 0;
  } catch (error) {
    console.error('获取书签错误:', error);
  } finally {
    loading.value = false; // 请求结束，无论成功与否都设置加载状态为 false
  }
};

// 分页切换
const handlePageChange = (page) => {
  fetchBookMarks(page);
  currentPage.value = page||1;
};

// 打开添加/编辑对话框    
//  打开对话框的时候 通过 有没有传参 bookMark 书签对象 来判断你是 编辑还是新建模式  
const openDialog = (bookMark = null) => {
  console.log("bookMark",bookMark);
  console.log("!!bookMark",!!bookMark);
  
  isEdit.value = !!bookMark;  // 如果 bookMark 不是 null 或 undefined，则 isEdit.value 被设置为 true，表示当前操作是在编辑模式下进行
                              // 否则，isEdit.value 被设置为 false，表示是在添加新书签模式下进行
  console.log("isEdit.value1",isEdit.value);
  
  if(bookMark){  // 有传参  肯定是编辑模式
      console.log("你进行的是编辑 书签操作!");
  }else{  // 没有传参 就是新建书签模式  
    console.log("你进行的是新建 书签操作!");
  }
  currentBookMark.value = bookMark ? { ...bookMark } : { name: '', url: '', source: '', purpose: '', tag: '' };
  dialogVisible.value = true;
};

// 编辑书签
const editBookMark = (bookMark) => {
  console.log("edtoBookMark: bookMark",bookMark);
  
  openDialog(bookMark); // 调用 openDialog 并传递当前书签对象
};

// 保存书签
const saveBookMark = async () => {
  // 查看  生产环境 还是 开发环境
  console.log("生产/开发：",process.env.NODE_ENV)  // 生产/开发： development

  if (isEdit.value) {
    console.log("保存书签的 一瞬间 判断你是 编辑模式--> /api/bookmarks/${currentBookMark.value.id}");
    console.log("isEdit.value2:",isEdit.value);
    
    await axios.put(`/api/bookmarks/${currentBookMark.value.id}`, currentBookMark.value);
  } else {
    console.log("保存书签的 一瞬间 判断你是 新建模式-->/api/bookmarks");
    // await axios.post('/api/bookmarks', currentBookMark.value);
    const obj= currentBookMark.value
    obj.id=""
    const response = await axios.post('/api/bookmarks', obj,{
      headers: {
        'Cache-Control': 'no-cache', // 在 Axios 请求中添加禁止缓存的配置
      },
    }
    );
    console.log('Axios 请求 URL:', response.config.url);
    console.log('Axios 请求数据:', response.data);
    
  }
  dialogVisible.value = false;
  fetchBookMarks();
};

// 删除书签
const deleteBookMark = async (id) => {
  await axios.delete(`/api/bookmarks/${id}`);
  fetchBookMarks();
};

onMounted(() => {
  fetchBookMarks();
});
</script>

<style scoped>
.el-container{
  height: 100vh;
  /* style="height: 100vh; background-color: #303841; color: #fff;" */
}

.el-header {
  background-color: #3a4750;
  color: #fff;
  text-align: center;
  line-height: 60px;
}

/* .el-table {
  background-color: #3a4750;
  color: #fff;
} */

.el-pagination {
  justify-content: center;
}

.el-main,.el-container,.el-row,.el-col,.el-input,.el-input__inner{
  background-color: #303841 !important;
  color: #fff;
}
</style>