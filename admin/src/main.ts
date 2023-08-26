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
  async (config: any) => {
    if (localStorage.getItem("authToken")) {
      config.headers = {
          Authorization: `Bearer ${localStorage.getItem("authToken")}`,
          Accept: "application/json",
          'Content-Type': 'application/json'
      };
    }
  
    return config;
  }
);

axios.interceptors.response.use(
  response => response,
  
  async error => {
    // console.log('SSSSS', error.response);
    if (typeof error.response === 'undefined') {
        store.commit(MutationTypes.SET_USER, null);
        store.commit(MutationTypes.SET_IS_LOADING, false)
        return Promise.reject(error);
    } else if (error.response.status === 422) {
      const errors = error.response.data.detail;
      store.commit(MutationTypes.SET_USER, null);
      store.commit(MutationTypes.SET_IS_LOADING, false)
      return Promise.reject(error);
    // } else if (error.response.status === 401) {
    //   const errors = error.response.data.detail;
    //   store.commit(MutationTypes.SET_USER, null);
    //   localStorage.removeItem("authToken");
    //   localStorage.removeItem("refreshToken");
    //   store.commit(MutationTypes.SET_IS_LOADING, false)
    //   return Promise.reject(error);
    } else if (error.response.status === 401) {
      // console.log('Start getting refresh token process... ');
      
      const originalConfig = error.config;
      originalConfig._retry = true;

      let isRefresh = false;

      const responseRefresh = await fetch(import.meta.env.VITE_APP_API_URL + "refresh", {
        method: 'POST',
        headers: {
          Authorization: `Bearer ${localStorage.getItem("authToken")}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({refresh_token: localStorage.getItem("refreshToken")})
      });
      // console.log('responseRefresh ', responseRefresh);
            
      if (responseRefresh.status !== 201) {
        store.commit(MutationTypes.SET_USER, null);
        localStorage.removeItem("authToken");
        localStorage.removeItem("refreshToken");
        store.commit(MutationTypes.SET_IS_LOADING, false)
        return Promise.reject(error);
      } else {
        const result = await responseRefresh.json();
        // console.log('Result: ', result);
        localStorage.setItem("authToken", result.access_token);
        localStorage.setItem("refreshToken", result.refresh_token);
        originalConfig.headers = {
          Authorization: `Bearer ${result.access_token}`,
          Accept: "application/json",
          'Content-Type': 'application/json'
        }
        isRefresh = true;
      }
     
      if (isRefresh) return axios(originalConfig);

    } else {
      store.commit(MutationTypes.SET_IS_LOADING, false)
      return Promise.reject(error);
    }
  }
);

createApp(App).component('font-awesome-icon', FontAwesomeIcon).component('QuillEditor', QuillEditor).use(router).use(store).mount('#app')
