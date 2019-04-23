<template>
  <div>
    <v-progress-circular
      indeterminate
      color="primary"
      v-if="waiting"
    ></v-progress-circular>
    <v-layout row wrap v-else>
      <v-flex xs12>
        <h3>{{ count }} reporst within {{ date_range }} days</h3>
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
        <v-progress-linear :indeterminate="page_loading" v-if="page_loading" />
        <v-pagination :length="length" v-model="page" />
      </v-flex>
    </v-layout>
  </div>
</template>
<script>
import { mapState, mapActions } from "vuex";
import reportCard from "@/components/report/ReportCard.vue";

export default {
  data() {
    return {
      page_rec: 1,
      page_loading: false
    };
  },
  computed: {
    ...mapState("search", [
      "reports",
      "waiting",
      "count",
      "start_date",
      "end_date"
    ]),
    date_range() {
      if (this.waiting || !this.start_date || !this.end_date) {
        return 0;
      }
      let sd = new Date(this.start_date);
      let ed = new Date(this.end_date);
      return (ed.getTime() - sd.getTime()) / 86400000;
    },
    page: {
      get() {
        return this.page_rec;
      },
      async set(val) {
        this.page_rec = val;
        while (this.page_rec > Math.ceil(this.reports.length / 12)) {
          this.page_loading = true;
          // recursive to the correct page
          await this.fetch_neon_next();
        }
        // load successful
        this.page_loading = false;
        return val;
      }
    },
    length() {
      return Math.ceil(this.count / 12);
    },
    reports_page() {
      if (this.waiting) {
        return [];
      }
      return this.reports.slice((this.page - 1) * 12, this.page * 12);
    }
  },
  methods: {
    ...mapActions("search", ["refresh_data", "fetch_neon_next"])
  },
  components: {
    reportCard
  }
};
</script>
