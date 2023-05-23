import store from '@/store'

export default defineNuxtRouteMiddleware((to, from) => {
  const isLogin = Boolean(store.getters['auth/USER'])
  if (!isLogin) {
    return navigateTo('/login');
  }
});
