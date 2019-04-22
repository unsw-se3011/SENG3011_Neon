<template>
  <v-container grid-list-xs>
    <h1 class="headline font-weight-medium">Report List</h1>
    <reportListComp />
  </v-container>
</template>

<script>
import reportListComp from "@/components/report/List.vue";
export default {
  components: {
    reportListComp
  },

  mounted() {
    this.$store.dispatch("search/refresh_data");
  }
};
</script>
