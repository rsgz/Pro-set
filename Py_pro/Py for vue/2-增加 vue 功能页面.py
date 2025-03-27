# 多页面 多层次 版本
r"""
这个使用的时候 需要判断 是否创建父目录
"""
import os

chuang=0  # 创建父目录吗
name = "WangZhanGaiBan"
zhongwen_ming = "网站改版"
pro_path=r"C:\Users\Administrator\Desktop\vue_pro"
file_name=f"MainView.vue"
# file_name_path = r"C:\Users\Administrator\Desktop\vue_pro\src\views\CssKu.vue"
fu_dir = fr"{pro_path}\src\views\{name}"

if chuang==1:
    os.mkdir(fu_dir)
file_name_path = fr"{pro_path}\src\views\{name}\MainView.vue"
print("vue 文件名:\t\t",file_name)
print(f"父目录：\t\t\t{fu_dir}")
print("vue 文件放置路径:",file_name_path)

print(fr"↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ {file_name} ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
s=fr"""
<template>
    <ul>
        <li><router-link to="/">返回主页</router-link></li>
    </ul>
</template>

<script setup>
</script>

<style scoped>
</style>
"""
print(s)

file_name_path=fr"{pro_path}\src\router\index.js"
print(fr"↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ \router\index.js ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
s = fr"""
# {file_name_path}
import {{ createRouter, createWebHistory }} from 'vue-router';
import {name} from '../views/{name}/{file_name}';

const routes = [
    {{
        path: '/{name}',
        name: '{zhongwen_ming}',
        component: {name}
    }},
];
const router = createRouter({{
    history: createWebHistory(process.env.BASE_URL),
    routes
}});
export default router;
"""
print(s)

print(fr"↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ main.js ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
s=fr"""
// main.js 或 main.ts
import {{ createApp }} from 'vue';
import App from './App.vue';

import router from './router';

const app = createApp(App);
app.use(router)
app.mount('#app');
"""
print(s)


print(fr"↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ other.vue ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
s=fr"""
<template>
<li><router-link to="/{name}">{zhongwen_ming}</router-link></li>
或者
<{name} />
</template>

<script setup>
import {name} from "./{name}.vue";
</script>

<style scoped></style>
"""
print(s)