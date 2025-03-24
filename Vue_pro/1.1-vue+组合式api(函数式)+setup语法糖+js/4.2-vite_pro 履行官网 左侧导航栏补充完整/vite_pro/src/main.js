import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

// createApp(App).mount('#app')

import router from './router/index.js'  // 增加 为了router
import '@/assets/icon/iconfont.css'

const app = createApp(App)
app.use(router)
app.mount('#app')

console.log("已经加载 main.js22");
