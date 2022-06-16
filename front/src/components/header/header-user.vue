<template lang="html">
  <div class="dropdown__content popup-cart">
      <div v-if = "currentScreen === 0" class="avatar__box">
        <div class="avatar icon-user flex-center"></div>
      </div>

      <button v-if = "currentScreen === 0" @click = "changeScreen(1)" class="btn black">
        Вход
      </button>

      <div v-if = "currentScreen === 0" @click = "changeScreen(2)" class="foot-lnk">
          Не помню пароль
      </div>
      <hr  v-if = "currentScreen === 0" class="hr">
      <div v-if = "currentScreen === 0" @click = "changeScreen(3)" class="foot-reg">
        Зарегистрироваться
      </div>

      <div v-if = "currentScreen === 1" class="popup__reg">
        <h3>Вход</h3>
        <div class="sign-in-htm">
          <div class="group">
            <label for="user" class="label">Электронная почта</label>
            <input id="user" type="text" class="input">
          </div>
          <div class="group">
            <label for="pass" class="label">Пароль</label>
            <input id="pass" type="password" class="input" data-type="password">
          </div>

          <div class="group">
            <button type="submit" class="btn black">Войти</button>
          </div>

          <div @click = "changeScreen(2)" class="foot-lnk">
           Не помню пароль
          </div>
          <div @click = "changeScreen(3)" class="foot-lnk">
            Зарегистрироваться
          </div>
        </div>
      </div>
      <div v-if = "currentScreen === 2" class="popup__reg">
        <h3>Восстановление пароля</h3>
        <div class="reset-pass">
          <div class="group">
            <label for="user" class="label">Электронная почта</label>
            <input id="user" type="text" class="input">
          </div>
          <div class="group">
            <button @click = "changeScreen(4)" type="submit" class="btn black">Восстановить</button>
          </div>
        </div>
      </div>
      <div v-if = "currentScreen === 4" class="popup__reg">
        <h3>Проверьте ваш email</h3>
        <div class="reset-pass">
          <div class="group">
            <p>Мы отправили ссылку для <b>восстановления пароля</b> к вашей учетной записи.</p>
          </div>
          <div class="group">
            <button @click = "changeScreen(0)" type="submit" class="btn empty">Вернуться на сайт</button>
          </div>
        </div>
      </div>

  </div>

</template>

<script>
export default {
  name: "HeaderUser",

  data: function() {
    return {
        currentScreen : 0,
      }
  },

  methods: {
    changeScreen(id){
        this.currentScreen = id;
        // this.$store.commit('notification/ADD_MESSAGE', {name: 'Сменили экран на ' + id, icon: 'check_circle', id: '10'})
    },

  }

}
</script>

<style lang="scss" scoped>
.popup-cart{
  text-align: center;
  padding: 40px 24px 40px 24px;


  .avatar{
    justify-content: center;
    width: 80px;
    height: 80px;
    border-radius: 50%;
    background: rgba(66, 117, 216, 0.07);
    font-size: 30px;
    color: #423E48;
    font-weight: 500;
  }
  .avatar__box{
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 24px 0;
  }

  button{
    margin-bottom: 20px;
  }
  .hr{
    height:2px;
    margin:44px 0 40px 0;
    background:#F0F0F1;
  }
  .foot-reg{
    font-weight: 400;
    font-size: 14px;
    line-height: 130%;
    text-align: center;
    color: #4275D8;
  }
  .foot-lnk{
    font-size: 12px;
    text-align: center;
    text-decoration-line: underline;
    opacity: 0.6;
    color: #423E48;
  }

}
.popup__reg{
  .sign-in-htm{
    text-align: center;
    margin: 0 auto;
  }

  h3{
    margin-bottom: 24px;
  }
  .group{
    //width: 100%;
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
  button{
    text-align: center;
  }
  .foot-lnk{
      font-size: 12px;
      text-align: center;
      text-decoration-line: underline;
      opacity: 0.6;
    &:nth-child(2){
        opacity: 1;
    }
  }
}
</style>
