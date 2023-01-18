import axios from "axios";

export default {
  namespaced: true,

  state: {
    orders: [],
    totalCost: 0,
  },

    getters: {
      ORDERS(state) {
        return state.orders;
      },
      TOTAL_ORDER_COST(state) {
        return state.totalCost;
      }
    },

    mutations: {
      SET_ORDERS(state, payload){
        state.orders = payload;
      },
  
      ADD_ITEM_TO_CART(state, payload) {
        if (!state.orders.length) {
          state.orders.push(payload);
        } else {
          const isItemInCart = state.orders.filter(item => item.product.id === payload.product.id);
          if (isItemInCart.length) {
            isItemInCart[0].amount = isItemInCart[0].amount + payload.amount;
          } else {
            state.orders.push(payload);
          }
        }
      },

      UPDATE_ITEM_IN_CART(state, payload){

      },
      
      REMOVE_ITEM_FROM_CART(state, payload) {
          const filteredItemsInCart = state.orders.filter(item => item.product.id !== payload.product.id);
          state.orders = [...filteredItemsInCart];
      },

      UPDATE_TOTAL_COST(state, payload) {
        if (payload.action = 'add') {
          state.totalCost = state.totalCost + payload.cost;
        } else {
          state.totalCost = state.totalCost - payload.cost;
        }
      }
    },

    actions: {
      async GET_USER_ORDER({ commit } ){
        try {
          const response = await axios.get(process.env.VUE_APP_API_URL + 'carts/mine/products');
          commit("SET_ORDERS", response.data);
        } catch (e) {
          console.log(e);
          commit("notification/ADD_MESSAGE", {name: "Не возможно обновить корзину", icon: "error", id: '1'}, {root: true})
        }
      }
    }
  };
