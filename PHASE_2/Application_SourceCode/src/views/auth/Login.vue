<template>
  <v-layout row ma-3>
    <v-flex md10 offset-md1 xs12 offset-xs0 lg6 offset-lg3>
      <h1>Login</h1>
      <v-form v-model="valid" @submit.prevent="login">
        <v-text-field
          v-model="username"
          label="Username"
          required
          autofocus
          autocomplete
        />
        <v-text-field
          v-model="password"
          :type="show ? 'text' : 'password'"
          label="Password"
          :append-icon="show ? 'visibility' : 'visibility_off'"
          autocomplete
          @click:append="show = !show"
          required
        />
        <p>
          New to Project Neon?
          <router-link :to="{ name: 'register' }"
            >Create an account.</router-link
          >
        </p>
        <p>{{ error }}</p>
        <v-btn type="submit">Login</v-btn>
      </v-form>
    </v-flex>
  </v-layout>
</template>

<script>
import { mapActions } from "vuex";

export default {
  data() {
    return {
      // prevent error because vuetify require this
      valid: false,
      // input of username and password
      username: "",
      password: "",
      // if show == true, show the password
      show: false,
      error: ""
    };
  },
  methods: {
    // map the login action from vuex
    ...mapActions("auth", ["loginByCredential"]),
    login() {
      // pass the user login credential
      this.loginByCredential({
        username: this.username,
        password: this.password
      })
        .then(() => {
          // console.log("imhere")
          if (this.$route.query.redirect) {
            // redirect request from another view
            this.$router.push(this.$route.query.redirect);
          } else {
            // go to previous page, if it's user direct to login
            this.$router.push("/");
          }
        })
        .catch(() => {
          this.error = "Wrong username or password.";
        });
    }
  }
};
</script>
