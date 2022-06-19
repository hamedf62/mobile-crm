<template>
  <!-- <v-flex md12 md4> -->
  <v-row align="center" justify="center">
    <v-col cols="4">
      <v-card elevation="12" color="blue">
        <v-form ref="loginForm" @submit.prevent="userLogin">
          <v-toolbar dark color="orange">
            <v-toolbar-title>Login form</v-toolbar-title>
          </v-toolbar>
          <v-card-text>
            <v-text-field
              v-model="login.email"
              prepend-icon="mdi-account"
              label="Email"
              type="text"
            ></v-text-field>
            <v-text-field
              v-model="login.password"
              prepend-icon="mdi-lock"
              label="Password"
              type="password"
            ></v-text-field>
          </v-card-text>
          <v-card-actions>
            <v-btn type="submit">Login</v-btn>
            <v-spacer />
            <v-btn type="submit" text>Forgot Password</v-btn>
          </v-card-actions>
        </v-form>
      </v-card>
    </v-col>
  </v-row>
  <!-- </v-flex> -->
</template>

<script>
export default {
  data() {
    return {
      login: {
        email: '',
        password: '',
      },
    }
  },
  methods: {
    async userLogin() {
      await this.$auth
        .loginWith('local', { data: this.login })
        .then((response) => {
          this.$nuxt.$emit('Message', {
            text: response.data.meta.message,
            color: 'green',
          })
        })
        .catch(() => {
          this.login.password = null
        })
    },
  },
}
</script>
