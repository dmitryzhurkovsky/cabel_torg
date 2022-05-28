import axios from "axios";

export default {
  namespaced: true,

  state: {
    likes: [],
    orders: [12,23],
    isMenuOpen: false,
    isCatalogOpen: false,
    munuItemActive : 1,
    topCategoriesItemActive: null,
    windowWidth: 1280,
    viewType: 1,
    categories: [],
  },

  getters: {
    LIKES_COUNT(state){
      return state.likes.length;
    },
    ORDER_COUNT(state){
      if (state.orders.length) {
          return state.orders.length;
      } else {
          return null;
      }
    },
    IS_MENU_OPEN(state){
      return state.isMenuOpen;
    },
    IS_CATALOG_OPEN(state){
      return state.isCatalogOpen;
    },
    MENU_ITEM_ACTIVE(state){
      return state.munuItemActive;
    },
    TOP_CATEGORIES_ITEM_ACTIVE(state){
      return state.topCategoriesItemActive;
    },
    VIEW_TYPE(state){
      return state.viewType;
    },
    WINDOW_WIDTH(state){
      return state.windowWidth;
    },
    TOP_CATEGORIES(state){
      const top = [];
      state.categories.forEach((item, i) => {
        if (item.parent_category_id === null) {
          top.push(item);
        }
      });
      return top;
    },
    SUB_CATEGORIES(state){
      const sub = [];
      state.categories.forEach(item => {
        if (item.parent_category_id == state.topCategoriesItemActive){
          sub.push({id : item.id, name: item.name, subItems : []});
        }
      });
      // console.log(sub);
      for (let i = 0; i < sub.length; i++){
        state.categories.forEach(item => {
          if (item.parent_category_id == sub[i].id){
            // console.log(item.parent_category_id, sub[i].id);
            sub[i].subItems.push({id : item.id, name : item.name});
          }
        });
      };
      // console.log(sub);
      return sub;
    },
    ALL_CATEGORIES(state){
      return state.categories;
    }

  },

  mutations: {
    UPDATE_IS_MENU_OPEN (state, newstate){
      state.isMenuOpen = newstate;
    },

    UPDATE_IS_CATALOG_OPEN (state, newstate){
      state.isCatalogOpen = newstate;
    },

    UPDATE_VIEW_PARAMETERS (state, newstate){
      state.windowWidth = newstate;
      // console.log(newstate);
      if (newstate > 480) {
        // XXXX - 480
        state.viewType = 1;
      } else if (newstate > 320) {
        // 480 - 380
        state.viewType = 2;
      } else {
        // 320 - 0
        state.viewType = 3;
      }
    },

    SET_CURRENT_TOP_CATEGORY(state, newstate){
      state.topCategoriesItemActive = newstate;
    },

    UPDATE_CATEGORIES (state, newstate){
      state.categories = newstate;
      if (state.categories.length > 0){
        state.topCategoriesItemActive = state.categories[0].id
      } else {
        state.topCategoriesItemActive = null;
      }
    },
  },

  actions: {
    async GET_CATEGORIES({ commit }, data){
      try {
        const response = await axios.get(process.env.VUE_APP_API_URL + 'categories/');
        commit("UPDATE_CATEGORIES", response.data);
      } catch (e) {
        console.log(e);
        commit("notification/ADD_MESSAGE", {name: "Не возможно обновить каталог товаров", icon: "error", id: '1'}, {root: true})
      }
    }
  }
};
