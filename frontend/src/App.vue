<!--
  Main app controller,defines the top tool bar with searchbar and login register entry
  as well as map entry
  This contains search bar and login components.
-->
<template>
  <v-app>
    <v-toolbar dark>
      <div class="text-uppercase md-and-up">
         <router-link to='/' style="text-decoration: none;">
          <v-btn flat>
            <span style="font-size:200%;">EpiWATCH</span>
          </v-btn>
         </router-link>
      </div>
      <v-spacer></v-spacer>

      <!-- Components insert -->
      <Login/>
     <!--
       About and support if is neccessary
       <router-link to='/about' style="text-decoration: none;">
        <v-btn flat>
          <span class="mr-1" style="color:white;font-size:20px">About</span>
        </v-btn>
      </router-link>
      <router-link to='/support' style="text-decoration: none;">
        <v-btn flat>
          <span class="mr-1" style="color:white;font-size:20px">Support</span>
        </v-btn>
      </router-link>
      -->

      <!-- map entry  -->
      <router-link to='/map' style="text-decoration: none;">
        <v-btn flat>
          <span class="mr-1" style="font-size:20px">Map</span>
        </v-btn>
      </router-link>
    </v-toolbar>
    <router-view/>
  </v-app>
</template>

<script>
// defines the location in maps imports components
import Login from '@/components/Login'
const locations = [
  {
    position: {
      lat: 48.160910,
      lng: 16.383330
    }
  },
  {
    position: {
      lat: 48.174270,
      lng: 16.329620
    }
  },
  {
    position: {
      lat: 48.146140,
      lng: 16.297030
    }
  },
  {
    position: {
      lat: 48.135830,
      lng: 16.194460
    }
  },
  {
    position: {
      lat: 48.306091,
      lng: 14.286440
    }
  },
  {
    position: {
      lat: 47.503040,
      lng: 9.747070
    }
  }
]

export default {
  name: 'App',
  components: {
    Login
  },
  data () {
    return {
      //
    }
  }
}
</script>
<!-- Baic web style controls the size of the webpage -->
<style>
html,
body {
  margin: 0;
  padding: 0;
}
.App {
  width: 100vw;
  height: 100vh;
}
</style>
