<template lang="html">
      <div class="catalog__menu menu__container">
        <div class="menu active _container">
          <div class="menu__scroll">
            <div class="container">
              <div class="left_sidebar">
                <ul class="menu__mass">
                  <li 
                      class="menu__item" 
                      :class = "{'active' : item.id === TOP_CATEGORIES_ITEM_ACTIVE}"
                      v-for   = "item in TOP_CATEGORIES"
                      :key    = "item.id"
                      @click.stop  = "changeCategory(item.id)"
                  >
                    <div class="menu__link">{{item.name}}</div>
                  </li>
                </ul>
                <a href="/catalog" class="menu__mass-lnk">Перейти в каталог</a>
              </div>

              <div class="menusub row">
                <div class="menusub__box">
                  <div class="menusub__item"
                    v-for   = "sub in SUB_CATEGORIES"
                    :key    = "sub.id"
                    @click.stop  = "subCategoryClick(sub.id)"
                  >
                    <div v-if = "sub.id" class="menu__rubric">{{sub.name}}</div>
                    <ul v-if = "sub.subItems.length > 0">
                      <li
                          v-for = "subItem in sub.subItems"
                          :key  = "subItem.id"
                      >
                        <div @click.stop = "subItemCategoryClick(subItem.id)" class="menu__linksub">{{subItem.name}}</div>
                      </li>
                    </ul>
                  </div>

                </div>

              </div>
            </div>
          </div>
        </div>
      </div>

</template>

<script>

import {mapGetters, mapMutations, mapActions} from 'vuex'

export default {
  name: "CatalogMenu",

  computed: {
    ...mapGetters("header", ["TOP_CATEGORIES_ITEM_ACTIVE", "SUB_CATEGORIES_ITEM_ACTIVE", "ALL_CATEGORIES", "TOP_CATEGORIES", "SUB_CATEGORIES", "IS_CATALOG_OPEN"]),
  },

  methods:{
    ...mapMutations("header", ["UPDATE_IS_CATALOG_OPEN"]),
    ...mapMutations("query", ["SET_CATEGORY_ID"]),
    ...mapActions("catalog", ["GET_CATALOG_ITEMS"]),
    ...mapActions("header", ["UPDATE_TOP_CATEGORY", "UPDATE_SUB_CATEGORY", "UPDATE_LAST_CATEGORY", "SET_ALL_CURRENT_CATEGORIES"]),

    changeCategory(id){
      this.SET_ALL_CURRENT_CATEGORIES({
          mainCategory: id,
          middleCategory: null,
          lastCategory: null,
      });
      this.SET_CATEGORY_ID(id);
    },

    subCategoryClick(id){
      this.SET_ALL_CURRENT_CATEGORIES({
            mainCategory: this.TOP_CATEGORIES_ITEM_ACTIVE,
            middleCategory: id,
            lastCategory: null,
      });
      this.SET_CATEGORY_ID(id);
      this.UPDATE_IS_CATALOG_OPEN(!this.IS_CATALOG_OPEN);
      this.$router.push('/catalog/' + id);
    },

    subItemCategoryClick(id){
      // console.log('кликнули по итему подкатегории ', id, event);
      this.SET_ALL_CURRENT_CATEGORIES({
            mainCategory: this.TOP_CATEGORIES_ITEM_ACTIVE,
            middleCategory: this.ALL_CATEGORIES.filter(item => item.id === id)[0].parent_category_id,
            lastCategory: id,
      });
      this.UPDATE_LAST_CATEGORY(id);
      this.SET_CATEGORY_ID(id);
      this.UPDATE_IS_CATALOG_OPEN(!this.IS_CATALOG_OPEN);
      this.$router.push('/catalog/' + id);
    },
  }
}
</script>

<style scoped lang="scss">

.catalog__menu{
  position: absolute;
  top: 50px;
  left: 0;
  padding: 38px 0 0 0;
  width: 100%;
  //height: 420px;
  background: #FFFFFF;
  box-shadow: 0px 4px 20px rgba(66, 62, 72, 0.05);
  z-index: 5;
}
.menu{

  .container {
    display: grid;
    grid-template-columns: 290px 1fr;
  }


  &__mass{
    min-width: 250px;
    max-height: 100%;
    position: static;
    &-lnk{
      padding-left: 15px;
      font-size: 14px;
      margin: 20px 0;
      color: #423E48;
      transition: all 0.3s ease;
      &:hover{
        color: #4275D8;
      }
    }
  }

  &__item{
    //margin: 20px 0;
    width: 100%;
    padding: 10px 15px;
    transition: all 0.2s ease;
    &:hover{
      color:#4275D8;
      background: rgba(66, 117, 216, 0.1);
      border-radius: 6px;
      padding: 10px 15px;

    }
  }




  &__link{
    font-weight: 500;
    font-size: 16px;
    line-height: 24px;
    color: #423E48;
    width: 100%;
    &:nth-child(1){
    }


  }

  .row{
    display: flex;
    align-items: flex-start;

  }
  .left_sidebar{


    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: space-between;
    height: 100%;
    box-shadow: 0px 4px 20px rgb(66 62 72 / 5%);
  }


  &__rubric{
    font-weight: 400;
    font-size: 14px;
    line-height: 20px;
    text-decoration-line: underline;
    color: #423E48;
    transition: all 0.2s ease;
    &:hover{
      color:#4275D8;
      opacity: 0.8;
    }

  }

  &__linksub{
    font-weight: 300;
    font-size: 14px;
    color: #423E48;
    margin-top: 8px;
    opacity: 0.5;
    &:hover{
      opacity: 0.7;
    }
  }
}

.menusub{
  display: flex;
  align-items: center;
  padding: 15px;
  width: 100%;
  max-height: 100%;
  position: static;

  &__box{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-template-rows: auto;
    gap: 12px;
  }

  &__item{

  }



}
</style>
