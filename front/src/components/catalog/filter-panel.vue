<template>
    <div class="filter__block">
        <div class="filter__box" 
            v-for   = "item in TOP_CATEGORIES"
            :key    = "item.id"
            @click  = "changeCategory(item.id, $event)"
        >
            <div class="filter__title icon-arrow-up">{{item.name}}</div>
            <div class="filter__block"  v-if = "item.id === TOP_CATEGORIES_ITEM_ACTIVE">
                <div class="filter__box" 
                    v-for   = "sub in SUB_CATEGORIES"
                    :key    = "sub.id"
                    @click  = "subCategoryClick(sub.id, $event)"
                >
                    <div class="filter__title icon-arrow-up">{{sub.name}}</div>
                    <div class="filter__checkbox-list"  v-if = "sub.id === SUB_CATEGORIES_ITEM_ACTIVE">
                        <div class="filter__checkbox__item"
                            v-for = "subItem in sub.subItems"
                            :key  = "subItem.id"
                            @click = "subItemCategoryClick(subItem.id, $event)"
                        >
                            <div class="checkbox-default">
                                <label class="checkbox__label">
                                    <input type="checkbox" name="" class="" value="">
                                    <div class="checkbox"></div>
                                    <div class="filter__text">
                                        <span class="">{{subItem.name}}</span>
                                    </div>
                                </label>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </div>

        <div class="filter__box">
            <div class="filter__title icon-arrow-up">Показывать:</div>

            <div class="filter__checkbox-list">
            <div class="filter__checkbox__item">
                <div class="checkbox-default">
                <label class="checkbox__label">
                    <input type="checkbox" name="" class="" value="">
                    <div class="checkbox"></div>
                    <div class="filter__text">
                    <span class="">Все товары</span>
                    </div>
                </label>
                </div>
            </div>
            <div class="filter__checkbox__item">
                <div class="checkbox-default">
                <label class="checkbox__label">
                    <input type="checkbox" name="" class="" value="">
                    <div class="checkbox"></div>
                    <div class="filter__text">
                    <span class="">Только товары со скидкой</span>
                    </div>
                </label>
                </div>
            </div>
            <div class="filter__checkbox__item">
                <div class="checkbox-default">
                <label class="checkbox__label">
                    <input type="checkbox" name="" class="" value="">
                    <div class="checkbox"></div>
                    <div class="filter__text">
                    <span class="">Только “В наличии”</span>
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

    computed: {
        ...mapGetters("header", ["TOP_CATEGORIES_ITEM_ACTIVE", "SUB_CATEGORIES_ITEM_ACTIVE", "TOP_CATEGORIES", "SUB_CATEGORIES"]),
    },

    watch: {

    },

    methods:{
        ...mapMutations("header", ["SET_CURRENT_TOP_CATEGORY", "SET_CURRENT_SUB_CATEGORY"]),
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
            console.log('SUB', id);
            if (this.SUB_CATEGORIES_ITEM_ACTIVE === id) {
                this.SET_CURRENT_SUB_CATEGORY(null);
            } else {
                this.SET_CURRENT_SUB_CATEGORY(id);
            }
        },
        subItemCategoryClick(id, event){
            event.stopImmediatePropagation();
            event.preventDefault();
            console.log('кликнули по итему подкатегории ', id, event);
        },

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
&__text{
  span{
    font-weight: 400;
    font-size: 14px;
    color: #423E48;
  }

}

}
</style>