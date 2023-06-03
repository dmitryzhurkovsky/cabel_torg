<template>
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
                  @click.stop  = "changeCategory(item)"
              >
                <div class="menu__link">{{item.name}}</div>
              </li>
            </ul>
            <a class="_link"
              :href = getCatalogUrl()
            >
              Перейти в каталог
            </a>
          </div>

          <div class="menusub row">
            <div class="menusub__box">
              <div class="menusub__item"
                v-for   = "sub in SUB_CATEGORIES"
                :key    = "sub.id"
                @click.stop  = "subCategoryClick(sub)"
              >
                <div v-if = "sub.id" class="menu__rubric">{{sub.name}}</div>
                <ul v-if = "sub.subItems.length > 0">
                  <li
                      v-for = "subItem in sub.subItems"
                      :key  = "subItem.id"
                  >
                    <div @click.stop = "subCategoryClick(subItem)" class="menu__linksub">{{subItem.name}}</div>
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
    ...mapGetters("header", ["CATALOG", "TOP_CATEGORIES_ITEM_ACTIVE", "SUB_CATEGORIES_ITEM_ACTIVE", "ALL_CATEGORIES", "TOP_CATEGORIES", "SUB_CATEGORIES", "IS_CATALOG_OPEN"]),
    ...mapGetters("query", ["LIMIT", "OFFSET", "VIEW_TYPE", "TYPE_OF_PRODUCT", "CATEGORY_ID", "MIN_PRICE", "MAX_PRICE", "SORT_TYPE", "SORT_DIRECTION"]),
  },

  methods:{
    ...mapMutations("header", ["UPDATE_IS_CATALOG_OPEN"]),
    ...mapMutations("query", ["SET_CATEGORY_ID", "SET_DEFAULT_PRICES"]),

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
        "&limit=" + this.LIMIT;
      if (this.MIN_PRICE != 0) url = url + "&actual_price_gte=" + this.MIN_PRICE;
      if (this.MAX_PRICE != 40000) url = url + "&actual_price_lte=" + this.MAX_PRICE;
      url = url + "&ordering=" + this.SORT_DIRECTION + this.SORT_TYPE;
      url = url + '&type_of_product=' + this.TYPE_OF_PRODUCT;
      // url = url + "&q=";
      //  + this.SEARCH_STRING;
      return url;        
    },

    changeCategory(category){
      this.SET_DEFAULT_PRICES();
      this.$router.push(this.getCategoryUrl(category.site_link));
    },

    subCategoryClick(category){
      this.UPDATE_IS_CATALOG_OPEN(!this.IS_CATALOG_OPEN);
      this.SET_DEFAULT_PRICES();
      const menuItem = this.ALL_CATEGORIES.filter(item => item.id == category.id)[0];
      this.$router.push(this.getCategoryUrl(menuItem.site_link));
    },

  },

}
</script>

<style scoped lang="scss">

.catalog__menu{
position: absolute;
top: 50px;
left: 0;
padding: 38px 0 20px 0;
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
.active .menu__link{

  color:#4275D8;
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
  ._link{
    padding-left: 15px;
  }
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
