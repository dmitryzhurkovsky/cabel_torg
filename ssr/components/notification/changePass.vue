<template>
  <div class="content__popup">
      <h3>Смена пароля</h3>
      <div class="">
          <div class="group">
              <label class="label">Новый пароль</label>
              <input type="password" class="input" :class="{ 'is-invalid': authErrors.password }" v-model="password" autocomplete=off>
              <div class="error-message" v-if="authErrors.password"> {{ authErrors.password }} </div>
          </div>
          <div class="group">
              <label class="label">Введите новый пароль еще раз</label>
              <input type="password" class="input" :class="{ 'is-invalid': authErrors.confirm }" v-model="confirm" autocomplete=off>
              <div class="error-message" v-if="authErrors.password"> {{ authErrors.confirm }} </div>
          </div>

          <div class="group__row flex-center mt-20">
              <div class="center-text">
                  <button @click = "cancelRequest()" type="submit" class="btn black">Отмена</button>
              </div>

              <div class="center-text">
                  <button @click = "sendRequest()" type="submit" class="btn black">Сохранить</button>
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

  const password = ref(null);
  const confirm = ref(null);
  const isLoading = ref(false);

  const { authErrors } = storeToRefs(authStore);

  const cancelRequest = () => {
    headerStore.setIsPopUpOpen(false);
    headerStore.setPopUpAction('');
    headerStore.setPopUpAdditionalData({});
  };

  const sendRequest = async () => {
    if (isLoading.value) return;

    isLoading.value = true;
    const errorsInData = {};
    if (!password.value || password.value.length < 8) {
      errorsInData.password = 'Пароль должен быть больше 8 символов'
    }
    if (password.value !== confirm.value) {
      errorsInData.confirm = 'Пароли не совпадают'
    }
    
    if (Object.keys(errorsInData).length) {
      authStore.setErrors(errorsInData);
    } else {
      const data = {
        password: password.value,
      };
      await authStore.updateUserRequest(data);
      isLoading.value = false;
    }
    isLoading.value = false;

    if (!Object.keys(errorsInData).length) {
      headerStore.setIsPopUpOpen(true);
      headerStore.setPopUpAction('ShowCompleteMsg');
      const msg = {};
          msg.main = 'Пароль изменен';
          msg.bolt = '';
          msg.sub = ''
      headerStore.setPopUpMessage(msg);
    }
    isLoading.value = false;
  }

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
