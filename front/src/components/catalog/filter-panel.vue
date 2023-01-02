<template>
    <div class="filter__block">
        <div class="filter__box">
            <div class="filter__title icon-arrow-up">Тип оборудования</div>

            <div class="filter__checkbox-list">
            <div class="filter__checkbox__item">
                <div class="checkbox-default">
                <label class="checkbox__label">
                    <input type="checkbox" name="" class="" value="">
                    <div class="checkbox"></div>
                    <div class="filter__text">
                    <span class="">Кабели и провода</span>
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
                    <span class="">Сетевое оборудование</span>
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
                    <span class="">Группа 3</span>
                    </div>
                </label>
                </div>
            </div>
            </div>


        </div>
        <div class="filter__box">
            <div class="filter__title icon-arrow-up">Категория</div>

            <div class="filter__checkbox-list">
            <div class="filter__checkbox__item">
                <div class="checkbox-default">
                <label class="checkbox__label">
                    <input type="checkbox" name="" class="" value="">
                    <div class="checkbox"></div>
                    <div class="filter__text">
                    <span class="">Плинты размыкаетмые</span>
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
                    <span class="">Коннекторы, разъемы, соединители</span>
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
                    <span class="">Категория 3</span>
                    </div>
                </label>
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

import {mapActions, mapGetters} from 'vuex'

export default {
    name: 'FilterPanel',

    computed: {
    // ...mapGetters("header", ["IS_CATALOG_OPEN", "TOP_CATEGORIES"]),
    // ...mapGetters("order", ["ORDER_COUNT"]),
    },

    methods:{

    }    
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