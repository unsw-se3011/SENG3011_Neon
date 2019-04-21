<template>
  <div>
    <v-progress-circular
      indeterminate
      color="primary"
      v-if="waiting"
    ></v-progress-circular>
    <v-layout row wrap v-else>
      <v-flex xs12>
        <h4>{{ count }} reporst within {{ date_range }} days</h4>
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
        <v-card :to="{ name: 'reportDetail', params: { id: report.id } }">
          <v-img
            :src="report.article.img"
            v-if="report.article.img"
            height="200px"
          >
          </v-img>
          <v-card-title primary-title>
            <div>
              <h3 class="headline mb-0">{{ report.article.headline }}</h3>
              <h5>{{ report.article.date_of_publication | showDate }}</h5>
              <div>
                Observed
                <span v-for="re in report.report_events" :key="re.id">
                  {{ re.number_affected }} {{ re.event_type }}
                </span>
                <span v-if="report.disease">
                  made by
                  {{ report.disease.join(", ") }}.
                </span>
                <span v-else>.</span>
                <br />
                <div v-if="report.syndrome.length != 0">
                  Causes {{ report.syndrome.join(", ") }} <br />
                </div>
                <span v-for="re in report.report_events" :key="re.id">
                  {{ re.location | showLocation }}
                </span>
              </div>
            </div>
          </v-card-title>
        </v-card>
      </v-flex>
      <v-flex xs12 class="text-xs-center">
        <v-progress-linear :indeterminate="page_loading" v-if="page_loading" />
        <v-pagination :length="length" v-model="page" />
      </v-flex>
    </v-layout>
  </div>
</template>
<script>
import { mapState, mapActions } from "vuex";

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
  }
};
</script>
