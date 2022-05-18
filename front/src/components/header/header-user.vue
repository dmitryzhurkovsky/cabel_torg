<template lang="html">
  <div class="dropdown__content popup-cart">
      <div class="avatar__box">
        <div class="avatar icon-user flex-center"></div>
      </div>

      <button v-if = "currentScreen === 0" @click = "changeScreen(1)" class="btn black">
        Вход
      </button>
      <div v-if = "currentScreen === 0" @click = "changeScreen(2)" class="popup__reset">
        Не помню пароль
      </div>
      <div v-if = "currentScreen === 0" @click = "changeScreen(3)" class="popup__reg">
        Зарегистрироваться
      </div>
      <div v-if = "currentScreen === 1" class="popup__reg">
        Тут входим
      </div>
      <div v-if = "currentScreen === 2" class="popup__reg">
        А тут восстанавливаем пароль
      </div>

  </div>

</template>

<script>
export default {
  name: "HeaderSearch",

  data: function() {
    return {
        currentScreen : 0,
      }
  },

  methods: {
    changeScreen(id){
        this.currentScreen = id;
    },

  }

}
</script>

<style lang="scss" scoped>
.popup-cart{
  text-align: center;

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

}
</style>
