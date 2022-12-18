<template lang="html">
  <div class="user-acc__content-block content-settings content-block">
    <div class="content-block__title">Ваши данные</div>
    <div class=" acc-settings">
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
        <label for="address" class="label">Адрес для доставки заказа</label>
        <div class="input__box">
          <input id="WarehouseAdress" type="text" class="input">
          <i class="icon-pen input__icon"></i>
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
          <i class="icon-pen input__icon"></i>
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
        <label for="user" class="label">БИК></label>
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

      <div class="group">
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
      // userNameActive: false,
      userName: null,
      userEmail: null,
      userPhone: null,
      userCompanyName: null,
      userUNP: null,
      userIBAN: null,
      userCompanyAdress: null,
      userBIC: null,
      userBank: null,
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
    this.userBIC = this.USER.BIC;
    this.userBank = this.USER.serving_bank;
  },

  methods: {
    ...mapMutations("auth", ["SET_ERRORS"]),
    ...mapActions("auth", ["UPDATE_USER_REQUEST"]),

    async updateUser() {
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
        errorsInData.userPhone = 'Укажите имя';
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
      
      console.log(errorsInData, Object.keys(errorsInData).length, Boolean(errorsInData));
      if (Object.keys(errorsInData).length) {
        this.SET_ERRORS(errorsInData);
      } else {
        const data = {
          email: this.userEmail,
          full_name: this.userName,
          phone_number: this.userPhone,
          company_name: this.userCompanyName,
          unp: this.userUNP,
          IBAN: this.userIBAN,
          legal_address: this.userCompanyAdress,
          serving_bank: this.userBank,
          BIC: this.userBIC,
          id: this.USER.id,
        };
        await this.UPDATE_USER_REQUEST(data);
        this.$router.push({name: "user-cab"});
      }
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
}

.input__box {
  .disabled {
    display: none;
  }
}

</style>
