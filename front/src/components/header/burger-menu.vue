<template lang="html">
  <div class="burger__menu__open">
    <ul class="burger__menu_list animated" v-if="CATALOG.length">
      <li 
        v-for   = "mainItem in CATALOG"
        :key    = "mainItem.id"
      >
        <div class="burger__menu_item flex-center">
          <label
              :class = "{'active' : mainItem.mobileMenu}"
              @click.stop  = "changeMainCategory(mainItem)"
          >
            {{ mainItem.name }}
          </label>
          <div
              :class = "{'active' : mainItem.mobileMenu}"
              class="icon-arrow-down"
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

                  @click.stop  = "changeSubCategory(mainItem, middleItem)"
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
                  @click.stop = "changeLastCategory(mainItem, middleItem, lastItem)"
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
    <ul class="burger__menu_list">
      <li><a href="">Покупателям</a></li>
      <li><a href="">О нас</a></li>
    </ul>
    <hr class="burger__menu__hr">
    <ul class="burger__menu_list">
      <li><a class="_link" href="tel:+375296889854">+375 29 6889854</a></li>
    </ul>


  </div>
</template>

<script>

import {mapGetters, mapMutations, mapActions} from 'vuex'

export default {
  name: "BurgerMenu",

  computed: {
    ...mapGetters("header", ["TOP_CATEGORIES_ITEM_ACTIVE", "SUB_CATEGORIES_ITEM_ACTIVE", "LAST_CATEGORIES_ITEM_ACTIVE", "CATALOG", "IS_CATALOG_OPEN"]),
  },

  methods:{
    // ...mapMutations("header", ["SET_CURRENT_TOP_CATEGORY", "SET_CURRENT_SUB_CATEGORY", "SET_CURRENT_LAST_CATEGORY", "UPDATE_IS_CATALOG_OPEN"]),
    ...mapMutations("header", ["UPDATE_IS_CATALOG_OPEN"]),
    ...mapMutations("query", ["SET_CATEGORY_ID"]),
    ...mapActions("header", ["SET_ALL_CURRENT_CATEGORIES"]),
    ...mapActions("catalog", ["GET_CATALOG_ITEMS"]),

    toggleCategory(item) {
      item.mobileMenu = !item.mobileMenu;
    },
    
    changeMainCategory(category){
      this.SET_ALL_CURRENT_CATEGORIES({
        mainCategory: category.id,
        middleCategory: null,
        lastCategory: null,
      });
      this.SET_CATEGORY_ID(category.id);
      // if (category.id === this.TOP_CATEGORIES_ITEM_ACTIVE) {
      //   this.SET_CURRENT_TOP_CATEGORY(null);
      // } else {
      //   this.SET_CURRENT_TOP_CATEGORY(category.id);
      // }
      this.openPage();
    },

    changeSubCategory(mainCategory, middleCategory){
      this.SET_ALL_CURRENT_CATEGORIES({
          mainCategory: mainCategory.id,
          middleCategory: middleCategory.id,
          lastCategory: null,
      });
      this.SET_CATEGORY_ID(middleCategory.id);
      // if (category.id === this.SUB_CATEGORIES_ITEM_ACTIVE) {
      //   this.SET_CURRENT_SUB_CATEGORY(null);
      // } else {
      //   this.SET_CURRENT_SUB_CATEGORY(category.id);
      // }
      this.openPage();
    },

    changeLastCategory(mainCategory, middleCategory, lastCategory){
      this.SET_ALL_CURRENT_CATEGORIES({
          mainCategory: mainCategory.id,
          middleCategory: middleCategory.id,
          lastCategory: lastCategory.id,
      });
      this.SET_CATEGORY_ID(lastCategory.id);
      // if (category.id === this.LAST_CATEGORIES_ITEM_ACTIVE) {
      //   this.SET_CURRENT_LAST_CATEGORY(null);
      // } else {
      //   this.SET_CURRENT_LAST_CATEGORY(category.id);
      // }
      this.openPage();
    },

    openPage() {
      this.UPDATE_IS_CATALOG_OPEN(!this.IS_CATALOG_OPEN);
      if (this.$router.path != '/catalog') {
          this.$router.push('/catalog');
      }
    },
  }
}
</script>

<style lang="scss" scoped>

.burger__menu__open{
  position: absolute;
  top: 125px;
  width: 100%;
  height: 100%;
  background-color: #fff;
  z-index: 3;
}

a {
  text-decoration: none;
}

.cd-accordion-menu label {
  cursor: pointer;
}

.burger__menu{
  color: #423E48;

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
  &__item{
    font-size: 12px;
    font-weight: bold;
    color:#423E48;

    a{
      color:#423E48;
      text-decoration: none;
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


</style>
