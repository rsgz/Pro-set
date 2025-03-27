import { createRouter, createWebHistory } from 'vue-router';
import Home from '../components/Home.vue';
import WenBenBiJiao from '../components/tools/wenben/WenBenBiJiao.vue';
// import Tool2 from '../components/tools/tool2.vue';

const routes = [
    { path: '/', component: Home },
    { path: '/WenBenBiJiao', component: WenBenBiJiao },
    //   { path: '/tool2', component: Tool2 },
    // 添加更多路由
];
const router = createRouter({
    history: createWebHistory(),
    routes,
});
export default router;