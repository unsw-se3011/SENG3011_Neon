<template>
  <v-container fluid grid-list-xs>
    <h2>Report List</h2>
    <v-progress-circular
      indeterminate
      color="primary"
      v-if="waiting"
    ></v-progress-circular>
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  computed: mapState("search", ["reports", "waiting"]),
  methods: {
    ...mapActions("search", ["refresh_data"])
  },
  mounted() {
    this.refresh_data();
  }

  // components: {
  // }
};
</script>
