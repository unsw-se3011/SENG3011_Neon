export default [
  {
    path: "/outbreak/",
    name: "outbreakIndex",
    component: () =>
      import(/* webpackChunkName: "about" */ "@/views/outbreak/List.vue")
  },
  {
    path: "/outbreak/:id",
    name: "outbreakDetail",
    component: () =>
      import(/* webpackChunkName: "about" */ "@/views/outbreak/Detail.vue")
  }
];
