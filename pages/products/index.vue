<template>
  <v-card>
    <v-card-title>
      Products
      <v-btn
        v-if="$route.name != 'Runs'"
        class="mx-2"
        color="red"
        text
        @click="refresh"
        >Refresh</v-btn
      >

      <v-btn class="mx-2" color="primary" text @click="showswal"
        >Show ME!</v-btn
      >

      <v-spacer></v-spacer>
    </v-card-title>

    <v-data-table
      :headers="headers"
      :items="products"
      :items-per-page="200"
      :search="search"
      height="500"
      fixed-header
      mobile-breakpoint="0"
      class="elevation-1"
      :sort-by.sync="sortBy"
      :sort-desc.sync="sortDesc"
    >
    </v-data-table>
  </v-card>
</template>

<script>
export default {
  auth: false,
  // layout: 'dashboard',
  data() {
    return {
      value: [],
      sortBy: 'id',
      sortDesc: true,
      search: '',
      products: [],
      headers: [
        { text: 'Id', value: 'id' },
        { text: 'PName', value: 'name' },
        { text: 'Price', value: 'price' },
      ],
    }
  },
  async fetch() {
    await this.refresh()
  },
  head() {
    return {
      title: 'Products',
    }
  },

  methods: {
    showswal() {
      this.$swal('Good job!', 'You clicked the button!', 'success')
    },
    async refresh() {
      const FlaskProducts = await this.$products.index()

      this.products = FlaskProducts.data
    },
  },
}
</script>

<style>
.v-data-table > .v-data-table__wrapper > table > thead > tr > th {
  font-size: 12px !important;
}

.v-data-table > .v-data-table__wrapper > table > tbody > tr > th {
  font-size: 3px !important;
}
</style>
