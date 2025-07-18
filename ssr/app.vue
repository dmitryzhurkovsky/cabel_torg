<template>
  <div id="app__component">
    <HeaderWrapper />
    <NotificationMain />
    <!-- <UiLoader /> -->
    <NuxtLoadingIndicator :color="'#FF9549'" />
    <ClientOnly fallback-tag="div">
      <NotificationPopUp/>
    </ClientOnly>
    <MyHeader />
    <!-- <Breadcrumb/> -->
    <NuxtPage />
    <MyFooter />
  </div>
</template>

<script setup>
  import { watch } from 'vue';
  import { useNotificationsStore } from '@/stores/notifications';
  import { useMainStore } from '@/stores/main';
  import { useOrdersStore } from '@/stores/orders';
  import { useAuthStore } from '@/stores/auth';
  import { useHeaderStore } from '@/stores/header';
  import { useFavoritesStore } from '@/stores/favorites';

  const route = useRoute();
  const notificationsStore = useNotificationsStore();
  const mainStore = useMainStore();
  const oredersStore = useOrdersStore();
  const authStore = useAuthStore();
  const headerStore = useHeaderStore();
  const favoritesStore = useFavoritesStore();

  const organizationData =  {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "ООО «КабельЭлектроТорг»",
    "url": "https://cabel-torg.by/",
    "logo": "https://cabel-torg.by/_nuxt/logo.3b81b796.svg",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "ул. ГОБК, 7, оф. 128",
      "addressLocality": "Брест",
      "postalCode": "224005",
      "addressCountry": "BY"
    },
  };

  const interval = ref(null);

  const setViewParametrs = () => {
    // console.log('Set innerWidth', window.innerWidth);
    headerStore.updateViewParameters(window.innerWidth);
  };

  watch(route, () => {
    setViewParametrs();
  });

  onBeforeUnmount( ()=> clearInterval(interval.value));

  onBeforeMount(async () => {
    interval.value = setInterval(()=> {
      setViewParametrs();
    }, 300)
    setViewParametrs();
    const nullData = [];
    if (!localStorage.getItem("carts")) localStorage.setItem("carts", JSON.stringify(nullData));
    if (!localStorage.getItem("favorites")) localStorage.setItem("favorites", JSON.stringify(nullData));
    await favoritesStore.getUserFavorite();
    await oredersStore.getUserOrder();
    if (localStorage.getItem("authToken")) {
        await authStore.getUserData();
    }
  });

  await useAsyncData(async () => {
    notificationsStore.setIsLoading(true);
    await headerStore.getCategories();
    await oredersStore.getOrderDeliveryTypes();
    await mainStore.getSettings();
    notificationsStore.setIsLoading(false);
    return true;
  });

  useHead(route.path === '/' ? {
    script: [{
      type: 'application/ld+json',
      children: JSON.stringify(organizationData)
    }]
  }: {}); 
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
  &:focus{
    outline: none!important;
  }
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

*:disabled {
  background-color: #dedede;
  opacity: 1;
}

//-webkit-overflow-scrolling: touch;
//animation-play-state: paused !important;


// Variables
// @import 'variables';

// Bootstrap
//@import '~bootstrap/scss/bootstrap';
//<МИКСИНЫ>===============================================================================================
//@import "mixins";
//</МИКСИНЫ>===============================================================================================

//<ШРИФТЫ>===============================================================================================

@import 'https://fonts.googleapis.com/css2?family=Rubik:wght@300;400;500;600;700&display=swap';

// @font-face {
//   font-family: 'icomoon';
//   src: url('@/assets/icons/fonts/icomoon.ttf?4vw17d') format('truetype'),
//   url('@/assets/icons/fonts/icomoon.woff?4vw17d') format('woff'),
//   url('@/assets/icons/fonts/icomoon.svg?4vw17d#icomoon') format('svg');
//   font-weight: normal;
//   font-style: normal;
//   font-display: block;
// }

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
    background: #fff;
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

#app__component{
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}
.app__content{
  flex: 1 0 auto;
  flex-grow: 1;
}
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
.center{
  text-align: center ;
}
h1{
  font-weight: 500;
  font-size: 36px;
  line-height: 43px;

  color: #423E48;
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
  padding: 12px 24px;
  min-width:180px;text-align: center;
  cursor: pointer;
  transition: all 0.3s ease;
  white-space: nowrap;
  &:hover{
    background: #6291ED;
  }
}
.btn-banner{
  @media (max-width: $md2+px){
    padding: 6px 12px;
  }
}

.black{
  background: $mainColor;
  border: 1.2px solid  $mainColor;
  padding: 12px 24px;
  &:hover{
    background: #5A5A5A;
  }
}
.empty_black {
  background: #F8FAFF;
  color: $mainColor;
  border: 1.2px solid $mainColor;
  padding: 12px 24px;
  filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));

  &:hover {
    background: #eaedf6;
    opacity: 0.8;
    color: $mainColor;
  }
}
.blue{
  padding: 12px 24px;
}


.empty{
  background: #fff;
  padding: 12px 24px;
  color: $mainColor;
  border: 1px solid #423E48;
}

.flex-center{
  display: flex;
  align-items: center;
}

.center-text{
  width: 100%;
  text-align: center;
}

._footnote{
  font-size: 10px;
  line-height: 20px;
  text-align: right;
  opacity: 0.5;
}

._title{
  font-weight: 500;
  font-size: 14px;
  line-height: 20px;
  color: #423E48;
}

._link{
  font-weight: 400;
  line-height: 130%;
  color: #4275D8;
}
.table3x{
  flex-basis: 33.333%;
  @media (max-width: $md3+px){
  }
}
.table3x{

    @media (max-width: $md3+px){
    }
}
//INPUT
.group__row{
  width: 100%;
  justify-content: space-between;
  gap: 10px;
}
//.group{
//  width: 100%;
//  display: flex;
//  flex-direction: column;
//  align-items: flex-start;
//  margin-bottom: 15px;
//  //text-align: center;
//  justify-content: center;
//}
label{
  text-align: left;
  font-size: 12px;
  line-height: 140%;
  color: #423E48;
  opacity: 0.6;
}

.input__box{
  width: 100%;
  position: relative;
}

.input__icon{
  position: absolute;
  top: 14px;
  right: 10px;
  color: rgba(66, 62, 72, 0.2);
  font-size: 14px;
}
input{
  width: 100%;
  background: #FFFFFF;
  border: 1px solid rgba(66, 62, 72, 0.2);
  border-radius: 8px;
  padding: 10px 30px 10px 16px;
  font-weight: 300;
}

//RADIO

.radio {
  margin: 10px 10px 10px 0;
  input[type="radio"] {
    position: absolute;
    opacity: 0;
    + .radio-label {
      &:before {
        content: '';
        background: #fff;
        border-radius: 100%;
        border: 1px solid darken(#fff, 25%);
        display: inline-block;
        width: 1.4em;
        height: 1.4em;
        position: relative;
        top: -0.2em;
        margin-right: 1em;
        vertical-align: top;
        cursor: pointer;
        text-align: center;
        transition: all 250ms ease;
      }
    }
    &:checked {
      + .radio-label {
        &:before {
          background-color: #3197EE;
          box-shadow: inset 0 0 0 4px #f4f4f4;
        }
      }
    }
    &:focus {
      + .radio-label {
        &:before {
          outline: none;
          border-color: #3197EE;
        }
      }
    }
    &:disabled {
      + .radio-label {
        &:before {
          box-shadow: inset 0 0 0 4px #f4f4f4;
          border-color: darken(#f4f4f4, 25%);
          background: darken(#f4f4f4, 25%);
        }
      }
    }
    + .radio-label {
      &:empty {
        &:before {
          margin-right: 0;
        }
      }
    }
  }
}

.form{
    &__body{
        @media (max-width: $md3+px) {
        }
    }
    &__input{
      border:0;
      outline:0;
        &:focus{
          outline: none!important;
        }
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
.dropdown{
  position: relative;
  display: inline-block;
  cursor: pointer;
  font-weight: 400;
  &__wrapper{
    display: none;
    position: absolute;
    left: -12px;
    top: 10px;
    background: transparent;
    padding: 20px 0;
    z-index: 5;
  }
  &:hover{
    color:#4275D8;
  }
  .wrapper__show{
    display: block;
    z-index: 105;
  }
  .wrapper__show:hover,
  .wrapper__show:focus
  .wrapper__show:active{
    display: block;
  }

  &__content{
    background: #FFFFFF;
    box-shadow: 0px 0px 10px rgb(0 0 0 / 8%);
    border-radius: 10px;
    padding: 16px 10px;
    min-width: 350px;
    width: 100%;

    a{
      font-weight: 500;
      font-size: 16px;
      line-height: 24px;
      color: #423E48;
      padding: 10px 16px;
      transition: all 0.3s ease;
      &:hover{
        background: rgba(66, 117, 216, 0.1);
        border-radius: 6px;
        color: #4275D8;

      }
    }
  }
}

.dropdown.dropdown__wrapper {
  display: block;
}

.long_text{
  width: 200px;
  overflow:hidden;
  white-space:nowrap;
  text-overflow: ellipsis;

}

.dropdown .wrapper__show {
  display: block;
  @media (max-width: $md3+px) {
    position: fixed;
    left: 50%!important;
    top: 50%;
    right: inherit!important;
    transform: translate(-50%, -50%);

  }
}

.section_title{
  font-size: 20px;
  letter-spacing: .44px;
  line-height: 24px;
  color: #423e48;
  font-weight: 500;
}

</style>
