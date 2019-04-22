<template>
  <v-btn
    :color="in_bookmark ? 'blue-grey' : 'blue-grey lighten-3'"
    flat
    v-if="username"
    icon
    @click.prevent="toggle"
  >
    <v-icon>
      {{ in_bookmark ? "star" : "star_border" }}
    </v-icon>
  </v-btn>
</template>
<script>
import { mapActions, mapState } from "vuex";
export default {
  props: {
    report_id: Number
  },
  computed: {
    ...mapState("auth", ["username"]),
    ...mapState("bookmark", ["bookmark_ids"]),
    in_bookmark() {
      return this.bookmark_ids.includes(this.report_id);
    }
  },
  methods: {
    ...mapActions("bookmark", ["toggle_bookmark"]),
    toggle() {
      this.toggle_bookmark(this.report_id);
    }
  }
};
</script>
