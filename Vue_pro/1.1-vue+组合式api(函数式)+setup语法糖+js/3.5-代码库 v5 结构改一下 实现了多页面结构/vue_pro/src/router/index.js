import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import BookMarks from '../views/BookMarks.vue';
import MeiTiChuangZuo from '../views/MeiTiChuangZuo.vue';
// 导入其他需要的视图组件...

const routes = [
    {
        path: '/',
        name: '首页',
        component: HomeView
    },
    {
        path: '/BookMarks',
        name: '书签',
        component: BookMarks
    },
    {
        path: '/MeiTiChuangZuo',
        name: '媒体创作',
        component: MeiTiChuangZuo
    },
    // 添加其他路由...
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
});

export default router;