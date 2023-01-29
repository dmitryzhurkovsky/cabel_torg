export default {
  namespaced: true,

  state: {
    stack : [
      {
          name: 'Главная',
          path: '/',
          type: 'global',
          class: '',
      },
    ],
  },

  getters: {
    STACK(state) {
      return state.stack
    },
  },

  mutations: {
    ADD_BREADCRUMB(state, breadCrumb) {
      state.stack.push(breadCrumb);
    },

    DELETE_BREADCRUMB(state) {
      state.stack.splice(state.stack.length - 1, 1);
    },

    RENAME_LAST_BREADCRUMB(state, breadCrumb) {
      if (state.stack.length - 1){
        state.stack[state.stack.length - 1].name = breadCrumb;
      }
    },

    RESET_ALL_BREADCRUMBS(state, breadCrumbs) {
      const main = {
        name: 'Главная',
        path: '/',
        type: 'global',
        class: '',
      };
      state.stack = [main, ...breadCrumbs];
    }
  },

  actions: {
    CHANGE_BREADCRUMB({ commit, getters }, id) {
      while (getters.STACK.length > id + 1){
        commit("DELETE_BREADCRUMB");
      }
    },

    MOVE_TO_SELECT_PATH({ commit, dispatch, getters }, element) {
      const elementData = getters.STACK[element];
      // commit("query/SET_SEARCH_STRING", '', {root: true});
      if (elementData.type === 'global') {
        dispatch("CHANGE_BREADCRUMB", element);
      } else {
        const route = getters.STACK[element];
        if (route.level === 'root') {
            dispatch("CHANGE_BREADCRUMB", element);
            dispatch("header/SET_ALL_CURRENT_CATEGORIES", {}, {root: true});
            commit("query/SET_CATEGORY_ID", null, {root: true});
        } else if (route.level === 'top') {
            const data = { mainCategory: route.category};
            dispatch("header/SET_ALL_CURRENT_CATEGORIES", data, {root: true});
            commit("query/SET_CATEGORY_ID", route.category, {root: true});
        } else if (route.level === 'sub') {
            const data = { mainCategory: getters.STACK[element - 1].category, middleCategory: route.category, lastCategory: null};
            dispatch("header/SET_ALL_CURRENT_CATEGORIES", data, {root: true});
            commit("query/SET_CATEGORY_ID", route.category, {root: true});
        } else if (route === 'last') {
            const data = { mainCategory: getters.STACK[element - 2].category, middleCategory: getters.STACK[element - 1].category, lastCategory: route.category};
            dispatch("header/SET_ALL_CURRENT_CATEGORIES", data, {root: true});
            commit("query/SET_CATEGORY_ID", route.category, {root: true});
        }
      }
    },
  },
}
