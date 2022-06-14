<template>
  <v-flex md12 md4>
    <v-form ref="loginForm" @submit.prevent="userLogin">
      <v-card elevation="12" color="blue">
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
          <v-btn class="mr-4" type="submit">Login</v-btn>
        </v-card-actions>
      </v-card>
    </v-form>
  </v-flex>
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
