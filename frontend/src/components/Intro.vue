<!-- Intro components put headline image -->

<template>
  <v-carousel height="400">
    <v-carousel-item
      v-for="(item,i) in items"
      :key="i"
      :src="item.src"
    ></v-carousel-item>
  </v-carousel>
</template>

<script>
// images are need to change everyday if is possible
export default {
  data () {
    return {
      items: [
        {
          src: 'https://steamcdn-a.akamaihd.net/steam/apps/514990/header.jpg?t=1523490090'
        }
      //  {
        //  src: 'https://cdn.vuetifyjs.com/images/carousel/sky.jpg'
        // },
      //  {
        //   src: 'https://cdn.vuetifyjs.com/images/carousel/bird.jpg'
        // },
        // {
        // src: 'https://cdn.vuetifyjs.com/images/carousel/planet.jpg'
        // }
      ]
    }
  }
}
</script>
