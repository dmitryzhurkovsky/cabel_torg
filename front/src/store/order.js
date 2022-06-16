import axios from "axios";

export default {
  namespaced: true,

  state: {
    orders: [12,23],
  },

    getters: {
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
