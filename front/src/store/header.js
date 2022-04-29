import axios from "axios";

export default {
  namespaced: true,

  state: {
    likes: [],
    orders: [15],
  },

  getters: {
    LIKES_COUNT(state){
      return state.likes.length;
    },
    ORDER_COUNT(state){
      return state.orders.length;
    },

  },

  mutations: {
  },

  actions: {
  }
};
