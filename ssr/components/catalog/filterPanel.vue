<template>
    <div class="filter__block" v-if="CATALOG.length">
        <div
          v-if    = "!isMobileVersion"
        >
          <div class="filter__box" 
              v-for   = "mainItem in CATALOG"
              :key    = "mainItem.id"
          >
              <div class="sidebar_menu__title">
                <a :class = "{'active' : mainItem.filterPanel}"
                  :href="createHref(mainItem.site_link)"
                  @click.stop.prevent = "openCategory(mainItem)"
                >
                  {{mainItem.name}}
                </a>
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
                          <a :class = "{'active' : middleItem.filterPanel}"
                            :href="createHref(middleItem.site_link)"
                            @click.stop.prevent  = "openCategory(middleItem)"
                          >
                            {{middleItem.name}}
                          </a>
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
                              @click.stop.prevent = "openCategory(lastItem)"
                          >
                              <div class="">
                                <a :class = "{'active' : LAST_CATEGORIES_ITEM_ACTIVE === lastItem.id}"
                                  :href="createHref(lastItem.site_link)"
                                >
                                  {{lastItem.name}}
                                </a>

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
  
        <CatalogPriceSlider v-if = "!isMobileVersion" class="filter__box" />

    </div>

</template>

<script>

import {mapMutations, mapGetters, mapActions} from 'vuex'

export default {
  name: 'FilterPanel',

  data(){
    return {
      isMobileVersion: false,
    }
  },

  computed: {
    ...mapGetters("header", ["ALL_CATEGORIES", "CATALOG", "TOP_CATEGORIES_ITEM_ACTIVE", "SUB_CATEGORIES_ITEM_ACTIVE", "LAST_CATEGORIES_ITEM_ACTIVE", "DEVICE_VIEW_TYPE"]),
    ...mapGetters("query", ["LIMIT", "OFFSET", "VIEW_TYPE", "TYPE_OF_PRODUCT", "CATEGORY_ID", "MIN_PRICE", "MAX_PRICE", "SORT_TYPE", 
      "SORT_DIRECTION", "SORT_ORDER", "ALL_TYPE_OF_PRODUCTS"
    ]),
  },

  watch: {
    DEVICE_VIEW_TYPE: async function() {
      setViewType(this.DEVICE_VIEW_TYPE);
    }  
  },

  methods:{
    ...mapMutations("query", ["SET_TYPE_OF_PRODUCT", "SET_CATEGORY_ID", "SET_OFFSET", "SET_DEFAULT_PRICES"]),
    ...mapActions("header",["SET_ALL_CURRENT_CATEGORIES"]),


    setViewType(curr) {
        if (curr > 1) {
          this.isMobileVersion = true
        } else {
          this.isMobileVersion = false
        }
    },

    getCatalogUrl(){
      let url = "/catalog";
      url = url + this.getLastPartOfUrl();
      return url;
    },

    createHref(category) {
      const URL = '/category/' + category;
      return URL;
    },

    getCategoryUrl(id){
      let url = "/category/";
      if (id) {
        const link = this.ALL_CATEGORIES.filter(item => item.id == id)[0].site_link
        url = url + link;
      }
      url = url + this.getLastPartOfUrl();
      // console.log('filterPanel ', url);
      return url;
    },

    getLastPartOfUrl(){
      let url = '?';
      if (this.OFFSET != 0 || this.LIMIT != 12) {
        url = url + "offset=" + this.OFFSET + '&'
        url = url + "limit=" + this.LIMIT + '&'
      }
      if (this.MIN_PRICE != 0 || this.MAX_PRICE != 80000) {
        url = url + "actual_price_gte=" + this.MIN_PRICE + '&';
        url = url + "actual_price_lte=" + this.MAX_PRICE + '&';
      }
      if (this.SORT_DIRECTION !== '-' || this.SORT_TYPE !== 'created_at') {
        url = url + "ordering=" + this.SORT_DIRECTION + this.SORT_TYPE + '&'
      }
      if (this.TYPE_OF_PRODUCT !== 'all') {
        url = url + "type_of_product=" + this.TYPE_OF_PRODUCT + '&'
      }
      const lastSymbol = url.slice(-1)
      if (lastSymbol === '&' || lastSymbol === '?') url = url.slice(0, -1)
      return url;        
    },

    toggleCategory(item) {
      item.filterPanel = !item.filterPanel;
    },

    openCategory(category){
      this.SET_CATEGORY_ID(category.id);
      this.SET_OFFSET(0);
      this.SET_DEFAULT_PRICES();
      this.SET_TYPE_OF_PRODUCT('all');
      // console.log('category.id', category.id);
      let url = this.getCategoryUrl(category.id);
      this.$router.push(url);
    },

    toggleFilterCategory(category){
      this.SET_TYPE_OF_PRODUCT(category);
      let url = "";
      if (this.CATEGORY_ID) {
        url = this.getCategoryUrl(this.CATEGORY_ID);
      } else {
        url = this.getCatalogUrl();
      }
      this.$router.push(url);
    },

  },

  beforeMount(){
    this.setViewType(this.DEVICE_VIEW_TYPE);
  },

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
    color: #423E48;
    div:first-child {
      cursor: pointer;
    }
    .active{
      color:#4275D8;
    }
    a{
    color: #423E48;;
    }

  }
  &__subtitle{
    color: #423E48;
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
    a{
      color: #423E48;
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
      a{
        color: #423E48;
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