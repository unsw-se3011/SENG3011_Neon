<!--
  Home component controls the section below intro & toolbar.
  Includes map, article and footer components in this section
-->

<template>
  <div class="home">
    <Intro/>
    <h1>Today is {{date}}</h1>
    <h2><SearchBar/> </h2>
    <p  style="color:#A9A9A9;font-size:15px"> *Start date and end date could not be the same </p>
    <Footer/>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import Intro from '@/components/Intro.vue'
import Footer from '@/components/Footer.vue'
import SearchBar from '@/components/SearchBar.vue'
@Component({
  components: {
    Intro,
    Footer,
    SearchBar
  }
})
export default class Home extends Vue {
  data () {
    return {
      date: new Date().toISOString().substr(0, 10)
    }
  }
}
</script>
