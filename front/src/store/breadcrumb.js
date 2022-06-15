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
      // {
      //     name: 'История покупок',
      //     path: '/user_cab',
      //     type: 'global',
      //     class: '',
      // },
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
