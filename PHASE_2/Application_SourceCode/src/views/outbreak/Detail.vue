<template>
  <v-container grid-list-sm>
    <h2 class="headline">{{ name }} Outbreak</h2>
    <h5>
      From {{ outbreak.start_date | showDate }} to
      {{ outbreak.end_date | showDate }}
    </h5>
    <h3>Infected Chart</h3>
    <ve-scatter :data="infected_data" :settings="chartSettings"></ve-scatter>
    <h2>Report List</h2>
    <reportList />
  </v-container>
</template>

<script>
import { mapState } from "vuex";
import reportList from "@/components/report/List";
import { truncate } from 'fs';
export default {
  data() {
    return {
      name: "",
      waiting: true,
      outbreak: {},
      chartSettings: {
        xAxisType: "time"
      }
    };
  },
  computed: {
    ...mapState("outbreak", ["outbreaks"]),
    ...mapState("search", ["reports"]),
    event_dict() {
      /**
       * to filter the data can be plot to chart
       * and process it to correct format
       */

      // fetch all the report events
      let re_list = [];
      this.reports.forEach(el => {
        re_list = [...re_list, ...el.report_events];
      });
      re_list = re_list.filter(
        el => el.event_type && el.number_affected && el.number_affected < 10000
      );
      let event_dict = {};
      re_list.forEach(el => {
        let this_date = el.start_date.substring(0, 10);
        if (!event_dict[this_date]) {
          // new record
          event_dict[this_date] = {};
        }
        event_dict[this_date][el.event_type] = el.number_affected;
      });
      // format the ouput
      return event_dict;
    },
    infected_data() {
      let infected = [];
      Object.keys(this.event_dict)
        .sort()
        .forEach(date => {
          if (this.event_dict[date]["Infected"]) {
            infected.push({
              date: date.substring(0, 12),
              Infected: this.event_dict[date]["Infected"]
            });
          }
        });

      // assemble the data
      return { columns: ["date", "Infected"], rows: infected };
    }
  },
  mounted() {
    // console.log(this.$route.params.id)
    let out = this.outbreaks.find(el => el.id == this.$route.params.id);
    this.outbreak = out;
    this.name = out.key_term;
    this.$store.commit("search/set_by_outbreak", out);
    // force frontend db to refresh data 
    this.$store.dispatch("search/refresh_data", true);
  },
  components: {
    reportList
  }
};
</script>
