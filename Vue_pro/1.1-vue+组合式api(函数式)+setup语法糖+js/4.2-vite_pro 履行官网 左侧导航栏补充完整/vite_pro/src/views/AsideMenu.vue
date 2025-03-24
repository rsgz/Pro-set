<script setup>
import {ref} from 'vue'


const isCollapse = ref(true)

// 引入阿里的fonticon
let asidelist = ref([
  {id:1,title:'酒店',icon:'icon-jiudian'},
  {id:2,title:'机票',icon:'icon-icon_jihuojipiaozhuanxiangjiada'},
  {id:3,title:'火车票',icon:'icon-icon_huochepiao'},
  {id:4,title:'旅游',icon:'icon-lvyou'},
  {id:5,title:'景点',icon:'icon-jingdian'},
  {id:6,title:'汽车票',icon:'icon-xiaoqiche'},
  {id:7,title:'船票',icon:'icon-chuan'},
  {id:8,title:'门票',icon:'icon-menpiao'},
])
</script>

<template>
    <!-- <el-aside width="200px">左侧导航栏</el-aside> -->
  <el-aside>
    <div class="aside_list">
            <el-menu
        default-active="2"
        class="el-menu-vertical-demo"
        :collapse="isCollapse"
        @open="handleOpen"
        @close="handleClose"
        >
        <el-radio-group v-model="isCollapse" style="margin-bottom: 20px">
            <el-radio-button :value="false" v-show="isCollapse">|||</el-radio-button>
            <el-radio-button :value="true" v-show="!isCollapse">|||</el-radio-button>
        </el-radio-group>

        <el-menu-item index="v.id" v-for="v in asidelist" :key="v.id">
            <!-- <el-icon><component :is="v.icon"></component></el-icon> -->
            <div class="y_duiqi">
                <i class="iconfont" :class="v.icon"></i>
            </div>
            
            <template #title>{{v.title}}</template>
        </el-menu-item>

        </el-menu>
    </div>
    
  </el-aside>
</template>


<style scoped>
.y_duiqi {
  display: flex;
  justify-content: center;
  /* 水平居中 */
  width: 35px;
  /* margin-right: 15px; */
}

/*el-aside  竖线 占据 一整页 */
.el-aside .el-menu {
    height:100vh;
}

/* 图标加粗 */
/*图标大小调节*/
.el-aside i{
    /* font-size: 24px;   */
    font-weight: 600;
}

/* 把左侧菜单 都给固定住，也就是加上position:fixed属性让他脱离文档流 */
.aside_list{
    border-color: red;
    position:fixed;
    left:0;
    width:120px;
}
</style>

<!-- 有时候样式不起作用 就去 写到全局 里面 -->
<style>
/*取消 上方按钮的 边框*/
span.el-radio-button__inner{
    font-size: 20px;
    border: none;
    /* background-color: aqua; */
}

.el-aside{
    /* width: 120px; */
    width: 58px;
}
</style>