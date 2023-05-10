<template lang="html">
  <div class="burger__menu__open">
    <div class="burger__menutop">
      <div class="burger__close">
        <svg @click="closeMenu" width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M1 1L15 15" stroke="#4275D8" stroke-width="2"/>
            <path d="M15 1L1 15" stroke="#4275D8" stroke-width="2"/>
        </svg>
        <TopMenuActions />
      </div>
      <HeaderSearchBurger/>
    </div>
    <ul class="burger__menu_list animated" v-if="CATALOG.length">
      <li 
        v-for   = "mainItem in CATALOG"
        :key    = "mainItem.id"
      >
        <div class="burger__menu_item flex-center">
          <label
              :class = "{'active' : mainItem.mobileMenu}"
              @click.stop  = "changeCategory(mainItem.id)"
          >
            {{ mainItem.name }}
          </label>
          <div
              :class = "[mainItem.mobileMenu ? 'icon-arrow-down burger__menu_active' : 'icon-arrow-down']"
              @click.stop  = "toggleCategory(mainItem)"
              v-if="mainItem.childrens.length"
          >
          </div>
        </div>

        <ul class="second" v-if = "mainItem.mobileMenu && mainItem.childrens.length">
          <li 
            v-for   = "middleItem in mainItem.childrens"
            :key    = "middleItem.id"
          >
            <div class="burger__menu_item flex-center">
              <label
                  :class = "{'active' : middleItem.mobileMenu}"

                  @click.stop  = "changeCategory(middleItem.id)"
              >
                {{ middleItem.name }}
              </label>
              <div
                  :class = "{'active' : middleItem.mobileMenu}"
                  class="icon-arrow-down"
                  @click.stop  = "toggleCategory(middleItem)"
                  v-if="middleItem.childrens.length"
              >

              </div>
            </div>

            <ul class="third" v-if = "middleItem.mobileMenu && middleItem.childrens.length">
              <li 
                class="has-children"
                v-for = "lastItem in middleItem.childrens"
                :key  = "lastItem.id"
              >
                <label for="sub-group-level-3"
                  @click.stop = "changeCategory(lastItem.id)"
                >
                  {{ lastItem.name }}
                </label>
              </li>
            </ul>
          </li>
        </ul>
      </li>
    </ul>
    <hr class="burger__menu__hr">
    <ul class="burger__menu_list animated">
      <li>
        <div class="burger__menu_item flex-center">
          <label :class = "{'active' : activeMenuItem === 'Покупателям'}"
            @click.stop  = "activeMenuItem === 'Покупателям' ? activeMenuItem = null: activeMenuItem = 'Покупателям'"
          >
            Покупателям
          </label>
          <div :class = "[activeMenuItem === 'Покупателям' ? 'icon-arrow-down burger__menu_active' : 'icon-arrow-down']"
            @click.stop  = "activeMenuItem === 'Покупателям' ? activeMenuItem = null: activeMenuItem = 'Покупателям'"
          >
          </div>
        </div>
        <ul class="second" v-if = "activeMenuItem === 'Покупателям'">
          <li><a @click.prevent="openPage('/how_to_work')">Как оформит заказ</a></li>        
          <li><a @click.prevent="openPage('/shipping')">Оплата и доставка</a></li>        
          <li><a @click.prevent="openPage('/wholesale')">Оптовым клиентам</a></li>        
          <li><a @click.prevent="openPage('/warranty')">Гарантийное обслуживание</a></li>        
          <li><a @click.prevent="openPage('/hoffer')">Публичная оферта</a></li>        
        </ul>  
      </li>
      <li>
        <div class="burger__menu_item flex-center">
          <label :class = "{'active' : activeMenuItem === 'О нас'}"
            @click.stop  = "activeMenuItem === 'О нас' ? activeMenuItem = null: activeMenuItem = 'О нас'"
          >
            О нас
          </label>
          <div :class = "[activeMenuItem === 'О нас' ? 'icon-arrow-down burger__menu_active' : 'icon-arrow-down']"
            @click.stop  = "activeMenuItem === 'О нас' ? activeMenuItem = null: activeMenuItem = 'О нас'"
          >
          </div>
        </div>
        <ul class="second" v-if = "activeMenuItem === 'О нас'">
          <li><a @click.prevent="openPage('/about')">О компании</a></li>        
          <li><a @click.prevent="openPage('/contacts')">Контактная информация</a></li>        
          <li><a @click.prevent="openPage('/news')">Новости</a></li>        
        </ul>  
      </li>
      <!-- <li>
        <a href="">Покупателям</a>
      </li>
      <li>
        <a href="">О нас</a>
      </li> -->
    </ul>
    <hr class="burger__menu__hr">
    <ul class="burger__menu_list">
      <li><a class="_link" href="tel:+375296889854">+375 29 6889854</a></li>
    </ul>


  </div>
</template>

<script>

import {mapGetters, mapMutations, mapActions} from 'vuex'
import TopMenuActions  from '@/components/header/header-actions.vue'
import HeaderSearchBurger from '@/components/header/header-search-burger.vue'

export default {
  name: "BurgerMenu",

  components:
  {
    HeaderSearchBurger, TopMenuActions
  },

  data(){
    return {
      activeMenuItem : null,

    }
  },

  computed: {
    ...mapGetters("header", ["TOP_CATEGORIES_ITEM_ACTIVE", "SUB_CATEGORIES_ITEM_ACTIVE", "LAST_CATEGORIES_ITEM_ACTIVE", "CATALOG", "IS_CATALOG_OPEN"]),
    ...mapGetters("query", ["LIMIT", "OFFSET", "VIEW_TYPE", "TYPE_OF_PRODUCT", "CATEGORY_ID", "MIN_PRICE", "MAX_PRICE", "SORT_TYPE", "SORT_DIRECTION"]),
  },

  methods:{
    ...mapMutations("header", ["UPDATE_IS_CATALOG_OPEN"]),
    ...mapMutations("query", ["SET_CATEGORY_ID"]),
    ...mapActions("header", ["SET_ALL_CURRENT_CATEGORIES"]),
    ...mapActions("catalog", ["GET_CATALOG_ITEMS"]),

    toggleCategory(item) {
      item.mobileMenu = !item.mobileMenu;
    },
    
    getCatalogUrl(){
      let url = "/catalog?";
      url = url + this.getLastPartOfUrl();
      return url;
    },

    getCategoryUrl(id){
      let url = "/category/";
      if (id) url = url + id + "?";
      url = url + this.getLastPartOfUrl();
      return url;
    },

    getLastPartOfUrl(){
      let url = "offset=" + this.OFFSET + 
        "&limit=" + this.LIMIT + 
        "&price_gte=" + this.MIN_PRICE + 
        "&price_lte=" + this.MAX_PRICE;
      url = url + "&ordering=" + this.SORT_DIRECTION + this.SORT_TYPE;
      url = url + '&type_of_product=' + this.TYPE_OF_PRODUCT;
      url = url + "&q=";
      return url;        
    },

    changeCategory(id){
      this.UPDATE_IS_CATALOG_OPEN(!this.IS_CATALOG_OPEN);
      this.$router.push(this.getCategoryUrl(id));
    },

    openPage(page) {
      this.UPDATE_IS_CATALOG_OPEN(false);
      console.log('Burger', page, this.$route.path);
      if (this.$route.path != page) {
        this.$router.push(page);
      }
    },

    closeMenu() {
      this.UPDATE_IS_CATALOG_OPEN(false);
    }
  }
}
</script>

<style lang="scss" scoped>

.burger__menu__open{
  position: absolute;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: #fff;
  z-index: 20;
}

a {
  text-decoration: none;
}

.cd-accordion-menu label {
  cursor: pointer;
}

.burger__menu{
  color: #423E48;

  &__menutop{
    display: flex;
    flex-direction: column;
  }
  &__block{
    padding: 16px 20px 16px 30px;
    border: 1px solid #F0F0F1;
    justify-content: flex-start;
    align-items: flex-start;
    flex-direction: column;
    .icon-phone{
      color: #4275D8;
      &:before{
        margin-right: 10px;
        font-size: 15px;
      }

    }
  }
  &_active{
    transform: rotate(180deg);
  }
  &__item{
    font-size: 12px;
    font-weight: bold;
    color:#423E48;

    a{
      color:#423E48;
      text-decoration: none;
    }
    
  }
  &__item {
    label .active{
      color: #4275D8;
    }
  }
  &__hr{
    height: 2px;
    background: #F0F0F1;
    width: 90%;
    margin: 0 auto;
  }

  &:last-child{
    color: #4275D8;
  }
}

.burger__menu{

  &_list{
    padding: 10px 16px;
    label, a{
      position: relative;
      display: block;
      padding: 10px 0;
      background: #fff;
      //color: #423E48;
      font-size: 12px;
      font-weight: 500;
      line-height: 12px;
      opacity: 1;
    }
    .second{
      padding-left: 16px;
    }
    .third{
      padding-left: 16px;

    }
  }
  &_item{
    justify-content: space-between;
}


}

.icon-arrow-down{
  font-size: 10px;
}

label[class="active"]{
  color: #4275D8;
}

div[class="active"]{
  transform: rotate(180deg);
}

.burger{
  &__close{
    padding: 16px 0 0 16px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
  }
}
</style>
