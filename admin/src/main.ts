import { createApp } from 'vue';
import App from '@/App.vue';
import { router } from './router';
import { store } from './store';
import axios from 'axios';
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faHeart, faHand, faAddressBook, faTrashCan, faPenToSquare, faFile } from '@fortawesome/free-regular-svg-icons'
library.add([faHeart, faHand, faAddressBook, faTrashCan, faPenToSquare, faFile])

axios.interceptors.request.use(
  (config) => {
    if (localStorage.getItem("authToken")) {
      config.headers = {
          Authorization: `Bearer ${localStorage.getItem("authToken")}`,
          Accept: "application/json"
      };
    }

    return config;
  }
);
  
createApp(App).component('font-awesome-icon', FontAwesomeIcon).use(router).use(store).mount('#app')
