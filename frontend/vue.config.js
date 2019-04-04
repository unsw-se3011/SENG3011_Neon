module.exports = {
  assetsDir: 'static',
  devServer: {
    proxy: 'http://localhost:6000'
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
