import createRepository from '~/api/repository'
export default (ctx, inject) => {
  // inject the repository in the context (ctx.app.$repository)
  // And in the Vue instances (this.$repository in your components)
  const repositoryWithAxios = createRepository(
    ctx.$axios,
    ctx.$store,
    ctx.$swal,
    ctx.i18n
  )
  inject('products', repositoryWithAxios('api/v1/products'))
  inject('users', repositoryWithAxios('api/v1/auth/users'))
}
