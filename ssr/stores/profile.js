import { ref } from 'vue';
import { defineStore } from 'pinia';

export const useProfileStore = defineStore ('profileStore', () => {
  const profileScreen = ref(0);
  const breadcrumb = ref(['Мои заказы', 'Избранные товары', 'Настройки аккаунта', 'Сменить пароль']);

  const changeScreen = (newscreen) => {
    profileScreen.value = newscreen;
  };

  return {
    profileScreen,
    breadcrumb,
    changeScreen,
  };
});