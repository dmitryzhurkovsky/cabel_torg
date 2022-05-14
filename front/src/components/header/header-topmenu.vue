<template lang="html">
  <div class="header__wrapper">
    <div class="header__content _container">
        <div class="header__topmenu topmenu flex-center">
          <div class="topmenu__left flex-center">
            <div class="topmenu__item">
              <div class="dropdown icon-burger" @mouseover="openMenu()" @mouseleave="closeMenu()">Каталог товаров
                <CatalogMenu v-if = "IS_CATALOG_OPEN"/>
              </div>
            </div>
            <div class="topmenu__item">
                  <div class="dropdown">Покупателям
                    <div class="dropdown__wrapper">
                      <div class="dropdown__content">
                        <a href="/how_to_order">Как оформить заказ</a>
                        <a href="/shipping">Оплата и доставка</a>
                        <a href="/about">Оптовым клиентам</a>
                        <a href="/warranty">Гарантийное обслуживание</a>
                        <a href="/puboffer">Публичная оферта</a>
                      </div>
                    </div>

                  </div>
            </div>
            <div class="topmenu__item">
              <div class="dropdown">О нас
                <div class="dropdown__wrapper">
                  <div class="dropdown__content">
                    <a href="/how_to_order">О компании</a>
                    <a href="/shipping">Контактная информация</a>
                    <a href="/about">Новости</a>
                  </div>
                </div>
              </div>

            </div>
          </div>
          <div class="topmenu__right client-bar flex-center">
            <div class="topmenu__item">
              <a class="icon-favorite" href=""></a>
            </div>
            <div class="topmenu__item popup-container">

              <label class="icon-user" for="login-popup"></label>
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
            <div class="topmenu__item">
              <div class="dropdown icon-cart">
                <div class="dropdown__wrapper">
                  <div class="dropdown__content popup-cart">
                    <h3 class="">Корзина</h3>
                    <div class="popup-cart__summary">
                      <div class="div">Товары в корзине: <span>12</span></div>
                      <div>на сумму <span>123.89</span><span>BYN</span></div>
                    </div>
                    <div class="popup-cart__list">
                      <div class="popup-cart__item row">
                        <div class="popup-cart__img">
                          <img src="../../assets/catalog/card1.png" alt="">
                        </div>
                        <div class="popup-cart__description">
                          <div class="popup-cart__title">Коммуникационный кабель</div>
                          <div class="popup-cart__uptitle">UTP cat.5e (патч-панель) 19″</div>

                        </div>
                        <div class="popup-cart__action">
                          <div class="popup-cart__price">12.03 <span>BYN</span></div>
                          <button class="icon-delete"></button>
                        </div>

                      </div>
                      <div class="popup-cart__item row">
                        <div class="popup-cart__img">
                          <img src="../../assets/catalog/card1.png" alt="">
                        </div>
                        <div class="popup-cart__description">
                          <div class="popup-cart__title">Коммуникационный кабель</div>
                          <div class="popup-cart__uptitle">UTP cat.5e (патч-панель) 19″</div>

                        </div>
                        <div class="popup-cart__action">
                          <div class="popup-cart__price">12.03 <span>BYN</span></div>
                          <button class="icon-delete"></button>
                        </div>

                      </div>
                    </div>
                    <button class="btn">Оформить заказ</button>
                    <div>
                      <a class="" href="">Перейти в корзину</a>
                    </div>



                  </div>
                </div>

              </div>






            </div>
          </div>
        </div>
    </div>
  </div>
</template>

<script>

import {mapActions, mapGetters} from 'vuex'
import CatalogMenu from '@/components/header/catalog-menu.vue'

export default {
  name: "HeaderTopMenu",

  components:
  {
    CatalogMenu,
  },

  computed: {
    ...mapGetters("header", ["ORDER_COUNT", "IS_CATALOG_OPEN"]),
  },

  methods:{
    toggleMenu() {
      this.$store.commit('header/UPDATE_IS_CATALOG_OPEN', !this.IS_CATALOG_OPEN);
      console.log(this.IS_CATALOG_OPEN);
    },
    openMenu(){
      this.$store.commit('header/UPDATE_IS_CATALOG_OPEN', true);
      console.log(this.IS_CATALOG_OPEN);
    },
    closeMenu(){
      this.$store.commit('header/UPDATE_IS_CATALOG_OPEN', false);
      console.log(this.IS_CATALOG_OPEN);
    }
  }
}
</script>

<style scoped lang="scss">
.header {
    &__wrapper{

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
    position: relative;
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
          font-weight: 500;
          color: $secondColor;
        }


      }
      &:nth-child(3){
        border-left: 1px solid #F0F0F1;
        border-right: 1px solid #F0F0F1;

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

.popup-cart{
  text-align: center;

  h3{
    font-weight: 500;
    font-size: 20px;
    line-height: 140%;
    text-align: center;
    margin-bottom: 16px;
  }



  &__summary{
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 16px 0;
    font-weight: 300;
    font-size: 14px;
    line-height: 140%;
    color: #423E48;
    opacity: 0.6;
    border-top: 1px solid #F0F0F1;
    border-bottom: 1px solid #F0F0F1;

    div:nth-child(1){
      span{
        font-weight: 500;
        opacity: 1;
      }
    }
    div:nth-child(2){
      span{
        font-weight: 500;
        opacity: 1;
      }


    }

  }

  &__list{
    margin: 30px 0;
  }

  &__item{
    display: grid;
    grid-template-columns: 1fr 2fr 1fr;
    gap:10px;
    align-items: self-start;

  }

  &__img{
    max-width: 100%;
    img{
      width: 100%;
    }

  }

  &__description{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    font-size: 12px;
    line-height: 140%;
    color: #423E48;
    text-align: left;
  }
  &__title{
    font-weight: 500;

  }
  &_action{
    align-items: stretch;

  }



  &__price{
    font-size: 12px;
    line-height: 140%;

    color: #423E48;
    margin-bottom: 20px;
  }

  .icon-delete{
    text-align: right;
    &:hover{
      color:#4275D8;
    }
  }

  button{
    margin-bottom: 20px;
  }


}




</style>
