import { createApp } from 'vue'
import App from './App.vue'

const app = createApp(App)

import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
app.use(ElementPlus)

// import { mavonEditor } from 'mavon-editor';
// import 'mavon-editor/dist/css/index.css';
// app.use(mavonEditor)

app.mount('#app')