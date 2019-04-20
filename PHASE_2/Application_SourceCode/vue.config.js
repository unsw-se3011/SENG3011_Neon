module.exports = {
  // this may not needed
  // assetsDir: "static",

  devServer: {
    proxy: "http://localhost:8000/"
  },

  // publicPath:
  //   process.env.NODE_ENV === "production"
  //     ? "http://neon.whiteboard.house/v0/"
  //     : "http://localhost:8000/v0/",

  pwa: {
    themeColor: "#2196F3"
  },

  pluginOptions: {
    moment: {
      locales: ["au"]
    }
  }
};
