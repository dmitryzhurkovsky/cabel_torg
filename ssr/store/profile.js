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

  },
}
