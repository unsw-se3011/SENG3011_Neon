<!-- footer section -->
<template>
  <v-footer
    dark color="black"
    height="auto"
  >
    <v-card
      flat
      tile
      class="text-xs-center"
    >
      <v-card-text>
        <v-btn
          v-for="icon in icons"
          :key="icon"
          class="mx-3"
          style="color:white"
          icon
        >
          <v-icon size="24px">{{ icon }}</v-icon>
        </v-btn>
      </v-card-text>

      <v-card-text style="color:white;font-family: 'ZCOOL QingKe HuangYou', cursive;">
        Welcome to Neon project EpiWatch website, we provide updated reports for diseases all over the world. We provide the reliable reports,alerts,analysed articles from the official news website and gorvornment website. All information come from Outbreak News Today...
      </v-card-text>

      <v-divider></v-divider>

      <v-card-text style="color:white;font-family: 'ZCOOL QingKe HuangYou', cursive;">
        &copy;2019 — <strong>Neon</strong>
      </v-card-text>
    </v-card>
  </v-footer>
</template>

<script>
export default {
  data: () => ({
    icons: [
      'fab fa-facebook',
      'fab fa-twitter',
      'fab fa-google-plus',
      'fab fa-linkedin',
      'fab fa-instagram'
    ]
  })
}
</script>
