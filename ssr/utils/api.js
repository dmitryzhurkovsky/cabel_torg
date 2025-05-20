import axios from 'axios'
import { useNotificationsStore } from '@/stores/notifications';
import { useAuthStore } from '@/stores/auth';

const api = axios.create({
    baseURL: process.server
        ? process.env.NUXT_APP_API_URL
        // : useRuntimeConfig().public.NUXT_APP_API_URL
        : 'https://cabel-torg.by/api/v1/'
})

api.interceptors.response.use(
    response => {
      return response;
    },
    error => {
      if (typeof window !== 'undefined') {
        const notificationsStore = useNotificationsStore();
        const authStore = useAuthStore();

        const router = useRouter();

        console.log('error.response ', error.response.status);
        
        if (typeof error.response === 'undefined') {
          notificationsStore.addMessage({id: 'upd', name: 'Ошибка авторизации. Сервер не отвечает', icon: "error"});
          authStore.clearUserData();
          return Promise.reject(error);
        } else if (error.response.status === 422) {
          console.log( error.response.data.detail);
          const errors = error.response.data.detail;
          for (let i = 0; i < errors.length; i++) {
            notificationsStore.addMessage({id: i, name: errors[i].msg, icon: "error"});
          }
        } else if (error.response.status === 401) {
          const currRoute = router.currentRoute.value.fullPath;
          authStore.setDestination(currRoute);
          authStore.clearUserData();
          router.push('/login');
          return Promise.reject(error);
        } else {
          return Promise.reject(error);
        }
      } else {
        return Promise.reject(error);
      }
    }
  );
  
  api.interceptors.request.use(function(config) {
    if (typeof window !== 'undefined') {
        if (localStorage.getItem("authToken")) {
        config.headers.common = {
          Authorization: `Bearer ${localStorage.getItem("authToken")}`,
          "Content-Type": "application/json",
          Accept: "application/json"
        }
      } else {
        config.headers.common = {
          "Content-Type": "application/json",
          Accept: "application/json"
        }
      }
    }
    return config;
  });
  

export default api