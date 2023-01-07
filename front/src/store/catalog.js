import axios from "axios";

export default {
  namespaced: true,

  state: {
    itemsList: [],
    activeItem: null,
  },

    getters: {
      ITEMS_LIST(state){
        return state.itemsList;
      },
      ACTIVE_ITEM(state){
        return state.activeItem;
      },
    },

    mutations: {
      SET_CATALOG_ITEMS(state, items) {
        state.itemsList = items;
      },
    },

    actions: {
      async GET_CATALOG_ITEMS({ commit, rootGetters }, data) {
        try {
            const response = await axios.get(process.env.VUE_APP_API_URL + 
                'products?category_id=' + data + 
                '&type_of_product=' + rootGetters['query/TYPE_OF_PRODUCT'] + 
                '&offset=' + rootGetters['query/OFFSET'] + 
                '&limit=' + rootGetters['query/LIMIT']);
            commit("SET_CATALOG_ITEMS", response.data);
        } catch (e) {
            console.log(e);
            commit("notification/ADD_MESSAGE", {name: "Не возможно загрузить каталог ", icon: "error", id: '1'}, {root: true})
        }
      },

      async GET_ALL_CATALOG_ITEMS({ commit, rootGetters }) {
        try {
            const response = await axios.get(process.env.VUE_APP_API_URL + 
                'products?type_of_product=' + rootGetters['query/TYPE_OF_PRODUCT'] + 
                '&offset=' + rootGetters['query/OFFSET'] + 
                '&limit=' + rootGetters['query/LIMIT']);
            commit("SET_CATALOG_ITEMS", response.data);
        } catch (e) {
            console.log(e);
            commit("notification/ADD_MESSAGE", {name: "Не возможно загрузить каталог ", icon: "error", id: '1'}, {root: true})
        }
      },

    }
  };
