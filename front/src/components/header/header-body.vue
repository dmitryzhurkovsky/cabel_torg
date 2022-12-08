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
            <TopMenuActions />
       <!-- # CLIENT-BAR -  Appears from tablet version -->

        </div>  <!--header__body -->
    </div>
  </div>

</template>

<script>
  import {mapActions, mapGetters} from 'vuex'
  import HeaderSearch from '@/components/header/header-search.vue'
  import BurgerMenu from '@/components/header/burger-menu.vue'
  // import UserActionsMobile from '@/components/auth/user-actions-mobile.vue'
  import TopMenuActions  from '@/components/header/header-actions.vue'

  export default {
    name: "HeaderBody",

    components:
    {
      HeaderSearch, BurgerMenu, TopMenuActions
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
