module.exports = {
  // this may not needed
  // assetsDir: "static",

  devServer: {
    proxy: "http://localhost:8000/v0/"
  },

  pwa: {
    themeColor: '#2196F3'
  }
};