<template>
  <v-card height="350px">
    <v-navigation-drawer
      absolute
      permanent
      right
    >
      <template v-slot:prepend>
        <v-list-item two-line>
          <v-list-item-avatar>
            <img src="">
          </v-list-item-avatar>

          <v-list-item-content>
            <v-list-item-title>name</v-list-item-title>
            <v-list-item-subtitle>Logged In</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </template>

      <v-divider></v-divider>

      <v-list dense>
        <v-list-item
          v-for="item in items"
          :key="item.title"
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>
     <v-main>
      <v-container flex>
        <Nuxt />
      </v-container>
     </v-main>
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </v-card>
</template>

<script>
  export default {
    data () {
      return {
        items: [
          { title: 'Profile', icon: 'mdi-face-man-profile'},
          { title: 'Gift Code', icon: 'mdi-gift' },
          { title: 'Credit Card', icon: 'mdi-credit-card' },
        ],
      }
    },
  }
</script>