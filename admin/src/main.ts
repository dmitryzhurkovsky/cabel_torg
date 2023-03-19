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
  error => {
    if (typeof error.response === 'undefined') {
        store.commit("notification/ADD_MESSAGE", {id: 'Err500', icon: 'error', name: 'Ошибка авторизации. Сервер не отвечает'});
        store.commit("auth/SET_USER_DATA", null);
        localStorage.removeItem("authToken");
        return Promise.reject(error);
    } else if (error.response.status === 422) {
        console.log( error.response.data.detail);
        const errors = error.response.data.detail;
        for (let i = 0; i < errors.length; i++) {
          store.commit("notification/ADD_MESSAGE", {id: i, icon: 'error', name: errors[i].msg});
        }
        store.commit("auth/SET_USER_DATA", null);
        localStorage.removeItem("authToken");
        return Promise.reject(error);
    } else if (error.response.status === 401) {
        store.commit("auth/SET_USER_DATA", null);
        localStorage.removeItem("authToken");
        return Promise.reject(error);
    } else {
        return Promise.reject(error);
    }
  }
);

createApp(App).component('font-awesome-icon', FontAwesomeIcon).component('QuillEditor', QuillEditor).use(router).use(store).mount('#app')
