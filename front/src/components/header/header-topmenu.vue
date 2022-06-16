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
          <div class="topmenu__right client-bar flex-center">
            <div class="topmenu__item right-direction">
              <div class="dropdown icon-favorite">
                <div class="dropdown__wrapper">
                  <div class="dropdown__content popup-cart">
                    <h3 class="">Избранные товары</h3>

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
                    <div>
                      <a class="" href="">Перейти в Избранное
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                          <path d="M3 12H20.5M20.5 12L16.5 8M20.5 12L16.5 16" stroke="white"/>
                        </svg>
                      </a>
                    </div>
                  </div>
                </div>

              </div>

            </div>
            <div class="topmenu__item right-direction">
              <div class="dropdown icon-user">
                <div class="dropdown__wrapper">
                  <HeaderUser/>
                </div>

              </div>

            </div>
            <div class="topmenu__item right-direction">
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
                      <a class="" href="">Перейти в корзину
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                          <path d="M3 12H20.5M20.5 12L16.5 8M20.5 12L16.5 16" stroke="white"/>
                        </svg>
                      </a>
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
import CatalogMenu  from '@/components/header/catalog-menu.vue'
import HeaderUser   from '@/components/header/header-user.vue'

export default {
  name: 'HeaderTopMenu',

  components:
  {
    CatalogMenu, HeaderUser
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
.right-direction .dropdown__wrapper{
  right: 0;
  left: unset;
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
    &:hover{
      background: #F9F9F9;
    }

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

  a{
    font-weight: 400;
    font-size: 14px;
    line-height: 130%;
    color: #4275D8;
  }


}

.popup__reg{
  width: 100%;
  padding: 30px 0 10px 0;
  border-top: 1px solid #F0F0F1;
  a{
    font-weight: 400;
    font-size: 14px;
    line-height: 130%;
    text-align: center;
    color: #4275D8;


  }


}
.popup__reset{
  margin-bottom: 40px;
  a{
    font-size: 12px;
    line-height: 140%;
    text-align: center;
    text-decoration-line: underline;
    color: #423E48;
    opacity: 0.6;

  }


}




</style>
