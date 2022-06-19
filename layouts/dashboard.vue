<template>
  <v-app>
    <v-btn @click="drawer = !drawer">
      <v-icon>mdi-pin</v-icon>
      show the menu
    </v-btn>
    <v-navigation-drawer
      v-model="drawer"
      :mini-variant="miniVariant"
      :clipped="clipped"
      fixed
      app
      color="blue"
    >
      <v-list>
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
          :to="item.to"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <p>this is test layout only</p>
    <v-main>
      <v-container flex>
        <Nuxt />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    clipped: true,
    drawer: false,
    miniVariant: false,
    items: [
      {
        icon: 'mdi-face-man-profile',
        title: 'Profile',
        to: '/profile',
      },
    ],
  }),
}
</script>
