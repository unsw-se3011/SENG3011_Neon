<template>
    <vue-google-autocomplete
        ref="address"
        id="map"
        classname="form-control"
        placeholder="Search by area"
        v-on:placechanged="getAddressData"
        size:300px
    >
    </vue-google-autocomplete>
</template>

<script>
import VueGoogleAutocomplete from 'vue-google-autocomplete'

export default {
  components: { VueGoogleAutocomplete },

  data: function () {
    return {
      address: ''
    }
  },
  /**
  mounted () {
    // To demonstrate functionality of exposed component functions
    // Here we make focus on the user input
    this.$refs.address.focus()
  },
*/
  methods: {
    /**
            * When the location found
            * @param {Object} addressData Data of the found location
            * @param {Object} placeResultData PlaceResult object
            * @param {String} id Input container ID
            */
    getAddressData: function (addressData, placeResultData, id) {
      this.address = addressData
      console.log(addressData)
      console.log(addressData.country)
      console.log(addressData.administrative_area_level_1)
      console.log(addressData.locality)
    }
  }
}
</script>
