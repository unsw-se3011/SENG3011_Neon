<template>
  <v-container fluid pa-0>
    <div
      class="white--text"
      style="background:linear-gradient(to bottom, #2196f3 , #5cbbf6)"
    >
      <v-layout align-center justify-center wrap py-5>
        <v-flex xs10>
          <h1 class="display-2 font-weight-light mb-4 text-xs-center">
            Let the Project Neon help you detect epidemic.
          </h1>
        </v-flex>
        <v-flex xs12>
          <v-layout row justify-center>
            <v-btn
              class="primary--text mr-0"
              color="white"
              large
              :to="{ name: 'reportList' }"
              >Get Started</v-btn
            >

            <v-btn
              class="primary--text ml-4"
              color="white"
              large
              :to="{ name: 'outbreakIndex' }"
              >Outbreak</v-btn
            >
          </v-layout>
        </v-flex>
        <v-flex xs3 pa-2 mt-5 mb-5>
          <v-card>
            <v-img
              :src="require('../../assets/data.png')"
              aspect-ratio="2.75"
            ></v-img>

            <v-card-title primary-title>
              <div>
                <h3 class="headline mb-0">Richful Dataset in Speed</h3>
                <div>
                  We watch CDC, WHO and Outbreak News Today to empower our
                  backend. We not only provided the richest dataset but also
                  maintain excellent response time.
                </div>
              </div>
            </v-card-title>
          </v-card>
        </v-flex>
        <v-flex xs3 pa-2 mt-5 mb-5>
          <v-card>
            <v-img
              :src="require('../../assets/analyze.png')"
              aspect-ratio="2.75"
            ></v-img>
            <v-card-title primary-title>
              <div>
                <h3 class="headline mb-0">Powerful Data Analytics</h3>
                <div>
                  We provided three real-time data analytic tools which let you
                  have a better insight toward the epidemic. Moreover, you can
                  feel this power within your mobile devices.
                </div>
              </div>
            </v-card-title>
          </v-card>
        </v-flex>
      </v-layout>
    </div>
  </v-container>
</template>
