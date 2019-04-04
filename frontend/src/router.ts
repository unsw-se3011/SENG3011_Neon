import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
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
      path: '/map',
      name: 'map',
      component: Map
    },
    {
      path: '/result/:start&:end&:keyword&:location',
      name: 'result',
      component: Result
    }
  ]
})
