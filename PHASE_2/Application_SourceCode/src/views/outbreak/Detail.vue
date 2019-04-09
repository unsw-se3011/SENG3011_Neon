<template>
  <v-container grid-list-sm>
    <h2 class="headline">{{ name }} Outbreak</h2>
    <h5>
      From {{ outbreak.start_date | showDate }} to
      {{ outbreak.end_date | showDate }}
    </h5>
    {{ chartData }}

    <h2>Report List</h2>
    <reportList />
  </v-container>
</template>

<script>
  // <ve-line :data="chartData" :settings="chartSettings"></ve-line>

import { mapState } from "vuex";
import reportList from "@/components/report/List";
export default {
  data() {
    return { name: "", waiting: true, outbreak: {}, 
    chartSettings : {
      xAxisType:'time'
    }
    };
  },
  computed: {
    ...mapState("outbreak", ["outbreaks"]),
    ...mapState("search", ["reports"]),
    chartData() {
      /**
       * to filter the data can be plot to chart
       * and process it to correct format
       */

      // fetch all the report events
      let re_list = [];
      this.reports.forEach(el => {
        re_list = [...re_list, ...el.report_events];
      });
      re_list = re_list.filter(el => el.event_type && el.number_affected);
      let event_dict = {}
      re_list.forEach(el => {
        let this_date = el.start_date.substring(0,10)
        if( ! event_dict[this_date]){
          // new record 
          event_dict[this_date] =  {}
        }
        event_dict[this_date][el.event_type] = el.number_affected
      })
      // format the ouput
      return {
        columns: [
          "date",
          "Presence",
          "Death",
          "Infected",
          "Hospitalised",
          "Recovered"
        ],
        rows: event_dict
      };
    }
  },
  mounted() {
    // console.log(this.$route.params.id)
    let out = this.outbreaks.find(el => el.id == this.$route.params.id);
    this.outbreak = out;
    this.name = out.key_term;
    this.$store.commit("search/set_by_outbreak", out);
  },
  components: {
    reportList
  }
};
</script>
