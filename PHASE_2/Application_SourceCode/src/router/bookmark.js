export default [
  {
    path: "/bookmark/",
    name: "bookmarkList",
    component: () =>
      import(/* webpackChunkName: "about" */ "@/views/bookmark/List.vue")
  }
];
