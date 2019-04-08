<template>
  <v-container grid-list-xs>
    <h2>Report List</h2>
    {{ reports }}
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  computed: mapState("search", ["reports"]),
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
