import axios from "axios";

export default {
  namespaced: true,

  state: {
    categoryId: 1,
    typeOfProduct: 'all',
    offset: 0,
    limit: 12,
  },

    getters: {
      CATEGORY_ID(state){
        return state.categoryId;
      },
      TYPE_OF_PRODUCT(state){
        return state.typeOfProduct;
      },
      OFFSET(state){
        return state.offset;
      },
      LIMIT(state){
        return state.limit;
      },
    },

    mutations: {
      SET_CATEGORY_ID(state, category) {
        state.categoryId = category;
      },
    },

    actions: {
    }
  };
