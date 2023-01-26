import axios from "axios";

export default {
  namespaced: true,

  state: {
    categoryId: null,
    typeOfProduct: {name : 'Все товары', type: 'all'},
    offset: 0,
    limit: 10,
    sort: {name: 'По дате добавления', type: 'date'},
    view: 'table',
    minPrice: 0,
    maxPrice: 10000,
    searchString: '',
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
      },
      MIN_PRICE(state){
        return state.minPrice;
      },
      MAX_PRICE(state){
        return state.maxPrice;
      },
      SEARCH_STRING(state){
        return state.searchString;
      }
    },

    mutations: {
      SET_CATEGORY_ID(state, category) {
        state.offset = 0;
        state.categoryId = category;
        state.searchString = '';
      },

      SET_TYPE_OF_PRODUCT(state, newTypeOfProduct) {
        state.offset = 0;
        state.typeOfProduct = newTypeOfProduct;
      },

      SET_OFFSET(state, newOffset) {
        state.offset = newOffset;
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

      SET_MIN_PRICE(state, price) {
        state.minPrice = price;
      },

      SET_MAX_PRICE(state, price) {
        state.maxPrice = price;
      },

      SET_SEARCH_STRING(state, query) {
        state.searchString = query;
        state.categoryId = null;
      },
    },

    actions: {
    }
  };
