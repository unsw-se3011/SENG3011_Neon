<template>
  <v-app>
    <v-navigation-drawer
      v-model="drawer"
      :clipped="$vuetify.breakpoint.lgAndUp"
      fixed
      app
    >
      <v-list dense>
        <template v-for="item in items">
          <v-layout v-if="item.heading" :key="item.heading" row align-center>
            <v-flex xs6>
              <v-subheader v-if="item.heading">{{ item.heading }}</v-subheader>
            </v-flex>
            <v-flex xs6 class="text-xs-center">
              <a href="#!" class="body-2 black--text">EDIT</a>
            </v-flex>
          </v-layout>
          <v-list-group
            v-else-if="item.children"
            :key="item.text"
            v-model="item.model"
            :prepend-icon="item.model ? item.icon : item['icon-alt']"
            append-icon
          >
            <template v-slot:activator>
              <v-list-tile>
                <v-list-tile-content>
                  <v-list-tile-title>{{ item.text }}</v-list-tile-title>
                </v-list-tile-content>
              </v-list-tile>
            </template>
            <v-list-tile v-for="(child, i) in item.children" :key="i" @click>
              <v-list-tile-action v-if="child.icon">
                <v-icon>{{ child.icon }}</v-icon>
              </v-list-tile-action>
              <v-list-tile-content>
                <v-list-tile-title>{{ child.text }}</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
          </v-list-group>
          <v-list-tile v-else :key="item.text" @click>
            <v-list-tile-action>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>{{ item.text }}</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </template>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar color="blue" dark fixed app clipped-left>
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title>Project Neon</v-toolbar-title>
      <v-text-field
        flat
        solo-inverted
        hide-details
        prepend-inner-icon="search"
        v-model="key_term"
        label="Search"
        class="pl-5 hidden-xs-and-down"
        @keydown="try_search"
      ></v-text-field>
      <v-btn icon flat @click.stop="toggle_filter()" class="hidden-xs-and-down">
        <v-icon>filter_list</v-icon>
      </v-btn>
      <v-spacer></v-spacer>
      <v-toolbar-items>
        <v-btn flat>Login</v-btn>
      </v-toolbar-items>
    </v-toolbar>
    <v-content>
      <router-view />
      <filterDialog />
    </v-content>
  </v-app>
</template>

<script>
import filterDialog from "@/components/filterDialog.vue";
import { mapActions, mapMutations } from "vuex";

export default {
  data: () => ({
    show_filter: false,
    drawer: true,
    items: [
      { icon: "contacts", text: "Reports" },
      { icon: "history", text: "Outbreaks" },
      { icon: "content_copy", text: "Map" },

      {
        icon: "keyboard_arrow_up",
        "icon-alt": "keyboard_arrow_down",
        text: "User",
        model: false,
        children: [{ text: "Profile" }, { icon: "settings", text: "Settings" }]
      },
      { icon: "chat_bubble", text: "Send feedback" },
      { icon: "help", text: "Help" },
      { icon: "phonelink", text: "App downloads" }
    ]
  }),
  props: {
    source: String
  },
  computed: {
    // double bind to vuex state
    key_term: {
      get() {
        return this.$store.state.search.key_term;
      },
      set(val) {
        this.$store.commit("search/set_key_term", val);
      }
    }
  },
  methods: {
    ...mapMutations("search", ["toggle_filter"]),
    ...mapActions("search", ["refresh_data"]),
    try_search(event) {
      if (event.key == "Enter") {
        // if it's not in the index, go to index to show the result
        if (this.$route.path != "/") {
          this.$router.push("/");
        } else {
          this.refresh_data();
        }
      }
    }
  },
  components: {
    filterDialog
  }
};
</script>

<style>
h1,
h2,
h3,
h4,
h5 {
  font-weight: 300 !important;
}
</style>
