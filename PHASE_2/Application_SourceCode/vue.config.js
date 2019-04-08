module.exports = {
  // this may not needed
  // assetsDir: "static",

  devServer: {
    proxy: "http://localhost:8000/v0/"
  },

  chainWebpack: config => {
    config.module
      .rule("eslint")
      .use("eslint-loader")
      .options({
        fix: true
      });
  },

  pwa: {
    themeColor: "#2196F3"
  }
};
