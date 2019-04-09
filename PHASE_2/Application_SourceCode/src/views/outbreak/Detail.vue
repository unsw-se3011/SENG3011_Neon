<template>
  <v-container grid-list-sm>
    <h2 class="headline">{{ name }} Outbreak</h2>
    <h5>
      From {{ outbreak.start_date | showDate }} to
      {{ outbreak.end_date | showDate }}
    </h5>
    <reportList />
  </v-container>
</template>

<script>
import { mapState } from "vuex";
import reportList from "@/views/report/List";
export default {
  data() {
    return { name: "", waiting: true, outbreak: {} };
  },
  computed: mapState("outbreak", ["outbreaks"]),
  mounted() {
    // console.log(this.$route.params.id)
    let out = this.outbreaks.find(el => el.id == this.$route.params.id);
    this.outbreak = out;
    this.name = out.key_term;
    this.$store.commit("search/set_by_outbreak", out);
  },
  components: {
    reportList
  }
};
</script>
