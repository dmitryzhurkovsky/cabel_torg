export default {
  namespaced: true,

  state: {
    messages : [],
    isLoading: false,
  },

  getters: {
    MESSAGES(state) {
      return state.messages;
    },
    LENGTH(state) {
      return state.messages.length;
    },
    IS_LOADING(state) {
      return state.isLoading;
    }
  },

  mutations: {
    ADD_MESSAGE(state, msg) {
      state.messages.unshift(msg);
    },
    DELETE_MESSAGE(state) {
      state.messages.pop();
    },
    SET_IS_LOADING(state, type) {
      state.isLoading = type;
    }
  },

  actions: {
  },
}
