import axios from "axios";

export default {
  namespaced: true,

  state: {
    likes: [],
    orders: [12,23],
    isMenuOpen: false,
    isCatalogOpen: false,
    munuItemActive : 1,
    catalogItemActive: 1,
    windowWidth: 1280,
    viewType: 1,
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
    CATALOG_ITEM_ACTIVE(state){
      return state.catalogItemActive;
    },
    VIEW_TYPE(state){
      return state.viewType;
    },
    WINDOW_WIDTH(state){
      return state.windowWidth;
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
    }
  },

  actions: {
  }
};
