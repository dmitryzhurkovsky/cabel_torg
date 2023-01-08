<template lang="html">
<!--      <div v-if = "CATALOG_ITEM_ACTIVE === 1">first category item</div>-->
<!--      <div v-if = "CATALOG_ITEM_ACTIVE === 2">second category item</div>-->
<!--      <div v-if = "CATALOG_ITEM_ACTIVE === 3">third category item</div>-->
      <div class="catalog__menu menu__container">
        <div class="menu active _container">
          <div class="menu__scroll">
            <div class="container row">
              <ul class="menu__mass">
                <li class="menu__item" :class = "{'active' : item.id === TOP_CATEGORIES_ITEM_ACTIVE}"
                    v-for   = "item in TOP_CATEGORIES"
                    :key    = "item.id"
                    @click  = "changeCategory(item.id)"
                >
                  <div class="menu__link">{{item.name}}</div>
                </li>
              </ul>
              <div class="menusub row">
                <div class="menusub__box">
                  <div class="menusub__item"
                    v-for   = "sub in SUB_CATEGORIES"
                    :key    = "sub.id"
                    @click  = "subCategoryClick(sub.id, $event)"
                  >
                    <div v-if = "sub.id" class="menu__rubric">{{sub.name}}</div>
                    <ul v-if = "sub.subItems.length > 0">
                      <li
                          v-for = "subItem in sub.subItems"
                          :key  = "subItem.id"
                      >
                        <div @click = "subItemCategoryClick(subItem.id, $event)" class="menu__linksub">{{subItem.name}}</div>
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
    ...mapGetters("header", ["TOP_CATEGORIES_ITEM_ACTIVE", "SUB_CATEGORIES_ITEM_ACTIVE", "TOP_CATEGORIES", "SUB_CATEGORIES", "IS_CATALOG_OPEN"]),
  },

  methods:{
    ...mapMutations("header", ["SET_CURRENT_TOP_CATEGORY", "SET_CURRENT_SUB_CATEGORY", "UPDATE_IS_CATALOG_OPEN"]),
    ...mapActions("catalog", ["GET_CATALOG_ITEMS"]),
    changeCategory(newActive){
        this.SET_CURRENT_TOP_CATEGORY(newActive);
    },
    subCategoryClick(id, event){
      this.SET_CURRENT_SUB_CATEGORY(id);
      this.GET_CATALOG_ITEMS(id);
      this.UPDATE_IS_CATALOG_OPEN(!this.IS_CATALOG_OPEN);
      if (this.$router.path != '/catalog') {
          this.$router.push('/catalog');
      }
    },
    subItemCategoryClick(id, event){
      // console.log('кликнули по итему подкатегории ', id, event);
      event.stopImmediatePropagation();
      this.GET_CATALOG_ITEMS(id);
      this.UPDATE_IS_CATALOG_OPEN(!this.IS_CATALOG_OPEN);
      if (this.$router.path != '/catalog') {
          this.$router.push('/catalog');
      }
    },
  }
}
</script>

<style scoped lang="scss">
    .catalog__menu{
      position: absolute;
      top: 50px;
      left: 0;
      padding: 38px 0;
      width: 100%;
      height: 420px;
      background: #FFFFFF;
      box-shadow: 0px 4px 20px rgba(66, 62, 72, 0.05);
      z-index: 5;
    }
.menu{

  &__mass{
    min-width: 250px;
    max-height: 100%;
    position: static;
  }

  &__item{
    //margin: 20px 0;
    width: 100%;
    padding: 10px 15px;
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

  &__rubric{
    font-weight: 400;
    font-size: 14px;
    line-height: 20px;
    text-decoration-line: underline;
    color: #423E48;

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
  box-shadow: 0px 4px 20px rgba(66, 62, 72, 0.05);
  width: 100%;
  max-height: 100%;
  position: static;
  width: 600px;

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
