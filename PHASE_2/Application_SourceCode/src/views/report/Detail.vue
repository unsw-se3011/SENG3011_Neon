<template>
  <v-container grid-list-xs v-if="!waiting">
    <h1 class="headline">
      {{ article.headline }}
      <v-btn flat color="success" :href="article.url">
        go Original
        <v-icon>launch</v-icon>
      </v-btn>
    </h1>
    <h5 class="info--text">{{ article.date_of_publication | showDate }}</h5>
    <p>{{ article.main_text }}</p>
    <div v-if="report.disease && report.disease.length != 0">
      <h3>Disease</h3>
      <p>{{ report.disease.join(", ") }}</p>
    </div>
    <div v-if="report.syndrome && report.syndrome.length != 0">
      <h3>Syndrome</h3>
      <p>{{ report.syndrome.join(", ") }}</p>
    </div>
    <div></div>
    <div v-if="report.report_events && report.report_events.length != 0">
      <h3>Events</h3>
      <div v-for="re in report.report_events" :key="re.event_type">
        <reportEvent :event="re" />
      </div>
    </div>
    <div>
      <h3>Comment</h3>
      <commentList
        v-if="username"
        :msg_list="report.comment"
        :report_id="report_id"
        @change="update_neon"
      />
    </div>
    <h3>Related</h3>
    <h5>
      {{ search_term }} from {{ search_start | showDate }} to
      {{ search_end | showDate }}
    </h5>
    <relatedNews
      :start_date="search_start"
      :end_date="search_end"
      :key_word="search_term"
    />
  </v-container>
</template>

<script>
import reportEvent from "@/components/reportEventCard.vue";
import CommentList from "@/components/report/CommentList.vue";
import relatedNews from "@/components/relatedNews.vue";
import { mapActions, mapState } from "vuex";
export default {
  data() {
    return {
      waiting: true,
      report: {},
      article: {}
    };
  },
  computed: {
    ...mapState("search", ["reports"]),
    ...mapState("auth", ["username"]),
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
    },
    is_neon() {
      let id = this.$route.params.id;
      let neon_id = /^n([0-9]+)/.exec(id);
      if (neon_id) {
        return true;
      }
      return false;
    },
    report_id() {
      return parseInt(this.$route.params.id.substr(1));
    }
  },

  methods: {
    ...mapActions("report", ["get_neon_report"]),
    async update_neon() {
      // fetch the report from backend
      let ret = await this.get_neon_report(this.report_id);
      this.report = ret.data;
      this.article = this.report.article;
      this.waiting = false;
    }
  },
  async mounted() {
    let re_src = this.$route.params.id.substr(0, 1);

    if (this.is_neon) {
      this.update_neon();
    } else if (re_src == "r") {
      /**
       * support the ramen api
       * Fetch the relative id from our backend
       */
      this.report_id;
      // assign the report and article
      this.report = this.reports.find(el => el.id == this.report_id);
      this.article = this.report.article;
      console.log(this.report);
      this.waiting = false;
    }
  },
  components: {
    reportEvent,
    relatedNews,
    CommentList
  }
};
</script>
