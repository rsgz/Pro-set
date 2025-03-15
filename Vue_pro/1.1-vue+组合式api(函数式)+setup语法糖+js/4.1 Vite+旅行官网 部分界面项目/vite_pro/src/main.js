import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

// createApp(App).mount('#app')

import router from './router/index.js'  // 增加 为了router

const app = createApp(App)
app.use(router)
app.mount('#app')