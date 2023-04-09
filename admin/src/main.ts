import { createApp } from 'vue';
import App from '@/App.vue';
import { router } from './router';
import { store } from './store';
import axios from 'axios';
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faHeart, faHand, faAddressBook, faTrashCan, faPenToSquare, faFile, faSquareCaretDown, faSquareCaretUp } from '@fortawesome/free-regular-svg-icons'
import { QuillEditor } from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css';
import { IDeliveryType } from './types';
import { request } from 'http';

library.add([faHeart, faHand, faAddressBook, faTrashCan, faPenToSquare, faFile, faSquareCaretDown, faSquareCaretUp] as any)

axios.interceptors.request.use(
  (config: any) => {
    if (localStorage.getItem("authToken")) {
      config.headers = {
          Authorization: `Bearer ${localStorage.getItem("authToken")}`,
          Accept: "application/json"
      };
    }

    return config;
  }
);

axios.interceptors.response.use(
  response => response,
  async error => {
    if (typeof error.response === 'undefined') {
        store.commit("notification/ADD_MESSAGE", {id: 'Err500', icon: 'error', name: 'Ошибка авторизации. Сервер не отвечает'});
        store.commit("auth/SET_USER_DATA", null);
        // localStorage.removeItem("authToken");
        return Promise.reject(error);
    } else if (error.response.status === 422) {
        console.log( error.response.data.detail);
        const errors = error.response.data.detail;
        for (let i = 0; i < errors.length; i++) {
          store.commit("notification/ADD_MESSAGE", {id: i, icon: 'error', name: errors[i].msg});
        }
        store.commit("auth/SET_USER_DATA", null);
        // localStorage.removeItem("authToken");
        return Promise.reject(error);
    } else if (error.response.status === 401) {
        const originalConfig = error.config;
        originalConfig._retry = true;
        const refresh = await axios.post(import.meta.env.VITE_APP_API_URL + "refresh", {refresh_token: localStorage.getItem("refreshToken")}) as IDeliveryType
        if (refresh.status === 201) {
          localStorage.setItem("authToken", refresh.data.access_token);
          localStorage.setItem("refreshToken", refresh.data.refresh_token);
          originalConfig.headers = {
            Authorization: `Bearer ${refresh.data.access_token}`,
            Accept: "application/json"
          }
          return axios(originalConfig)
        } else {
          store.commit("auth/SET_USER_DATA", null);
          localStorage.removeItem("authToken");
          localStorage.removeItem("refreshToken");
          return Promise.reject(error);
        }
    } else {
        return Promise.reject(error);
    }
  }
);

createApp(App).component('font-awesome-icon', FontAwesomeIcon).component('QuillEditor', QuillEditor).use(router).use(store).mount('#app')
