<template>
  <v-container grid-list-sm>
    <h2 class="display-1 font-weight-medium font-weight-medium">
      {{ name }} Outbreak
    </h2>
    <h4>
      From {{ outbreak.start_date | showDate }} to
      {{ outbreak.end_date | showDate }}
    </h4>

    <ve-scatter
      v-if="!waiting"
      :data="chart_data"
      :settings="chartSettings"
    ></ve-scatter>

    <h1 class="my-1 font-weight-medium">Map</h1>
    <mapComp :chartData="chart_data.map_arr" style="max-height:500px" />

    <div class="my-1" v-if="!waiting">
      <h2 class="font-weight-medium">Report List</h2>
      <reportList />
    </div>
  </v-container>
</template>

<script>
import { mapState } from "vuex";
import reportList from "@/components/report/List";
import mapComp from "@/components/map/MapDigest.vue";
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
    reportList,
    mapComp
  }
};
</script>
