// import { createApp } from 'vue'
// import App from './App.vue'

// createApp(App).mount('#app')


// main.js 或 main.ts
import { createApp } from 'vue';
import App from './App.vue';

import router from './router';

const app = createApp(App);
app.use(router)

// https://element-plus.org/zh-CN/guide/quickstart.html
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

// import mavonEditor from 'mavon-editor';
// import 'mavon-editor/dist/css/index.css';

app.use(ElementPlus)

// mavonEditor不兼容
// app.use(mavonEditor);
// 全局注册 mavon-editor
// app.component('mavon-editor', mavonEditor.mavonEditor);

// 用这个替代
import VMdEditor from '@kangc/v-md-editor';
import '@kangc/v-md-editor/lib/style/base-editor.css';
import vuepressTheme from '@kangc/v-md-editor/lib/theme/vuepress.js';
import '@kangc/v-md-editor/lib/theme/style/vuepress.css';

// VMdEditor.use(vuepressTheme);
// app.use(VMdEditor);

// 安装 PrismJS 及其 JSON 语法高亮插件
// Prism
import Prism from 'prismjs';
// highlight code
import 'prismjs/components/prism-json';

VMdEditor.use(vuepressTheme, {
    Prism,
});
app.use(VMdEditor);

app.mount('#app');