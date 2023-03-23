import axios from "axios";

const mainBreadCrumb = {
  name: 'Каталог',
  path: '/catalog',
  type: 'global',
  class: '',
  category: 1,
  level: 'root',
}

export default {
  namespaced: true,

  state: {
    likes: [],
    isCatalogOpen: false,
    topCategoriesItemActive: 1,
    subCategoriesItemActive: null,
    lastCategoriesItemActive: null,
    windowWidth: 1280,
    viewType: 1,
    categories: [],
    catalog: [],
    isPopUpOpen: false,
    popUpAction: '',
    popUpMessage: null,
    requestCallType: 'U',
    popUpAdditionalData: {},
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
    DEVICE_VIEW_TYPE(state){
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
    IS_POPUP_OPEN(state) {
      return state.isPopUpOpen;
    },
    POPUP_ACTION(state) {
      return state.popUpAction;
    },
    POPUP_MESSAGE(state) {
      return state.popUpMessage;
    },
    REQUEST_CALL_TYPE(state) {
      return state.requestCallType;
    },
    POPUP_ADDITONAL_DATA(state) {
      return state.popUpAdditionalData;
    }
  },

  mutations: {
    UPDATE_IS_CATALOG_OPEN (state, catalogSatae){
      state.isCatalogOpen = catalogSatae;
    },

    UPDATE_VIEW_PARAMETERS (state, width){
      state.windowWidth = width;
      if (width > 767.98) {
        // XXXX - 768
        state.viewType = 1;
      } else if (width > 479.98) {
        // 768 - 480
        state.viewType = 2;
      } else {
        // 480 - 0
        state.viewType = 3;
      }
    },

    SET_CURRENT_TOP_CATEGORY(state, id){
      state.topCategoriesItemActive = id;
    },

    SET_CURRENT_SUB_CATEGORY(state, id){
      state.subCategoriesItemActive = id;
    },

    SET_CURRENT_LAST_CATEGORY(state, id){
      state.lastCategoriesItemActive = id;
    },

    UPDATE_CATEGORIES(state, categories){
      state.categories = categories;
      if (state.categories.length > 0){
        state.topCategoriesItemActive = state.categories[0].id
      } else {
        state.topCategoriesItemActive = null;
      }
    },

    CREATE_MENU_ITEMS(state, categories) {
      let menuItems = [];
      const mainLevel = categories.filter(item => item.parent_category_id === null);
      let otherItems = categories.filter(item => item.parent_category_id !== null);
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

    SET_IS_POPUP_OPEN(state, status) {
      state.isPopUpOpen = status;
    },

    SET_POPUP_ACTION(state, action) {
      state.popUpAction = action;
    },

    SET_POPUP_MESSAGE(state, msg) {
      state.popUpMessage = {...msg};
    },

    SET_REQUEST_CALL_TYPE(state, type) {
      state.requestCallType = type;
    },

    SET_POPUP_ADDITIONAL_DATA(state, data) {
      state.popUpAdditionalData = data;
    }
  },

  actions: {
    async GET_CATEGORIES({ commit }){
      try {
        const response = await axios.get(process.env.VUE_APP_API_URL + 'categories/');
        commit("UPDATE_CATEGORIES", response.data);
        commit("CREATE_MENU_ITEMS", response.data);
      } catch (e) {
        console.log(e);
        commit("notification/ADD_MESSAGE", {name: "Не возможно обновить каталог товаров", icon: "error", id: '1'}, {root: true})
      }
    },

    SET_ALL_CURRENT_CATEGORIES({ commit, getters }, categoryState){
      const { mainCategory, middleCategory, lastCategory } = categoryState;
      // console.log(categoryState);
      const breadCrumbs = [ mainBreadCrumb ];
      if (mainCategory) {
        commit("SET_CURRENT_TOP_CATEGORY", mainCategory);
        const currCategory = getters.ALL_CATEGORIES.filter(item => item.id === mainCategory)[0];
        const currBreadCrumb  = {
          name: currCategory.name,
          path: '/category/' + currCategory.id,
          type: 'global',
          class: '',
          category: currCategory.id,
          level: 'top',
        };
        breadCrumbs.push(currBreadCrumb);
      } else {
        commit("SET_CURRENT_TOP_CATEGORY", null);
      }
      if (middleCategory) {
        commit("SET_CURRENT_SUB_CATEGORY", middleCategory);
        const currCategory = getters.ALL_CATEGORIES.filter(item => item.id === middleCategory)[0];
        const currBreadCrumb  = {
          name: currCategory.name,
          path: '/category/' + currCategory.id,
          type: 'global',
          class: '',
          category: currCategory.id,
          level: 'sub',
        };
        breadCrumbs.push(currBreadCrumb);
      } else {
        commit("SET_CURRENT_SUB_CATEGORY", null);
      }
      if (lastCategory) {
        commit("SET_CURRENT_LAST_CATEGORY", lastCategory);
        const currCategory = getters.ALL_CATEGORIES.filter(item => item.id === lastCategory)[0]
        const currBreadCrumb  = {
          name: currCategory.name,
          path: '/category/' + currCategory.id,
          type: 'global',
          class: '',
          category: currCategory.id,
          level: 'last',
        };
        breadCrumbs.push(currBreadCrumb);
      } else {
        commit("SET_CURRENT_LAST_CATEGORY", null);
      }
      commit("breadcrumb/RESET_ALL_BREADCRUMBS", breadCrumbs, {root: true});
    },

    async SEND_REQUEST_CALL({ commit }, data){
      try {
        await axios.post(process.env.VUE_APP_API_URL + 'service_entities/request_calls', data);
        commit("SET_POPUP_ACTION", 'ShowCompleteMsg');
        const msg ={};
        msg.main = 'Наш менеджер свяжется с вами в ближайшее время.';
        msg.bolt = 'Время работы:';
        msg.sub = ' Пн-Пт - 9:00 - 17:00'
        commit("SET_POPUP_MESSAGE", msg);
      } catch (e) {
        console.log(e);
        commit("notification/ADD_MESSAGE", {name: "Не возможно обновить каталог товаров", icon: "error", id: '1'}, {root: true})
        commit("SET_POPUP_MESSAGE", {});
        commit("SET_IS_POPUP_OPEN", false);
        commit("SET_POPUP_ACTION", '');
      }
    },

    async SEND_REQUEST_FEEDBACK({ commit }, data){
      try {
        await axios.post(process.env.VUE_APP_API_URL + 'service_entities/feedbacks', data);
        commit("SET_POPUP_ACTION", 'ShowCompleteMsg');
        const msg ={};
        msg.main = 'Наш менеджер свяжется с вами в ближайшее время.';
        msg.bolt = 'Время работы:';
        msg.sub = ' Пн-Пт - 9:00 - 17:00'
        commit("SET_POPUP_MESSAGE", msg);
        commit("SET_IS_POPUP_OPEN", true);
      } catch (e) {
        console.log(e);
        commit("notification/ADD_MESSAGE", {name: "Не возможно обновить каталог товаров", icon: "error", id: '1'}, {root: true})
        commit("SET_POPUP_MESSAGE", {});
        commit("SET_IS_POPUP_OPEN", false);
        commit("SET_POPUP_ACTION", '');
      }
    },
    
  }
};
