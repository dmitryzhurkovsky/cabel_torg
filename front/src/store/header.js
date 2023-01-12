import axios from "axios";

export default {
  namespaced: true,

  state: {
    likes: [],
    // orders: [12,23],
    // isMenuOpen: false,
    isCatalogOpen: false,
    // munuItemActive : 1,
    topCategoriesItemActive: null,
    subCategoriesItemActive: null,
    lastCategoriesItemActive: null,
    windowWidth: 1280,
    viewType: 1,
    categories: [],
  },

  getters: {
    LIKES_COUNT(state){
      return state.likes.length;
    },
    // IS_MENU_OPEN(state){
    //   return state.isMenuOpen;
    // },
    IS_CATALOG_OPEN(state){
      return state.isCatalogOpen;
    },
    // MENU_ITEM_ACTIVE(state){
    //   return state.munuItemActive;
    // },
    TOP_CATEGORIES_ITEM_ACTIVE(state){
      return state.topCategoriesItemActive;
    },
    SUB_CATEGORIES_ITEM_ACTIVE(state){
      return state.subCategoriesItemActive;
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
      for (let i = 0; i < sub.length; i++){
        state.categories.forEach(item => {
          if (item.parent_category_id == sub[i].id){
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
    // UPDATE_IS_MENU_OPEN (state, payload){
    //   state.isMenuOpen = payload;
    // },

    UPDATE_IS_CATALOG_OPEN (state, payload){
      state.isCatalogOpen = payload;
    },

    UPDATE_VIEW_PARAMETERS (state, payload){
      state.windowWidth = payload;
      if (payload > 767.98) {
        // XXXX - 768
        state.viewType = 1;
      } else if (payload > 479.98) {
        // 768 - 480
        state.viewType = 2;
      } else {
        // 480 - 0
        state.viewType = 3;
      }
    },

    SET_CURRENT_TOP_CATEGORY(state, payload){
      state.topCategoriesItemActive = payload;
    },

    SET_CURRENT_SUB_CATEGORY(state, payload){
      state.subCategoriesItemActive = payload;
    },

    UPDATE_CATEGORIES (state, payload){
      state.categories = payload;
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
