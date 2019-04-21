<template>
  <GChart
    type="GeoChart"
    :data="chartData"
    :options="chartOptions"
    :settings="settings"
    style="max-height:80%"
  />
</template>

<script>
import { GChart } from "vue-google-charts";

export default {
  props: {
    chartData: Array
  },
  data() {
    return {
      // map api key
      api_key: "AIzaSyB6IaopsDWBemevu37s39weiIuF0Y8_cgY",
      // Array will be automatically processed with visualization.arrayToDataTable function
      // chartData: [
      //   ["Country", "Affected"],
      //   ["Germany", 200],
      //   ["United States", 300],
      //   ["Brazil", 400],
      //   ["Canada", 500],
      //   ["France", 600],
      //   ["RU", 700]
      // ],
      chartOptions: {
        height: window.innerHeight * 0.5,
        backgroundColor: "",
        colors: ["#FFCDD2", "#F44336"]
      },
      settings: {
        packages: ["geochart"],
        mapsApiKey: "AIzaSyB6IaopsDWBemevu37s39weiIuF0Y8_cgY"
      }
    };
  },
  mounted() {},
  components: {
    GChart
  }
};
</script>
