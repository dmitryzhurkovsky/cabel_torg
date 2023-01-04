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
      async GET_CATALOG_ITEMS({ commit }, data) {
        try {
            // ?category_id=12&type_of_product=all&offset=0&limit=12
            const response = await axios.get(process.env.VUE_APP_API_URL + 'products?category_id=' + data + '&type_of_product=all&offset=0&limit=12');
            console.log(response.data);
            commit("SET_CATALOG_ITEMS", response.data);
        } catch (e) {
            console.log(e);
            commit("notification/ADD_MESSAGE", {name: "Не возможно загрузить каталог ", icon: "error", id: '1'}, {root: true})
        }
      },
    }
  };
