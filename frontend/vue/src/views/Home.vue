<template>
  <div class="home">
    <Intro/>
    <h1 style="font-family: 'ZCOOL QingKe HuangYou', cursive;">Today is {{date}}
          <Location/>
    </h1>
    <Article/>
    <Footer/>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import Intro from '@/components/Intro.vue' // @ is an alias to /src
import Sheets from '@/components/Sheets.vue'
import Footer from '@/components/Footer.vue'
import Article from '@/components/Articles.vue'
import Location from '@/components/Location.vue'
@Component({
  components: {
    Intro,
    Sheets,
    Footer,
    Article,
    Location
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
