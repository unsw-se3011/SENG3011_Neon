<template>
  <v-container grid-list-xs>
    <h2 class="headline">Outbreak List</h2>
    <v-layout row wrap v-if="waiting == false">
      <v-flex v-for="out in outbreaks" :key="out.id" md6 xl4 pa-2>
        <v-card :to="{ name: 'outbreakDetail', params: { id: out.id } }">
          <v-img :src="out.img" v-if="out.img" height="200px"> </v-img>
          <v-card-title primary-title>
            <div>
              <h3 class="headline mb-0">
                From {{ out.start_date | showYearMonth }} to
                {{ out.end_date | showYearMonth }} <br />
                {{ out.key_term }} Outbreak
              </h3>
            </div>
          </v-card-title>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapState } from "vuex";
export default {
  computed: {
    ...mapState("outbreak", ["outbreaks", "waiting"])
  },
  mounted() {
    this.$store.dispatch("outbreak/refresh_data");
  }
};
</script>
