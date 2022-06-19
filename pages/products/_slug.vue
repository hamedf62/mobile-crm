<template>
  <v-card>
    <v-card-title>
      Orders
      <v-btn v-if="$route.name != 'Runs'" class="mx-2" @click="refresh"
        >Refresh</v-btn
      >
      <vue-json-to-csv :json-data="orders" :csv-title="'fileName'">
        <v-btn color="success" class="mx-2">
          Export <i class="mdi mdi-export-variant" aria-hidden="true"></i>
        </v-btn>
      </vue-json-to-csv>
      <v-spacer></v-spacer>
      <v-select
        v-model="search"
        :items="tradingAssets"
        label="Select columns"
        class="mx-2"
      ></v-select>
      <v-select
        v-model="value"
        :items="headers"
        label="Select an Asset"
        multiple
        return-object
        class="mx-2"
      >
        <template #selection="{ item, index }">
          <v-chip v-if="index === 0">
            <span>{{ item.text }}</span>
          </v-chip>
          <span v-if="index === 1" class="grey--text caption"
            >(+{{ value.length - 1 }} others)</span
          >
        </template>
      </v-select>
    </v-card-title>

    <v-data-table
      :headers="selectedHeaders"
      :items="orders"
      :items-per-page="200"
      :item-class="itemRowBackground"
      :search="search"
      height="500"
      fixed-header
      mobile-breakpoint="0"
      class="elevation-1"
      :sort-by.sync="sortBy"
      :sort-desc.sync="sortDesc"
    >
      <template #[`item.asset`]="{ item }">
        <nuxt-link :to="`/Ledgers/${item.run_id}/${item.asset}`">
          <!-- <nuxt-link :to="{ name: 'Ledgers-slug', params: { run_id: 1 } }"> -->
          {{ item.asset }}
        </nuxt-link>
      </template>
      <template #[`item.time`]="{ item }">
        {{
          $moment(item.time, 'YYYY-MM-DD HH:mm:SS')
            .locale('en')
            .format('YY-MMM-DD HH:mm:SS')
        }}
      </template>
      <template #[`item.type`]="{ item }">
        {{ $t(`enums.orders.${item.type}`) }}
      </template>
    </v-data-table>
  </v-card>
</template>

<script>
import VueJsonToCsv from 'vue-json-to-csv'
export default {
  auth: false,
  components: { VueJsonToCsv },
  layout: 'dashboard',
  data() {
    return {
      value: [],
      selectedHeaders: [],
      sortBy: 'id',
      sortDesc: true,
      search: '',
      orders: [],
      tradingAssets: [],
      headers: [
        { text: 'Id', value: 'id' },
        { text: 'Time', value: 'time' },
        { text: 'Type', value: 'type' },
        { text: 'BuyId', value: 'buy_id' },
        { text: 'Asset', value: 'base_asset' },
        { text: 'origPrice', value: 'orig_price' },
        { text: 'execPrice', value: 'executed_price' },
        { text: 'HPrice', value: 'hprice' },
        { text: 'LPrice', value: 'lprice' },
        { text: 'tempPNL', value: 'temp_PNL' },
        { text: 'tempPNL%', value: 'temp_PNLp' },
        { text: 'origQty', value: 'orig_qty' },
        { text: 'execQty', value: 'executed_qty' },
        // { text: "BuyRemainOrig", value: "buy_remain_orig_qty" },
        { text: 'BuyRemainExec', value: 'buy_remain_executed_qty' },
        { text: 'OrderVal', value: 'cummulative_quote_qty' },
        { text: 'origPNL', value: 'orig_PNL' },
        { text: 'origPNL%', value: 'orig_PNLp' },
        { text: 'execPNL', value: 'executed_PNL' },
        { text: 'execPNL%', value: 'executed_PNLp' },

        { text: 'Reason', value: 'reason' },
        { text: 'SellIds', value: 'sell_ids' },
        { text: 'SellReasons', value: 'sell_reasons' },
        { text: 'binStatus', value: 'bin_status' },
        { text: 'binOrderId', value: 'bin_order_id' },
      ],
    }
  },
  fetch() {
    this.refresh()
    // const ordersData = await app.$products.show(
    //   `${params.runType}/${params.id}/${params.slug}`
    // );
    // const tradingAssetsData = await app.$runTradingAssets.show(
    //   `${params.runType}/${params.id}`
    // );
    // this.orders = ordersData.data;
    // this.tradingAssets = tradingAssetsData.data.assets.sort();
    // return {
    //   orders: response.data,
    //   tradingAssets: responseTAssets.data.assets.sort(),
    // };
  },
  // async asyncData({ params, app }) {
  //   const response = await app.$products.show(`${params.runType}/${params.id}/${params.slug}`);
  //   const responseTAssets = await app.$runTradingAssets.show(`${params.runType}/${params.id}`);
  //   return {
  //     orders: response.data,
  //     tradingAssets: responseTAssets.data.assets.sort(),
  //   };
  // },
  head() {
    return {
      title: 'Orders',
    }
  },
  watch: {
    value(val) {
      this.selectedHeaders = val
    },
  },
  created() {
    // this.selectedHeaders = this.headers;
    this.selectedHeaders = [0, 2, 4, 6, 7, 8, 10, 12, 13].map(
      (x) => this.headers[x]
    )
  },
  methods: {
    async refresh() {
      // this.$fetch();
      const ordersData = await this.$products.show(
        `${this.$route.params.runType}/${this.$route.params.id}/${this.$route.params.slug}`
      )

      this.orders = ordersData.data
    },
    itemRowBackground(item) {
      return [1, 3].includes(item.type)
        ? item.executed_qty === 0
          ? 'style-buy-not-executed'
          : item.buy_remain_executed_qty > 0
          ? 'style-buy-executed-open'
          : 'style-buy-executed-close'
        : item.executed_qty === 0
        ? 'style-sell-not-executed'
        : 'style-sell-executed'
    },
  },
}
</script>

<style>
.style-buy-not-executed {
  background-color: lightgreen;
}

.style-buy-executed-open {
  background-color: lightgreen;
  /* font-size: 18px; */
  /* color: rgb(157, 0, 8); */
  font-weight: bold;
}

.style-buy-executed-close {
  background-color: darkgreen;
}

.style-sell-not-executed {
  background-color: rgb(254, 110, 110, 0.2);
}

.style-sell-executed {
  background-color: rgb(254, 110, 110);
}

.v-data-table > .v-data-table__wrapper > table > thead > tr > th {
  font-size: 12px !important;
}

.v-data-table > .v-data-table__wrapper > table > tbody > tr > th {
  font-size: 3px !important;
}
</style>
