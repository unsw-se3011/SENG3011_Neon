import Vue from "vue";
import Router from "vue-router";

import report from "./report";
import outbreak from "./outbreak";
import auth from "./auth.js";
import bookmark from "./bookmark.js";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    ...report,
    ...outbreak,
    ...auth,
    ...bookmark,
    { path: "*", redirect: { name: "home" } }
  ]
});
