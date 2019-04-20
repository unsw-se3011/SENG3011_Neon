<template>
  <v-container grid-list-sm>
    <h2 class="headline">{{ name }} Outbreak</h2>
    <h5>
      From {{ outbreak.start_date | showDate }} to
      {{ outbreak.end_date | showDate }}
    </h5>
    <h3>Infected Chart</h3>
    <ve-scatter
      v-if="!waiting"
      :data="chart_data"
      :settings="chartSettings"
    ></ve-scatter>
    <div v-if="!waiting">
      <h2>Report List</h2>
      <reportList />
    </div>
  </v-container>
</template>

<script>
import { mapState } from "vuex";
import reportList from "@/components/report/List";
export default {
  data() {
    return {
      name: "",
      waiting: true,
      outbreak: {},
      chartSettings: {
        xAxisType: "time"
      },
      chart_data: {}
    };
  },
  computed: {
    ...mapState("outbreak", ["outbreaks"])
  },
  async mounted() {
    // console.log(this.$route.params.id)

    let ret = await this.$store.dispatch(
      "outbreak/get_detail",
      this.$route.params.id
    );
    this.outbreak = ret.data;
    this.chart_data = this.outbreak.chart;
    this.name = this.outbreak.key_term;
    this.$store.commit("search/set_by_outbreak", this.outbreak);
    // force frontend db to refresh data
    this.$store.dispatch("search/refresh_data", true);
    this.waiting = false;
  },
  components: {
    reportList
  }
};
</script>
