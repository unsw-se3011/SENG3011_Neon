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
            <v-list-tile v-for="(child, i) in item.children" :key="i">
              <v-list-tile-action v-if="child.icon">
                <v-icon>{{ child.icon }}</v-icon>
              </v-list-tile-action>
              <v-list-tile-content>
                <v-list-tile-title>{{ child.text }}</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
          </v-list-group>
          <v-list-tile
            v-else
            :key="item.text"
            :to="item.href ? { name: item.href } : null"
          >
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
    <v-toolbar color="blue" dark fixed app clipped-left :flat="is_flat">
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title>
        <span class="font-weight-light">Project</span>Neon
      </v-toolbar-title>
      <v-text-field
        solo-inverted
        hide-details
        prepend-inner-icon="search"
        clearable
        flat
        v-model="key_term"
        label="Search"
        class="pl-5 ml-5 hidden-sm-and-down neon-round"
        style=" border-radius: 20px;"
        @click:clear="clear_and_search"
        @keydown.enter="try_search"
      ></v-text-field>
      <v-btn icon flat @click.stop="toggle_filter()" class="hidden-sm-and-down">
        <v-icon>filter_list</v-icon>
      </v-btn>
      <v-spacer></v-spacer>
      <v-toolbar-items>
        <v-btn v-if="!username" flat :to="{ name: 'login' }">Login</v-btn>
        <v-menu offset-y v-else>
          <v-btn flat v-if="username" slot="activator">{{ username }}</v-btn>
          <v-list>
            <v-list-tile :to="{ name: 'logout' }">Logout</v-list-tile>
          </v-list>
        </v-menu>
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
import { mapActions, mapMutations, mapState } from "vuex";

export default {
  data: () => ({
    show_filter: false,
    drawer: false,
    items: [
      { icon: "contacts", text: "Reports", href: "reportList" },
      { icon: "history", text: "Outbreaks", href: "outbreakIndex" },
      // { icon: "map", text: "Map" },
      { icon: "content_copy", text: "Bookmark", href: "bookmarkList" }

      // {
      //   icon: "keyboard_arrow_up",
      //   "icon-alt": "keyboard_arrow_down",
      //   text: "User",
      //   model: false,
      //   children: [
      //     { icon: "person", text: "Profile" },
      //     { icon: "settings", text: "Settings" }
      //   ]
      // },
      // { icon: "chat_bubble", text: "Send feedback" },
      // { icon: "help", text: "Help" },
      // { icon: "phonelink", text: "App downloads" }
    ]
  }),
  props: {
    source: String
  },
  computed: {
    ...mapState("auth", ["username"]),
    // double bind to vuex state
    key_term: {
      get() {
        return this.$store.state.search.key_term;
      },
      set(val) {
        this.$store.commit("search/set_key_term", val);
      }
    },
    is_flat() {
      return this.$route.name == "index";
    }
  },
  methods: {
    ...mapMutations("search", ["toggle_filter"]),
    ...mapActions("search", ["refresh_data"]),
    ...mapMutations("auth", "clear_all"),
    async clear_and_search() {
      await this.$store.commit("search/reset");
      this.try_search();
    },
    try_search() {
      // if it's not in the index, go to index to show the result
      if (this.$route.path != "/reports") {
        this.$router.push("/reports");
      }
      // we press enter, it must search
      this.refresh_data(true);
    },
    logout() {
      this.clear_all();
      this.$router.push("/");
    }
  },
  components: {
    filterDialog
  },
  mounted() {
    // console.log(this.$route.name)
    // if (this.$route.name == "index") {
    //   this.drawer =false
    // }
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
.v-card,
.v-text-field.v-text-field--enclosed .v-text-field__details,
.v-text-field.v-text-field--enclosed > .v-input__control > .v-input__slot,
.v-text-field--outline > .v-input__control > .v-input__slot,
.v-btn--round {
  border-radius: 8px;
}
.v-btn {
  margin: 0;
}
</style>
