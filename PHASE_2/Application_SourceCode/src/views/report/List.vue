<template>
  <v-container grid-list-xs>
    <h1 class="headline">Report List</h1>
    <reportListComp />
  </v-container>
</template>

<script>
import reportListComp from "@/components/report/List.vue";
export default {
  components: {
    reportListComp
  }
};
</script>
