import axios from "axios";

export default {
  namespaced: true,

  state: {
    partners: [],
    news: [],
  },

  getters: {
    PARTNERS(state) {
      return state.partners;
    },
    NEWS(state) {
      return state.news;
    }
  },

  mutations: {
    SET_PARTNERS(state, partners) {
      state.partners = [...partners];
    },

    SET_NEWS(state, news) {
      state.news = [...news];
    },
  },

  actions: {
    async GET_PARTNERS({ commit }){
      try {
        const response = await axios.get(process.env.VUE_APP_API_URL + 'service_entities/partners');
        commit("SET_PARTNERS", response.data);
      } catch (e) {
        console.log(e);
        commit("notification/ADD_MESSAGE", {name: "Не возможно обновить партнеров", icon: "error", id: '1'}, {root: true})
      }
    },

    async GET_NEWS({ commit }){
      try {
        const response = await axios.get(process.env.VUE_APP_API_URL + 'service_entities/articles');
        commit("SET_NEWS", response.data);
      } catch (e) {
        console.log(e);
        commit("notification/ADD_MESSAGE", {name: "Не возможно обновить новости", icon: "error", id: '1'}, {root: true})
      }
    },
  }
}