<!-- Initial article section with latest report -->
<template>
  <v-container grid-list-xl>
    <v-layout wrap>
      <v-flex xs4 v-for="(item, index) in wholeResponse.slice(offset,offset+12)" :key="index" mb-2>
        <v-card>
          <v-img v-if="item.article.img !== '' " v-bind:url="item.article.img" aspect-ratio="2.75"></v-img>
          <v-img v-else :src="image" aspect-ratio="2.75"></v-img>
          <!--  <img  :src="images.sample"> -->

          <a
            v-bind:href="item.article.url"
            style="color:orange;font-size:20px;font-weight:bold;text-decoration: none;"
          >{{ item.article.headline}}</a>
          <div></div>
          <!--<div> Publish Date : {{ item.article.date_of_publication.substring(0,10) + " " + item.article.date_of_publication.substring(11,19) }} </div>-->
          Publish Date : {{ item.article.date_of_publication | dateStr}}
          <div>Disease : {{ item.disease }}</div>
          <div>{{ item.article.main_text | liveSubstr }}</div>
          <v-card-actions>
            <div class="text-xs-center">
              <v-dialog v-model="dialog" width="500">
                <v-btn slot="activator" color="orange" flat @click="attract(item)">Explore</v-btn>

                <v-card>
                  <v-card-title class="headline" style="color:orange;font-weight:bold;">
                    <a
                      v-bind:href="headlineUrl"
                      style="color:orange;font-size:20px;font-weight:bold"
                    >{{ headline }}</a>
                  </v-card-title>
                  <v-divider></v-divider>
                  <v-card-text>
                    <div style="color:orange">
                      <div>Disease : {{ disease }}</div>
                      <div>Syndrome : {{ syndrome }}</div>
                      <div>Type : {{ type }}</div>
                      <div>Start Date : {{ start_date }}</div>
                      <!--    <div v-if="item.report_events[0].location.city && item.report_events[0].location.country"> Location : {{ item.report_events[0].location + "," + item.report_events[0].location}} </div> -->
                      <div>Location : {{ location }}</div>
                      <div>Number effect : {{ effect }}</div>
                    </div>
                    {{ details }}
                  </v-card-text>
                  <div>
                    <v-toolbar dense flat color="white">
                      <v-text-field
                        hide-details
                        color="orange"
                        prepend-icon="comment"
                        label="Comment for this article"
                        single-line
                        v-model="comment"
                        @keyup.enter="submit"
                      >
                        <!--  <input icon="search" type="text" v-model="search" placeholder="Search disease" @keyup.enter="submit" /> -->
                      </v-text-field>
                    </v-toolbar>
                    <v-alert :value="false" type="error" v-model="warn">Pleaser login first</v-alert>
                  </div>
                  <template v-for="(index) in comments">
                    <v-list two-line :key="index.name">
                      <v-list-tile-content>
                        <v-list-tile-title
                          v-html="index.name + ' : ' + index.comment"
                          style="color:orange"
                        ></v-list-tile-title>
                      </v-list-tile-content>
                    </v-list>
                  </template>
                  <v-divider></v-divider>

                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="orange" flat @click="dialog = false">Close</v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </div>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
    <v-btn v-if="offset > 0" color="orange" flat @click="offset=offset-12;">Prev</v-btn>
    <v-btn
      v-if="result === false && (offset+12) < count"
      color="orange"
      flat
      @click="offset=offset+12"
    >Next</v-btn>
    <router-link
      v-if="result"
      to="/"
      style="text-decoration: none; font-size:30px"
    >Oops! No result, back to search >></router-link>
  </v-container>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      warn: false,
      url: '/reports/?start_date=',
      wholeResponse: [],
      comments: [],
      comment: '',
      img: '',
      list: [{ name: 'Today', comment: 'good article' }],
      headline: '',
      headlineUrl: '',
      disease: '',
      syndrome: '',
      start_date: '',
      location: '',
      dialog: false,
      offset: 0,
      publish: new Date().toISOString().substr(0, 10),
      result: false,
      dDate: new Date().toISOString().substr(0, 10),
      type: '',
      details: '',
      count: 200,
      effect: '',
      token: '',
      image: require('@/assets/outbreak.png')
    }
  },
  filters: {
    liveSubstr: function (string) {
      return string.substring(0, 30) + '...'
    },
    dateStr: function (string) {
      return string.substring(0, 10) + ' ' + string.substring(11, 19)
    }
  },
  mounted: function () {
    this.getData()
  },
  methods: {
    attract: function (Obj) {
      console.log(Obj)
      console.log(Obj.article.url)
      this.headlineUrl = Obj.article.url
      this.headline = Obj.article.headline
      this.disease = Obj.disease.toString()
      this.syndrome = Obj.syndrome.toString()
      this.type = Obj.report_events[0].event_type
      this.start_date =
        Obj.report_events[0].start_date.substring(0, 10) +
        ' ' +
        Obj.report_events[0].start_date.substring(11, 19)
      this.location =
        Obj.report_events[0].location.city +
        ', ' +
        Obj.report_events[0].location.state +
        ', ' +
        Obj.report_events[0].location.country
      this.details = Obj.article.main_text
      this.effect = Obj.report_events[0].number_affected
      this.comments = Obj.comment
    },
    submit: function () {
      console.log(`${this.comment}`)
      this.token = localStorage.getItem('token')
      console.log(`${this.token}`)
      if (this.token !== '' && this.token !== null) {
        axios
          .post('http://neon.whiteboard.house/v0/RefreshJSONWebToken/', {
            token: this.token
          })
          .then(
            response => {
              console.log(response)
            },
            error => {
              console.log(error)
            }
          )
      } else {
        this.warn = true
      }
      this.comment = ''
    },
    getData: function () {
      this.url =
        this.url +
        this.$route.params.start +
        'T00:00:00&end_date=' +
        this.$route.params.end +
        'T00:00:00'
      console.log(this.$route.params.start)
      console.log(this.$route.params.end)
      console.log(this.$route.params.keyword)
      console.log(this.$route.params.location)
      if (this.$route.params.location !== '/') {
        this.url = this.url + '&location=' + this.$route.params.location
      }
      if (this.$route.params.keyword !== '/') {
        this.url = this.url + '&key_term=' + this.$route.params.keyword
      }
      console.log(this.url)
      axios
        .get(this.url)
        .then(response => {
          console.log(response.data)
          this.count = response.data.count
          if (response.data.count !== 0) {
            this.wholeResponse = response.data.results
            console.log(`${this.wholeResponse[0].article.headline}`)
            console.log(
              `${this.wholeResponse[0].report_events[0].location.city}`
            )
          } else {
            this.result = true
          }
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>
