import axios from "axios";

export default {
  namespaced: true,

  state: {
    categoryId: null,
    typeOfProduct: 'all',
    offset: 0,
    limit: 12,
    sort: 'created_at',
    direction: '-',
    view: 'table',
    minPrice: 0,
    maxPrice: 10000,
    searchString: '',
    findedElements: [],
    allTypesOfProduct: [
      {name : 'Все товары', type: 'all'},
      {name : 'Акции', type: 'with_discount'}, 
      {name : 'В наличии', type: 'available'},
      {name : 'Топ продаж', type: 'popular'},
    ],
    allSortsOfProduct: [
      {name: 'По дате добавления', type: 'created_at'},
      {name: 'цене', type: 'price'},
      {name: 'скидке', type: 'discount'},
    ],
    limitItems : [12, 24, 48],
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
      SORT_DIRECTION(state){
        return state.direction;
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
      },
      ALL_TYPE_OF_PRODUCTS(state){
        return state.allTypesOfProduct;
      },
      ALL_SORT_OF_PRODUCTS(state){
        return state.allSortsOfProduct;
      },
      LIMIT_ITEMS(state){
        return state.limitItems;
      },
    },

    mutations: {
      SET_CATEGORY_ID(state, category) {
        if (state.categoryId !== category) {
          state.offset = 0;
        }
        state.categoryId = category;
        // state.searchString = '';
      },

      SET_TYPE_OF_PRODUCT(state, newTypeOfProduct) {
        if (state.typeOfProduct !== newTypeOfProduct) state.offset = 0;
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

      SET_SORT_DIRECTION(state, direction) {
        state.direction = direction;
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
      },

      SET_FINDED_ELEMENTS(state, items) {
        state.findedElements = items.data;
      },
    },

    actions: {
      async FIND_ELEMENTS({ commit, getters }) {
        try {
            const query = getters.SEARCH_STRING ? '&q=' + getters.SEARCH_STRING : '';
            const response = await axios.get(useRuntimeConfig().public.NUXT_APP_API_URL + 
                'products?' + 
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
