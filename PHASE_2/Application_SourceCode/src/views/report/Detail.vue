<template>
  <v-container grid-list-xs v-if="!waiting">
    <h1 class="headline">{{ article.headline }}</h1>
    <h5 class="info--text">{{ article.date_of_publication | showDate }}</h5>
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
    <h5>{{ search_term }} from {{ search_start | showDate }}</h5>
    <relatedNews
      :start_date="search_start"
      :end_date="search_end"
      :key_word="search_term"
    />
  </v-container>
</template>

<script>
import reportEvent from "@/components/reportEventCard.vue";
import relatedNews from "@/components/relatedNews.vue";
import { mapActions } from "vuex";
export default {
  data() {
    return {
      waiting: true,
      report: {},
      article: {}
    };
  },
  computed: {
    search_start() {
      // algorithem to minux 15 days from publish
      // let stamp = new Date(this.article.date_of_publication).getTime();
      let stamp = new Date().getTime();
      stamp -= 1296000 * 1000;
      return new Date(stamp).toISOString();
    },
    search_end() {
      // algorithem to plus 15 days from publish
      // let stamp = new Date(this.article.date_of_publication).getTime();
      // stamp+=1296000*1000;
      return new Date().toISOString();
    },
    search_term() {
      // by hiarachy to return
      // Disease > Syndrome > Location
      if (this.report.disease.length != 0) {
        // find a disease that's not others
        let disease_name = this.report.disease.find(el => el != "other");
        if (disease_name) {
          return disease_name;
        }
      }
      if (this.report.syndrome.length != 0) {
        return this.report.syndrome[0];
      }
      if (this.report.report_events.length != 0) {
        // the first element with country attr
        let el = this.report.report_events.find(
          el => el.location && el.location.country
        );
        return el.location.country;
      }
      // failover
      return "zika";
    }
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
    reportEvent,
    relatedNews
  }
};
</script>
