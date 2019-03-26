<template>
  <div class="text-xs-center">
    <v-layout>
        <v-dialog v-model="dialog" persistent max-width="600px">
        <v-btn slot="activator" color="#ADFF2F" dark flat p3>
            <span class="mr-1" style="color:greenyellow;font-size:20px">Login</span> 
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
            </v-card-text>
            <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="orange" flat @click="dialog = false">Close</v-btn>
            <v-btn color="orange" flat @click="submit" @keyup.enter="submit">Login</v-btn>
            </v-card-actions>
        </v-card>
        </v-dialog>
    </v-layout>
  </div>
</template>

<script>
  export default {
    data: () => ({
      dialog: false,
      Password:'',
      Username:'',
      warn: false,
    }),
    methods:{
        submit: function (){
            console.log(`Username is ${this.Username} and pw is ${this.Password}`);
            if(this.Password != '' && this.Username != ''){
                 this.dialog = false;
                 this.warn = false;
            }
            else{
                this.warn = true;
            }
        }
    }
  }
</script>