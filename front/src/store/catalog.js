import axios from "axios";

export default {
  namespaced: true,

  state: {
    itemsList: [],
    recomendedList: [],
    activeItem: null,
  },

    getters: {
      ITEMS_LIST(state){
        return state.itemsList;
      },
      ACTIVE_ITEM(state){
        return state.activeItem;
      },
      RECOMENDED_ITEMS(state){
        return state.recomendedList;
      }
    },

    mutations: {
      SET_CATALOG_ITEMS(state, items) {
        state.itemsList = items;
      },

      SET_RECOMENDED_ITEMS(state, items) {
        state.recomendedList = items;
      },
    },

    actions: {
      async GET_CATALOG_ITEMS({ commit, rootGetters }, data) {
        try {
            const response = await axios.get(process.env.VUE_APP_API_URL + 
                'products?category_id=' + data + 
                '&type_of_product=' + rootGetters['query/TYPE_OF_PRODUCT'].type + 
                '&offset=' + rootGetters['query/OFFSET'] + 
                '&limit=' + rootGetters['query/LIMIT']);
            commit("SET_CATALOG_ITEMS", response.data.data);
        } catch (e) {
            console.log(e);
            commit("notification/ADD_MESSAGE", {name: "Не возможно загрузить каталог ", icon: "error", id: '1'}, {root: true})
        }
      },

      async GET_ALL_CATALOG_ITEMS({ commit, rootGetters }) {
        try {
            const response = await axios.get(process.env.VUE_APP_API_URL + 
                'products?type_of_product=' + rootGetters['query/TYPE_OF_PRODUCT'].type + 
                '&offset=' + rootGetters['query/OFFSET'] + 
                '&limit=' + rootGetters['query/LIMIT']);
            commit("SET_CATALOG_ITEMS", response.data.data);
        } catch (e) {
            console.log(e);
            commit("notification/ADD_MESSAGE", {name: "Не возможно загрузить каталог ", icon: "error", id: '1'}, {root: true})
        }
      },

      async GET_RECOMENDED_ITEMS({ commit }) {
        try {
            const response = await axios.get(process.env.VUE_APP_API_URL + 
                'products?type_of_product=all' + 
                '&offset=0' +  
                '&limit=10');
            commit("SET_RECOMENDED_ITEMS", response.data.data);
        } catch (e) {
            console.log(e);
            commit("notification/ADD_MESSAGE", {name: "Не возможно загрузить каталог ", icon: "error", id: '1'}, {root: true})
        }
      },

    }
  };
