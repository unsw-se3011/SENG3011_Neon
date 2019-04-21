export default [
  {
    path: "/auth/login/",
    name: "login",
    component: () =>
      import(/* webpackChunkName: "about" */ "@/views/auth/Login.vue")
  },
  {
    path: "/auth/logout/",
    name: "logout",
    component: () =>
      import(/* webpackChunkName: "about" */ "@/views/auth/Logout.vue")
  },
  {
    path: "/auth/register/",
    name: "register",
    component: () =>
      import(/* webpackChunkName: "about" */ "@/views/auth/Register.vue")
  }
];
