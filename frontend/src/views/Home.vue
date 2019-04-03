<!--
  Home component controls the section below intro & toolbar.
  Includes map, article and footer components in this section
-->

<template>
  <div class="home">
    <Intro/>
    <h1>Today is {{date}}</h1>
    <h2><SearchBar/> </h2>
    <Article/>
    <Footer/>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import Intro from '@/components/Intro.vue'
import Footer from '@/components/Footer.vue'
import Article from '@/components/Articles.vue'
import SearchBar from '@/components/SearchBar.vue'
@Component({
  components: {
    Intro,
    Footer,
    Article,
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
