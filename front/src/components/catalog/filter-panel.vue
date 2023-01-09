<template>
    <div class="filter__block">
        <div class="filter__box" 
            v-for   = "item in TOP_CATEGORIES"
            :key    = "item.id"
            @click  = "changeCategory(item.id, $event)"
        >
            <div class="filter__title icon-arrow-l">{{item.name}}</div>
            <div class="filter__block"  v-if = "item.id === TOP_CATEGORIES_ITEM_ACTIVE">
                <div class="filter__box" 
                    v-for   = "sub in SUB_CATEGORIES"
                    :key    = "sub.id"
                    @click  = "subCategoryClick(sub.id, $event)"
                >
                    <div class="filter__subtitle">{{sub.name}}</div>
                    <div class="filter__checkbox-list filter__subtitle-child "  v-if = "sub.id === SUB_CATEGORIES_ITEM_ACTIVE">
                        <div class="filter__subtitle-child"
                            v-for = "subItem in sub.subItems"
                            :key  = "subItem.id"
                            @click = "subItemCategoryClick(subItem.id, $event)"
                        >
                            <div class="checkbox-default">
                              <div class="filter__text filter__subtitle-child">
                                {{subItem.name}}
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
    </div>

</template>

<script>

import {mapMutations, mapGetters} from 'vuex'

export default {
    name: 'FilterPanel',

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
        ...mapGetters("header", ["TOP_CATEGORIES_ITEM_ACTIVE", "SUB_CATEGORIES_ITEM_ACTIVE", "TOP_CATEGORIES", "SUB_CATEGORIES"]),
        ...mapGetters("query", ["TYPE_OF_PRODUCT"]),

    },

    methods:{
        ...mapMutations("header", ["SET_CURRENT_TOP_CATEGORY", "SET_CURRENT_SUB_CATEGORY"]),
        ...mapMutations("query", ["SET_TYPE_OF_PRODUCT", "SET_CATEGORY_ID"]),

        changeCategory(newActive, event){
            if (this.TOP_CATEGORIES_ITEM_ACTIVE === newActive) {
                this.SET_CURRENT_TOP_CATEGORY(null);
            } else {
                this.SET_CURRENT_TOP_CATEGORY(newActive);
            }
        },
        subCategoryClick(id, event){
            event.stopImmediatePropagation();
            event.preventDefault();
            if (this.SUB_CATEGORIES_ITEM_ACTIVE === id) {
                this.SET_CURRENT_SUB_CATEGORY(null);
            } else {
                this.SET_CURRENT_SUB_CATEGORY(id);
            }
        },
        subItemCategoryClick(id, event){
            event.stopImmediatePropagation();
            event.preventDefault();
            // console.log('кликнули по итему подкатегории ', id, event);
            this.SET_CATEGORY_ID(id);
        },
        changeFilterCategory(event, category){
            event.stopImmediatePropagation();
            event.preventDefault();
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
        margin: 0px 15px 10px 0px;
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