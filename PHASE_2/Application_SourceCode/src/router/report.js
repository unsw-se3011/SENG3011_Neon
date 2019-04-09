export default [
  {
    path: "/",
    name: "home",
    component: () =>
      import(/* webpackChunkName: "about" */ "@/views/ReportList.vue")
  },
  {
    path: "/reports/detail/",
    name: "reportDetail",
    component: () =>
      import(/* webpackChunkName: "about" */ "@/views/ReportList.vue")
  }
];
