import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from "axios";

axios.interceptors.response.use(
  response => response,
  error => {
    if (typeof error.response === 'undefined') {
        console.log(error);
        store.commit("notification/ADD_MESSAGE", {id: JSON.stringify(error), icon: 'error', name: 'Ошибка авторизации. Сервер не отвечает'});
        store.commit("auth/SET_USER_DATA", null);
        localStorage.removeItem("authToken");
        localStorage.removeItem("refreshToken");
        return Promise.reject(error);
    } else if (error.response.status === 422 || error.response.status === 500) {
        console.log( error.response.data.detail);
        const errors = error.response.data.detail;
        for (let i = 0; i < errors.length; i++) {
          store.commit("notification/ADD_MESSAGE", {id: i, icon: 'error', name: errors[i].msg});
        }
        store.commit("auth/SET_USER_DATA", null);
        localStorage.removeItem("authToken");
        localStorage.removeItem("refreshToken");
        return Promise.reject(error);
    } else if (error.response.status === 401) {
        store.commit("auth/SET_USER_DATA", null);
        localStorage.removeItem("authToken");
        localStorage.removeItem("refreshToken");
        return Promise.reject(error);
    } else {
        return Promise.reject(error);
    }
  }
);

axios.interceptors.request.use(function(config) {
  config.headers.common = {
      Authorization: `Bearer ${localStorage.getItem("authToken")}`,
      "Content-Type": "application/json",
      Accept: "application/json"
  };

  return config;
});

const app = createApp(App)

app.config.warnHandler = function (msg, vm, trace) {
  return null
}

app.use(store).use(router).mount('#app')
// new Vue({
//   router,
//   store,
//   render: h => h(App)
// }).$mount("#app");
