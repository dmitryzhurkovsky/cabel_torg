import axios from "@/utils/api";
import { ref } from 'vue';
import { defineStore } from 'pinia';
import { useNotificationsStore } from "@/stores/notifications";

export const useMainStore = defineStore ('mainStore', () => {

  const notificationsStore = useNotificationsStore();

  const settings = ref([]);
  const news = ref([]);
  const partners = ref([]);
  const banners = ref([]);

  const getSettings = async () => {
    try {
      const response = await axios.get('service_entities/vendor_info/1');
      settings.value = response.data;
    } catch (e) {
      console.log(e);
      // notificationsStore.addMessage(
      //   {name: "Не возможно обновить настройки " + e, icon: "error", id: '1'}
      // )
    }
  };

  const getNews = async () => {
    try {
      const response = await axios.get('service_entities/articles');
      if (response && response.data) {
        news.value = response?.data?.length ? response?.data?.sort( (a, b) => Number(b.id) - Number(a.id)): [];
        return news.value;
      } else {
        return [];
      }
    } catch (e) {
      console.log(e);
    }
  };


  const getPartners = async () => {
    try {
      const response = await axios.get('service_entities/partners');
      partners.value = response.data;
    } catch (e) {
      console.log(e);
    }
  };

  const getBanners = async () => {
    try {
      const response = await axios.get('service_entities/banners');
      banners.value = response.data;
    } catch (e) {
      console.log(e);
    }
  };

  return {
    settings,
    news,
    partners,
    banners,
    getSettings,
    getNews,
    getPartners,
    getBanners,
  }
});
