<template lang="html">
    <div>
      <div class="_container">
        <div v-if = "AUTH_TYPE === 1" class="popup__reg full-open">
          <h3>Вход</h3>
          <div class="sign-in-htm">
            <div class="group">
              <label for="user" class="label">Электронная почта</label>
              <input type="email" class="input" :class="{ 'is-invalid': ERRORS.email }" id="email" v-model="email">
              <div class="error-message" v-if="ERRORS.email"> {{ ERRORS.email }} </div>
            </div>
            <div class="group">
              <label for="pass" class="label">Пароль</label>
              <input type="password" class="input" :class="{ 'is-invalid': ERRORS.password }" id="password" v-model="password">
              <div class="error-message" v-if="ERRORS.password"> {{ ERRORS.password }} </div>
            </div>

            <div class="center-text">
              <button @click = "userLogin()" type="submit" class="btn black">Войти</button>
            </div>

            <div @click = "changeScreen(2)" class="foot-lnk mt-20">Не помню пароль</div>
            <div @click = "changeScreen(3)" class="bottom-link mt-20">Зарегистрироваться</div>
          </div>
        </div>
        <div v-if = "AUTH_TYPE === 2" class="popup__reg full-open">
          <h3>Восстановление пароля</h3>
          <div class="reset-pass">
            <div class="group">
              <label for="user" class="label">Электронная почта</label>
              <input id="user" type="text" class="input">
            </div>
            <div class="center-text">
              <button @click = "changeScreen(4)" type="submit" class="btn black">Восстановить</button>
            </div>
            <div @click = "changeScreen(1)" class="foot-lnk mt-20">
              Войти
            </div>
            <div @click = "changeScreen(3)" class="bottom-link mt-20">
              Зарегистрироваться
            </div>
          </div>
        </div>
        <div v-if = "AUTH_TYPE === 3" class="popup__reg full-open">
          <h3>Регистрация для юрлица</h3>
          <div class="register">
            <div class="group">
              <label for="email" class="label">Электронная почта</label>
              <input id="email" type="email" class="input" :class="{ 'is-invalid': ERRORS.email }" v-model="email" autocomplete=off>
              <div class="error-message" v-if="ERRORS.email"> {{ ERRORS.email }} </div>
            </div>
            <div class="group">
              <label for="password" class="label">Пароль</label>
              <input id="password" type="password" class="input" :class="{ 'is-invalid': ERRORS.password }" v-model="password" autocomplete=off>
              <div class="error-message" v-if="ERRORS.password"> {{ ERRORS.password }} </div>
            </div>
            <div class="group">
              <label for="confirm" class="label">Подтверждение пароля</label>
              <input id="confirm" type="password" class="input" :class="{ 'is-invalid': ERRORS.confirm }" v-model="confirm" autocomplete=off>
              <div class="error-message" v-if="ERRORS.confirm"> {{ ERRORS.confirm }} </div>
            </div>
            <div class="group">
              <label for="username" class="label">Имя</label>
              <input id="username" type="text" class="input" :class="{ 'is-invalid': ERRORS.username }" v-model="username" autocomplete=off>
              <div class="error-message" v-if="ERRORS.username"> {{ ERRORS.username }} </div>
            </div>
            <div class="group">
              <label for="phone" class="label">Телефон</label>
              <input id="phone" type="tel" class="input" :class="{ 'is-invalid': ERRORS.phone }" v-model="phone" autocomplete=off>
              <div class="error-message" v-if="ERRORS.phone"> {{ ERRORS.phone }} </div>
            </div>
            <div class="group">
              <label for="company" class="label">Компания</label>
              <input id="company" type="text" class="input" :class="{ 'is-invalid': ERRORS.company }" v-model="company" autocomplete=off>
              <div class="error-message" v-if="ERRORS.company"> {{ ERRORS.company }} </div>
            </div>
            <div class="group">
              <label for="unp" class="label">УНП</label>
              <input id="unp" type="number" class="input" :class="{ 'is-invalid': ERRORS.unp }" v-model="unp" autocomplete=off>
              <div class="error-message" v-if="ERRORS.unp"> {{ ERRORS.unp }} </div>
            </div>
            <div class="">
              <button @click = "userRegister" type="submit" class="btn black">Регистрация</button>
            </div>
            <div @click = "changeScreen(1)" class="foot-lnk mb-20 mt-20">Войти</div>
<!--            <div @click = "changeScreen(2)" class="foot-lnk mt-20">Не помню пароль</div>-->
          </div>
        </div>
        <div v-if = "AUTH_TYPE === 4" class="popup__reg full-open">
          <h3>Проверьте ваш email</h3>
          <div class="reset-pass">
            <div class="group">
              <p>Мы отправили ссылку для <b>восстановления пароля</b> к вашей учетной записи.</p>
            </div>
            <div class="">
              <button @click = "changeScreen(0)" type="submit" class="btn empty">Вернуться на сайт</button>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
import { mapGetters, mapActions, mapMutations } from "vuex";
import { isValidEmail } from "../../common/validation";

export default {
  name: "UserActions",

  data: function() {
      return {
          email     : '',
          password  : '',
          confirm: '',
          username: '',
          phone: '',
          company: '',
          unp: null,
          isLoading: false,
      }
  },

  computed: {
     ...mapGetters("auth",["ERRORS", "AUTH_TYPE", "IS_OPEN_MAIN_LOGIN", "USER", "REDIRECT_AFTER_LOGIN"]),
  },

  async mounted() {
      this.SET_IS_OPEN_MAIN_LOGIN(false);
  },

  async beforeUnmount() {
      this.SET_ERRORS({});
      this.SET_IS_OPEN_MAIN_LOGIN(true);
  },

  methods: {
    ...mapActions("auth", ["SEND_LOGIN_REQUEST", "SEND_REGISTER_REQUEST", "SEND_LOGOUT_REQUEST"]),
    ...mapMutations("auth", ["SET_ERRORS", "SET_TYPE", "SET_IS_OPEN_MAIN_LOGIN"]),

    changeScreen(auth_type) {
        this.SET_TYPE(auth_type);
    },

    async userLogin() {
        if (this.isLoading) return;

        this.isLoading = true;
        const errorsInData = {};
        this.SET_ERRORS(errorsInData);

        if (!isValidEmail(this.email)) {
            errorsInData.email = 'Укажите валидный адрес эл. почты'
        }
        if (!this.password || this.password.length < 8) {
            errorsInData.password = 'Пароль должен быть больше 8 символов'
        }
        if (Object.keys(errorsInData).length) {
            this.SET_ERRORS(errorsInData);
        } else {
          const data = new FormData();
          data.append('username', this.email);
          data.append('password', this.password);
          await this.SEND_LOGIN_REQUEST(data);

          if (this.USER) {
              if (this.REDIRECT_AFTER_LOGIN) {
                  this.$router.push(this.REDIRECT_AFTER_LOGIN);
              } else {
                  this.$router.push({name: "user-cab"});
              }
          }
        }  
        this.isLoading = false;
    },

    async userRegister() {
      
        if (this.isLoading) return;

        this.isLoading = true;
        const errorsInData = {};
        this.SET_ERRORS(errorsInData)

        if (!isValidEmail(this.email)) {
            errorsInData.email = 'Укажите валидный адрес эл. почты'
        }
        if (!this.password || this.password.length < 8) {
            errorsInData.password = 'Пароль должен быть больше 8 символов'
        }
        if (this.password !== this.confirm) {
            errorsInData.confirm = 'Пароли не совпадают'
        }
        if (!this.username) { 
            errorsInData.username = 'Укажите имя'
        }
        if (!this.phone) {
            errorsInData.phone = 'Укажите номер телефона'
        }
        if (!this.company) {
            errorsInData.company = 'Укажите название компании'
        }
        if (!this.unp || this.unp.toString().length !== 9) {
            errorsInData.unp = 'Укажите валидное УНП'
            console.log(this.unp);
        }
        if (Object.keys(errorsInData).length) {
            this.SET_ERRORS(errorsInData);
        } else {
            const data = {
                email: this.email,
                full_name: this.username,
                phone_number: this.phone,
                company_name: this.company,
                unp: this.unp,
                password: this.password
            };
            await this.SEND_REGISTER_REQUEST(data);
            // this.$router.push({name: "user-cab"});
        }
        this.isLoading = false;
    },

  }

}
</script>

<style lang="scss" scoped>
.popup__reg{
  po

  .sign-in-htm{
    text-align: center;
    margin: 0 auto;
  }


  h3{
    margin-bottom: 24px;
  }
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
  label{
    text-align: left;
    font-size: 12px;
    line-height: 140%;
    color: #423E48;
    opacity: 0.6;
  }
  p{
    font-size: 14px;
    line-height: 140%;
    text-align: center;
    color: #423E48;
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
  button{
    text-align: center;
  }
  .foot-lnk{
      font-size: 12px;
      text-align: center;
      text-decoration-line: underline;
      opacity: 0.6;
      cursor: pointer;
    &:nth-child(2){
        opacity: 1;
    }
  }
  .bottom-link{
    font-weight: 400;
    font-size: 14px;
    line-height: 130%;
    color: #4275D8;
    text-decoration: none;
    cursor: pointer;
  }
}
.full-open{
  max-width: 500px;
  margin: 0 auto;
  text-align: center;
}
.center-text{
  text-align: center;
}
</style>
