import axios from "axios";

export default {
  namespaced: true,

  state: {
    itemsList: [],
    tatalPages: 0,
    activePage: 0,
    recomendedList: [],
    searchString: '',
    recomendationType: 'all',
    recomendationOrder: '',
    recomendationQuantity: 10,
    shownItemslist: [],
    category: {},
  },

  getters: {
    ITEMS_LIST(state){
      return state.itemsList;
    },
    TOTAL_PAGES(state){
      return state.tatalPages;
    },
    ACTIVE_PAGE(state){
      return state.activePage
    },
    RECOMENDED_ITEMS(state){
      return state.recomendedList;
    },
    CATALOG_SEARCH_STRING(state){
      return state.searchString;
    },
    RECOMENDATION_TYPE(state) {
      return state.recomendationType;
    },
    RECOMENDATION_ORDER(state) {
      return state.recomendationOrder;
    },
    RECOMENDATION_QUANTITY(state) {
      return state.recomendationQuantity;
    },
    SHOWN_ITEMS_LIST(state){
      return state.shownItemslist;
    },
    CATEGORY(state){
      return state.category;
    }
  },

  mutations: {
    SET_CATALOG_ITEMS(state, items) {
      state.itemsList = items.data;
    },

    SET_RECOMENDED_ITEMS(state, items) {
      state.recomendedList = items.data;
    },

    SET_PAGE_STATE(state, data) {
      if (!data.offset) {
        state.activePage = 1;
      } else {
        state.activePage =  Math.floor(data.offset / data.limit) + 1;
      }
      state.tatalPages =  data.back.total % data.limit === 0 ? data.back.total / data.limit: Math.floor(data.back.total / data.limit) + 1;
    },

    SET_CATALOG_SEARCH_STRING(state, searchStr) {
      state.searchString = searchStr;
    },

    SET_RECOMENDATION_TYPE(state, type) {
      state.recomendationType = type;
    },

    SET_RECOMENDATION_ORDER(state, order) {
      state.recomendationOrder = order;
    },

    SET_RECOMENDATION_QUANTITY(state, quantity) {
      state.recomendationQuantity = quantity;
    },

    SET_SHOWN_ITEMS_LIST(state, list) {
      state.shownItemslist = [...list];
    },

    SET_CATEGORY(state, category) {
      state.category = category;
    }
  },

  actions: {
    async GET_CATALOG_ITEMS({ commit, rootGetters }, data) {
      try {
        let queryData = 'products?category_id=' + data + 
        '&offset=' + rootGetters['query/OFFSET'] + 
        '&limit=' + rootGetters['query/LIMIT'] + 
        '&actual_price_gte=' + rootGetters['query/MIN_PRICE'] + 
        '&actual_price_lte=' + rootGetters['query/MAX_PRICE'] +
        '&ordering=' + rootGetters['query/SORT_DIRECTION'] + rootGetters['query/SORT_TYPE'] +
        '&q=' + rootGetters['catalog/CATALOG_SEARCH_STRING'];

        if (rootGetters['query/TYPE_OF_PRODUCT'] !== 'all') queryData = queryData + '&type_of_product=' + rootGetters['query/TYPE_OF_PRODUCT'];
        const response = await axios.get(useRuntimeConfig().public.NUXT_APP_API_URL + queryData);
        commit("SET_CATALOG_ITEMS", response.data);
        commit("SET_PAGE_STATE", { back: response.data, offset: rootGetters['query/OFFSET'], limit: rootGetters['query/LIMIT']});
      } catch (e) {
        console.log(e);
        // commit("notification/ADD_MESSAGE", {name: "Не возможно загрузить каталог категории " + data, icon: "error", id: '1'}, {root: true})
      }
    },

    async GET_ALL_CATALOG_ITEMS({ commit, rootGetters }) {
      try {
        let queryData = 'products?' + 
        'offset=' + rootGetters['query/OFFSET'] + 
        '&limit=' + rootGetters['query/LIMIT']
          + 
        '&actual_price_gte=' + rootGetters['query/MIN_PRICE'] + 
        '&actual_price_lte=' + rootGetters['query/MAX_PRICE'] +
        '&ordering=' + rootGetters['query/SORT_DIRECTION'] + rootGetters['query/SORT_TYPE'] +
        '&q=' + rootGetters['catalog/CATALOG_SEARCH_STRING'];
        if (rootGetters['query/TYPE_OF_PRODUCT'] !== 'all') queryData = queryData + '&type_of_product=' + rootGetters['query/TYPE_OF_PRODUCT']
        const response = await axios.get(useRuntimeConfig().public.NUXT_APP_API_URL + queryData);
        commit("SET_CATALOG_ITEMS", response.data);
        // console.log('GET_ALL_CATALOG_ITEMS ', rootGetters['query/OFFSET'], rootGetters['query/LIMIT'])
        commit("SET_PAGE_STATE", { back: response.data, offset: rootGetters['query/OFFSET'], limit: rootGetters['query/LIMIT']});
        return response.data;
      } catch (e) {
        console.log(e);
        // commit("notification/ADD_MESSAGE", {name: "Не возможно загрузить весь каталог ", icon: "error", id: '1'}, {root: true})
        return []
      }
    },

    async GET_RECOMENDED_ITEMS({ commit, getters, rootGetters }) {
      try {
        let queryData = 'products?offset=0' +  
        '&limit=' + getters.RECOMENDATION_QUANTITY;

        if (getters.RECOMENDATION_TYPE !== 'all') queryData = queryData + '&type_of_product=' + getters.RECOMENDATION_TYPE;
        if (getters.RECOMENDATION_ORDER) queryData = queryData + '&ordering=' + rootGetters['query/SORT_DIRECTION'] + getters.RECOMENDATION_ORDER;
        const response = await axios.get(useRuntimeConfig().public.NUXT_APP_API_URL + queryData);
        commit("SET_RECOMENDED_ITEMS", response.data);
      } catch (e) {
        console.log(e);
        // commit("notification/ADD_MESSAGE", {name: "Не возможно загрузить рекомендованные товары ", icon: "error", id: '1'}, {root: true})
      }
    },
  }
};
