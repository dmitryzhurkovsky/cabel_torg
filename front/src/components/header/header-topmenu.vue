<template lang="html">
  <div class="header__topmenu topmenu flex-center">
    <div class="topmenu__left flex-center">
      <div class="burger-menu burger-menu--closed">
        <div class="bar"></div>
        <div class="bar"></div>
        <div class="bar"></div>
      </div>


      <div class="topmenu__item"><a href="">Каталог товаров</a></div>
      <div class="topmenu__item"><a href="">Покупателям</a></div>
      <div class="topmenu__item"><a href="">О нас</a> </div>
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
    </div>
  </div>
</template>

<script>

import { mapGetters } from "vuex";

export default {
  name: "HeaderTopMenu",

  computed: {
    ...mapGetters("header", ["ORDER_COUNT"]),
  },
}
</script>

<style lang="scss">
.header {
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
        border-left: 1px solid $mainColor;
        border-right: 1px solid $mainColor;

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

.popup-container {
  display: flex;
  justify-content: center;
  align-items: center ;
  //height: 100vh;

  .popup {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(#000,.5);
    z-index: 10;
    opacity: 0;
    visibility: hidden;
    transition: 400ms all;
    >label {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      cursor: pointer;
    }
    .inner {
      position: absolute;
      top: 100%;
      left: 50%;
      padding: 38px 24px 40px 24px;
      transform: translate(-50%, -50%);
      background: #fff;
      box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.08);
      border-radius: 16px;
      min-width: 300px;
      box-sizing: border-box;
      transition: 400ms all;
      z-index: 10;
      max-height: 100%;
      overflow: auto;
      .close-popup{
        position: absolute;
        top: 10px;
        right: 10px;
      }
      .title {
        margin-bottom: 25px;
        position: sticky;
        top: 0;
        background: #fff;
        text-align: center;
        h6 {
          font-weight: 500;
          font-size: 20px;
          line-height: 140%;

        }
        label {
          font-size: 14px;
          color: #999;
          cursor: pointer;
          &:hover {
            color: #222;
          }
        }
      }
      .content {
        //padding: 5px 15px 15px;
        ul {
          li {
            margin-bottom: 15px;
            &:last-child {
              margin-bottom: 0;
            }
            input {
              width: 100%;
              padding: 10px 16px;
              font-size: 14px;
              box-sizing: border-box;
              background: #FFFFFF;
              border: 1px solid rgba(66, 62, 72, 0.2);
              border-radius: 8px;
              &:focus {
                outline: 0;
                border-color: #272643;
              }
            }
            button {
              background: #423E48;
              cursor: pointer;
            }
            .label_input{
              font-weight: 300;
              font-size: 12px;
              line-height: 140%;
              opacity: 0.6;
            }
          }
        }
        p {
          font-size: 13px;
          line-height: 130%;
          margin-bottom: 15px;
          &:last-child {
            margin-bottom: 0;
          }
        }
        .close-btn {
          margin-top: 15px;
          padding-top: 15px;
          border-top: 1px solid #ddd;
          label {
            background: rgba(#000, .05);
            display: block;
            line-height: 30px;
            text-align: center;
            font-size: 13px;
            color: #444;
            border-radius: 3px;
            cursor: pointer;
            &:hover {
              background: rgba(#000,.1);
            }
          }
        }
      }
    }
  }
  >input {
    position: absolute;
    left: -9999px;
    opacity: 0;
    &:checked + .popup {
      opacity: 1;
      visibility: visible;
      .inner {
        top: 50%;
      }
    }
  }
}


</style>
