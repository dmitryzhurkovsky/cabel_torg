<template lang="html">
  <div class="header__wrapper">
    <div class="header__content _container">
        <div class="header__topmenu topmenu flex-center">
          <div class="topmenu__left flex-center">
            <div class="topmenu__item">
              <div class="dropdown icon-burger catalog__btn" @click="toggleMenu()">Каталог товаров</div>
              <CatalogMenu v-if = "IS_CATALOG_OPEN"/>
            </div>
            <div class="topmenu__item">
                  <div class="dropdown">Покупателям
                    <div class="dropdown__wrapper">
                      <div class="dropdown__content">
                        <a @click="openPage('/how_to_work')">Как оформить заказ</a>
                        <a @click="openPage('/shipping')">Оплата и доставка</a>
                        <a @click="openPage('/wholesale')">Оптовым клиентам</a>
                        <a @click="openPage('/warranty')">Гарантийное обслуживание</a>
                        <a @click="openPage('/offer')">Публичная оферта</a>
                      </div>
                    </div>

                  </div>
            </div>
            <div class="topmenu__item">
              <div class="dropdown">О нас
                <div class="dropdown__wrapper">
                  <div class="dropdown__content ">
                    <a @click="openPage('/about')">О компании</a>
                    <a @click="openPage('/contacts')">Контактная информация</a>
                    <a @click="openPage('/news')">Новости</a>
                  </div>
                </div>
              </div>

            </div>
          </div>
          <TopMenuActions />
        </div>
    </div>
  </div>
</template>

<script>

import {mapActions, mapGetters} from 'vuex'
import CatalogMenu  from '@/components/header/catalog-menu.vue'
import TopMenuActions  from '@/components/header/header-actions.vue'

export default {
  name: 'HeaderTopMenu',

  components:
  {
    CatalogMenu, TopMenuActions
  },

  computed: {
    ...mapGetters("header", ["IS_CATALOG_OPEN", "TOP_CATEGORIES"]),
    ...mapGetters("order", ["ORDER_COUNT"]),
  },

  methods:{
    toggleMenu() {
      this.$store.commit('header/UPDATE_IS_CATALOG_OPEN', !this.IS_CATALOG_OPEN);
      console.log(this.IS_CATALOG_OPEN);
    },
    openPage(page) {
      if (this.$router.path != page) {
          this.$router.push(page);
      }
    }
    // openMenu(){
    //   this.$store.commit('header/UPDATE_IS_CATALOG_OPEN', true);
    //   console.log(this.IS_CATALOG_OPEN);
    // },
    // closeMenu(){
    //   this.$store.commit('header/UPDATE_IS_CATALOG_OPEN', false);
    //   console.log(this.IS_CATALOG_OPEN);
    // }
  }
}
</script>

<style scoped lang="scss">
.header {
    &__wrapper{
      position: relative;

    }
    &__topmenu{
      padding: 20px 0;
      justify-content: space-between;
      @media (max-width: $md2+px) {
        display: none!important;
      }

    }
}

.topmenu{

  &__item{
    padding: 0 10px 0 10px;
    //position: relative;
  }
  &__left{
    .topmenu__item{
      a{
        font-weight: 400;
        font-size: 16px;
        line-height: 19px;
        display: flex;
        align-items: center;
        color: #423E48;
      }

      &:nth-child(2){
        a{
          color: $mainColor;
        }


      }
      &:nth-child(3){
        border-left: 1px solid #F0F0F1;
        border-right: 1px solid #F0F0F1;

      }

      .catalog__btn{
        font-weight: 500;
        color: #4275D8;
      }

    }

  }
  &__cart{
      position: absolute;
      width: 12px;
      height: 12px;
      font-size:12px;
      color: #fff;
      background: red;
      border-radius:50%;
      padding: 0 3px;
      right: 6px;
      top: 10px;
      opacity:0.9;
}
  .icon-burger{
    &:before{
      margin-right: 10px;
    }

  }

}

.menu{
    flex: 0 1 540px;
    &__body{
        @media (max-width: $md2+px) {
            position: fixed;
            width: 100%;
            //height: 100%;
            overflow: auto;
            top: -100%;
            left: 0;
            background-color: #07095E;
            transition: left 0.3s ease 0s;
            padding: 35px 15px 30px 15px;
            z-index: 2;
            &._active{
                top: 0;
            }

        }

    }
    &__list{
        margin-bottom:0;
        @media (min-width:$md2+px) {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-evenly;

        }
    }
    &__item{
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        padding: 5px 0;
        position: relative;
        // @include adaptiv-value("margin-right",35,5,1);
        margin-right: 35px;
        &:last-child{
            margin-right: 0;
        }
        @media (max-width:$md2+px) {
            margin-bottom: 20px;
        }

    }
    &__link{

        // @include adaptiv-font(14, 11, 14);
        font-weight: 600;
        text-transform: uppercase;
        transition: color 0.3s ease 0s;
        &:hover{
            transition: color 300ms ease-in-out;
        }

        @media (max-width: $md2+px){
            color: #fff;
        }
    }
}


</style>
