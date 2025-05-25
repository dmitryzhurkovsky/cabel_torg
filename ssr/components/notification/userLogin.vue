<template>
    <div class="content__popup">
        <div>Вход</div>
        <div class="">
            <div class="group">
                <label class="label">E-mail</label>
                <input v-if = "popUpAdditionalData"  type="text" class="input" :class="{ 'is-invalid': authErrors.email }" v-model="popUpAdditionalData.email" disabled>
                <div class="error-message" v-if="authErrors.email"> {{ authErrors.email }} </div>
            </div>
            <div class="group">
                <label class="label">Пароль</label>
                <input type="password" class="input" :class="{ 'is-invalid': authErrors.password }" v-model="password" autocomplete=off>
                <div class="error-message" v-if="authErrors.password"> {{ authErrors.password }} </div>
            </div>

            <div class="group__row flex-center mt-20">
                <div class="center-text">
                    <button @click = "cancelRequest()" type="submit" class="btn black">Отмена</button>
                </div>

                <div class="center-text">
                    <button @click = "sendLoginRequest()" type="submit" class="btn black">Войти</button>
                </div>

            </div>
        </div>
    </div>
</template>

<script setup>
  import { ref, onBeforeUnmount } from 'vue';
  import { useAuthStore } from '@/stores/auth';
  import { useHeaderStore } from '@/stores/header';

  const authStore = useAuthStore();
  const headerStore = useHeaderStore();

  const password = ref('');
  const isLoading = ref(false);

  const { userData, authErrors } = storeToRefs(authStore);
  const { popUpAdditionalData } = storeToRefs(headerStore);

  const cancelRequest = () => {
    headerStore.setIsPopUpOpen(false);
    headerStore.setPopUpAction('');
    headerStore.setPopUpAdditionalData({});
  };

  const sendLoginRequest = async () => {
    if (isLoading.value) return;

    isLoading.value = true;
    const data = new FormData();
    data.append('username', popUpAdditionalData.value.email);
    data.append('password', password.value);
    authStore.sendLoginRequest(data);

    if (userData.value) {
      headerStore.setIsPopUpOpen(true);
      headerStore.setPopUpAction('ShowCompleteMsg');
      const msg ={};
          msg.main = 'Авторизация прошла успешно';
          msg.bolt = 'Обращаем Ваше внимание, что реквизиты заказа синхронизированы с учетной записью.';
          msg.sub = 'Подтведите оформление заказа'
      headerStore.setPopUpMessage(msg);
    }
    isLoading.value = false;
  };

  onBeforeUnmount( async () => {
    authStore.setErrors({});
  });
</script>

<style lang="scss" scoped>
  .group{
    //width: 100%;
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    margin-bottom: 15px;
    text-align: center;
    justify-content: center;
  }
  input{
    width: 100%;
    background: #FFFFFF;
    border: 1px solid rgba(66, 62, 72, 0.2);
    border-radius: 8px;
    padding: 10px 16px;
  }
  .is-invalid{
    border: 1px solid #E30044;
  }
  .error-message {
    position: absolute;
    left: 15px;
    bottom: -4px;
    padding: 0 8px 0 8px;
    font-size: 12px;
    background-color: #fff;
    color: #E30044;

  }
</style>
