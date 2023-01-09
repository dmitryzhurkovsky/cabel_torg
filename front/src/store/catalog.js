import axios from "axios";

export default {
  namespaced: true,

  state: {
    itemsList: [],
    activeItem: null,
    tatalPages: 0,
    activePage: 0,
    recomendedList: [],
  },

    getters: {
      ITEMS_LIST(state){
        return state.itemsList;
      },
      ACTIVE_ITEM(state){
        return state.activeItem;
      },
      TOTAL_PAGES(state){
        return state.tatalPages;
      },
      ACTIVE_PAGE(state){
        return state.activePage
      },
      RECOMENDED_ITEMS(state){
        return state.recomendedList;
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
          console.log('Active page',state.activePage);
        }
        state.tatalPages =  data.back.total % data.limit === 0 ? data.back.total / data.limit: Math.floor(data.back.total / data.limit) + 1;
        console.log('SET_PAGE_DATA', state);
      }
    },

    actions: {
      async GET_CATALOG_ITEMS({ commit, rootGetters }, data) {
        try {
            const response = await axios.get(process.env.VUE_APP_API_URL + 
                'products?category_id=' + data + 
                '&type_of_product=' + rootGetters['query/TYPE_OF_PRODUCT'].type + 
                '&offset=' + rootGetters['query/OFFSET'] + 
                '&limit=' + rootGetters['query/LIMIT']);
            commit("SET_CATALOG_ITEMS", response.data);
            commit("SET_PAGE_STATE", { back: response.data, offset: rootGetters['query/OFFSET'], limit: rootGetters['query/LIMIT']});
        } catch (e) {
            console.log(e);
            commit("notification/ADD_MESSAGE", {name: "Не возможно загрузить каталог категории", icon: "error", id: '1'}, {root: true})
        }
      },

      async GET_ALL_CATALOG_ITEMS({ commit, rootGetters }) {
        try {
            const response = await axios.get(process.env.VUE_APP_API_URL + 
                'products?type_of_product=' + rootGetters['query/TYPE_OF_PRODUCT'].type + 
                '&offset=' + rootGetters['query/OFFSET'] + 
                '&limit=' + rootGetters['query/LIMIT']);
            commit("SET_CATALOG_ITEMS", response.data);
            commit("SET_PAGE_STATE", { back: response.data, offset: rootGetters['query/OFFSET'], limit: rootGetters['query/LIMIT']});
        } catch (e) {
            console.log(e);
            commit("notification/ADD_MESSAGE", {name: "Не возможно загрузить весь каталог ", icon: "error", id: '1'}, {root: true})
        }
      },

      async GET_RECOMENDED_ITEMS({ commit }) {
        try {
            const response = await axios.get(process.env.VUE_APP_API_URL + 
                'products?type_of_product=all' + 
                '&offset=0' +  
                '&limit=10');
            commit("SET_RECOMENDED_ITEMS", response.data);
        } catch (e) {
            console.log(e);
            commit("notification/ADD_MESSAGE", {name: "Не возможно загрузить рекомендованные товары ", icon: "error", id: '1'}, {root: true})
        }
      },

    }
  };
