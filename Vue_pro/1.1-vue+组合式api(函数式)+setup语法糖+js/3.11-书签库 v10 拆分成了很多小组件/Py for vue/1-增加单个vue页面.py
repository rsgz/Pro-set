
name = "CssKu"
zhongwen_ming = "Css库"
pro_path=r"C:\Users\Administrator\Desktop\vue_pro"
file_name=f"{name}.vue"
# file_name_path = r"C:\Users\Administrator\Desktop\vue_pro\src\views\CssKu.vue"
file_name_path = fr"{pro_path}\src\views\{name}.vue"
print("vue 文件名:",file_name)
print("vue 文件放置路径:",file_name_path)

print(fr"↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ {file_name} ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
s=fr"""
<template>
</template>

<script setup>
</script>

<style scoped>
</style>
"""
print(s)


# r"C:\Users\Administrator\Desktop\vue_pro\src\router\index.js"
file_name_path=fr"{pro_path}\src\router\index.js"
print(fr"↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ {file_name_path} ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
s = fr"""
import {{ createRouter, createWebHistory }} from 'vue-router';
import {name} from '../views/{file_name}';

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


print(fr"↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ other.vue 中引用这个组件 ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
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