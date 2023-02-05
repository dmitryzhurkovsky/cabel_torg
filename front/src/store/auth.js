import axios from "axios";

export default {
  namespaced: true,

  state: {
      userData: null,
      errors: {},
      type: 1,
      isOpen: true,
      destination: '',
  },

  getters: {
      USER(state){
        return state.userData;
      },
      ERRORS(state) {
          return state.errors;
      },
      AUTH_TYPE(state) {
          return state.type;
      },
      IS_OPEN_MAIN_LOGIN(state) {
          return state.isOpen;
      },
      REDIRECT_AFTER_LOGIN(state) {
          return state.destination;
      },
  },

  mutations: {
      SET_USER_DATA(state, user) {
          state.userData = user;
      },
      SET_ERRORS(state, errors) {
          state.errors = errors;
      },
      SET_TYPE(state, type) {
          state.type = type;
      },
      SET_IS_OPEN_MAIN_LOGIN(state, status) {
          state.isOpen = status;
      },
      SET_DESTINATION(state, route) {
          state.destination = route;
      },
  },

  actions: {
    async GET_USER_DATA({ commit }) {
    try {
          const response = await axios.get(process.env.VUE_APP_API_URL + "users/mine");
          commit("SET_USER_DATA", response.data);
      }
      catch (e) {
          console.log(e);
      };
    },

    async SEND_LOGIN_REQUEST({ dispatch, commit, getters }, data) {
        commit("SET_ERRORS", {});
        try {
            const response = await axios.post(process.env.VUE_APP_API_URL + "token", data);
            localStorage.setItem("authToken", response.data.access_token);
            localStorage.setItem("refreshToken", response.data.refresh_token);
            await dispatch("GET_USER_DATA");
            await dispatch("order/MERGE_USER_OREDRS_AND_LOCAL_STORAGE", null, {root: true});
            await dispatch("favorite/MERGE_USER_FAVORITES_AND_LOCAL_STORAGE", null, {root: true});
        }
        catch (e) {
            console.log(e);
        };
    },

    async SEND_REGISTER_REQUEST({ dispatch, commit }, data) {
      commit("SET_ERRORS", {});
      try {
        const response = await axios.post(process.env.VUE_APP_API_URL + "users", data);
        const loginData = new FormData();
        data.append('username', response.email);
        data.append('password', response.this.password);
        await dispatch("SEND_LOGIN_REQUEST", loginData)
      }
      catch (e) {
          console.log(e);
      };
    },

    async UPDATE_USER_REQUEST({ commit }, data) {
      commit("SET_ERRORS", {});
      try {
        const response = await axios.patch(process.env.VUE_APP_API_URL + "users/mine", data);
        commit("SET_USER_DATA", response.data);
        commit('notification/ADD_MESSAGE', {id: 'upd', name: 'Данные профиля обновлены'}, {root: true});
      }
      catch (e) {
          console.log(e);
      };
    },

    async SEND_LOGOUT_REQUEST({ commit }) {
        commit("SET_USER_DATA", null);
        commit("order/SET_ORDERS", [], {root: true});
        commit("favorite/SET_FAVORITES", [], {root: true});
        localStorage.removeItem("authToken");
        commit("order/SET_IS_APPLICATION_OPEN", false, {root: true});
        commit("SET_DESTINATION", '');
    },

    // sendVerifyResendRequest() {
    //   return axios.get(process.env.VUE_APP_API_URL + "email/resend");
    // },
    //
    // sendVerifyRequest({ dispatch }, hash) {
    //   return axios
    //     .get(process.env.VUE_APP_API_URL + "email/verify/" + hash)
    //     .then(() => {
    //       dispatch("GET_USER_DATA");
    //     });
    // },

  }
};
