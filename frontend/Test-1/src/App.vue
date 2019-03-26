<template>
  <v-app>
    <v-toolbar dark color="black" style="font-family: 'ZCOOL QingKe HuangYou', cursive;">
      <div class="white--text text-uppercase md-and-up">
         <router-link to='/' style="text-decoration: none;">
          <v-btn flat>
            <span style="color:greenyellow;font-size:200%;">Neon</span> 
          </v-btn> 
         </router-link>
      </div>
      <v-spacer></v-spacer>
      <SearchBar/>
      <Login/>
      <router-link to='/about' style="text-decoration: none;">
        <v-btn flat>
          <span class="mr-1" style="color:greenyellow;font-size:20px">About</span> 
        </v-btn> 
      </router-link>
      <router-link to='/support' style="text-decoration: none;">
        <v-btn flat>
          <span class="mr-1" style="color:greenyellow;font-size:20px">Support</span> 
        </v-btn> 
      </router-link>
      <router-link to='/map' style="text-decoration: none;">
        <v-btn flat>
          <span class="mr-1" style="color:greenyellow;font-size:20px">Map</span> 
        </v-btn> 
      </router-link>
    </v-toolbar>
    <router-view/>
  </v-app>
</template>

<script>
//import HelloWorld from '@/components/HelloWorld';
//import Sheets from '@/components/Sheets';
//import Intro from '@/components/Intro';
import SearchBar from '@/components/SearchBar';
import Login from '@/components/Login';
const locations = [
  {
    position: {
      lat: 48.160910,
      lng: 16.383330,
    },
  },
  {
    position: {
      lat: 48.174270,
      lng: 16.329620,
    },
  },
  {
    position: {
      lat: 48.146140,
      lng: 16.297030,
    },
  },
  {
    position: {
      lat: 48.135830,
      lng: 16.194460,
    },
  },
  {
    position: {
      lat: 48.306091,
      lng: 14.286440,
    },
  },
  {
    position: {
      lat: 47.503040,
      lng: 9.747070,
    },
  },
];

export default {
  name: 'App',
  components: {
    SearchBar,
    Login,
  },
  data() {
    return {
      //
    }
  }
}
</script>

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


