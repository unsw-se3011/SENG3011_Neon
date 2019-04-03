import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import About from './views/About.vue'
import Support from './views/Support.vue'
import Map from './views/Map.vue'
import Result from './views/Result.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: About
    },
    {
      path: '/support',
      name: 'support',
      component: Support
    },
    {
      path: '/map',
      name: 'map',
      component: Map
    },
    {
      path: '/result/:start/:end/:keyword/:add',
      name: 'result',
      component: Result
    }
  ]
})
