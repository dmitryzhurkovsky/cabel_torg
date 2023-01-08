import axios from "axios";

export default {
  namespaced: true,

  state: {
    categoryId: 1,
    typeOfProduct: {name : 'Все товары', type: 'all'},
    offset: 0,
    limit: 10,
    sort: {name: 'По дате добавления', type: 'date'},
    view: 'row',
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
      SORT_TYPE(state){
        return state.sort;
      },
      VIEW_TYPE(state){
        return state.view;
      }
    },

    mutations: {
      SET_CATEGORY_ID(state, category) {
        state.categoryId = category;
      },

      SET_LIMIT(state, newlimit) {
        state.limit = newlimit;
      },

      SET_SORT_TYPE(state, newSortType) {
        state.sort = newSortType;
      },

      SET_VIEW_TYPE(state, newViewType) {
        state.view = newViewType;
      },

      SET_TYPE_OF_PRODUCT(state, newTypeOfProduct) {
        state.typeOfProduct = newTypeOfProduct;
      },
    },

    actions: {
    }
  };
