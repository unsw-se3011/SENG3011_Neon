<template>
  <div class="map">
<GmapMap
  :center="{lat:-34.397, lng:150.644 }"
  :zoom="7"
  map-type-id="terrain"
  style="width: 100%; height: 580px;"

>
</GmapMap>
  </div>
</template>
<script>
import { gmapApi } from 'vue2-google-maps'

export default {
  computed: {
    google: gmapApi
  }
}
</script>
