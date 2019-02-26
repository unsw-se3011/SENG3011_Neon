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
    </v-toolbar>
    <router-view/>
  </v-app>
</template>

<script>
//import HelloWorld from '@/components/HelloWorld';
//import Sheets from '@/components/Sheets';
//import Intro from '@/components/Intro';
import SearchBar from '@/components/SearchBar';
export default {
  name: 'App',
  components: {
    SearchBar,
  },
  data() {
    return {
      //
    }
  }
}
</script>

