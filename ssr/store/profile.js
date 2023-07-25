export default {
  namespaced: true,

  state: {
    orders : [],
    screen : 0,
    breadcrumb: ['Мои заказы', 'Избранные товары', 'Настройки аккаунта', 'Сменить пароль'],
  },

  getters: {
    ORDERS(state) {
      return state.orders;
    },
    SCREEN(state) {
      return state.screen;
    },
    BREADCRUMB(state){
      return state.breadcrumb;
    }
  },

  mutations: {
    CHANGE_SCREEN(state, newstate) {
      state.screen = newstate;
    },

    // DELETE_BREADCRUMB(state, newstate) {
    //   state.stack.splice(state.stack.length - 1, 1);
    // }
  },

  actions: {
    // CHANGE_BREADCRUMB({ commit, getters }, id) {
    //   while (getters.STACK.length > id+1){
    //     commit("DELETE_BREADCRUMB");
    //   }
    // }
  },
}
