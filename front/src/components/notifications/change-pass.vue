<template>
  <div class="content__popup">
      <h3 class="mb-20">Смена пароля</h3>
      <div class="">
          <div class="group">
              <label class="label">Новый пароль</label>
              <input type="password" class="input" :class="{ 'is-invalid': ERRORS.password }" v-model="password" autocomplete=off>
              <div class="error-message" v-if="ERRORS.password"> {{ ERRORS.password }} </div>
          </div>
          <div class="group">
              <label class="label">Введите новый пароль еще раз</label>
              <input type="password" class="input" :class="{ 'is-invalid': ERRORS.confirm }" v-model="confirm" autocomplete=off>
              <div class="error-message" v-if="ERRORS.password"> {{ ERRORS.confirm }} </div>
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

<script>

import { mapActions, mapGetters, mapMutations } from "vuex";

export default {
  name: "ChangePass",

  data: function() {
    return {
        password  : null,
        confirm  : null,
        isLoading: false,
    }
  },

  computed: {
    ...mapGetters("auth",["ERRORS", "USER"]),
    ...mapGetters("header",["REQUEST_CALL_TYPE", "POPUP_ADDITONAL_DATA"]),

  },

  async beforeUnmount() {
    this.SET_ERRORS({});
  },

  methods: {
    ...mapMutations("header", ["SET_IS_POPUP_OPEN", "SET_POPUP_ACTION", "SET_POPUP_MESSAGE", "SET_POPUP_ADDITIONAL_DATA"]),
    ...mapMutations("auth", ["SET_ERRORS",]),
    ...mapActions("auth", ["UPDATE_USER_REQUEST",]),

    cancelRequest(){
      this.SET_IS_POPUP_OPEN(false);
      this.SET_POPUP_ACTION('');
      this.SET_POPUP_ADDITIONAL_DATA({});
    },

    async sendRequest(){
      if (this.isLoading) return;

      this.isLoading = true;
      const errorsInData = {};
      if (!this.password || this.password.length < 8) {
        errorsInData.password = 'Пароль должен быть больше 8 символов'
      }
      if (this.password !== this.confirm) {
        errorsInData.confirm = 'Пароли не совпадают'
      }
      
      if (Object.keys(errorsInData).length) {
        this.SET_ERRORS(errorsInData);
      } else {
        const data = {
          password: this.password,
        };
        await this.UPDATE_USER_REQUEST(data);
        this.isLoading = false;
      }
      this.isLoading = false;

      if (!Object.keys(errorsInData).length) {
        this.SET_IS_POPUP_OPEN(true);
        this.SET_POPUP_ACTION('ShowCompleteMsg');
        const msg ={};
            msg.main = 'Пароль изменен';
            msg.bolt = '';
            msg.sub = ''
        this.SET_POPUP_MESSAGE(msg);
      }
      this.isLoading = false;
    }
  }
}
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
