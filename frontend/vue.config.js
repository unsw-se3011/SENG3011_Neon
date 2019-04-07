module.exports = {
  assetsDir: 'static',
  devServer: {
    proxy: 'http://localhost:8000/v0/'
  },
  chainWebpack: (config) => {
    config.module
      .rule('eslint')
      .use('eslint-loader')
      .loader('eslint-loader')
      .options({
        fix: true
      })
  }
}
