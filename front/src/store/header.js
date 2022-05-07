import axios from "axios";

export default {
  namespaced: true,

  state: {
    likes: [],
    orders: [12,23],
    isMenuOpen: false,
    munuItemActive : 1,
  },

  getters: {
    LIKES_COUNT(state){
      return state.likes.length;
    },
    ORDER_COUNT(state){
      if (state.orders.length) {
          return state.orders.length;
      } else {
          return null;
      }
    },
    IS_MENU_OPEN(state){
      return state.isMenuOpen;
    },
    MENU_ITEM_ACTIVE(state){
      return state.munuItemActive;
    }

  },

  mutations: {
    UPDATE_IS_MENU_OPEN (state, newstate){
      state.isMenuOpen = newstate
    },
  },

  actions: {
  }
};
