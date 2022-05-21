export default {
  namespaced: true,

  state: {
    messages : [],
  },

  getters: {
    MESSAGES(state) {
      return state.messages
    },
  },

  mutations: {
    ADD_MESSAGE(state, newstate) {
      state.messages.unshift(newstate);
    },
    DELETE_MESSAGE(state, newstate) {
      state.messages.splice(state.messages.length - 1, 1);
    }
  },

  actions: {
  },
}
