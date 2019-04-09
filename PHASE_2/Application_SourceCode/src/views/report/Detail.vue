<template>
  <v-container grid-list-xs v-if="!waiting">
    <h2>{{ article.headline }}</h2>
    <h5 class="info--text">{{ article | showDate }}</h5>
    <p>
      {{ article.main_text }}
    </p>
    <div v-if="report.disease.length != 0">
      <h3>Disease</h3>
      <p>{{ report.disease.join(", ") }}</p>
    </div>
    <div v-if="report.syndrome.length != 0">
      <h3>Syndrome</h3>
      <p>{{ report.syndrome.join(", ") }}</p>
    </div>
    <div></div>
    <div v-if="report.report_events.length != 0">
      <h3>Events</h3>
      <div v-for="re in report.report_events" :key="re.event_type">
        <reportEvent :event="re" />
      </div>
    </div>
    <h3>Comment</h3>
    <p>
      Carly: This event should have more care
    </p>
    <h3>Related</h3>
  </v-container>
</template>

<script>
import reportEvent from "@/components/reportEventCard.vue";
import { mapActions } from "vuex";
export default {
  data() {
    return {
      waiting: true,
      report: {},
      article: {}
    };
  },
  methods: {
    ...mapActions("report", ["get_neon_report"])
  },
  async mounted() {
    let id = this.$route.params.id;
    // try to match the neon id
    let neon_id = /^n([0-9]+)/.exec(id);
    if (neon_id) {
      neon_id = neon_id[1];
      // fetch the report from backend
      let ret = await this.get_neon_report(neon_id);
      this.report = ret.data;
      this.article = this.report.article;
      this.waiting = false;
    } else {
      // pass, to suppport multiple api
    }
  },
  components: {
    reportEvent
  }
};
</script>
