<template lang="html">
  <div class="topmenu__right client-bar flex-center">
    <div class="topmenu__item right-direction">
      <div class="dropdown icon-favorite">
        <div class="dropdown__wrapper">
          <HeaderFavorite/>
        </div>

      </div>

    </div>
    <div class="topmenu__item right-direction">
      <div class="dropdown icon-user">
        <div v-if = "IS_OPEN_MAIN_LOGIN && !USER" class="dropdown__wrapper qq">
          <div class="dropdown__content popup-cart">
            <div class="avatar__box">
              <div class="avatar icon-user flex-center"></div>
            </div>

            <button @click="handleClick('/login', 1)" class="btn black">
              Вход
            </button>

            <div @click="handleClick('/login', 2)" class="foot-lnk">
                Не помню пароль
            </div>
            <hr class="hr">
            <div @click="handleClick('/login', 3)" class="foot-reg">
              Зарегистрироваться
            </div>
          </div>
          <!-- <UserActions/> -->
        </div>
        <div v-if = "IS_OPEN_MAIN_LOGIN && USER" class="dropdown__wrapper">

          <div class="dropdown__content popup-cart">
            <div class="avatar__box">
              <div class="avatar icon-user flex-center"></div>
            </div>
            <div>
              <div @click="handleClick('/user-cab', 1)" class="">
                Профиль
              </div>
              <div @click="" class="">
                Выйти
              </div>
            </div>


          </div>
          <!-- <UserActions/> -->
        </div>

      </div>

    </div>
    <div class="topmenu__item right-direction">
      <div class="dropdown icon-cart">
        <div class="dropdown__wrapper">
          <HeaderCart/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import HeaderCart   from '@/components/header/header-cart.vue'
import HeaderFavorite   from '@/components/header/header-favorite.vue'
import {mapGetters, mapMutations} from 'vuex'

export default {
  name: 'TopMenuActions',

  components:
  {
    HeaderCart, HeaderFavorite
  },

  computed: {
    ...mapGetters("auth", ["AUTH_TYPE", "IS_OPEN_MAIN_LOGIN", "USER"]),
},

  methods: {
    ...mapMutations("auth", ["SET_TYPE"]),

    handleClick (URL, auth_type) {
      if (this.$route.path != URL) {
        this.SET_TYPE(auth_type);
        this.$router.push(URL);
      } else {
        this.SET_TYPE(auth_type);
      }
    },

  },

}
</script>

<style lang="css" scoped>

.right-direction .dropdown__wrapper{
  right: 0;
  left: unset;
}

.topmenu{
  &__item{
    padding: 0 10px 0 10px;
    //position: relative;
  }
}

.popup-cart{
  text-align: center;
  padding: 40px 24px 40px 24px;
}
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

.topmenu__right{
  gap:20px;

}



</style>
