// main.js 或 main.ts   这是最原始的
import { createApp } from 'vue';
import App from './App.vue';
// import './styles/main.scss';
// 增加了路由  app.use(router)
import router from './router';
// https://element-plus.org/zh-CN/guide/quickstart.html app.use(ElementPlus)
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
// 这个好像不兼容
// import mavonEditor from 'mavon-editor';
// import 'mavon-editor/dist/css/index.css';
// mavonEditor不兼容
// app.use(mavonEditor);
// 全局注册 mavon-editor
// app.component('mavon-editor', mavonEditor.mavonEditor);
// 用这个替代
import VMdEditor from '@kangc/v-md-editor';
import '@kangc/v-md-editor/lib/style/base-editor.css';
import vuepressTheme from '@kangc/v-md-editor/lib/theme/vuepress.js';
import '@kangc/v-md-editor/lib/theme/style/vuepress.css';
// 覆盖 element-plus 的样式
// import './styles/main.scss';
/*
// VMdEditor.use(vuepressTheme);
// app.use(VMdEditor);
或者
VMdEditor.use(vuepressTheme, {
    Prism,
});
app.use(VMdEditor);
*/
// 安装 PrismJS 及其 JSON 语法高亮插件
// Prism
import Prism from 'prismjs';
// highlight code
import 'prismjs/components/prism-json';

const app = createApp(App);
app.use(router)
app.use(ElementPlus)
VMdEditor.use(vuepressTheme, {
    Prism,
});
app.use(VMdEditor);

app.mount('#app');
console.log("成功加载 main.js");
