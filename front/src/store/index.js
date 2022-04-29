import { createStore } from 'vuex'
import auth from "./auth.js";
import header from "./header.js"

export default createStore({

  state: {

    errors: []
  },

  getters: {

    errors: state => state.errors
  },

  mutations: {

    setErrors(state, errors) {
      state.errors = errors;
    }
  },

  actions: {
  },

  modules: {
    auth:   auth,
    header: header,
  }
})
