<template>
  <v-layout>
    <v-flex v-for="i in 3" :key="`4${i}`" xs4 mr-4 mb-4 ml-4 mt-4>
      <v-card>
        <v-img
          src="https://cdn.vuetifyjs.com/images/cards/desert.jpg"
          aspect-ratio="2.75"
        ></v-img>

        <v-card-title primary-title>
          <div>
            <v-btn icon href="http://www.google.com" style="color:orange;" large>
             {{headline}}
            </v-btn>
            <div> Publish Date : {{ publish }} </div>
            <div> Disease : {{ disease }} </div>
            <div> {{ mainText }} </div>
          </div>
        </v-card-title>

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
                 <v-btn icon href="http://www.google.com" style="color:orange;" large>
                  {{headline}}
                 </v-btn>
                </v-card-title>
                <v-divider></v-divider>
                <v-card-text>
                  <div style="color:orange">
                    <div> Disease : {{ disease }} </div>
                    <div> Syndrome : {{ syndrome }} </div>
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
                <template v-for="(item) in list">
                   <v-list 
                      two-line
                     :key="item.name"
                   >
                  <v-list-tile-content>
                      <v-list-tile-title v-html="item.name + ' : ' + item.comment" style="color:orange"></v-list-tile-title>
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
</template>

<script>
  export default {
    data () {
      return {
        comment:'',
        list:[
           { name: 'Today',
             comment: 'good article',
           },
        ],
        dialog:false,
        headline: 'First aid',
        publish: new Date().toISOString().substr(0, 10),
        disease: 'H5N1',
        syndrome: 'something',
        dDate:  new Date().toISOString().substr(0, 10),
        type:'Death',
        mainText: 'Lorem ipsum dolor sit amet, brute iriure accusata ne mea. Eos suavitate referrentur ad, te duo agam libris qualisque, utroque quaestio accommodare no qui. Et percipit laboramus usu, no invidunt verterem nominati mel. Dolorem ancillae an mei, ut putant invenire splendide mel, ea nec propriae adipisci. Ignota salutandi accusamus in sed, et per malis fuisset, qui id ludus appareat.',
        details:'',
        location:'somewhere',
        effect: '12',
        detailText: 'Lorem ipsum dolor sit amet, brute iriure accusata ne mea. Eos suavitate referrentur ad, te duo agam libris qualisque, utroque quaestio accommodare no qui. Et percipit laboramus usu, no invidunt verterem nominati mel. Dolorem ancillae an mei, ut putant invenire splendide mel, ea nec propriae adipisci. Ignota salutandi accusamus in sed, et per malis fuisset, qui id ludus appareat.'
      }
    },
     methods:{
        submit: function (){
            console.log(`${this.comment}`);
            this.comment='';
        }
    }
  }
</script>