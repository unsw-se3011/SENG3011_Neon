<template>
  <div>
    <v-progress-circular
      indeterminate
      color="primary"
      v-if="waiting"
    ></v-progress-circular>
    <v-layout row wrap v-else>
      <v-flex xs12>
        <h4>{{ count }} reporst within {{date_range}} days
        </h4>
      </v-flex>
      <v-flex v-for="report in reports" :key="report.id" md6 xl4 xm12 pr-3 pb-3>
        <v-card :to="{ name: 'reportDetail', params: { id: report.id } }">
          <v-img
            :src="report.article.img"
            v-if="report.article.img"
            height="200px"
          >
          </v-img>
          <v-card-title primary-title>
            <div>
              <h3 class="headline mb-0">
                Observed
                <span v-for="re in report.report_events" :key="re.id">
                  {{ re.number_affected }} {{ re.event_type }}
                </span>
                make by
                {{ report.disease.join(", ") }}
              </h3>
              <div>
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
    </v-layout>
  </div>
</template>
<script>
import { mapState, mapActions } from "vuex";

export default {
  computed: {
    ...mapState("search", [
      "reports",
      "waiting",
      "count",
      "start_date",
      "end_date"
    ]),
    date_range() {
      if(this.waiting || !this.start_date || !this.end_date){
        return 0
      }
      let sd = new Date(this.start_date);
      let ed = new Date(this.end_date);
      return (ed.getTime() - sd.getTime())/86400000
    }
  },
  methods: {
    ...mapActions("search", ["refresh_data"])
  },
};
</script>
