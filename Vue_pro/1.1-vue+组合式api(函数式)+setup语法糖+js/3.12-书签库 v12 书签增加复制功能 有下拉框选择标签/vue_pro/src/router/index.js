import { createRouter, createWebHistory } from 'vue-router';
// import HomeView from '../views/HomeView.vue';
import MeiTiChuangZuo from '../views/MeiTiChuangZuo.vue';
import DaiMaKu from '../views/DaiMaKu.vue';

import HomeView from '../views/HomeView/HomeView.vue';
import BookMarks from '../views/BookMarks/BookMarks.vue';
import CssKu from '../views/CssKu/CssKu.vue';
import ToolSets from '../views/ToolSets/ToolSets.vue';
import AITiWen from '../views/AITiWen/MainView.vue';
import WangZhanGaiBan from '../views/WangZhanGaiBan/MainView.vue';
// 导入其他需要的视图组件...

const routes = [
    {
        path: '/',
        name: '首页',
        component: HomeView
    },

    {
        path: '/WangZhanGaiBan',
        name: '网站改版',
        component: WangZhanGaiBan
    },
    {
        path: '/AITiWen',
        name: 'AI提问',
        component: AITiWen
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
    {
        path: '/DaiMaKu',
        name: '代码库',
        component: DaiMaKu
    },
    {
        path: '/CssKu',
        name: 'Css库',
        component: CssKu
    },
    {
        path: '/ToolSets',
        name: 'Tools',
        component: ToolSets
    },
    // 添加其他路由...
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
});

export default router;