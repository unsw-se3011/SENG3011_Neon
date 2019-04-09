import Vue from "vue";
import "./plugins/axios";
import "./plugins/vuetify";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "./registerServiceWorker";

Vue.config.productionTip = false;

Vue.filter("showLocation", lo => {
  if (!lo) {
    return "";
  } else {
    let str = "In ";
    if (lo.city || lo.state) {
      return str + `${lo.city} ${lo.state} ,${lo.country}`;
    }
    // else only have country
    return str + lo.country;
  }
});

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
