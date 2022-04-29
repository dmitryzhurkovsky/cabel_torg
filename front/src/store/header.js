import axios from "axios";

export default {
  namespaced: true,

  state: {
    likes: [],
    orders: [12,23],
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

  },

  mutations: {
  },

  actions: {
  }
};
