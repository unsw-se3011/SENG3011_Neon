<template>
  <v-container grid-list-xs>
    <v-layout row ma-3>
      <v-flex md10 offset-md1 xs12 offset-xs0 lg6 offset-lg3>
        <h1 v-if="!isEdit">Sign Up</h1>
        <h1 v-else>Edit Profile</h1>

        <form @submit.prevent="submit">
          <v-snackbar v-model="snackbar">
            {{ snackText }}
            <v-btn flat color="error" @click.native="snackbar = false"
              >Close</v-btn
            >
          </v-snackbar>
          <v-text-field
            v-model="username"
            outline
            label="Username"
            required
            autofocus
            autocomplete
          />
          <v-text-field
            v-model="password"
            outline
            :type="show ? 'text' : 'password'"
            label="Password"
            :append-icon="show ? 'visibility' : 'visibility_off'"
            autocomplete
            @click:append="show = !show"
            required
          />
          <v-layout row wrap>
            <v-flex xs12 md6>
              <v-text-field
                outline
                v-model="first_name"
                label="First Name"
                required
              />
            </v-flex>
            <v-flex xs12 md6>
              <v-text-field
                outline
                v-model="last_name"
                label="Last Name"
                required
              />
            </v-flex>
          </v-layout>
          <v-btn type="submit" outline color="blue" round v-if="!isEdit"
            >Register</v-btn
          >
          <v-btn type="submit" color="success" v-else>Save</v-btn>
        </form>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapActions } from "vuex";
// import postCard from "@/components/helper/addressInput";
export default {
  data() {
    return {
      // input of username and password
      username: "",
      password: "",
      first_name: "",
      last_name: "",
      show: false,
      snackbar: false,
      snackText: ""
    };
  },
  computed: {
    isEdit() {
      // if the name is profile Edit, then this is an edit page
      return this.$route.name == "ProfileEdit";
    }
  },
  methods: {
    // map the login action from vuex
    ...mapActions("auth", ["registerByUser", "editUser"]),
    submit() {
      let promise;
      if (this.isEdit) {
        // edit mode
        promise = this.editUser({
          id: this.id,
          username: this.username,
          password: this.password
        }).then(res => {
          // go to the detail page
          // redirect request from another view
          this.$router.push({
            name: "ProfileDetail",
            // pass with user's data
            params: { user: res.data }
          });
        });
      } else {
        // register mode
        promise = this.registerByUser({
          username: this.username,
          password: this.password,
          first_name: this.first_name,
          last_name: this.last_name
        }).then(() => {
          // go to main page
          // console.log(this);
          if (this.$route.query.redirect) {
            // redirect request from another view
            this.$router.push(this.$route.query.redirect);
          } else {
            // go to previous page, if it's user direct to login
            this.$router.go(-3);
          }
        });
      }
      promise.catch(err => {
        if (err.response.data.username) {
          this.snackText = err.response.data.username[0];
        }
        this.snackbar = true;
        this.error = err.response.data;
      });
    }
  },
  mounted() {
    if (this.isEdit) {
      this.$store.dispatch("getUserDetail").then(res => {
        // map these inpo to the input area
        this.username = res.data.username;
        this.location = res.data.location;
        this.tel = res.data.tel;
        this.id = res.data.id;
      });
    }
  },
  components: {}
};
</script>
