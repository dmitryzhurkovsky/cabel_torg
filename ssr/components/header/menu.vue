<template>
  <div class="header__wrapper">
    <div class="header__content _container">
        <div class="header__topmenu topmenu flex-center">
          <div class="topmenu__left flex-center">
            <div class="topmenu__item" @click="toggleMenu()">
              <div class="dropdown icon-burger catalog__btn">Каталог товаров</div>
              <HeaderCatalogMenu v-if = "IS_CATALOG_OPEN"/>
            </div>
            <div class="topmenu__item" 
                @mouseenter="onCustomerIconEnter()"
                @mouseleave="onIconLeave()"
            >
              <div class="dropdown">Покупателям
                <div :class="[!customerHover ? 'dropdown__wrapper': 'dropdown__wrapper wrapper__show']">
                  <div class="dropdown__content">
                    <a @click.prevent="openPage('/how_to_work', $event)" href = "/how_to_work">Как оформить заказ</a>
                    <a @click.prevent="openPage('/shipping', $event)" href = "/shipping">Оплата и доставка</a>
                    <a @click.prevent="openPage('/wholesale', $event)" href = "/wholesale">Оптовым клиентам</a>
                    <a @click.prevent="openPage('/warranty', $event)" href = "/warranty">Гарантийное обслуживание</a>
                    <a @click.prevent="openPage('/offer', $event)" href = "/offer">Публичная оферта</a>
                  </div>
                </div>
              </div>
            </div>
            <div class="topmenu__item"  
                @mouseenter="onAboutIconEnter()"
                @mouseleave="onIconLeave()"
            >
              <div class="dropdown">О нас
                <div :class="[!aboutHover ? 'dropdown__wrapper': 'dropdown__wrapper wrapper__show']">
                  <div class="dropdown__content ">
                    <a @click.prevent="openPage('/about', $event)" href = "/about">О компании</a>
                    <a @click.prevent="openPage('/contacts', $event)" href = "/contacts">Контактная информация</a>
                    <a @click.prevent="openPage('/news', $event)" href = "/news">Новости</a>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <HeaderActions />
        </div>
    </div>
  </div>
</template>

<script>

import {mapMutations, mapGetters} from 'vuex'

export default {
  name: 'HeaderTopMenu',

  data: function(){
    return {
      customerHover: false,
      aboutHover: false,
    }
  },

  computed: {
    ...mapGetters("header", ["IS_CATALOG_OPEN", "TOP_CATEGORIES"]),
  },

  methods:{
    ...mapMutations("header", ["UPDATE_IS_CATALOG_OPEN"]),
    ...mapMutations("query", ["SET_SEARCH_STRING"]),

    toggleMenu() {
      this.UPDATE_IS_CATALOG_OPEN(!this.IS_CATALOG_OPEN);
      this.SET_SEARCH_STRING('');
      // console.log(this.IS_CATALOG_OPEN);
    },
    openPage(page, event) {
      event.stopImmediatePropagation();
      event.preventDefault();
      this.customerHover = false;
      this.aboutHover = false;
      if (this.$router.path != page) {
          this.$router.push(page);
          this.clearSearchString();
      }
    },
    
    clearSearchString(){
      this.SET_SEARCH_STRING('');
    },

    onCustomerIconEnter() {
      this.SET_SEARCH_STRING('');
      this.customerHover = true;
    },

    onAboutIconEnter() {
      this.SET_SEARCH_STRING('');
      this.aboutHover = true;
    },

    onIconLeave() {
      this.customerHover = false;
      this.aboutHover = false;
    },
  
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
    &:nth-child(1){
      padding: 0 10px 0 0;
    }
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
        &:hover{
          opacity: 0.8;
        }
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
