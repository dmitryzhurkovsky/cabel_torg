import axios from "axios";

export default {
  namespaced: true,

  state: {
    likes: [],
    isCatalogOpen: false,
    topCategoriesItemActive: null,
    subCategoriesItemActive: null,
    lastCategoriesItemActive: null,
    windowWidth: 1280,
    viewType: 1,
    categories: [],
    catalog: [],
    isPopUpOpen: false,
  },

  getters: {
    LIKES_COUNT(state){
      return state.likes.length;
    },
    IS_CATALOG_OPEN(state){
      return state.isCatalogOpen;
    },
    TOP_CATEGORIES_ITEM_ACTIVE(state){
      return state.topCategoriesItemActive;
    },
    SUB_CATEGORIES_ITEM_ACTIVE(state){
      return state.subCategoriesItemActive;
    },
    LAST_CATEGORIES_ITEM_ACTIVE(state){
      return state.lastCategoriesItemActive;
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
    },
    CATALOG(state) {
      return state.catalog;
    },
    IS_POP_UP_OPEN(state) {
      return state.isPopUpOpen;
    }

  },

  mutations: {
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

    SET_CURRENT_LAST_CATEGORY(state, payload){
      state.lastCategoriesItemActive = payload;
    },

    SET_ALL_CURRENT_CATEGORIES(state, payload){
      if (payload.mainCategory) state.topCategoriesItemActive = payload.mainCategory;
      if (payload.middleCategory) state.subCategoriesItemActive = payload.middleCategory;
      if (payload.lastCategory) state.subCategoriesItemActive = payload.lastCategory;
    },

    UPDATE_CATEGORIES(state, payload){
      state.categories = payload;
      if (state.categories.length > 0){
        state.topCategoriesItemActive = state.categories[0].id
      } else {
        state.topCategoriesItemActive = null;
      }
    },

    CREATE_MENU_ITEMS(state, data) {
      let menuItems = [];
      const mainLevel = data.filter(item => item.parent_category_id === null);
      let otherItems = data.filter(item => item.parent_category_id !== null);
      menuItems = [...mainLevel];
      menuItems.forEach(item => {
        item.selected = false;
        item.filterPanel = false;
        item.mobileMenu = false;
        item.childrens = [];
      });
      menuItems.forEach(mainItem => {
        const mainItemChildrens = otherItems.filter( item => item.parent_category_id === mainItem.id);
        otherItems = otherItems.filter(item => item.parent_category_id !== mainItem.id);
        mainItemChildrens.forEach(item => {
          item.selected = false;
          item.filterPanel = false;
          item.mobileMenu = false;
          item.childrens = [];
        });
        mainItemChildrens.forEach(middleItem => {
          const lastChildrens = otherItems.filter( item => item.parent_category_id === middleItem.id);
          otherItems = otherItems.filter(item => item.parent_category_id !== middleItem.id);
          lastChildrens.forEach(item => {
            item.selected = false;
            item.filterPanel = false;
            item.mobileMenu = false;
            item.childrens = [];
          });
          middleItem.childrens = [...lastChildrens];
        })
        mainItem.childrens = [...mainItemChildrens];
      });
      state.catalog = menuItems;
    },

    SET_IS_POP_UP_OPEN(state, status) {
      state.isPopUpOpen = status;
    }
  },

  actions: {
    async GET_CATEGORIES({ commit }, data){
      try {
        const response = await axios.get(process.env.VUE_APP_API_URL + 'categories/');
        commit("UPDATE_CATEGORIES", response.data);
        commit("CREATE_MENU_ITEMS", response.data);
      } catch (e) {
        console.log(e);
        commit("notification/ADD_MESSAGE", {name: "Не возможно обновить каталог товаров", icon: "error", id: '1'}, {root: true})
      }
    }
  }
};
