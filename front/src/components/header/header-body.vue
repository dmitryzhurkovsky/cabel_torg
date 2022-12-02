<template lang="html">
  <BurgerMenu v-if = "IS_MENU_OPEN"/>
  <div class="header__wrapper">
    <div class="header__content _container">
        <div class="header__body ">
      <!--  # BURGER Appears from tablet version-->
            <div  @click="toggleMenu()" class="burger-menu burger-menu--closed">
              <div class="bar"></div>
              <div class="bar"></div>
              <div class="bar"></div>
            </div>

            <a href="/" class="header__logo">
                <img src="@/assets/logo.svg" alt="CabelTorg">
            </a>
            <HeaderSearch/>
            <div class="header__info info-header flex-center">
                  <div class="info-header__item">
                    <a href="tel:+375296889454">+375 29 688 94 54</a>
                  </div>
                  <div class="info-header__item">
                    <a href="mail:info@cabeltorg.by">info@cabeltorg.by</a>
                  </div>
<!--                  <div class="info-header__item">BYN</div>-->
            </div> <!--     header__info-->
      <!--  # CLIENT-BAR -  Appears from tablet version-->
            <div class="topmenu__right client-bar flex-center">
              <div class="topmenu__item">
                <a class="icon-favorite"></a>
              </div>
              <div class="topmenu__item popup-container">

                <label class="icon-user" for="login-popup"></label>
                <input type="checkbox" id="login-popup">
                <div class="popup">
                  <label for="login-popup"></label>
                  <UserActionsMobile />
                </div>

              </div>
              <div class="topmenu__item popup-container">

                <label class="icon-cart" for="login-popup"></label>
                <input type="checkbox" id="login-popup">

                <div class="popup">
                  <label for="login-popup"></label>
                  <div class="inner">
                    <label class=" close-popup icon-plus"></label>
                    <div class="title">
                      <h6>Вход</h6>

                    </div>
                    <div class="content">
                      <ul>
                        <li>
                          <label class="label_input">Электронная почта</label>
                          <input type="text" placeholder="">
                        </li>
                        <li>
                          <label class="label_input">Пароль</label>
                          <input type="password" placeholder="">
                        </li>
                        <li  class="center">
                          <button type="submit" class="btn">Войти</button>
                        </li>
                        <li class="center">
                          <a href="" class="label_input popu">Не помню пароль</a>
                        </li>
                        <li  class="center">
                          <a href="" class="">Зарегистрироваться</a>
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>

              </div>
            </div><!--    client-bar-->

        </div>  <!--header__body -->
    </div>
  </div>

</template>

<script>
  import {mapActions, mapGetters} from 'vuex'
  import HeaderSearch from '@/components/header/header-search.vue'
  import BurgerMenu from '@/components/header/burger-menu.vue'
  import UserActionsMobile from '@/components/auth/user-actions-mobile.vue'

  export default {
    name: "HeaderBody",

    components:
    {
      HeaderSearch, BurgerMenu, UserActionsMobile
    },

    computed: {
      ...mapGetters("header", ["IS_MENU_OPEN"]),
    },

    methods:{
      toggleMenu() {
        this.$store.commit('header/UPDATE_IS_MENU_OPEN', !this.IS_MENU_OPEN);
        // console.log(this.IS_MENU_OPEN);
      },
    }

  }
</script>

<style lang="scss" scoped>
.header {
  &__wrapper{
    padding: 24px 0;
    background: #F8FAFF;
  }
    &__body {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    &__info{
     justify-content: space-between;
      @media (max-width: $md2+px) {
        display: none;
      }
    }

    &__logo {
    }
  .burger-menu{
    display: None;
    @media (max-width: $md2+px) {
      display: flex;
      flex-direction: column;
    }
  }
  .client-bar{
    display: None;
    @media (max-width: $md2+px) {
      display: flex;
      gap: 16px;
    }

  }
}

.info-header{
    &__item{
    padding: 0 20px 0 20px;
    &:nth-child(1){
      width: 170px;
      a{
        font-weight: 500;
        font-size: 14px;
        color: $mainColor;
      }
    }
    &:nth-child(2){
      border-left: 1px solid $mainColor;
      //border-right: 1px solid $mainColor;
      a{
        font-weight: 300;
        text-decoration-line: underline;
      }
    }
    &:nth-child(3){
    }
  }
}

</style>
