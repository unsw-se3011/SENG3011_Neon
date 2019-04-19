<template>
  <v-dialog v-model="filter_show" width="800px">
    <v-card>
      <v-card-title class="grey lighten-4 py-4 title">Filters</v-card-title>
      <v-container grid-list-sm class="pa-4">
        <v-layout row wrap>
          <v-flex xs6>
            <v-menu
              ref="startdate_menu"
              :close-on-content-click="false"
              v-model="startdate_menu"
              :nudge-right="40"
              lazy
              transition="scale-transition"
              offset-y
              full-width
              min-width="290px"
            >
              <v-text-field
                slot="activator"
                v-model="start_date"
                label="Start Date"
                prepend-icon="event"
                readonly
              ></v-text-field>
              <v-date-picker v-model="start_date" landscape />
            </v-menu>
          </v-flex>
          <v-flex xs6>
            <v-menu
              ref="enddate_menu"
              :close-on-content-click="false"
              v-model="enddate_menu"
              :nudge-right="40"
              lazy
              transition="scale-transition"
              offset-y
              full-width
              min-width="290px"
            >
              <v-text-field
                slot="activator"
                v-model="end_date"
                label="End Date"
                prepend-icon="event"
                readonly
              ></v-text-field>
              <v-date-picker v-model="end_date" landscape />
            </v-menu>
          </v-flex>
          <v-flex sm12>
            <v-text-field
              slot="activator"
              v-model="location"
              label="Location"
              prepend-icon="place"
            ></v-text-field>
          </v-flex>
        </v-layout>
      </v-container>
      <v-card-actions>
        <v-btn flat color="primary">More</v-btn>
        <v-spacer></v-spacer>
        <v-btn flat color="primary" @click="cancel">Cancel</v-btn>
        <v-btn flat @click="confirm">Save</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import { mapMutations, mapActions } from "vuex";

export default {
  // we use vuex to pass the filter's information0
  data() {
    return {
      startdate_menu: false,
      enddate_menu: false,
      start_date: this.$store.state.search.start_date,
      end_date: this.$store.state.search.end_date,
      location: this.$store.state.search.location
    };
  },
  computed: {
    // double bind to vuex state
    filter_show: {
      get() {
        return this.$store.state.search.filter_show;
      },
      set() {
        this.$store.commit("search/toggle_filter");
      }
    }
  },
  methods: {
    ...mapMutations("search", [
      "toggle_filter",
      "set_start_date",
      "set_end_date",
      "set_location"
    ]),
    ...mapActions("search", ["refresh_data"]),
    cancel() {
      // reset the value to default one
      (this.start_date = this.$store.state.search.start_date),
        (this.end_date = this.$store.state.search.end_date),
        (this.location = this.$store.state.search.location);
      // toggle and not to show
      this.toggle_filter();
    },
    confirm() {
      // pass the arguments to vuex
      this.set_start_date(this.start_date);
      this.set_end_date(this.end_date);
      this.set_location(this.location);

      // romove the dialog
      this.toggle_filter();
      if (this.$route.path != "/") {
        this.$router.push("/");
      } else {
        // refresh those data
        // it must changed 
        this.refresh_data(true);
      }
    }
  }
};
</script>
