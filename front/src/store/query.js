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
    findedElements: [],
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
      },
      FINDED_ELEMENTS(state){
        return state.findedElements;
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
        // state.categoryId = null;
      },

      SET_FINDED_ELEMENTS(state, items) {
        state.findedElements = items.data;
      }
    },

    actions: {
      async FIND_ELEMENTS({ commit, getters }) {
        try {
            const query = getters.SEARCH_STRING ? '&q=' + getters.SEARCH_STRING : '';
            const response = await axios.get(process.env.VUE_APP_API_URL + 
                'products?type_of_product=all' + 
                '&offset=0' +  
                '&limit=10' + 
                query
            );
            commit("SET_FINDED_ELEMENTS", response.data);
        } catch (e) {
            console.log(e);
            commit("notification/ADD_MESSAGE", {name: "Не возможно загрузить искомые товары ", icon: "error", id: '1'}, {root: true})
        }
      },
    }
  };
