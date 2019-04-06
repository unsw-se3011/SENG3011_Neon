<!-- search bar handles users input for search, time period of result is required -->
<template>
  <div>
  <!-- calendar section both start date and end date -->
  <v-container grid-list-sm>
    <v-layout row wrap>
      <v-flex xs12 lg3>
        <v-menu
          ref="menu1"
          v-model="menu1"
          :close-on-content-click="false"
          :nudge-right="10"
          lazy
          transition="scale-transition"
          offset-y
          full-width
          max-width="290px"
          min-width="290px"
        >
          <template v-slot:activator="{ on }">
            <v-text-field
              v-model="dateFormatted"
              label="Start Date"
              hint="DD/MM/YYYY format"
              persistent-hint
              prepend-icon="event"
              @blur="date = parseDate(dateFormatted)"
              v-on="on"
            ></v-text-field>
          </template>
          <v-date-picker v-model="date" no-title @input="menu1 = false"></v-date-picker>
        </v-menu>
      </v-flex>

       <v-flex xs12 lg3>
        <v-menu
          ref="menu2"
          v-model="menu2"
          :close-on-content-click="false"
          :nudge-right="10"
          lazy
          transition="scale-transition"
          offset-y
          full-width
          max-width="290px"
          min-width="290px"
        >
          <template v-slot:activator="{ on }">
            <v-text-field
              v-model="dateFormatted2"
              label="End Date"
              hint="DD/MM/YYYY format"
              persistent-hint
              prepend-icon="event"
              @blur="date2 = parseDate(dateFormatted2)"
              v-on="on"
              width="20px"
            ></v-text-field>
          </template>
          <v-date-picker v-model="date2" no-title @input="menu2 = false"></v-date-picker>
        </v-menu>
      </v-flex>

        <!-- Search keyword section -->
        <v-text-field
        hide-details
        color="black"
        prepend-icon="search"
        label="Search disease"
        single-line
        v-model="search"
        @keyup.enter="submit"
         >
        </v-text-field>

        <vue-google-autocomplete
        ref="address"
        id="map"
        classname="form-control"
        single-line
        placeholder="Search by area"
        types="(cities)"
        v-on:placechanged="getAddressData"
        >
        </vue-google-autocomplete>

        <div class="text-uppercase md-and-up">
           <router-link v-if="search && city && date !== date2" :to="{ name: 'result', params: { start:this.date,end:this.date2,keyword:this.search,location:this.city}}">
       <!-- <router-link to='/map' style="text-decoration: none;">-->
          <v-btn flat>
              GO!
          </v-btn>
        </router-link>
        <router-link v-if="search && date !== date2" :to="{ name: 'result', params: { start:this.date,end:this.date2,keyword:this.search,location:'/'}}">
       <!-- <router-link to='/map' style="text-decoration: none;">-->
          <v-btn flat>
              GO!
          </v-btn>
        </router-link>
         <router-link v-else-if="city && date !== date2" :to="{ name: 'result', params: { start:this.date,end:this.date2,keyword:'/',location:this.city}}">
       <!-- <router-link to='/map' style="text-decoration: none;">-->
          <v-btn flat>
              GO!
          </v-btn>
        </router-link>
        <router-link v-else-if="date !== date2" :to="{ name: 'result', params: { start:this.date,end:this.date2,keyword:'/',location:'/'}}">
       <!-- <router-link to='/map' style="text-decoration: none;">-->
          <v-btn flat>
              GO!
          </v-btn>
        </router-link>
      </div>
    </v-layout>
  </v-container>
  </div>
</template>

<!-- js section format the date from selected calendar
      and get the search keyword request for the API
      redirect to the pure article page
-->
<script>
import VueGoogleAutocomplete from 'vue-google-autocomplete'
import axios from 'axios'
export default {
  components: { VueGoogleAutocomplete },
  data: vm => ({
    address: null,
    date: new Date().toISOString().substr(0, 10),
    dateFormatted: vm.formatDate(new Date().toISOString().substr(0, 10)),
    menu1: false,
    search: null,
    menu2: false,
    date2: new Date().toISOString().substr(0, 10),
    dateFormatted2: vm.formatDate(new Date().toISOString().substr(0, 10)),
    city: null,
    state: null,
    country: null
  }),

  watch: {
    date (val) {
      this.dateFormatted = this.formatDate(this.date)
    },
    date2 (val) {
      this.dateFormatted2 = this.formatDate(this.date2)
    }
  },

  methods: {
    getAddressData: function (addressData, placeResultData, id) {
      this.address = addressData
      this.city = addressData.locality
      this.state = addressData.administrative_area_level_1
      this.country = addressData.country
      console.log(addressData)
      console.log(addressData.country)
      console.log(addressData.administrative_area_level_1)
      console.log(addressData.locality)
    },

    formatDate (date) {
      if (!date) return null

      const [year, month, day] = date.split('-')
      return `${day}/${month}/${year}`
    },
    parseDate (date) {
      if (!date) return null

      const [day, month, year] = date.split('/')
      return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
    },

    submit: function () {
      console.log(`${this.search}`)
      console.log(`${this.date}`)
      console.log(`${this.date2}`)
      if (this.date === this.date2) {
        //   this.warning = true
      } // else if (this.address === '' && this.search === '') {
      //  this.city = '?'
      // this.state = '?'
      // this.country = '?'
      // this.search = '?'
      // } else if (this.address === '') {
      //  this.city = '?'
      //  this.state = '?'
      // this.country = '?'
      // } else if (this.search === '') {
      // this.search = '?'
      // } else {

      // }
      // if (this.search !== '') {
      // axios.get(url, {
      // 'search': this.search
      // })
      // .then(response => {
      //  console.log(response.data)
      // })
      // .catch(error => {
      // console.log(error)
      // })
      // }
    }
  }
}
</script>
