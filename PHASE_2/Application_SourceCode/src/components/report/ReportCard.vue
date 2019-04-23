<template>
  <v-card :to="{ name: 'reportDetail', params: { id: report.id } }">
    <v-img :src="report.article.img" v-if="report.article.img" height="200px">
    </v-img>
    <v-card-title primary-title>
      <div class="px-2">
        <h3 class="headline mb-0">
          {{ report.article.headline }}
        </h3>
        <h4>
          {{ report.article.date_of_publication | showDate }}
          <BookmarkBtn :report_id="report_id" />
        </h4>
        <div class="mt-1">
          Observed
          {{ event_digest }}
          <span v-if="report.disease">
            of
            {{ report.disease.join(", ") }}.
          </span>
          <span v-else>.</span>
          <br />
          <div v-if="report.syndrome.length != 0">
            Causes {{ report.syndrome.join(", ") }} <br />
          </div>
          {{ location_digest }}
        </div>
      </div>
    </v-card-title>
  </v-card>
</template>

<script>
import BookmarkBtn from "@/components/bookmark/Btn.vue";
import { mapState } from "vuex";
export default {
  props: {
    report: Object
  },
  computed: {
    ...mapState("bookmark", ["bookmark_ids"]),
    report_id() {
      if (typeof this.report.id == "number") {
        return this.report.id;
      }
      return parseInt(this.report.id.substr(1));
    },
    event_digest() {
      let event_dict = {};
      for (const re in this.report.report_events) {
        if (this.report.report_events.hasOwnProperty(re)) {
          const element = this.report.report_events[re];
          if (!event_dict.hasOwnProperty(element.event_type)) {
            event_dict[element.event_type] = 0;
          }
          event_dict[element.event_type] += element.number_affected;
        }
      }
      return Object.keys(event_dict)
        .map(k => {
          if (event_dict[k] == 0) {
            return `${k}`;
          } else {
            return `${event_dict[k]} ${k}`;
          }
        })
        .join(", ");
    },
    location_digest() {
      let location_list = this.report.report_events
        .map(el => el.location)
        .filter(el => el)
        .map(function(el) {
          if (el.city || el.state) {
            return `${el.city} ${el.state}, ${el.country}`;
          } else {
            return el.country;
          }
        });
      if (location_list.length == 0) {
        return "";
      }
      if (location_list.length < 3) {
        return "In " + location_list.join("; ") + ".";
      } else {
        return (
          "In " +
          location_list.splice(0, 3).join("; ") +
          ` and other ${location_list.length} palces.`
        );
      }
    }
  },
  components: {
    BookmarkBtn
  }
};
</script>
