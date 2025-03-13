// import { createApp } from 'vue'
// import App from './App.vue'

// createApp(App).mount('#app')


// main.js 或 main.ts
import { createApp } from 'vue';
import App from './App.vue';

const app = createApp(App);

// https://element-plus.org/zh-CN/guide/quickstart.html
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

// import mavonEditor from 'mavon-editor';
// import 'mavon-editor/dist/css/index.css';



app.use(ElementPlus)

// app.use(mavonEditor);
// 全局注册 mavon-editor
// app.component('mavon-editor', mavonEditor.mavonEditor);

app.mount('#app');