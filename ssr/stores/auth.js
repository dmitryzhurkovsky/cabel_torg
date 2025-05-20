import axios from "@/utils/api";
import { ref } from 'vue';
import { defineStore } from 'pinia';
import { useNotificationsStore } from "@/stores/notifications";
import { useOrdersStore } from "@/stores/orders";
import { useFavoritesStore } from "@/stores/favorites";
import { useCookie } from "#app";

export const useAuthStore = defineStore ('authStore', () => {

  const notificationsStore = useNotificationsStore();
  const ordersStore = useOrdersStore();
  const favoritesStore = useFavoritesStore();

  const userData = ref(null);
  const authErrors = ref({});
  const authType = ref(1);
  const redirectAfterLogin = ref('');
  const token = useCookie('authToken', {
    maxAge: 60*60*24*365
  });

  const getUserData = async () => {
  try {
        const response = await axios.get("users/mine");
        userData.value = response.data;
    }
    catch (e) {
        console.log(e);
    };
  };

  const sendLoginRequest = async (data) => {
    authErrors.value = {};
    try {
        const response = await axios.post("token", data);
        localStorage.setItem("authToken", response.data.access_token);
        localStorage.setItem("refreshToken", response.data.refresh_token);
        token.value = response.data.access_token;
        await getUserData();
        await ordersStore.mergeUserOrdersAndLocalStorage();
        await favoritesStore.mergeUserFavoritesAndLocalStorage();
    }
    catch (e) {
        console.log(e.message);
        token.value = null;
        if (e.message === 'Request failed with status code 401') {
            authErrors.value = { password: 'Неверный пароль' };
        } else if (e.message === 'Request failed with status code 404') {
            authErrors.value = { email: 'Пользователя с таким адресом не существует' };
        }
    };
  };

  const sendRegisterRequest = async (data) => {
    authErrors.value = {};
    try {
      const response = await axios.post("users", data);
      const loginData = new FormData();
      loginData.append('username', data.email);
      loginData.append('password', data.password);
      await sendLoginRequest(loginData);
    }
    catch (e) {
      console.log(e.message);
      if (e.message === 'Request failed with status code 400') {
        authErrors.value = { email: 'Такой пользователь уже существует в системе' };
      } 
    };
  };

  const updateUserRequest  = async (data) => {
    authErrors.value = {};
    try {
      const response = await axios.patch("users/mine", data);
      userData.value = response.data;
      notificationsStore.addMessage({id: 'upd', name: 'Данные профиля обновлены'});
    }
    catch (e) {
        console.log(e);
    };
  };

  const sendLogoutRequest = async () => {
    userData.value =  null;
    ordersStore.clearOrders();
    favoritesStore.clearFavorites();
    localStorage.removeItem("authToken");
    localStorage.removeItem("refreshToken");
    ordersStore.setIsApplicationOpen(false);
    redirectAfterLogin.value = '';
    token.value = null;
  };

  const sendRestorePasswordRequest = async (data) => {
    authErrors.value = {};
    try {
      authErrors.value = {};
      const response = await axios.post("users/reset_password", data);
    }
    catch (e) {
      console.log(e.message);
      if (e.message === 'Request failed with status code 404') {
        authErrors.value = {email: 'Такой пользователь не существует в системе'};
      } 
    };
  };

  const clearUserData = () => {
    userData.value = null;
    localStorage.removeItem("authToken");
    localStorage.removeItem("refreshToken");
    token.value = null
  }

  const setErrors = (errors) => {
    authErrors.value = errors;
  };

  const setAuthType = (type) => {
    authType.value = type;
  };

  const setDestination = (route) => {
    redirectAfterLogin.value = route;
  };

  return {
    userData,
    authErrors,
    authType,
    redirectAfterLogin,
    getUserData,
    sendLoginRequest,
    sendRegisterRequest,
    updateUserRequest,
    sendLogoutRequest,
    sendRestorePasswordRequest,
    clearUserData,
    setErrors,
    setAuthType,
    setDestination,
  }
});

