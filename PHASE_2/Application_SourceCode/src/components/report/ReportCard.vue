<template>
  <v-card :to="{ name: 'reportDetail', params: { id: report.id } }">
    <v-img :src="report.article.img" v-if="report.article.img" height="200px">
    </v-img>
    <v-card-title primary-title>
      <div>
        <h3 class="headline mb-0">
          {{ report.article.headline }}
          <v-btn
            :color="in_bookmark ? 'blue-grey' : 'blue-grey lighten-3'"
            flat
            v-if="username"
            icon
            @click.prevent="toggle"
          >
            <v-icon>
              {{ in_bookmark ? "star" : "star_border" }}
            </v-icon>
          </v-btn>
        </h3>
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
</template>

<script>
import { mapActions, mapState } from "vuex";
export default {
  props: {
    report: Object
  },
  computed: {
    ...mapState("bookmark", ["bookmark_ids"]),
    ...mapState("auth", ["username"]),
    report_id() {
      if (typeof this.report.id == "number") {
        return this.report.id;
      }
      return parseInt(this.report.id.substr(1));
    },
    in_bookmark() {
      return this.bookmark_ids.includes(this.report_id);
    }
  },
  methods: {
    ...mapActions("bookmark", ["toggle_bookmark"]),
    toggle() {
      this.toggle_bookmark(this.report_id);
    }
  }
};
</script>
