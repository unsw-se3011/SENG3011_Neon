<template>
  <div>
    <p v-for="msg in msg_list" :key="msg.id">
      <b>{{ msg.user }}</b>
      {{ msg.msg }}
    </p>
    <v-form @submit.prevent="submit">
      <v-layout row wrap>
        <v-flex xs12>
          <v-text-field
            v-model="message"
            label="Message"
            type="text"
            append-icon="send"
            @click:append="submit"
          />
        </v-flex>
      </v-layout>
    </v-form>
  </div>
</template>

<script>
export default {
  props: {
    msg_list: Array,
    report_id: Number
  },
  data() {
    return {
      message: ""
    };
  },
  methods: {
    async submit() {
      await window.axios.post("/message/", {
        report: this.report_id,
        msg: this.message
      });
      // clear the message and delcear change
      this.message = "";
      this.$emit("change");
    }
  },
  mounted() {}
};
</script>
