import colors from 'vuetify/es5/util/colors'

export default {
  ssr: false, // Disable Server Side rendering

  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    titleTemplate: '%s - mobile_crm',
    title: 'mobile_crm',
    htmlAttrs: {
      lang: 'en',
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' },
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/eslint
    '@nuxtjs/eslint-module',
    // https://go.nuxtjs.dev/vuetify
    '@nuxtjs/vuetify',
    '@nuxtjs/dotenv',
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    '@nuxtjs/auth-next',
    '@nuxtjs/i18n',
    'nuxt-highcharts',
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: { proxy: true, credentials: true },
  proxy: {
    '/api/v1/': {
      target:
        process.env.NODE_ENV === 'dev'
          ? process.env.DEV_BASE_URL
          : process.env.PRODUCTION_BASE_URL,
    },
    // process.env.NODE_ENV === "dev" ? process.env.DEV_BASE_URL : process.env.PRODUCTION_BASE_URL,
    // pathRewrite: { "^/api/": "" },
    changeOrigin: true,
  },

  auth: {
    scopeKey: 'roles',
    rewriteRedirects: true,
    strategies: {
      local: {
        scheme: 'refresh',
        token: {
          property: 'meta.access_token',
          maxAge: 1800,
          global: true,
          type: 'Bearer',
        },
        refreshToken: {
          property: 'meta.refresh_token',
          data: 'refresh_token',
          maxAge: 60 * 60 * 24 * 30,
        },
        user: {
          property: 'data',
          // autoFetch: true
        },
        // url: "api",
        endpoints: {
          login: { url: 'api/v1/auth/login', method: 'post' },
          refresh: { url: 'api/v1/auth/refresh', method: 'post' },
          user: { url: 'api/v1/auth/user', method: 'get' },
          logout: { url: 'api/v1/auth/logout', method: 'post' },
        },
        // autoLogout: false
      },
    },
    redirect: {
      login: '/auth/login',
      logout: '/',
      callback: '/auth/login',
      home: '/',
    },
  },

  i18n: {
    lazy: true,
    langDir: '~/locales/',
    detectBrowserLanguage: false,
    strategy: 'no_prefix',
    vueI18nLoader: true,
    defaultLocale: 'fa',

    locales: [
      {
        code: 'en',
        name: 'English',
        iso: 'en-US',
        file: 'en.json',
      },
      {
        code: 'fa',
        name: 'Farsi',
        iso: 'fa-IR',
        file: 'fa.json',
      },
    ],
  },

  // Vuetify module configuration: https://go.nuxtjs.dev/config-vuetify
  vuetify: {
    customVariables: ['~/assets/variables.scss'],
    theme: {
      dark: true,
      themes: {
        dark: {
          primary: colors.blue.darken2,
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3,
        },
      },
    },
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {},
  router: {
    middleware: ['auth'],
  },
}
