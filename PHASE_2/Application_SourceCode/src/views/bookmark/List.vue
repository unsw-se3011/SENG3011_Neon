<template>
  <v-container grid-list-xs>
    <h1 class="display-1 font-weight-medium">Bookmarked</h1>

    <div v-if="waiting == false">
      <v-progress-circular
        indeterminate
        color="primary"
        v-if="waiting"
      ></v-progress-circular>
      <v-layout row wrap v-else>
        <v-flex xs12>
          <h3>{{ bookmarks.length }} reports.</h3>
        </v-flex>
        <v-flex
          v-for="report in reports_page"
          :key="report.id"
          md6
          xl4
          xm12
          pr-3
          pb-3
        >
          <reportCard :report="report" />
        </v-flex>
        <v-flex xs12 class="text-xs-center" v-if="length > 1">
          <v-pagination :length="length" v-model="page" />
        </v-flex>
      </v-layout>
    </div>
  </v-container>
</template>
<script>
import { mapState, mapActions } from "vuex";
import reportCard from "@/components/report/ReportCard.vue";

export default {
  data() {
    return {
      page: 1
    };
  },
  computed: {
    ...mapState("bookmark", ["bookmarks", "waiting"]),
    length() {
      return Math.ceil(this.bookmarks.length / 12);
    },
    reports_page() {
      if (this.waiting) {
        return [];
      }
      return this.bookmarks
        .slice((this.page - 1) * 12, this.page * 12)
        .map(el => {
          el.id = "n" + el.id;
          return el;
        });
    }
  },
  methods: {
    ...mapActions("bookmark", ["refresh_data"])
  },
  mounted() {
    this.refresh_data();
  },
  components: {
    reportCard
  }
};
</script>
