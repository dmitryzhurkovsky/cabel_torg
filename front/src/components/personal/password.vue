<template lang="html">
  <div class="user-acc__content-block content-settings content-block">
    <div class="content-block__title">Смена пароля</div>
    <div class=" acc-settings">
      
      <div class="group">
        <label for="user" class="label">Новый пароль</label>
        <div class="input__box">
          <input id="user" type="password" class="input" :class="{ 'is-invalid': ERRORS.password }" v-model="password" autocomplete=off>
          <i class="icon-pen input__icon"></i>
          <div class="error-message" v-if="ERRORS.password"> {{ ERRORS.password }} </div>
        </div>
      </div>
      
      <div class="group">
        <label for="email" class="label">Подтверждение пароля</label>
        <div class="input__box">
          <input id="email" type="password" class="input" :class="{ 'is-invalid': ERRORS.confirm }" v-model="confirm" autocomplete=off>
          <i class="icon-pen input__icon"></i>
          <div class="error-message" v-if="ERRORS.confirm"> {{ ERRORS.confirm }} </div>
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
  name: "password",

  data: function() {
    return {
      password: null,
      confirm: null,
      isLoading: false,
    }
  },

  computed: {
    ...mapGetters("auth",["ERRORS", "USER"]),
  },

  methods: {
    ...mapMutations("auth", ["SET_ERRORS"]),
    ...mapActions("auth", ["UPDATE_USER_REQUEST"]),

    async updateUser() {
      if (this.isLoading) return;

      this.isLoading = true;
      const errorsInData = {};
      if (!this.password || this.password.length < 8) {
        errorsInData.password = 'Пароль должен быть больше 8 символов'
      }
      if (this.password !== this.confirm) {
        errorsInData.confirm = 'Пароли не совпадают'
      }
      
      // console.log(errorsInData, Object.keys(errorsInData).length, Boolean(errorsInData));
      if (Object.keys(errorsInData).length) {
        this.SET_ERRORS(errorsInData);
      } else {
        const data = {
          password: this.password,
        };
        await this.UPDATE_USER_REQUEST(data);
        this.isLoading = false;
        // this.$router.push({name: "user-cab"});
      }
      this.isLoading = false;
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
    border: 1px solid #E30044;
  }
  .error-message {
    color: #E30044;

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
  .acc-settings{
    max-width: 400px;
  }
}

.input__box {
  .disabled {
    display: none;
  }
}

</style>
