<template>
  <div>
    <v-toolbar
      dense
      floating
    >
        <v-text-field
        hide-details
        color="#9ACD32"
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
  export default {
    name:'search',
    data () {
      return {
        search: '',
      }
    },
    methods:{
        submit: function (){
            console.log(`${this.search}`)
        }
    }
  }
</script>
