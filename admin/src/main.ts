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
import { MutationTypes } from './store/mutation-types'
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
    // console.log(error.response);
    if (typeof error.response === 'undefined') {
        store.commit(MutationTypes.SET_USER, null);
        store.commit(MutationTypes.SET_IS_LOADING, false)
        return Promise.reject(error);
    } else if (error.response.status === 422) {
      const errors = error.response.data.detail;
      store.commit(MutationTypes.SET_USER, null);
      store.commit(MutationTypes.SET_IS_LOADING, false)
      return Promise.reject(error);
    } else if (error.response.status === 401) {
      const originalConfig = error.config;
      // originalConfig._retry = true;

      axios.post(import.meta.env.VITE_APP_API_URL + "refresh", {refresh_token: localStorage.getItem("refreshToken")}).then((refresh) => {
        console.log('QQQQQ ', refresh);
      
        if (refresh.status === 201) {
          console.log('201', refresh.data);
          
          localStorage.setItem("authToken", refresh.data.access_token);
          localStorage.setItem("refreshToken", refresh.data.refresh_token);
          originalConfig.headers = {
            Authorization: `Bearer ${refresh.data.access_token}`,
            Accept: "application/json"
          }
          // console.log('OriginalConfig', originalConfig);
          
          return axios(originalConfig)
        } else {
          store.commit(MutationTypes.SET_USER, null);
          localStorage.removeItem("authToken");
          localStorage.removeItem("refreshToken");
          store.commit(MutationTypes.SET_IS_LOADING, false)
          return Promise.reject(error);
        }
      }).catch((e) => {
        console.log(e);
      
        store.commit(MutationTypes.SET_USER, null);
        localStorage.removeItem("authToken");
        localStorage.removeItem("refreshToken");
        store.commit(MutationTypes.SET_IS_LOADING, false)
        return Promise.reject(error);
      })
    } else {
      store.commit(MutationTypes.SET_IS_LOADING, false)
      return Promise.reject(error);
    }
  }
);

createApp(App).component('font-awesome-icon', FontAwesomeIcon).component('QuillEditor', QuillEditor).use(router).use(store).mount('#app')
