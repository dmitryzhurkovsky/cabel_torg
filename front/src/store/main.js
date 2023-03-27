import axios from "axios";

export default {
  namespaced: true,

  state: {
    partners: [],
    news: [],
    banners: [],
    settings: {},
  },

  getters: {
    PARTNERS(state) {
      return state.partners;
    },
    NEWS(state) {
      const sorted = state.news.sort( (a, b) => Number(b.id) - Number(a.id));
      // return state.news;
      return sorted;
    },
    BANNERS(state) {
      return state.banners;
    },
    SETTINGS(state) {
      return state.settings;
    }
  },

  mutations: {
    SET_PARTNERS(state, partners) {
      state.partners = [...partners];
    },

    SET_NEWS(state, news) {
      state.news = [...news];
    },

    SET_BANNERS(state, banners) {
      state.banners = [...banners];
    },

    SET_SETTINGS(state, settings) {
      state.settings = {...settings};
    }
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

    async GET_BANNERS({ commit }){
      try {
        const response = await axios.get(process.env.VUE_APP_API_URL + 'service_entities/banners');
        commit("SET_BANNERS", response.data);
      } catch (e) {
        console.log(e);
        commit("notification/ADD_MESSAGE", {name: "Не возможно обновить новости", icon: "error", id: '1'}, {root: true})
      }
    },

    async GET_SETTINGS({ commit }){
      try {
        const response = await axios.get(process.env.VUE_APP_API_URL + 'service_entities/vendor_info/1');
        commit("SET_SETTINGS", response.data);
      } catch (e) {
        console.log(e);
        commit("notification/ADD_MESSAGE", {name: "Не возможно обновить новости", icon: "error", id: '1'}, {root: true})
      }
    },
  }
}