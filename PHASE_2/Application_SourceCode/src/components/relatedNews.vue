<template>
  <div v-if="!waiting">
    <v-layout row wrap>
      <v-flex
        v-for="new_obj in news.articles"
        :key="new_obj.id"
        md6
        xl4
        xm12
        pa-2
      >
        <v-card :href="new_obj.url">
          <v-img :src="new_obj.urlToImage" v-if="new_obj.urlToImage" height="150px">
          </v-img>
          <v-card-title primary-title>
            <div>
              <h3 class="headline mb-0">{{ new_obj.title }}</h3>
              <h5>
                {{ new_obj.author }} | {{ new_obj.source.name }} on
                {{ new_obj.publishedAt | showDate }}
              </h5>
              <div>
                {{ new_obj.content }}
              </div>
            </div>
          </v-card-title>
        </v-card>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  props: {
    start_date: String,
    end_date: String,
    key_word: String
  },
  data() {
    return {
      waiting: true,
      news: []
    };
  },
  methods: {
    ...mapActions("report", ["get_relate_news"])
  },
  async mounted() {
    let ret = await this.get_relate_news({
      from: this.start_date,
      to: this.end_date,
      q: this.key_word
    });
    this.news = ret.data;
    this.waiting = false;
  }
};
</script>
