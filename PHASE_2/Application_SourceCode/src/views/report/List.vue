<template>
  <v-container grid-list-xs>
    <h1 class="display-1 font-weight-medium">Report List</h1>
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
    // I may need a book mark array
    this.$store.dispatch("bookmark/refresh_data");
  }
};
</script>
