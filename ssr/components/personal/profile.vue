<template>
  <div class="user-acc__content-block content-settings content-block">
    <div class="content-block__title">Ваши данные</div>
    <div class="acc-settings">
      <div class="group">
        <label for="user" class="label">Имя</label>
        <div class="input__box">
          <input id="name" type="text" class="input" :class="{ 'is-invalid': authErrors.userName }" v-model="userName" autocomplete=off>
          <i class="icon-pen input__icon"></i>
          <div class="error-message" v-if="authErrors.userName"> {{ authErrors.userName }} </div>
        </div>
      </div>
      <div class="group__row flex-center">
        <div class="group">
          <label for="email" class="label">Электронная почта</label>
          <div class="input__box">
            <input id="email" type="email" class="input" :class="{ 'is-invalid': authErrors.userEmail }" v-model="userEmail" autocomplete=off>
            <i class="icon-pen input__icon"></i>
            <div class="error-message" v-if="authErrors.userEmail"> {{ authErrors.userEmail }} </div>
          </div>
        </div>
        <div class="group">
          <label for="phone" class="label">Номер телефона</label>
          <div class="input__box">
            <input id="phone" type="phone" class="input" :class="{ 'is-invalid': authErrors.userPhone }" v-model="userPhone" autocomplete=off>
            <i class="icon-pen input__icon"></i>
            <div class="error-message" v-if="authErrors.userPhone"> {{ authErrors.userPhone }} </div>
          </div>
        </div>
      </div>
      <div class="group">
        <label for="deliveryAddress" class="label">Адрес для доставки заказа</label>
        <div class="input__box">
          <input id="deliveryAddress" type="text" class="input" :class="{ 'is-invalid': authErrors.userDeliveryAdress }" v-model = "userDeliveryAdress" autocomplete=off>
          <i class="icon-pen input__icon"></i>
          <div class="error-message" v-if="authErrors.userDeliveryAdress"> {{ authErrors.userDeliveryAdress }} </div>
        </div>
      </div>

      <div class="group__row flex-center">
        <div class="group">
          <label for="pass" class="label">Пароль</label>
          <div class="input__box">
            <input id="pass" type="password" class="input" data-type="password" disabled>
            <i class="icon-visible input__icon"></i>
          </div>
        </div>
        <div class="popup__link foot-lnk" @click="onPasswordChange">Изменить пароль</div>
      </div>

      <div class="group">
        <label for="user" class="label">Название компании</label>
        <div class="input__box">
          <input id="companyName" type="text" class="input"  :class="{ 'is-invalid': authErrors.userCompanyName }" v-model="userCompanyName" autocomplete=off>
          <i class="icon-pen input__icon"></i>
          <div class="error-message" v-if="authErrors.userCompanyName"> {{ authErrors.userCompanyName }} </div>
        </div>
      </div>

      <div class="group">
        <label for="user" class="label">УНП</label>
        <div class="input__box">
          <input id="UNP" type="text" class="input"  :class="{ 'is-invalid': authErrors.userUNP }" v-model = "userUNP" autocomplete=off>
          <i class="icon-pen input__icon"></i>
          <div class="error-message" v-if="authErrors.userUNP"> {{ authErrors.userUNP }} </div>
        </div>
      </div>

      <div class="group">
        <label for="user" class="label">Расчетный счет IBAN</label>
        <div class="input__box">
          <input id="IBAN" type="text" class="input"  :class="{ 'is-invalid': authErrors.userIBAN }" v-model = "userIBAN" autocomplete=off>
          <div id="anim" class="icon_info input__icon">
              <div class="tooltip flex-center" data-tooltip="Новые счета IBAN записываются в таком формате: ААВВ СССС DDDD ЕЕЕЕ ЕЕЕЕ ЕЕЕЕ ЕЕЕЕ.">!</div>
          </div>

          <div class="error-message" v-if="authErrors.userIBAN"> {{ authErrors.userIBAN }} </div>
        </div>
      </div>

      <div class="group">
        <label for="user" class="label">Юридический адрес</label>
        <div class="input__box">
          <input id="companyAdress" type="text" class="input" :class="{ 'is-invalid': authErrors.userCompanyAdress }" v-model = "userCompanyAdress" autocomplete=off>
          <i class="icon-pen input__icon"></i>
          <div class="error-message" v-if="authErrors.userCompanyAdress"> {{ authErrors.userCompanyAdress }} </div>
        </div>
      </div>

      <div class="group">
        <label for="user" class="label">БИК</label>
        <div class="input__box">
          <input id="BIC" type="text" class="input" :class="{ 'is-invalid': authErrors.userBIC }" v-model = "userBIC" autocomplete=off>
          <i class="icon-pen input__icon"></i>
          <div class="error-message" v-if="authErrors.userBIC"> {{ authErrors.userBIC }} </div>
        </div>
      </div>

      <div class="group">
        <label for="user" class="label">Обслуживающий банк</label>
        <div class="input__box">
          <input id="bank" type="text" class="input" :class="{ 'is-invalid': authErrors.userBank }" v-model = "userBank"  autocomplete=off>
          <i class="icon-pen input__icon"></i>
          <div class="error-message" v-if="authErrors.userBank"> {{ authErrors.userBank }} </div>
        </div>
      </div>

      <div class="group mt-20">
        <button type="submit" class="btn black" @click = "updateUser">Сохранить изменения</button>
      </div>

    </div>
  </div>
</template>

<script setup>
  import { ref, onBeforeMount } from 'vue';
  import { useAuthStore } from '@/stores/auth';
  import { useHeaderStore } from '@/stores/header';

  const authStore = useAuthStore();
  const headerStore = useHeaderStore();

  const { userData, authErrors } = storeToRefs(authStore);

  const userName = ref(null);
  const userEmail = ref(null);
  const userPhone = ref(null);
  const userCompanyName = ref(null);
  const userUNP = ref(null);
  const userIBAN = ref(null);
  const userCompanyAdress = ref(null);
  const userDeliveryAdress = ref(null);
  const userBIC = ref(null);
  const userBank = ref(null);
  const isLoading = ref(false);

  onBeforeMount(() => {
    userName.value = userData.value.full_name;
    userEmail.value = userData.value.email;
    userPhone.value = userData.value.phone_number;
    userCompanyName.value = userData.value.company_name;
    userUNP.value = userData.value.unp;
    userIBAN.value = userData.value.IBAN;
    userCompanyAdress.value = userData.value.legal_address;
    userDeliveryAdress.value = userData.value.delivery_address;
    userBIC.value = userData.value.BIC;
    userBank.value = userData.value.serving_bank;
  });

  const onPasswordChange = () => {
    headerStore.setIsPopUpOpen(true);
    headerStore.setPopUpAction('ChangePassword');
  };

  const updateUser = async () => {
    if (isLoading.value) return;

    isLoading.value = true;
    const errorsInData = {};
    if (!userEmail.value || !isValidEmail(userEmail.value)) {
      errorsInData.userEmail = 'Укажите валидный адрес эл. почты';
    }
    // if (!this.password || this.password.length < 8) {
    //   errorsInData.password = 'Пароль должен быть больше 8 символов'
    // }
    // if (this.password !== this.confirm) {
    //   errorsInData.confirm = 'Пароли не совпадают'
    // }
    if (!userName.value) {
      errorsInData.userName = 'Укажите имя';
    }
    if (!userPhone.value) {
      errorsInData.userPhone = 'Укажите телефон';
    }
    if (!userBank.value) {
      errorsInData.userBank = 'Укажите название банка';
    }
    if (!userCompanyName.value) {
      errorsInData.userCompanyName = 'Укажите наименование компании';
    }
    if (!userUNP.value || userUNP.value.toString().length !== 9) {
      errorsInData.userUNP = 'Укажите валидное УНП';
    }
    if (!userIBAN.value || userIBAN.value.toString().length !== 28) {
      errorsInData.userIBAN = 'Укажите валидный IBAN счет';
    }
    if (!userBIC.value || userBIC.value.toString().length < 6) {
      errorsInData.userBIC = 'Укажите валидный BIC банка';
    }
    if (!userCompanyAdress.value) {
      errorsInData.userCompanyAdress = 'Укажите юридический адрес';
    }
    if (!userDeliveryAdress.value) {
      errorsInData.userDeliveryAdress = 'Укажите адрес доставки';
    }
    
    // console.log(errorsInData, Object.keys(errorsInData).length, Boolean(errorsInData));
    if (Object.keys(errorsInData).length) {
      authStore.setErrors(errorsInData)
    } else {
      const data = {
        email: userEmail.value,
        full_name: userName.value,
        phone_number: userPhone.value,
        company_name: userCompanyName.value,
        unp: userUNP.value,
        legal_address: userCompanyAdress.value,
        delivery_address: userDeliveryAdress.value,
        IBAN: userIBAN.value,
        BIC: userBIC.value,
        serving_bank: userBank.value,
      };
      await authStore.updateUserRequest(data);
      isLoading.value = false;
      // this.$router.push({name: "user-cab"});
    }
    isLoading.value = false;
  };

  const isValidEmail = (email) => {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
  };
</script>

<style lang="scss" scoped>
.content-block{

  &__title{
    font-weight: 500;
    font-size: 20px;
    line-height: 24px;
    color: #423E48;
    margin-bottom: 40px;
  }
}
.is-invalid{
    border: 1px solid rgba(255, 99, 71, 0.9);
  }
  .error-message {
    color: rgba(255, 99, 71, 0.9);
  }

.content-settings{
  button{
    text-align: center;
  }
  .foot-lnk{
    font-size: 12px;
    text-align: center;
    text-decoration-line: underline;
    opacity: 0.6;
    width: 150px;
    &:hover{
      cursor: pointer;
      opacity: 1;
    }
  }
  .acc-settings .group{
      margin-bottom: 10px;
  }
  .acc-settings .group__row .group{
    width: 100%;
  }
  }
 .input__box {
  .disabled {
    display: none;
  }
  .icon_info{
    right: 3px;
    top: 6px;
  }
}
// tooltip style

.tooltip {
  position: relative;
  border: 2px solid #8c8b8e;
  //padding: 5px 12px;
  width: 20px;
  height: 20px;
  margin: 5px;
  color: #8c8b8e;
  font-weight: 600;
  font-size: 15px;
  border-radius: 50%;
  opacity: 0.5;
  padding-top: 2px;
  justify-content: center;
}

.tooltip:before,
.tooltip:after {
  position: absolute;
  content: '';
  opacity: 0;
  transition: all 0.4s ease;
}

.tooltip:before {
  border-width: 10px 8px 0 8px;
  border-style: solid;
  border-color:#423E48 transparent transparent transparent;
  top: -15px;
  transform: translateY(20px);
}

.tooltip:after {
  content: attr(data-tooltip);
  background: #423E48;
  border: 1px solid #423E48;
  color: #fff;
  width: 330px;
  height: 40px;
  font-size: 12px;
  line-height: 1.3;
  font-weight: 300;
  top: -50px;
  right: 0;

  padding: 5px 10px;
  border: 1px solid #423E48;
  border-radius: 5px;
  transform: translateY(20px);
}

.tooltip:hover::before,
.tooltip:hover::after {
  opacity: 1;
  transform: translateY(-2px);
}

@keyframes shake {
  0% {
    transform: rotate(2deg);
  }
  50% {
    transform: rotate(-3deg);
  }
  70% {
    transform: rotate(3deg);
  }

  100% {
    transform: rotate(0deg);
  }
}

#anim:hover {
  animation: shake 500ms ease-in-out forwards;
}
</style>
