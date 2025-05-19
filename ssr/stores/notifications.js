import { ref } from 'vue';
import { defineStore } from 'pinia';

export const useNotificationsStore = defineStore ('notificationsStore', () => {
  const messages = ref([]);
  const isLoading = ref(false);

  const addMessage = (msg) => {
    messages.value.unshift(msg);
  };

  const deleteMessage = () => {
    messages.value.pop();
  };

  const setIsLoading = (type) => {
    isLoading.value = type; 
  }

  return {
    messages,
    isLoading,
    addMessage,    
    deleteMessage,
    setIsLoading,
  }
});
