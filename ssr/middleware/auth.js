// import store from '@/store'
import { useStore } from 'vuex'

const store = useStore()
console.log('Auth middleware ', store);
export default defineNuxtRouteMiddleware((to, from) => {
  const isLogin = Boolean(store.getters['auth/USER'])
  if (!isLogin) {
    return navigateTo('/login');
  }
});
