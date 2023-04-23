import axios from 'axios';

export default defineNuxtPlugin(nuxtApp => {

  let api = axios.create();

  api.interceptors.response.use(
    response => response,
    error => {
      if (typeof error.response === 'undefined') {
          store.commit("notification/ADD_MESSAGE", {id: 'Err500', icon: 'error', name: 'Ошибка авторизации. Сервер не отвечает'});
          store.commit("auth/SET_USER_DATA", null);
          localStorage.removeItem("authToken");
          return Promise.reject(error);
      } else if (error.response.status === 422 || error.response.status === 500) {
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
  
  api.interceptors.request.use(function(config) {
    config.headers.common = {
        Authorization: `Bearer ${localStorage.getItem("authToken")}`,
        "Content-Type": "application/json",
        Accept: "application/json"
    };
  
    return config;
  });
    
  return {
    provide: {
      api: api,
    },
  };
})
