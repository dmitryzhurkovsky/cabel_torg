import store from '@/store'

export default defineNuxtRouteMiddleware(() => {
  const isLogin = Boolean(store.getters['auth/USER'])
  return isLogin
});
