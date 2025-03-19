const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,  // 转译某些依赖项
})

module.exports = {
  // 添加的 devServer 配置
  devServer: {
    port: 8081, // 设置开发服务器的端口号
    host: "0.0.0.0", // 主机地址
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000', // 指向你的后端服务地址
        changeOrigin: true,              // 是否跨域 解决了跨域问题
        // ws: true,     //   不加这个属性，浏览器控制台会一直报连不上 socket 的错
        // pathRewrite: { '^/api': '' }, // 如果需要去除前缀  // 路径重写
        pathRewrite: { '^/api': '/api' }, // 如果需要去除前缀  // 路径重写
        onProxyReq: function (proxyReq, req, res) {
          console.log('代理指向-->:', proxyReq.path);
        }
      }
    }
  },
  // lintOnSave: false   // 取消 eslint 验证  当你设置 lintOnSave: false 时，Vue CLI 将不会在你每次保存项目文件时自动运行 ESLint 检查 
}