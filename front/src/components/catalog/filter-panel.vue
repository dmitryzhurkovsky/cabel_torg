<template>
    <div class="filter__block" v-if="CATALOG.length">
        <div class="filter__box" 
            v-for   = "mainItem in CATALOG"
            :key    = "mainItem.id"
        >
            <div class="sidebar_menu__title">
              <div :class = "{'active' : mainItem.filterPanel}"
                  @click.stop = "openCategory(mainItem)"
              >
                {{mainItem.name}}
              </div>
              <div v-if="mainItem.childrens.length"
                   :class="[ mainItem.filterPanel ? 'sidebar_menu__open  icon-arrow-r' : 'sidebar_menu__close icon-arrow-l']"
                   @click.stop = "toggleCategory(mainItem)"
              >
              </div>
            </div >

            <div class="filter__block"  v-if = "mainItem.childrens.length && mainItem.filterPanel">

                    <div class="sidebar_menu__subtitle"
                        v-for   = "middleItem in mainItem.childrens"
                        :key    = "middleItem.id"
                    >
                      <div class="subtitle__row">
                        <div :class = "{'active' : middleItem.filterPanel}"
                            @click.stop  = "openCategory(middleItem)"
                        >
                          {{middleItem.name}}
                        </div>
                        <div v-if="middleItem.childrens.length"
                             :class="[ middleItem.filterPanel ? 'sidebar_menu__open icon-arrow-r' : 'sidebar_menu__close icon-arrow-l']"
                             @click.stop = "toggleCategory(middleItem)"
                        >
                        </div>
                      </div>


                    <div class="subtitle__list "  v-if = "middleItem.childrens.length &&  middleItem.filterPanel">
                        <div class="sidebar_menu__subtitle-child"
                            v-for = "lastItem in middleItem.childrens"
                            :key  = "lastItem.id"
                            @click.stop = "openCategory(lastItem)"
                        >
                            <div class="">
                              <div :class = "{'active' : LAST_CATEGORIES_ITEM_ACTIVE === lastItem.id}">
                                {{lastItem.name}}
                              </div>

                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </div>

        <div class="filter__box">
            <div class="filter__title icon-arrow-up">Показывать:</div>

            <div class="filter__checkbox__list">

              <label class="checkbox__container"
                v-for = "category in ALL_TYPE_OF_PRODUCTS"
                :key = "category"
              >
                {{ category.name }}
                <input type="checkbox" v-if = "category.type === TYPE_OF_PRODUCT" checked>
                <input type="checkbox" v-if = "category.type !== TYPE_OF_PRODUCT" @click.prevent = toggleFilterCategory(category.type)>
                <span class="checkmark"></span>
              </label>

            </div>


        </div>
      <!--            # PRICE SLIDER-->
      <PriceSlider class="filter__box" />

    </div>

</template>

<script>

import {mapMutations, mapGetters, mapActions} from 'vuex'
import PriceSlider from '@/components/catalog/price-slider.vue';

export default {
  name: 'FilterPanel',

  components: {
    PriceSlider,
  },

  computed: {
    ...mapGetters("header", ["CATALOG", "TOP_CATEGORIES_ITEM_ACTIVE", "SUB_CATEGORIES_ITEM_ACTIVE", "LAST_CATEGORIES_ITEM_ACTIVE"]),
    ...mapGetters("query", ["LIMIT", "OFFSET", "VIEW_TYPE", "TYPE_OF_PRODUCT", "CATEGORY_ID", "MIN_PRICE", "MAX_PRICE", "SORT_TYPE", 
      "SORT_DIRECTION", "SORT_ORDER", "ALL_TYPE_OF_PRODUCTS"
    ]),
    // ...mapGetters("catalog", ["CATALOG_SEARCH_STRING"]),
  },

  methods:{
    ...mapMutations("query", ["SET_TYPE_OF_PRODUCT", "SET_CATEGORY_ID", "SET_OFFSET"]),
    ...mapActions("header",["SET_ALL_CURRENT_CATEGORIES"]),

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

    getTypeOfProduct(type) {
      return '&type_of_product=' + type;
    },

    getLastPartOfUrl(){
      let url = "offset=" + this.OFFSET + 
        "&limit=" + this.LIMIT + 
        "&actual_price_gte=" + this.MIN_PRICE + 
        "&actual_price_lte=" + this.MAX_PRICE;
      url + "&ordering=" + this.SORT_DIRECTION + this.SORT_TYPE;
      url = url + "&q=";
      //  + this.CATALOG_SEARCH_STRING;
      return url;        
    },

    toggleCategory(item) {
      item.filterPanel = !item.filterPanel;
    },

    openCategory(category){
      this.SET_OFFSET(0);
      let url = this.getCategoryUrl(category.id);
      url = url + this.getTypeOfProduct(this.TYPE_OF_PRODUCT);
      this.$router.push(url);
    },

    toggleFilterCategory(category){
      let url = this.getCategoryUrl(this.CATEGORY_ID);
      url = url + this.getTypeOfProduct(category);
      this.$router.push(url);
    },
  },

  // mounted(){
  //   console.log(this.TYPE_OF_PRODUCT);
  //   this.toggleFilterCategory(this.TYPE_OF_PRODUCT);
  // },
}
</script>

<style scoped lang="scss">
.filter{

    &__block{}
    &__checkbox{

    &__item{
        margin: 0 15px 10px 15px;
        //height: 18px;
        input{
            position: absolute;
            opacity: 0;
            z-index: -1;
        }
    }


    }
    &__box{
        font-weight: 400;
        position: relative;
      .icon-arrow-l:before{
        transform: rotate(90deg);
        cursor: pointer;
      }
      .icon-arrow-r:before{
        transform: rotate(-90deg);
        cursor: pointer;
      }
    }

    &__title{
        background: #F8FAFF;
        padding: 6px 8px;
        font-weight: 500;
        font-size: 14px;
        line-height: 24px;
        color: #423E48;
        margin: 12px 0;
        &:before{
            position: absolute;
            top: 12px;
            right: 10px;
            font-size: 10px;
            //transform: rotate(-90deg);
        }
    }
    &__subtitle{
      font-size: 13px;
      padding: 5px 0 5px 20px;
      cursor: pointer;
      &-child{
      }
    }
    &__field{
      flex-direction: column;
      align-items: flex-start;
        input{
          width: 100%;
          height: 100%;
          outline: none;
          font-size: 16px;
          border-radius: 5px;
          padding: 5px 10px;
          text-align: left;
          border: 1px solid #999;
          -moz-appearance: textfield;
      }
    }
    &__text{
        span{
            font-weight: 400;
            font-size: 14px;
            color: #423E48;
        }
        .active{
            color: #423E48;
            font-weight: 500;
            }
    }

}
.checkbox{
 margin-right: 12px;



 &:before{
   content: "";
   width: 18px;
   height: 18px;
   display: inline-block;
   background: rgb(249, 249, 249);
   border: 1px solid rgb(163, 163, 163);
 }


 &__label{
   display: flex;
   align-items: flex-start;
   justify-content: flex-start;
   height: 30px;
 }
}

.sidebar_menu{
  &__title{
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 10px 10px 0;
    line-height: 1.8;
    div:first-child {
      cursor: pointer;
    }
    .active{
      color:#4275D8;
    }
  }
  &__subtitle{
    .subtitle__row{
      div:first-child {
        cursor: pointer;
      }
      .active{
        color:#4275D8;
      }
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 10px 10px 10px 5px;
      font-size: 14px;
    }
    .subtitle__list{
      padding-left: 10px;
    }
    &-child{
      cursor: pointer;
      font-size: 13px;
      line-height: 1.2;
      padding: 5px 5px;
      opacity: 0.8;
      .active{
        color:#4275D8;
      }
    }
  }
}
.sidebar_menu {

  transition: all 0.3s ease;
  &__open {
    font-size: 12px;
    transform: rotate(-90deg);
    color:#4275D8;
    > div{
      color: red;
    }
  }
  &__close {
    font-size: 12px;
    transform: rotate(90deg);
  }
}

 .checkbox__container {
   display: block;
   position: relative;
   padding-left: 30px;
   margin-bottom: 12px;
   cursor: pointer;
   font-size: 14px;
   -webkit-user-select: none;
   -moz-user-select: none;
   -ms-user-select: none;
   user-select: none;
   opacity: 1;
 }

/* Hide the browser's default checkbox */
.checkbox__container input {
  position: absolute;
  opacity: 0;
  cursor: pointer;
  height: 0;
  width: 0;
}

/* Create a custom checkbox */
.checkmark {
  position: absolute;
  top: 0;
  left: 0;
  height: 18px;
  width: 18px;
  background-color: #eee;
}

/* On mouse-over, add a grey background color */
.checkbox__container:hover input ~ .checkmark {
  background-color: #ccc;
}

/* When the checkbox is checked, add a blue background */
.checkbox__container input:checked ~ .checkmark {
  background-color: #4275D8;
}

 /* Create the checkmark/indicator (hidden when not checked) */
 .checkmark:after {
   content: "";
   position: absolute;
   display: none;
 }

 /* Show the checkmark when checked */
 .checkbox__container input:checked ~ .checkmark:after {
   display: block;
 }

 /* Style the checkmark/indicator */
 .checkbox__container .checkmark:after {
   left: 6px;
   top: 2px;
   width: 6px;
   height: 12px;
   border: solid white;
   border-width: 0 2px 2px 0;
   transform: rotate(45deg);
   -webkit-transform: rotate(45deg);
   -ms-transform: rotate(45deg);
   transform: rotate(45deg);
 }


</style>