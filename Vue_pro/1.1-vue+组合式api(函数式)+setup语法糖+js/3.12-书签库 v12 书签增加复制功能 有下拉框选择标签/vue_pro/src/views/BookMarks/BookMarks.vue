<!-- npm install element-plus axios -->

<template>
  <el-container>
    <!-- 头部 -->
    <el-header>
      <div class="shouye">
        <ShouYe_Btn />
        <span class="shu">书签集合</span>
    </div>
      
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

      <!-- 书签表格  ================== 书签展示区域 ==================-->
      <el-table :data="bookMarks" style="width: 100%; background-color: #303841; color: #3a4750;">
        <el-table-column prop="id" label="ID">
          <template #default="scope">
            <span>{{ formatId(scope.row.id) }}</span>
          </template>
        </el-table-column>

        <el-table-column prop="name" label="名称" />

        <!-- <el-table-column prop="url" label="网址" >
          <template #default="scope">
            <span>{{ formatUrl(scope.row.url) }}</span>
          </template>
        </el-table-column> -->

        <el-table-column prop="url" label="网址" show-overflow-tooltip>
          <template #default="scope">
            <div class="yihang">
              <!-- 可点击的链接 -->
              <a :href="scope.row.url" target="_blank" @click="incrementClicks(scope.row.id)" style="margin-right: 10px;">
                {{ formatUrl(scope.row.url) }}
              </a>
              <!-- 复制按钮 -->
              <el-button
                class="fuzhi_lianjie_anniu"
                size="mini"
                type="primary"
                @click="copyUrl(scope.row.url)"
              >
                复制
              </el-button>
            </div>
            
          </template>
        </el-table-column>

        <el-table-column prop="source" label="来源" />
        <el-table-column prop="purpose" label="用途" />
        <el-table-column prop="tag" label="标签" />

        <!-- 使用插槽为标签列添加下拉选择菜单 -->
        <!-- <el-table-column prop="tag" label="标签">
          <template #default="scope">
            <el-select v-model="scope.row.tag" placeholder="选择分类">
              <el-option
                v-for="tag in availableTags"
                :key="tag"
                :label="tag"
                :value="tag"
              ></el-option>
            </el-select>
          </template>
        </el-table-column> -->

        <!-- 新增一个 点击量 记录 -->
        <el-table-column prop="clicks" label="点击量">
          <template #default="scope">
            <span>{{ scope.row.clicks }}</span>
          </template>
        </el-table-column>

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

      <!-- ================= 添加/编辑对话框 ================= -->
      <el-dialog v-model="dialogVisible" :title="isEdit ? '编辑书签' : '添加书签'">
        <el-form ref="bookmarkForm" :model="currentBookMark" :rules="rules">
          <el-form-item label="ID">
            <el-input v-model="currentBookMark.id" />
          </el-form-item>
          <el-form-item label="名称" prop="name" :rules="rules.name">
            <el-input v-model="currentBookMark.name" />
          </el-form-item>

          <el-form-item label="网址" prop="url" :rules="rules.url">
            <el-input v-model="currentBookMark.url" />
          </el-form-item>

          <el-form-item label="来源">
            <el-input v-model="currentBookMark.source" />
          </el-form-item>

          <el-form-item label="用途">
            <el-input v-model="currentBookMark.purpose" />
          </el-form-item>

          <!-- <el-form-item label="标签">
            <el-input v-model="currentBookMark.tag" />
          </el-form-item> -->

          <!-- 标签选择 -->
          <el-form-item label="标签">
            <!-- <el-cascader
              v-model="currentBookMark.tag"
              :options="tagOptions"
              placeholder="选择标签"
              multiple
              filterable
            /> -->

            <el-tree
            :data="tagOptions"
            show-checkbox
            node-key="value"
            :default-expand-all="false"
            highlight-current
            v-model="currentBookMark.tag"
          />
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
import ShouYe_Btn from '@/components/ShouYe_Btn.vue';
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { ElMessage } from 'element-plus'
// import { reactive } from "vue";

// const bookMarks = ref([]);   // 用于存储书签数据
const bookMarks = ref([]);   // 用于存储书签数据

const searchQuery = ref({ name: '', source: '', tag: '' });  // 搜索查询条件
const dialogVisible = ref(false);
const isEdit = ref(false);
const currentBookMark = ref({ id:'',name: '', url: '', source: '', purpose: '', tag: '',clicks:'' });
const loading = ref(false); // 加载状态

const currentPage = ref(1);  // 当前页码
const total = ref(0);        // 总记录数
// const items=ref([]);  // 当前页数据

const bookmarkForm = ref(null); // 用于格式验证



// 标签分类数据
const tagOptions = [
  {
    value: "素材",
    label: "素材",
    children: [
      {
        value: "文字",
        label: "文字",
        children: [{ value: "字体", label: "字体" }, { value: "综合", label: "综合" }],
      },
      {
        value: "图片",
        label: "图片",
        children: [
          { value: "app logo", label: "app logo" },
          { value: "菜单 icon", label: "菜单 icon" },
          { value: "表情包", label: "表情包" },
          { value: "壁纸", label: "壁纸" },
          { value: "综合", label: "综合" },
        ],
      },
      {
        value: "音频",
        label: "音频",
        children: [
          { value: "音乐", label: "音乐" },
          { value: "背景音乐", label: "背景音乐" },
          { value: "拟声", label: "拟声" },
        ],
      },
    ],
  },
  {
    value: "工具",
    label: "工具",
    children: [
      {
        value: "文本",
        label: "文本",
        children: [
          { value: "排序", label: "排序" }, 
          { value: "左右翻转", label: "左右翻转" }, 
          { value: "加序号", label: "加序号" },
          { value: "差异对比", label: "差异对比" },
          { value: "AI提示词", label: "AI提示词" },
          { value: "文字乱序", label: "文字乱序" },
          { value: "震惊标题", label: "震惊标题" },
          { value: "文案生成", label: "文案生成" },
          { value: "简体繁体", label: "简体繁体" },
        ],
      },
      {
        value: "图片",
        label: "图片",
        children: [
          { value: "转格式", label: "转格式" }, 
          { value: "高清放大", label: "高清放大" },
          { value: "制作gif", label: "制作gif" },
          { value: "制作印章", label: "制作印章" },
          { value: "加水印", label: "加水印" },
          { value: "解析二维码", label: "解析二维码" },
          { value: "生成二维码", label: "生成二维码" },
          { value: "生成椰树风格", label: "生成椰树风格" },
          { value: "抠图", label: "抠图" },
        ],
      },
      {
        value: "人像",
        label: "人像",
        children: [
          { value: "人像动漫化", label: "人像动漫化" },
          { value: "人像素描", label: "人像素描" },
        ],
      },

      {
        value: "日期",
        label: "日期",
        children: [
          { value: "天数间隔", label: "天数间隔" }, 
          { value: "人生进度", label: "人生进度" }, 
          
        ],
      },
    ]
  },
  {
    value: "文档",
    label: "文档",
    children: [
      {
        value: "待定",
        label: "待定",
        children: [
          { value: "待定", label: "待定" }, 
          { value: "待定", label: "待定" }],
      },
    ]
  },
  {
    value: "教程",
    label: "教程",
    children: [
      {
        value: "文字教程",
        label: "文字教程",
        children: [
          { value: "汇编", label: "汇编" }, 
          { value: "C语言", label: "C语言" }, 
          { value: "C++", label: "C++" }, 
          { value: "Rust", label: "Rust" }, 
          { value: "Python3", label: "Python3" }, 
          { value: "Java", label: "Java" }, 
          { value: "Go", label: "Go" }, 
          { value: "JavaScript", label: "JavaScript" }, 
        ],
      },
    ]
  },
  {
    value: "文章",
    label: "文章",
    children: [

    ]
  },
  {
    value: "资料",
    label: "资料",
    children: [{ value: "社工库", label: "社工库" }],
  },
  {
    value: "平台",
    label: "平台",
    children: [
      { value: "社交平台", label: "社交平台" },
    ],
  },
  {
    value: "下载",
    label: "下载",
    children: [
      { value: "应用商店", label: "应用商店" },
    ],
  },
];

// const rules = ref({
//   url: [
//     { required: true, message: '网址不能为空', trigger: 'blur' },
//     {
//       validator: (rule, value, callback) => {
//         const urlPattern = /^(https?:\/\/)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,6}(\/\S*)?$/
//         // console.log("效验的值",value);
//         if (!urlPattern.test(value)) {
//           callback(new Error('请输入有效的网址'))
//         } else {
//           console.log("校验的值",value);
//           callback()
//         }
//       },
//       trigger: 'blur'
//     }
//   ]
// })



// 点击量 累计
const incrementClicks = async (id) => {
  try {
    // 假设后端支持更新点击量的 API
    await axios.post(`/api/bookmarks/${id}/incrementClicks`);
    // 本地更新点击量
    const bookmark = bookMarks.value.find((item) => item.id === id);
    if (bookmark) {
      bookmark.clicks += 1;
    }
  } catch (error) {
    console.error('更新点击量失败:', error);
  }
};

// 验证规则
const rules = ref({
  name: [{ required: true, message: '名称不能为空', trigger: 'blur' }],
  url: [
    { required: true, message: '网址不能为空', trigger: 'blur' },
    // { type: 'url', message: '请输入有效的网址', trigger: 'blur' }
    {
      validator: (rule, value, callback) => {
        // 定义严格的 URL 正则表达式
        const urlPattern = /^(https?:\/\/)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,6}(\/\S*)?$/
        if (!urlPattern.test(value)) {
          callback(new Error('请输入有效的网址'))
        } else {
          console.log("校验的值 通过",value);
          callback()
        }
      },
      trigger: 'blur'
    }
  ]
})

window.rules = rules

// 格式化 ID 的方法
const formatId = (id) => {
  // <span>{{ formatId(scope.row.id) }}</span>
  return id.length > 15 ? id.slice(0, 15) + '...' : id
}

// url
const formatUrl = (url) => {
  // <span>{{ formatId(scope.row.id) }}</span>
  return url.length > 20 ? url.slice(0, 20) + '...' : url
}

// 复制书签逻辑
const copyUrl = (url) => {
  navigator.clipboard.writeText(url).then(() => {
    ElMessage({
      message: '网址已复制！',
      type: 'success'
    })
  }).catch(() => {
    ElMessage({
      message: '复制失败，请重试',
      type: 'error'
    })
  })
}



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
    console.log("如果mysql 没有开启，请开启mysql服务器：\nnet start MySQL84");
    
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

/*
// 保存书签
const saveBookMark1 = async () => {
  // 查看  生产环境 还是 开发环境
  console.log("生产/开发：",process.env.NODE_ENV)  // 生产/开发： development
  
  // 提交数据 之前 先来 验证一下 url 是不是符合要求的
  bookmarkForm.value.validate((valid) => {
    
    if (valid) {
      // 验证通过，执行保存操作
      console.log('表单 url已经验证：可以提交');
      // 在这里添加你的保存逻辑
    } else {
      // 验证失败，显示错误提示
      console.log('表单验证失败');
      ElMessage.error('URL 格式不正确，请检查！'); // 显示错误消息
      return;
    }
  });

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
*/


// 保存书签
const saveBookMark = async () => {
  console.log('生产/开发：', process.env.NODE_ENV);

  await bookmarkForm.value.validate(async (valid) => {
    if (valid) {
      console.log('表单 url已经验证：可以提交');

      if (isEdit.value) { // 编辑模式
        console.log(
          '保存书签的 一瞬间 判断你是 编辑模式--> /api/bookmarks/${currentBookMark.value.id}'
        );
        console.log('isEdit.value2:', isEdit.value);

        await axios.put(`/api/bookmarks/${currentBookMark.value.id}`, currentBookMark.value);
        fetchBookMarks(currentPage.value); // 重新获取当前页的数据

      } else {  // 新建模式
        console.log('保存书签的 一瞬间 判断你是 新建模式-->/api/bookmarks');
        const obj = { ...currentBookMark.value, id: ''}; // 创建一个新对象，避免修改原对象
        
        const response = await axios.post('/api/bookmarks', obj, {
          headers: {
            'Cache-Control': 'no-cache',
          },
        });
        console.log('Axios 请求 URL:', response.config.url);
        console.log('Axios 请求数据:', response.data);
      }

      dialogVisible.value = false;
      // fetchBookMarks(); 
    } else {
      console.log('表单验证失败');
      ElMessage.error('格式：不能为空或者格式不对!');
    }
  });
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


<!-- 标签 下拉菜单的样式 -->


<!-- 网址那一栏 设置成一行样式 -->
<style scoped>
.yihang {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.fuzhi_lianjie_anniu {
  /* margin-left: auto; */
  margin: 0px;    
  padding: 0px;
  border: none;
  /* background-color: #303841; */
  /* color: #a9a297; */
  font-size: 12px;
  cursor: pointer;
  white-space: nowrap; /* 防止内容换行 */
  height: auto;
  width: auto;
  padding: 3px;
  
}
</style>


<!-- 设置 顶部那个 首页 那一行 -->
<style scope>
.shouye{
    display: flex;
    align-items: center;
    padding: 10px 0px;
    height: 45px;
    /* text-align: center; */
}

.shu{
  font-size:30px;
  font-weight: 600;
  padding-left: 35vw;
}

.el-header {
  background-color: #3a4750;
  color: #a9a297;
  /* text-align: center; */
  /* line-height: 60px; */
}
</style>

<!-- 这个设置 界面主题色 主要是 表单form与 table -->
<style>
.el-container{
  height: 100vh;
  /* style="height: 100vh; background-color: #303841; color: #fff;" */
}

/* .el-table {
  background-color: #3a4750;
  color: #fff;
} */

.el-pagination {
  justify-content: center;
}

.el-main,.el-container,.el-row,.el-col,.el-input,.el-col,.el-input__inner,.el-input__wrapper{
  background-color: #303841 !important;
  color: #00ffff;
  color: #a9a297 !important;
}

table,tr,th,td{
  background-color: #303841 !important;
  color: #00ffff;
  color: #a9a297 !important;
}


.el-tree-node,.el-tree-node__content,
.el-dialog,.el-form,.el-form-item__label{
  background-color: #38414b !important;
  color: #00ffff !important;
  color: #a9a297 !important;
}

.el-input__inner{
  color: #a9a297 !important;
}

.el-dialog__title{
  color: #a9a297 !important;
}
</style>