export default {
  namespaced: true,

  state: {
    messages : [],
  },

  getters: {
    MESSAGES(state) {
      return state.messages;
    },
    LENGTH(state) {
      return state.messages.length;
    },
  },

  mutations: {
    ADD_MESSAGE(state, payload) {
      state.messages.unshift(payload);
    },
    DELETE_MESSAGE(state) {
      state.messages.pop();
    },
  },

  actions: {
  },
}
