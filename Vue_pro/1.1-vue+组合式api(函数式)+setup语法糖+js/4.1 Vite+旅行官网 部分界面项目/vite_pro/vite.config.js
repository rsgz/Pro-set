import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

import path from 'path'    //  这个用来配置 resolve alias src别名

// unplugin-vue-components 是一个用于 Vue 项目的开源插件，其主要作用是实现按需自动导入组件
import Components from 'unplugin-vue-components/vite' // 增加
import { ElementPlusResolver } from 'unplugin-vue-components/resolvers'  // 增加

// https://vite.dev/config/
export default defineConfig({
  server: {
    open: true,// 自动浏览
    port: 8088,
  },

  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'), // 就是将 @符号配置成了src
    }
  },

  plugins: [
    vue(),
    // 增加 Components
    Components({
      resolvers: [ElementPlusResolver()],
    }),
  ],
})
