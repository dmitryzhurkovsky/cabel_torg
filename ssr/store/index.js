import { createStore } from 'vuex'
import auth from './auth.js';
import header from './header.js';
import notification from './notification.js';
import breadcrumb from './breadcrumb.js';
import profile from './profile.js';
import order from './order.js';
import query from './query.js';
import catalog from './catalog';
import favorite from './favorite';
import main from './main';
import axios from 'axios';

axios.interceptors.response.use(
  response => {
    store.commit("notification/ADD_MESSAGE", {id: 'Err500', icon: 'error', name: 'Ошибка авторизации. Сервер не отвечает'});
    return response;
  },
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

axios.interceptors.request.use(function(config) {
  config.headers = {
      Authorization: `Bearer ${localStorage.getItem("authToken")}`,
      "Content-Type": "application/json",
      Accept: "application/json"
  };
  return config;
});

const store = createStore({

  modules: {
    auth          : auth,
    header        : header,
    notification  : notification,
    breadcrumb    : breadcrumb,
    profile       : profile,
    order         : order,
    query         : query,
    catalog       : catalog,
    favorite      : favorite,
    main          : main,
  }
})

export default store
