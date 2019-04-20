export default [
  {
    path: "/auth/login/",
    name: "login",
    component: () =>
      import(/* webpackChunkName: "about" */ "@/views/auth/Login.vue")
  },
  {
    path: "/auth/register/",
    name: "register",
    component: () =>
      import(/* webpackChunkName: "about" */ "@/views/auth/Register.vue")
  }
];
