<template>
  <div id="app__component">
    <Header/>
    <router-view/>
    <Footer/>
  </div>
</template>

<script>

  import Header from '@/components/header.vue'
  import Footer from "@/components/footer.vue";

  export default {

    name: "App",

    computed: {
    },

    components:
    {
      Header, Footer,
    },

    methods: {
    },

    created() {
    },

  };
</script>

<style lang="scss">
* {
    padding: 0px;
    margin: 0px;
    border: 0px;
}
*,
*:before,
*:after {
    -moz-box-sizing: border-box;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
}
:focus,
:active {
    // outline: none;
}
a:focus,
a:active {
    // outline: none;
}
aside,
nav,
footer,
header,
section {
    display: block;
}
html {
    font-size: #{$fontSize + px};
}
html,
body {
    height: 100%;
    min-width: $minWidth;
}
body {
    line-height: 1;
    font-family: $fontFamily;
    //text-rendering: optimizeLegibility;
    -ms-text-size-adjust: 100%;
    -moz-text-size-adjust: 100%;
    -webkit-text-size-adjust: 100%;
}
input,
button,
textarea {
    font-family: $fontFamily;
    font-size: inherit;
}
input::-ms-clear {
    display: none;
}
button {
    cursor: pointer;
    background-color: inherit;
}
button::-moz-focus-inner {
    padding: 0;
    border: 0;
}
a,
a:visited {
    text-decoration: none;
}
a:hover {
    text-decoration: none;
}
ul li {
    list-style: none;
}
img {
    vertical-align: top;
}
h1,
h2,
h3,
h4,
h5,
h6 {
    font-weight: inherit;
    font-size: inherit;
}
//-webkit-overflow-scrolling: touch;
//animation-play-state: paused !important;


// Variables
// @import 'variables';

// Bootstrap
//@import '~bootstrap/scss/bootstrap';
//<МИКСИНЫ>===============================================================================================
// @import "mixins";
//</МИКСИНЫ>===============================================================================================

//<ШРИФТЫ>===============================================================================================

@import url('https://fonts.googleapis.com/css2?family=Rubik:wght@300;400;500;600;700&display=swap');

//<Подключаем шрифты>=======================================================================================
//&display=swap&subset=cyrillic-ext
// @import "fonts";
//</Подключаем шрифты>=======================================================================================

//<Иконочные шрифты>==========================================================================================
// @import "icons";
//</Иконочные шрифты>==========================================================================================

//<ОБНУЛЕНИЕ, ОБЩИЕ ПАРАМЕТРЫ>===============================================================================================
// @import "null";
body {
    color: $mainColor;
    font-size: 16px ;
    font-weight: 300;
    font-family: 'Rubik', sans-serif;
    &._lock {
        overflow: hidden;
    }
}
//</ОБНУЛЕНИЕ, ОБЩИЕ ПАРАМЕТРЫ>===============================================================================================

//<ОБОЛОЧКА>===========================================================================================================
.wrapper {
    width: 100%;
    min-height: 100%;
    font-size: $fontSize;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    &._loaded {
    }
}
//</ОБОЛОЧКА>===========================================================================================================

//<ОСНОВНАЯ СЕТКА>===========================================================================================================
._container {
    max-width: $maxWidthContainer + px;
    margin: 0 auto;
    padding: 0 2%;
    @media (max-width: $md1+px) {
        max-width: 970px;
    }
    @media (max-width: $md2+px) {
        max-width: 750px;
    }
    @media (max-width: $md3+px) {
        max-width: none;
        padding: 0 10px;
    }
}
//</ОСНОВНАЯ СЕТКА>===========================================================================================================

//<ПОДКЛЮЧЕНИЕ ФАЙЛОВ UI СТИЛЕЙ, ФОРМ И ГОТОВЫХ КЛАССОВ>====================================================================================================
//@import "forms";
//@import "ui";
//</ПОДКЛЮЧЕНИЕ ФАЙЛОВ UI СТИЛЕЙ, ФОРМ И ГОТОВЫХ КЛАССОВ>====================================================================================================

//<ПОДКЛЮЧЕНИЕ ФАЙЛОВ СТИЛЕЙ СТРАНИЦ И ЭЛЕМЕНТОВ>====================================================================================================
//@import "datepicker";
//@import "lightgallery";
//@import "pagging";
//@import "popup";
//@import "header";
//@import "head";
//@import "footer";

//@import "home";
//</ПОДКЛЮЧЕНИЕ ФАЙЛОВ СТИЛЕЙ СТРАНИЦ И ЭЛЕМЕНТОВ>====================================================================================================

//<ОСНОВНОЙ БЛОК>====================================================================================================
.page {
    flex: 1 1 auto;
}
//===================================================================================================================================

//</ОСНОВНОЙ БЛОК>====================================================================================================
.mt-20{
    margin-top: 20px;
}
.mb-20{
    margin-bottom: 20px;
}

.mr-20{
    margin-right: 20px;
}

h3{
  font-weight: 500;
  font-size: 20px;
  line-height: 24px;
  letter-spacing: 0.44px;
  color: #423E48;
}

.btn {
  background: #4275D8;
  border-radius: 6px;
  color:#fff;
  padding: 8px 24px;
  min-width:180px;
}

.flex-center{
  display: flex;
  align-items: center;
}

._title{
  font-weight: 500;
  font-size: 14px;
  line-height: 20px;
  color: #423E48;
}

.page__link{

}
.table3x{

    @media (max-width: $md3+px){
    }
}

.form{
    &__body{
        @media (max-width: $md3+px) {
        }

    }
    &__item{

    }
    &__label{

        // @include adaptiv-value( 'line-height', 50, 30, 1);
    }
    &__input{

        &:focus{

        }
        ._error{

        }
    }
    &__button{

    }
    &__errormsg{

    }

}

.breadcrumb{
  display: flex;
  align-items: center;
  padding: 20px 0 30px 0;

  li{
    a{
      font-weight: 300;
      font-size: 12px;
      line-height: 16px;
      text-align: center;
      color: #423E48;
      margin-right: 10px;
    }

  }
  .active{
    font-weight: 300;
    font-size: 12px;
    line-height: 16px;
    text-align: center;
    opacity: 0.5;

  }

}


// Templates for structure
.structure {

  &__title{
    margin: 30px 0;

  }
  &__block{
    padding: 0px 0 60px 0;
  }

  &__list{
    &__item{
      line-height: 30px;
      font-size: 18px;
      &:last-child{
        margin-bottom: 30px;
      }
    }
  }

  &__text{
    font-weight: 300;
    font-size: 18px;
    line-height: 140%;
    color: #423E48;
    margin-bottom: 20px;

  }
}

</style>
