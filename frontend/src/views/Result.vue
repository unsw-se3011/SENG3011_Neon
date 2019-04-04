
<template>
  <div class="result">
    <Article/>
    <Footer/>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import Article from '@/components/Articles.vue'
@Component({
  components: {
    Article
  }
})
export default class Result extends Vue {
  data () {
    return {
    }
  }
}
</script>
