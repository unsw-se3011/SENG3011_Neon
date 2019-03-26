import Vue from 'vue'
import './plugins/vuetify'
import './registerServiceWorker'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import { library } from '@fortawesome/fontawesome-svg-core'
import {
  faTwitter, faFacebook, faStackOverflow, faGithub
} from '@fortawesome/free-brands-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import * as VueGoogleMaps from 'vue2-google-maps'
import axios from 'axios'
import store from './store'
import router from './router'
import App from './App.vue'

Vue.use(Vuetify)
library.add(faTwitter, faFacebook, faStackOverflow, faGithub)
Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.config.productionTip = false
Vue.prototype.$axios = axios

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyDjxqr5F7xTf1c1ZnEfbIDE4-Q7a37H3Sk',
    libraries: 'places',
    load: {
      region: 'AU',
      language: 'en'
    }
    // This is required if you use the Autocomplete plugin
    // OR: libraries: 'places,drawing'
    // OR: libraries: 'places,drawing,visualization'
    // (as you require)

    // // If you want to set the version, you can do so:
    // v: '3.26',
  }
})
