import Vue from "vue";
import Vuex from "vuex";
import search from "./search.js";
import report from "./report.js";
import outbreak from "./outbreak.js";
import auth from "./auth.js";
import bookmark from "./bookmark.js";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {},
  mutations: {},
  actions: {},
  modules: { search, report, outbreak, auth, bookmark }
});
