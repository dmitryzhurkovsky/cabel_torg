<template lang="html">
  <!-- <BurgerMenu v-if = "IS_MENU_OPEN"/> -->
  <BurgerMenu v-if = "IS_CATALOG_OPEN&&DEVICE_VIEW_TYPE>1"/>
  <div class="header__wrapper">
    <div class="header__content _container">
        <div class="header__body ">
      <!--  # BURGER Appears from tablet version-->
            <div  @click="toggleMenu()" class="burger-menu burger-menu--closed">
              <div class="bar"></div>
              <div class="bar"></div>
              <div class="bar"></div>
            </div>

            <a @click ="onOpenLink('/', $event)" href="/" class="header__logo">
                <img src="@/assets/logo.svg" alt="CabelTorg">
            </a>
            <HeaderSearch/>
            <div class="header__info info-header flex-center">
                  <div class="info-header__item">
                    <a :href="'tel:' + String(SETTINGS.phone).replace(/ /g,'')">{{ SETTINGS.phone }}</a>
                  </div>
                  <div class="info-header__item">
                    <a :href="'mailto:' + SETTINGS.email">{{ SETTINGS.email }}</a>
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
  import {mapMutations, mapGetters} from 'vuex'
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
      ...mapGetters("header", ["IS_CATALOG_OPEN", "TOP_CATEGORIES", "DEVICE_VIEW_TYPE"]),
      ...mapGetters("main", ["SETTINGS"]),
    },

    methods:{
      ...mapMutations("header", ["UPDATE_IS_CATALOG_OPEN"]),
      ...mapMutations("query", ["SET_SEARCH_STRING"]),

      toggleMenu() {
        this.UPDATE_IS_CATALOG_OPEN(!this.IS_CATALOG_OPEN);
      },

      onOpenLink(link, event) {
        event.stopImmediatePropagation();
        event.preventDefault();
        this.SET_SEARCH_STRING('');
        if (this.$router.path != link) {
            this.$router.push(link);
        }
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
      &:last-child{
        padding: 0 0 0 20px;
      }

    &:nth-child(1){
      width: 170px;
      a{
        font-weight: 500;
        font-size: 14px;
        color: $mainColor;
        transition: color 0.3s ease;
        &:hover{
          color: #4275D8;
        }
      }
    }
    &:nth-child(2){
      border-left: 1px solid $mainColor;
      //border-right: 1px solid $mainColor;
      a{
        font-weight: 400;
        color:#4275D8;
        letter-spacing: 0.6px;
        //text-decoration-line: underline;
      }
    }
    &:nth-child(3){
    }
  }
}

//Burger
.burger-menu{
  //margin: 0 auto;
  width: 24px;
  display: block;
  transition: all .3s;
  cursor: pointer;
  height: 24px;

  .bar{
    transition: all .3s;
    height: 2px;
    width: 100%;
    display: block;
    background-color: $secondColor;
    &:nth-of-type(2){
      margin: 5px 0;
    }
  }
  &--closed{
    transition-delay: .3s;
    .bar:nth-of-type(2){
      width: 75%;
      transition-property: margin, height, width;
      transition-delay: .3s, .3s, 0s;
    }
    .bar:nth-of-type(3) {
      width: 50%;
    }
    &:hover{
      .bar:nth-of-type(2){
        width: 100%;
      }
      .bar:nth-of-type(3){
        width: 100%;
      }

    }
    &--opened{
      padding-top: 12px;
      .bar:nth-of-type(1){
        transform: rotate(45deg);
        transition-delay: .3s;
        height: 2px;
      }

      .bar:nth-of-type(2){
        opacity: 0;
        height: 0;
        margin: -3px;
      }

      .bar:nth-of-type(3){
        transform: rotate(-45deg);
        transition-delay: .3s;
        height: 2px
      }
    }
  }
}
</style>
