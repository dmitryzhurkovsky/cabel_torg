<template lang="html">
  <div class="header__body">

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
            <div class="info-header__item">BYN</div>
      </div> <!--     header__main-->
  </div>  <!--header__body -->

</template>

<script>
  import HeaderSearch from '@/components/header/header-search.vue'

  export default {
    name: "HeaderBody",

    components:
    {
      HeaderSearch,
    },
  }
</script>

<style lang="scss" scoped>
.header {
    &__body {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    &__info{
     justify-content: space-between;
    }

    &__logo {
    }
}

.info-header{
    &__item{
    padding: 0 20px 0 20px;
    &:nth-child(1){
      a{
        font-weight: 500;
        font-size: 14px;
        color: $mainColor;
      }
    }
    &:nth-child(2){
      border-left: 1px solid $mainColor;
      border-right: 1px solid $mainColor;
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
