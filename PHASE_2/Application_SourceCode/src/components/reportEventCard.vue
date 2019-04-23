<template>
  <v-card class="my-3">
    <v-card-title primary-title>
      <div class="pa-1">
        <h3 class="headline mb-0">
          {{ event.numer_affected }} {{ event.event_type }}
        </h3>
        <div>
          From {{ event.start_date | showDate }} to
          {{ event.end_date | showDate }} <br />
          {{ event.location | showLocation }}
        </div>
      </div>
    </v-card-title>
  </v-card>
</template>

<script>
export default {
  props: {
    event: Object
  }
};
</script>
