import Vue from "vue";
import VCharts from "v-charts";
import "./plugins/axios";
import "./plugins/vuetify";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "./registerServiceWorker";
import moment from "moment";

Vue.use(VCharts);
Vue.config.productionTip = false;

Vue.filter("showDate", s => {
  return moment(s).format("YYYY MMM DD");
});

Vue.filter("showLocation", lo => {
  if (!lo) {
    return "";
  } else {
    let str = "In ";
    if (lo.city || lo.state) {
      return str + `${lo.city} ${lo.state}, ${lo.country}`;
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
