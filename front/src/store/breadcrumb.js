export default {
  namespaced: true,

  state: {
    stack : [
      {
          name: 'Главная',
          path: '/',
          type: 'global',
          class: '',
      },
    ],
  },

  getters: {
    STACK(state) {
      return state.stack
    },
  },

  mutations: {
    ADD_BREADCRUMB(state, newstate) {
      state.stack.push(newstate);
    },

    DELETE_BREADCRUMB(state, newstate) {
      state.stack.splice(state.stack.length - 1, 1);
    },

    RENAME_LAST_BREADCRUMB(state, newstate){
      if (state.stack.length - 1){
        state.stack[state.stack.length - 1].name = newstate;
      }
    }
},

  actions: {
    CHANGE_BREADCRUMB({ commit, getters }, id) {
      while (getters.STACK.length > id+1){
        commit("DELETE_BREADCRUMB");
      }
    }
  },
}
