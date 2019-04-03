<!-- Login & registration entry
     registration is invisible initially
     login is visible
     after enter the button of register the gegistration sheet will appear
-->
<template>
  <div class="text-xs-center">
    <v-layout>
        <v-btn slot="activator" color="white" dark flat v-if="!visible">
          <span class="mr-1" style="color:white;font-size:20px" @click="logoutLocal">Logout</span>
        </v-btn>
        <!-- Login -->
        <v-dialog v-model="dialog" persistent max-width="600px">
        <v-btn slot="activator" color="white" dark flat v-if="visible">
          <span class="mr-1" style="font-size:20px">Login</span>
        </v-btn>
        <v-card>
            <v-card-title>
            <span class="headline" style="color:orange;">Login</span>
            </v-card-title>
            <v-card-text>
            <v-container grid-list-md>
                <v-layout wrap>
                <v-flex xs12 sm6 md4>
                    <v-text-field label="Username*" required v-model="Username"></v-text-field>
                </v-flex>
                <v-flex xs12>
                    <v-text-field label="Password*" type="password" required  v-model="Password"></v-text-field>
                </v-flex>
                </v-layout>
            </v-container>
            <small>*indicates required field</small>
            <v-alert
            :value="false"
            type="error"
            v-model="warn"
            >
            Pleaser enter username and password
            </v-alert>
             <v-alert
            :value="false"
            type="error"
            v-model="warn3"
            >
            Invalid username and password
            </v-alert>
            </v-card-text>
            <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="orange" flat @click="dialog = false">Close</v-btn>

            <!-- register -->
            <v-dialog v-model="Register" persistent max-width="600px" height="700px;">
                <template v-slot:activator="{ on }">
                    <v-btn color="orange" flat @click="dialog = false,Register = true">Register</v-btn>
                </template>
                 <v-card>
                    <v-card-title>
                      <span class="headline" style="color:orange;">Register form</span>
                    </v-card-title>
                    <v-card-text>
                       <v-container grid-list-md>
                          <v-layout wrap>
                            <v-flex xs12 sm6 md4>
                              <v-text-field label="First name*" required v-model="first_name"></v-text-field>
                            </v-flex>
                            <v-flex xs12 sm6 md4>
                              <v-text-field
                                label="Last name*"
                                hint="example of persistent helper text"
                                persistent-hint
                                required
                                v-model="last_name"
                              ></v-text-field>
                            </v-flex>
                            <v-flex xs12>
                              <v-text-field label="Email*" required v-model="Email"></v-text-field>
                            </v-flex>
                            <v-flex xs12>
                              <v-text-field label="Username*" required v-model="UsernameR"></v-text-field>
                            </v-flex>
                            <v-flex xs12>
                              <v-text-field label="Password*" type="password"  required v-model="PasswordR"></v-text-field>
                            </v-flex>

                            </v-layout>
                          </v-container>
                          <small>*indicates required field</small>
                      </v-card-text>
                      <v-alert
                          :value="false"
                          type="error"
                          v-model="warn1"
                          >
                          Pleaser enter all information
                      </v-alert>
                       <v-alert
                          :value="false"
                          type="error"
                          v-model="warn2"
                          >
                          Username is already exist
                      </v-alert>
                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="orange" flat @click="Register = false">Close</v-btn>
                        <v-btn color="orange" flat  @click="submit1" @keyup.enter="submit1">Register</v-btn>
                      </v-card-actions>
                  </v-card>
            </v-dialog>
            <v-btn color="orange" flat @click="submit" @keyup.enter="submit">Login</v-btn>
            </v-card-actions>
        </v-card>
      </v-dialog>
    </v-layout>
  </div>
</template>

<!-- js that controls the input and request for the api check the validation -->
<script>
import axios from 'axios'
export default {
  data: () => ({
    dialog: false,
    Register: false,
    PasswordR: '',
    UsernameR: '',
    Password: '',
    Username: '',
    Email: '',
    first_name: '',
    last_name: '',
    warn: false,
    warn1: false,
    warn2: false,
    warn3: false,
    visible: true,
    url: 'http://neon.whiteboard.house/v0/users/'
  }),
  methods: {
    // submit for login
    submit: function () {
      console.log(`Username is ${this.Username} and pw is ${this.Password}`)
      if (this.Password !== '' && this.Username !== '') {
        axios.post('http://neon.whiteboard.house/v0/jwt/', {
          'username': this.Username,
          'password': this.Password
        })
          .then((response) => {
            console.log(response)
            if (response.status === 200) {
              console.log(response.data)
              localStorage.setItem('token', response.data.token)
              this.dialog = false
              this.warn = false
              this.warn3 = false
              this.visible = false
            } else {
              this.warn3 = true
              this.warn = false
            }
          }, (error) => {
            console.log(error)
            this.warn3 = true
            this.warn = false
          })
      } else {
        this.warn = true
        this.warn3 = false
      }
    },
    // logout function
    logoutLocal: function () {
      console.log('Logging out')
      localStorage.clear()
      this.visible = true
    },
    // register function
    submit1: function () {
      console.log(`Username is ${this.UsernameR} and pw is ${this.PasswordR}`)
      console.log(`First name is ${this.first_name} and last is ${this.last_name}`)
      if (this.PasswordR !== '' && this.UsernameR !== '' && this.first_name !== '' && this.last_name !== '') {
        axios.post(this.url, {
          'username': this.UsernameR,
          'password': this.PasswordR,
          'first_name': this.first_name,
          'last_name': this.last_name
        }).then((response) => {
          console.log(response)
          if (response.status === 201) {
            console.log(response.data)
            this.Register = false
            this.warn1 = false
            this.warn2 = false
          } else {
            this.warn2 = true
            this.warn1 = false
          }
        }, (error) => {
          console.log(error)
          this.warn2 = true
          this.warn1 = false
        })
      } else {
        this.warn1 = true
        this.warn2 = false
      }
    }
  }
}
</script>
