import { createRouter, createWebHashHistory } from "vue-router"

// 路由 是一个数组对象  用来配置路由的
const routes = [{
    path: '/',  // 路径
    name: 'Home',  // 名字
    // 组件
    component: () => import('@/views/index.vue')  // 这个导入的空的也是会报错的
}]

const router = createRouter({
    history: createWebHashHistory(),
    routes  // 键值对 如果一样 就可以简写了
})

export default router  // 这个导出了 其他地方才能导入这个