<template>
  <div class="map">
    <GmapMap
  :center="{lat: -34.397, lng: 150.644}"
  :options="{
   zoomControl: true,
   mapTypeControl: false,
   scaleControl: false,
   streetViewControl: false,
   rotateControl: false,
   fullscreenControl: true,
   disableDefaultUi: false
  }"
  :zoom="7"
  map-type-id="terrain"
  style="width: 100%; height: 580px"
>
  <GmapMarker
    :key="index"
    v-for="(m, index) in markers"
    :position="m.position"
    :clickable="true"
    :draggable="true"
    @click="center=m.position"
  />
</GmapMap>
  </div>
</template>
