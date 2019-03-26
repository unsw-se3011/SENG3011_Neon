<template>
  <div>
    <v-toolbar
      dense
      floating
    >
        <v-text-field
        hide-details
        color="black"
        prepend-icon="search"
        label="Search disease"
        single-line
        v-model="search"
        @keyup.enter="submit"
         >
      <!--  <input icon="search" type="text" v-model="search" placeholder="Search disease" @keyup.enter="submit" /> -->
        </v-text-field>
    </v-toolbar>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'search',
  data () {
    return {
      search: ''
    }
  },
  methods: {
    submit: function () {
      console.log(`${this.search}`)
      if (this.search !== '') {
        axios.get('http://localhost:8080/v0/articles/', {
          'search': this.search
        })
          .then(response => {
            console.log(response.data)
          })
          .catch(error => {
            console.log(error)
          })
      }
    }
  }
}
</script>
