<template>
    <div class="content__popup">
        <div v-if = "popUpAdditionalData?.cardID" class="mb-20">Узнать о поступлении</div>
        <div v-else class="section_title mb-20">Заказать звонок</div>
        <div class="">
            <div class="group">
                <label class="label">Ваше имя</label>
                <input type="text" class="input" :class="{ 'is-invalid': authErrors.name }" v-model="name">
                <div class="error-message" v-if="authErrors.name"> {{ authErrors.name }} </div>
            </div>
            <div class="group">
                <label class="label">Контактный телефон</label>
                <input type="text" class="input" :class="{ 'is-invalid': authErrors.phone }" v-model="phone">
                <div class="error-message" v-if="authErrors.phone"> {{ authErrors.phone }} </div>
            </div>

            <div class="group__row flex-center mt-20">
                <div class="center-text">
                    <button @click = "cancelRequest()" type="submit" class="btn black">Отмена</button>
                </div>

                <div class="center-text">
                    <button @click = "sendRequest()" type="submit" class="btn black">Заказать звонок</button>
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

  const name = ref('');
  const phone = ref('');
  const isLoading = ref(false);

  const { authErrors } = storeToRefs(authStore);
  const { requestCallType, popUpAdditionalData } = storeToRefs(headerStore);

  const cancelRequest = () => {
    headerStore.setIsPopUpOpen(false)
    headerStore.setPopUpAction('');
    headerStore.setPopUpAdditionalData({});
  };

  const sendRequest = async () => {
    if (isLoading.value) return;

    isLoading.value = true;
    const errorsInData = {};
    authStore.setErrors(errorsInData);

    if (!name.value) {
      errorsInData.name = 'Укажите валидное имя'
    }
    if (!phone.value) {
      errorsInData.phone = 'Укажите номер телефона'
    }
    if (Object.keys(errorsInData).length) {
      authStore.setErrors(errorsInData);
    } else {
      const data = {
          fullname: name.value,
          phone_number: phone.value,
          type: requestCallType.value,
          product_id: Number(popUpAdditionalData.value.cardID),
      };
      // Тут посылаем на бэк запрос и ждем ответа, по результатам фомируем окно с ответом
      await headerStore.sendRequestCall(data);
      headerStore.setPopUpAdditionalData({});
      headerStore.setRequestCallType('');
    }
    isLoading.value = false;
  };

  onBeforeUnmount( async () =>{
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
  .content__popup .btn{
      min-width: auto;
  }
</style>
