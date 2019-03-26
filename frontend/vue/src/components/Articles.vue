<template>
<v-container grid-list-xl>
  <v-layout wrap>
  <!--  <v-flex v-for="i in 3" :key="`4${i}`" xs4 mr-4 mb-4 ml-4 mt-4> -->
    <v-flex xs4
        v-for="(item, index) in wholeResponse"
        :key="index"
        mb-2>
      <v-card>
        <v-img
          v-bind:src="item"
          aspect-ratio="2.75"
        ></v-img>

     <!--   <v-card-title primary-title>
          <div>
            <v-btn icon href="" style="color:orange;">
             {{ item.title }}
            </v-btn>
            <div> Publish Date : {{ item.publishedAt }} </div>
            <div> Disease : {{ disease }} </div>
            <div> {{ mainText }} </div>
          </div>
        </v-card-title> -->
        <!--    <v-subheader
              v-if="item.title"
              :key="item.title"
              style="color:orange"
            >
             {{item.title}}
            </v-subheader>-->
             <a v-bind:href="item.url" style="color:orange;font-size:20px;font-weight:bold;text-decoration: none;">
              {{ item.headline}}
             </a>
             <div>
             </div>
             <div> Publish Date : {{ item.publish.substring(0,10) + " " + item.publish.substring(11,19) }} </div>
            <div> Disease : {{ item.reports }} </div>
            <div> {{ item.main_text }} </div>
        <v-card-actions>
            <div class="text-xs-center">
            <v-dialog
              v-model="dialog"
              width="500"
            >
              <v-btn
                slot="activator"
                color="orange"
                dark
                flat
              >
                Explore
              </v-btn>

              <v-card>
                <v-card-title
                  class="headline"
                  style="color:orange;font-weight:bold;"
                >
                 <a v-bind:href="item.url" style="color:orange;font-size:20px;font-weight:bold">
                    {{ item.headline }}
                   </a>
                </v-card-title>
                <v-divider></v-divider>
                <v-card-text>
                  <div style="color:orange">
                    <div> Disease : {{ item.reports }} </div>
                    <div> Syndrome : {{ item.reports }} </div>
                    <div> Type : {{ type }} </div>
                    <div> Date : {{ dDate }} </div>
                    <div> Location : {{ location }} </div>
                    <div> Number effect : {{ effect }} </div>
                  </div>
                  {{ detailText }}
                </v-card-text>
                <div>
                  <v-toolbar
                    dense
                    flat
                    color="white"
                  >
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
                </div>
                <template v-for="(index) in item.comment">
                   <v-list
                      two-line
                     :key="index.name"
                   >
                  <v-list-tile-content>
                      <v-list-tile-title v-html="index.name + ' : ' + index.comment" style="color:orange"></v-list-tile-title>
                    </v-list-tile-content>
                  </v-list>

                </template>
                <v-divider></v-divider>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                    color="orange"
                    flat
                    @click="dialog = false"
                  >
                    Close
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </div>
        </v-card-actions>
      </v-card>

    </v-flex>
  </v-layout>
</v-container>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      wholeResponse: [],
      comment: '',
      img: '',
      list: [
        { name: 'Today',
          comment: 'good article'
        }
      ],
      dialog: false,
      headline: 'First aid',
      publish: new Date().toISOString().substr(0, 10),
      disease: 'H5N1',
      syndrome: 'something',
      dDate: new Date().toISOString().substr(0, 10),
      type: 'Death',
      mainText: 'Lorem ipsum dolor sit amet, brute iriure accusata ne mea. Eos suavitate referrentur ad, te duo agam libris qualisque, utroque quaestio accommodare no qui. Et percipit laboramus usu, no invidunt verterem nominati mel. Dolorem ancillae an mei, ut putant invenire splendide mel, ea nec propriae adipisci. Ignota salutandi accusamus in sed, et per malis fuisset, qui id ludus appareat.',
      details: '',
      location: 'somewhere',
      effect: '12',
      detailText: 'Lorem ipsum dolor sit amet, brute iriure accusata ne mea. Eos suavitate referrentur ad, te duo agam libris qualisque, utroque quaestio accommodare no qui. Et percipit laboramus usu, no invidunt verterem nominati mel. Dolorem ancillae an mei, ut putant invenire splendide mel, ea nec propriae adipisci. Ignota salutandi accusamus in sed, et per malis fuisset, qui id ludus appareat.'
    }
  },
  methods: {
    submit: function () {
      console.log(`${this.comment}`)
      this.comment = ''
    }
  },
  mounted () {
    axios
      .get('http://localhost:8080/v0/articles/')
      .then(response => {
        console.log(response.data)
        if (response.data.count !== 0) {
          this.wholeResponse = response.data.results
          console.log(`${this.wholeResponse[0].headline}`)
        }
      })
      .catch(error => {
        console.log(error)
      })
  }
}
</script>
