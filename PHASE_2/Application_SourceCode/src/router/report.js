export default [
  {
    path: "/",
    name: "home",
    component: () =>
      import(/* webpackChunkName: "about" */ "@/views/report/List.vue")
  },
  {
    path: "/reports/detail/:id",
    name: "reportDetail",
    component: () =>
      import(/* webpackChunkName: "about" */ "@/views/report/Detail.vue")
  }
];
