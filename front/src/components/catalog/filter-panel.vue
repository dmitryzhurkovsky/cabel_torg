<template>
    <div class="filter__block" v-if="CATALOG.length">
        <div class="filter__box" 
            v-for   = "mainItem in CATALOG"
            :key    = "mainItem.id"
        >
            <div
                @click  = "openMainCategory(mainItem, $event)"
            >
                {{mainItem.name}}
            </div>
            <div v-if="mainItem.childrens.length"
                :class="[ mainItem.filterPanel ? 'filter__title icon-arrow-r' : 'filter__title icon-arrow-l']"
                @click="toggleCategory(mainItem, $event)"
            >
            </div>
            <div class="filter__block"  v-if = "mainItem.childrens.length && mainItem.filterPanel">
                <div class="filter__subtitle"
                    v-for   = "middleItem in mainItem.childrens"
                    :key    = "middleItem.id"
                >
                    <div 
                        @click  = "openMiddleCategory(middleItem, $event)"
                    >
                        {{middleItem.name}}
                    </div>
                    <div v-if="middleItem.childrens.length"
                        :class="[ middleItem.filterPanel ? 'filter__subtitle icon-arrow-r' : 'filter__subtitle icon-arrow-l']"
                        @click="toggleCategory(middleItem, $event)"
                    >
                    </div>
                    <div class="filter__checkbox-list filter__subtitle-child "  v-if = "middleItem.childrens.length &&  middleItem.filterPanel">
                        <div class="filter__subtitle-child"
                            v-for = "lastItem in middleItem.childrens"
                            :key  = "lastItem.id"
                            @click = "openLastCategory(lastItem, $event)"
                        >
                            <div class="checkbox-default">
                              <div class="filter__text filter__subtitle-child">
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

            <div class="filter__checkbox-list">
                <div class="filter__checkbox__item"
                    v-for = "category in categories"
                    :key = "category"
                >
                    <div 
                        class = "checkbox-default"
                        @click="changeFilterCategory($event, category)"
                    >
                        <label class="checkbox__label">
                            <input type="checkbox" name="" class="" value="">
                            <div class="checkbox"></div>
                            <div class="filter__text">
                            <span :class="[category.type === TYPE_OF_PRODUCT.type ? 'active' : '']">{{ category.name }}</span>
                            </div>
                        </label>
                    </div>
                </div>
            </div>


        </div>
      <!--            # PRICE SLIDER-->
      <PriceSlider class="filter__box" />

    </div>

</template>

<script>

import {mapMutations, mapGetters} from 'vuex'
import PriceSlider from '@/components/catalog/price-slider.vue';

export default {
    name: 'FilterPanel',

    components: {
      PriceSlider,
    },

    data(){
        return {
            categories: [
                {name : 'Все товары', type: 'all'},
                {name : 'Только товары со скидкой', type: 'with_discount'} , 
                {name : 'В наличии', type: 'available'},
            ],
        }
    },

    computed: {
        ...mapGetters("header", ["CATALOG", "TOP_CATEGORIES_ITEM_ACTIVE", "SUB_CATEGORIES_ITEM_ACTIVE", "LAST_CATEGORIES_ITEM_ACTIVE"]),
        ...mapGetters("query", ["TYPE_OF_PRODUCT"]),
    },

    methods:{
        ...mapMutations("header", [, "SET_CURRENT_TOP_CATEGORY", "SET_CURRENT_SUB_CATEGORY", "SET_CURRENT_LAST_CATEGORY"]),
        ...mapMutations("query", ["SET_TYPE_OF_PRODUCT", "SET_CATEGORY_ID"]),

        toggleCategory(item, event) {
            event.stopPropagation();
            item.filterPanel = !item.filterPanel;
        },

        openMainCategory(category, event){
            event.stopPropagation();
            if (this.TOP_CATEGORIES_ITEM_ACTIVE === category.id) {
                this.SET_CURRENT_TOP_CATEGORY(null);
            } else {
                this.SET_CURRENT_TOP_CATEGORY(category.id);
            }
        },

        openMiddleCategory(category, event){
            event.stopPropagation();
            if (this.SUB_CATEGORIES_ITEM_ACTIVE === category.id) {
                this.SET_CURRENT_SUB_CATEGORY(null);
            } else {
                this.SET_CURRENT_SUB_CATEGORY(category.id);
            }
        },

        openLastCategory(category, event){
            event.stopPropagation();
            this.SET_CATEGORY_ID(category.id);
        },

        changeFilterCategory(event, category){
            event.stopImmediatePropagation();
            event.preventDefault();
            if (this.SUB_CATEGORIES_ITEM_ACTIVE === category.id) {
                this.SET_CURRENT_LAST_CATEGORY(null);
            } else {
                this.SET_CURRENT_LAST_CATEGORY(category.id);
            }
            this.SET_TYPE_OF_PRODUCT(category);
        }
    },
}
</script>

<style scoped lang="scss">
.filter{

    &__block{

    }
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
        color: red;
        font-size: 12px;
        padding: 0px 0 0px 10px;
        cursor: pointer;
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

</style>