<template>
  <v-row justify="center" align="center">
    <v-col cols="12" sm="8" md="6">
      <v-card>
        <v-card-title class="headline">
          Welcome to the Mobile CRM
        </v-card-title>
        <v-card-text>
          <p>please login at the first....</p>
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn color="primary" nuxt to="/auth/login"> Login </v-btn>
          <v-btn color="primary" nuxt to="/auth/register"> Register </v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'IndexPage',
}
</script>
