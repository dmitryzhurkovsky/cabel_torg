<template lang="html">
  <div class="user-acc__content-block content-settings content-block">
    <div class="content-block__title">Ваши данные</div>
    <div class="acc-settings">
      <div class="group">
        <label for="user" class="label">Имя</label>
        <div class="input__box">
          <input id="name" type="text" class="input" :class="{ 'is-invalid': ERRORS.userName }" v-model="userName" autocomplete=off>
          <i class="icon-pen input__icon"></i>
          <div class="error-message" v-if="ERRORS.userName"> {{ ERRORS.userName }} </div>
        </div>
      </div>
      <div class="group__row flex-center">
        <div class="group">
          <label for="email" class="label">Электронная почта</label>
          <div class="input__box">
            <input id="email" type="email" class="input" :class="{ 'is-invalid': ERRORS.userEmail }" v-model="userEmail" autocomplete=off>
            <i class="icon-pen input__icon"></i>
            <div class="error-message" v-if="ERRORS.userEmail"> {{ ERRORS.userEmail }} </div>
          </div>
        </div>
        <div class="group">
          <label for="phone" class="label">Номер телефона</label>
          <div class="input__box">
            <input id="phone" type="phone" class="input" :class="{ 'is-invalid': ERRORS.userPhone }" v-model="userPhone" autocomplete=off>
            <i class="icon-pen input__icon"></i>
            <div class="error-message" v-if="ERRORS.userPhone"> {{ ERRORS.userPhone }} </div>
          </div>
        </div>
      </div>
      <div class="group">
        <label for="deliveryAddress" class="label">Адрес для доставки заказа</label>
        <div class="input__box">
          <input id="deliveryAddress" type="text" class="input" :class="{ 'is-invalid': ERRORS.userDeliveryAdress }" v-model = "userDeliveryAdress" autocomplete=off>
          <i class="icon-pen input__icon"></i>
          <div class="error-message" v-if="ERRORS.userDeliveryAdress"> {{ ERRORS.userDeliveryAdress }} </div>
        </div>
      </div>

      <!-- <div class="group__row flex-center">
        <div class="group">
          <label for="pass" class="label">Пароль</label>
          <div class="input__box">
            <input id="pass" type="password" class="input" data-type="password">
            <i class="icon-visible input__icon"></i>
          </div>
        </div>
        <div class="popup__link foot-lnk">Изменить пароль</div>
      </div> -->

      <div class="group">
        <label for="user" class="label">Название компании</label>
        <div class="input__box">
          <input id="companyName" type="text" class="input"  :class="{ 'is-invalid': ERRORS.userCompanyName }" v-model="userCompanyName" autocomplete=off>
          <i class="icon-pen input__icon"></i>
          <div class="error-message" v-if="ERRORS.userCompanyName"> {{ ERRORS.userCompanyName }} </div>
        </div>
      </div>

      <div class="group">
        <label for="user" class="label">УНП</label>
        <div class="input__box">
          <input id="UNP" type="text" class="input"  :class="{ 'is-invalid': ERRORS.userUNP }" v-model = "userUNP" autocomplete=off>
          <i class="icon-pen input__icon"></i>
          <div class="error-message" v-if="ERRORS.userUNP"> {{ ERRORS.userUNP }} </div>
        </div>
      </div>

      <div class="group">
        <label for="user" class="label">Расчетный счет IBAN</label>
        <div class="input__box">
          <input id="IBAN" type="text" class="input" :class="{ 'is-invalid': ERRORS.userIBAN }" v-model = "userIBAN" autocomplete=off>
<!--          <i class="icon-pen input__icon"></i>-->
          <div id="anim" class="icon_info input__icon">
              <div class="tooltip flex-center" data-tooltip="Новые счета IBAN записываются в таком формате: ААВВ ССС DDDD ЕЕЕЕ ЕЕЕЕ ЕЕЕЕ ЕЕЕЕ.">!</div>
          </div>

          <div class="error-message" v-if="ERRORS.userIBAN"> {{ ERRORS.userIBAN }} </div>
        </div>
      </div>

      <div class="group">
        <label for="user" class="label">Юридический адрес</label>
        <div class="input__box">
          <input id="companyAdress" type="text" class="input" :class="{ 'is-invalid': ERRORS.userCompanyAdress }" v-model = "userCompanyAdress" autocomplete=off>
          <i class="icon-pen input__icon"></i>
          <div class="error-message" v-if="ERRORS.userCompanyAdress"> {{ ERRORS.userCompanyAdress }} </div>
        </div>
      </div>

      <div class="group">
        <label for="user" class="label">БИК</label>
        <div class="input__box">
          <input id="BIC" type="text" class="input" :class="{ 'is-invalid': ERRORS.userBIC }" v-model = "userBIC" autocomplete=off>
          <i class="icon-pen input__icon"></i>
          <div class="error-message" v-if="ERRORS.userBIC"> {{ ERRORS.userBIC }} </div>
        </div>
      </div>

      <div class="group">
        <label for="user" class="label">Обслуживающий банк</label>
        <div class="input__box">
          <input id="bank" type="text" class="input" :class="{ 'is-invalid': ERRORS.userBank }" v-model = "userBank"  autocomplete=off>
          <i class="icon-pen input__icon"></i>
          <div class="error-message" v-if="ERRORS.userBank"> {{ ERRORS.userBank }} </div>
        </div>
      </div>

      <div class="group mt-20">
        <button type="submit" class="btn black" @click = "updateUser">Сохранить изменения</button>
      </div>

    </div>
  </div>
</template>

<script>

import { mapGetters, mapActions, mapMutations } from "vuex";

export default {
  name: "profile",

  data: function() {
    return {
      userName: null,
      userEmail: null,
      userPhone: null,
      userCompanyName: null,
      userUNP: null,
      userIBAN: null,
      userCompanyAdress: null,
      userDeliveryAdress: null,
      userBIC: null,
      userBank: null,
      isLoading: false,
    }
  },

  computed: {
    ...mapGetters("auth",["ERRORS", "USER"]),
  },

  async mounted() {
    this.userName = this.USER.full_name;
    this.userEmail = this.USER.email;
    this.userPhone = this.USER.phone_number;
    this.userCompanyName = this.USER.company_name;
    this.userUNP = this.USER.unp;
    this.userIBAN = this.USER.IBAN;
    this.userCompanyAdress = this.USER.legal_address;
    this.userDeliveryAdress = this.USER.delivery_address;
    this.userBIC = this.USER.BIC;
    this.userBank = this.USER.serving_bank;
  },

  methods: {
    ...mapMutations("auth", ["SET_ERRORS"]),
    // ...mapMutations("notification", ["ADD_MESSAGE"]),
    ...mapActions("auth", ["UPDATE_USER_REQUEST"]),

    async updateUser() {
      if (this.isLoading) return;

      this.isLoading = true;
      const errorsInData = {};
      if (!this.userEmail || !this.isValidEmail(this.userEmail)) {
        errorsInData.userEmail = 'Укажите валидный адрес эл. почты'
      }
      // if (!this.password || this.password.length < 8) {
      //   errorsInData.password = 'Пароль должен быть больше 8 символов'
      // }
      // if (this.password !== this.confirm) {
      //   errorsInData.confirm = 'Пароли не совпадают'
      // }
      if (!this.userName) {
        errorsInData.userName = 'Укажите имя';
      }
      if (!this.userPhone) {
        errorsInData.userPhone = 'Укажите телефон';
      }
      if (!this.userBank) {
        errorsInData.userBank = 'Укажите название банка';
      }
      if (!this.userCompanyName) {
        errorsInData.userCompanyName = 'Укажите наименование компании';
      }
      if (!this.userUNP || this.userUNP.toString().length !== 9) {
        errorsInData.userUNP = 'Укажите валидное УНП';
      }
      if (!this.userIBAN || this.userIBAN.toString().length !== 28) {
        errorsInData.userIBAN = 'Укажите валидный IBAN счет';
      }
      if (!this.userBIC || this.userBIC.toString().length < 6) {
        errorsInData.userBIC = 'Укажите валидный BIC банка';
      }
      if (!this.userCompanyAdress) {
        errorsInData.userCompanyAdress = 'Укажите юридический адрес';
      }
      if (!this.userDeliveryAdress) {
        errorsInData.userDeliveryAdress = 'Укажите адрес доставки';
      }
      
      // console.log(errorsInData, Object.keys(errorsInData).length, Boolean(errorsInData));
      if (Object.keys(errorsInData).length) {
        this.SET_ERRORS(errorsInData);
      } else {
        const data = {
          email: this.userEmail,
          full_name: this.userName,
          phone_number: this.userPhone,
          company_name: this.userCompanyName,
          unp: this.userUNP,
          legal_address: this.userCompanyAdress,
          delivery_address: this.userDeliveryAdress,
          IBAN: this.userIBAN,
          BIC: this.userBIC,
          serving_bank: this.userBank,
        };
        await this.UPDATE_USER_REQUEST(data);
        this.isLoading = false;
        // this.$router.push({name: "user-cab"});
      }
      this.isLoading = false;

    },

    isValidEmail: function (email) {
      const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return re.test(email);
    },

  }

}
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
