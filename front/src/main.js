import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from "axios";

axios.interceptors.response.use(
  response => response,
  error => {
    console.log(error.response);
    if (error.response.status === 422) {
      store.commit("notification/ADD_MESSAGE", error.response.data.errors);
    } else if (error.response.status === 401) {
      store.commit("auth/SET_USER_DATA", null);
      localStorage.removeItem("authToken");
      router.push({ name: "Login" });
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
