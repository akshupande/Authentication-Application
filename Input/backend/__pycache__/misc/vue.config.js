// vue.config.js
module.exports = {
  configureWebpack: {
    devtool: 'source-map'
  },
  publicPath: process.env.NODE_ENV === "production" ? "/test/" : "/",
  devServer: {
    port: 8081,
    proxy: {
      // 代理所有请求
      "/api": {
        // 后端rest服务
        target: "https://xxx.com/api",
        ws: false,
        changeOrigin: true,
        pathRewrite: {
          '^/api': '' // 这个是定义要访问的路径，名字随便写
        }
      }
    }
  }
};
