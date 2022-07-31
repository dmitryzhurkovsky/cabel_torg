import axios from "axios";

export default {
  namespaced: true,

  state: {
    userData: 0,
    errors: []
  },

  getters: {
    USER(state){
      return state.userData;
    },
    ERRORS(state) {
      return state.errors
    }
  },

  mutations: {
    SET_USER_DATA(state, user) {
      state.userData = user;
    },
    SET_ERRORS(state, errors) {
      state.errors = errors;
    }
  },

  actions: {
    async GET_USER_DATA({ commit }) {
    try {
          const response = await axios.get(process.env.VUE_APP_API_URL + "user");
          commit("SET_USER_DATA", response.data);
      }
      catch (e) {
          console.log(e);
      };
    },

    sendLoginRequest({ commit }, data) {
      // commit("setErrors", [], { root: true });
      return axios
        .post(process.env.VUE_APP_API_URL + "login", data)
        .then(response => {
          commit("SET_USER_DATA", response.data.user);
          localStorage.setItem("authToken", response.data.token);
        });
    },

    SEND_REGISTER_REQUEST({ commit }, data) {
      // commit("setErrors", [], { root: true });
      return axios
        .post(process.env.VUE_APP_API_URL + "users", data)
        .then(response => {
          console.log(response);
          commit("SET_USER_DATA", response.data.user);
          // localStorage.setItem("authToken", response.data.token);
        });
    },

    sendLogoutRequest({ commit }) {
      axios.post(process.env.VUE_APP_API_URL + "logout").then(() => {
        commit("SET_USER_DATA", null);
        localStorage.removeItem("authToken");
      });
    },

    sendVerifyResendRequest() {
      return axios.get(process.env.VUE_APP_API_URL + "email/resend");
    },

    sendVerifyRequest({ dispatch }, hash) {
      return axios
        .get(process.env.VUE_APP_API_URL + "email/verify/" + hash)
        .then(() => {
          dispatch("GET_USER_DATA");
        });
    },

  }
};
