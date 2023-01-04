<template>
  <div class="catalog">
    <div class="catalog__wrapper">
      <div class="catalog__content _container">
        <div class="catalog__body">

          <div class="catalog__block">

<!--        # SIDEBAR-->
            <div class="catalog__sidebar filter">
              <FilterPanel />
            </div>
<!--        # CONTENT-->
            <div class="content-block">
              <div class="content-block__subcategory recomendation__nav">
                  <div class="recomendation__nav__item">Для кабеля витая пара</div>
                  <div class="recomendation__nav__item">Для коаксиального кабеля</div>
                  <div class="recomendation__nav__item">Маршрутизаторы</div>
              </div>
              <div class="content-block__topfilter topfilter">
                <ul class="tools-sort icon-change">
                  <li class="tools-sort_item">
                    <a href="" class="tools-sort_link">по дате добавления</a>
                  </li>
                  <li class="tools-sort__item">
                    <a href="" class="tools-sort__link active">цене</a>
                  </li>
                  <li class="tools-sort__item">
                    <a href="" class="tools-sort__link">скидке</a>
                  </li>
                </ul>
                <div class="topfilter__right flex-center">

                  <div class="topfilter__page-result">Показывать по: </div>
                  <ul class="tools-pages">
                    <li class="tools-pages__item">
                      <a href="" class="tools-pages__link">10</a>
                    </li>
                    <li class="tools-pages__item">
                      <a href="" class="tools-pages__link active">30</a>
                    </li>
                    <li class="tools-pages__item">
                      <a href="" class="tools-pages__link">60</a>
                    </li>
                  </ul>

                  <ul class="tools-view">

                    <li class="tools-view__item">
                      <a href="catalog/?view=grid" class="tools-view__link icon-catalog-table"></a>
                    </li>
                    <li class="tools-view__item">
                      <a href="catalog/?view=list" class="tools-view__link icon-catalog-row active"></a>
                    </li>
                  </ul>
                </div>


              </div>
              <div class="content-block__list">
                <CatalogItem />
              </div>
              <div class="content-block__pagination">
                <a class="pagination_link active">1</a>
                <a class="pagination_link">2</a>
                <a class="pagination_link">3</a>
                <a class="pagination_link">...</a>
                <a class="pagination_link">5</a>
                <a class="pagination_link">6</a>
              </div>

            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

  import FilterPanel from '@/components/catalog/filter-panel.vue';
  import CatalogItem from '@/components/catalog/catalog-item.vue';
  import {mapGetters, mapActions} from 'vuex'


  export default {
    name: 'Catalog',

    components:
    {
      FilterPanel, CatalogItem
    },

    computed: {
        ...mapGetters("header", ["TOP_CATEGORIES_ITEM_ACTIVE", "SUB_CATEGORIES_ITEM_ACTIVE"]),
    },

    methods: {
      ...mapActions("catalog", ["GET_CATALOG_ITEMS", "GET_ALL_CATALOG_ITEMS"]),

    },

    mounted() {
      if (this.TOP_CATEGORIES_ITEM_ACTIVE && this.SUB_CATEGORIES_ITEM_ACTIVE) {
        this.GET_CATALOG_ITEMS(this.SUB_CATEGORIES_ITEM_ACTIVE||this.TOP_CATEGORIES_ITEM_ACTIVE);
      } else {
        this.GET_ALL_CATALOG_ITEMS();
      }
    }    
  }
</script>

<style scoped lang="scss">

.catalog {

  &__wrapper{

  }
  &__content{

  }

  &__body{
  }



  &__item{


  }
  &__block{
    display: flex;
    align-items: flex-start;

}
  &__sidebar{
    min-width: 260px;
    width: 272px;
    padding-right: 10px;
  }
  .content-block{

  }


}

.content-block{

  &__subcategory{
    display: grid;
    gap: 10px;
    grid-template-columns: repeat(3, minmax(0, 300px));
    text-align: center;
    //padding: 24px 20px 20px 0;

    .recomendation__nav__item{
      background: #FFFFFF;
      border: 1px solid rgba(0, 0, 0, 0.05);
      border-radius: 50px;
      font-size: 14px;
      line-height: 24px;
      text-align: center;
      opacity: 0.5;
      margin-right: 10px;
      padding: 6px 20px;
      //max-width: 25%;
      text-overflow: ellipsis;
      white-space: nowrap;
      overflow: hidden;
      transition: all 0.5s ease;

      cursor: pointer;
      &:hover{
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.08);
        color:#4275D8;
        font-weight: 500;
        opacity: 1;
      }
    }

  }
  &__pagination{
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    padding: 20px 0;
    .pagination_link{
      width: 40px;
      height: 40px;
      background: rgba(66, 62, 72, 0.07);
      border-radius: 2px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #423E48;
      transition: all 0.3s ease;
      &:hover{
        border: 1.2px solid #4275D8;
      }
    }
    .active{
      background: #4275D8;
      color: #fff;
    }
  }
  &__item{
    margin-bottom: 16px;
  }

  &__topfilter{
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 0;
    font-size: 12px;
  }

}

.tools-sort{

}
.tools-pages, .tools-sort{
  display: flex;
  align-items: center;
  gap: 10px;
  margin-right: 20px;
  &__item{
    .active{
      color: #423E48;
      font-weight: 500;
    }

  }
  a{
    font-size: 12px;
    color:#000;
    opacity: 0.8;
    transition: all ease 1ms;
    &:hover{
      color: #423E48;
      opacity: 0.8;
    }
  }
}
.tools-view{
  float: right;
  display: flex;
  align-items: center;
  gap: 10px;
  &__item{
    .active{
      color: #423E48;
    }
  }
  a{
    font-size: 20px;
    color: #ddd;
    transition: all 0.3s ease;
    &:hover{
      color: #423E48;
      opacity: 0.8;
    }
  }


}
.topfilter{

  &__right{

  }
  &__page-result{
    margin-right: 15px;
  }
  &__box-view{
    margin-right: 15px;
    font-size: 20px;
  }
  &__row-view{
    font-size: 20px;

  }
  .active{
    opacity: 0.5;
  }

}

.product{
    display: flex;
    position: relative;
    background: #FFFFFF;
    border: 2px solid #EEEEEE;
    box-sizing: border-box;
    border-radius: 8px;
    padding: 20px 22px 20px 22px;

  ._label{
    font-size: 12px;
    line-height: 20px;
  }

    &__img {
      width: 100%;
      flex-basis: 30%;
      img{
        max-width: 100%;
      }
    }
  &__info{
    flex-basis: 45%;
    padding: 0 10px;

  }

  &__action{
    flex-basis: 25%;
    padding: 0 10px;
  }

    &__tag{
      background: #7700AF;
      border-radius: 2px;
      padding: 2px 11px;
      position: absolute;
      font-weight: 400;
      font-size: 12px;
      left:20px;
      top:20px;
      color: #fff;
    }
    &__wishlist{

      &.added {
        fill: #ff6f60;
        path {
          stroke: #ff6f60;
        }
      }

      cursor: pointer;
      fill: none;
      margin-right: 10px;
    }
  &__price{
    font-size: 20px;
    margin-bottom: 10px;
    text-align: right;
    span:nth-child(1){
      font-weight: 500;
      margin-right: 5px;
    }
  }


    &__row {
      justify-content: space-between;
      &:nth-child(1){
        margin-bottom: 3px;
      }
      &:nth-child(2){
        margin-bottom: 15px;
      }
    }

    &__buy {
      &:before {
        cursor: pointer;
        padding: 10px 10px;
      }
      &:hover{
        background: #4275D8;
        border-radius: 6px;
        color: #fff;
      }


    }

    .notice{
      font-weight: 300;
      font-size: 10px;
      opacity: 0.5;
      text-align: right;
    }



    .current_price {
      font-weight: 500;
      font-size: 20px;
      line-height: 24px;
      span{
        font-weight: 300;
      }

    }

    &__title {
      margin-bottom: 10px;
      a{
        font-weight: 500;
        font-size: 15px;

        color: #423E48;
      }

    }

    &__uptitle {
      a{
        font-weight: 400;
        font-size: 14px;
        line-height: 130%;
        color: #423E48;
      }

    }
  &__status{
    &:before{
      margin-right: 10px;
    }
  }
  &__article{
    text-align: right;
  }

  &__count{
    margin: 24px 0;
    span:nth-child(1){
      margin-right: 10px;
    }

    .icon-plus, .icon-minus{
      cursor: pointer;
    }
  }

  &__input{
    width: 40px;
    height: 40px;
    padding: 9px 8px;
    background: rgba(66, 62, 72, 0.07);
    border-radius: 2px;
    border: none;
    margin: 0 10px;
  }

  &__btn{
    margin: 24px 0 ;
  }

}
//PRICE SLIDER
.price-input{
  width: 100%;
  display: flex;
  margin: 30px 0 35px;
}
.price-input .field{
  display: flex;
  width: 100%;
  height: 45px;
  align-items: center;
}
.field input{
  width: 100%;
  height: 100%;
  outline: none;
  font-size: 19px;
  margin-left: 12px;
  border-radius: 5px;
  text-align: center;
  border: 1px solid #999;
  -moz-appearance: textfield;
}
input[type="number"]::-webkit-outer-spin-button,
input[type="number"]::-webkit-inner-spin-button {
  -webkit-appearance: none;
}
.price-input .separator{
  width: 130px;
  display: flex;
  font-size: 19px;
  align-items: center;
  justify-content: center;
}
.slider{
  height: 5px;
  position: relative;
  background: #ddd;
  border-radius: 5px;
}
.slider .progress{
  height: 100%;
  left: 25%;
  right: 25%;
  position: absolute;
  border-radius: 5px;
  background: #17A2B8;
}
.range-input{
  position: relative;
}
.range-input input{
  position: absolute;
  width: 100%;
  height: 5px;
  top: -5px;
  background: none;
  pointer-events: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}
input[type="range"]::-webkit-slider-thumb{
  height: 17px;
  width: 17px;
  border-radius: 50%;
  background: #17A2B8;
  pointer-events: auto;
  -webkit-appearance: none;
  box-shadow: 0 0 6px rgba(0,0,0,0.05);
}
input[type="range"]::-moz-range-thumb{
  height: 17px;
  width: 17px;
  border: none;
  border-radius: 50%;
  background: #17A2B8;
  pointer-events: auto;
  -moz-appearance: none;
  box-shadow: 0 0 6px rgba(0,0,0,0.05);
}


</style>

<!--<script>-->
<!--  const rangeInput = document.querySelectorAll(".range-input input"),-->
<!--  priceInput = document.querySelectorAll(".price-input input"),-->
<!--  range = document.querySelector(".slider .progress");-->
<!--  let priceGap = 1000;-->

<!--  priceInput.forEach(input =>{-->
<!--    input.addEventListener("input", e =>{-->
<!--          let minPrice = parseInt(priceInput[0].value),-->
<!--          maxPrice = parseInt(priceInput[1].value);-->

<!--          if((maxPrice - minPrice >= priceGap) && maxPrice <= rangeInput[1].max){-->
<!--            if(e.target.className === "input-min"){-->
<!--                  rangeInput[0].value = minPrice;-->
<!--                  range.style.left = ((minPrice / rangeInput[0].max) * 100) + "%";-->
<!--            }else{-->
<!--                  rangeInput[1].value = maxPrice;-->
<!--                  range.style.right = 100 - (maxPrice / rangeInput[1].max) * 100 + "%";-->
<!--            }-->
<!--          }-->
<!--    });-->
<!--  });-->

<!--  rangeInput.forEach(input =>{-->
<!--    input.addEventListener("input", e =>{-->
<!--          let minVal = parseInt(rangeInput[0].value),-->
<!--          maxVal = parseInt(rangeInput[1].value);-->

<!--          if((maxVal - minVal) < priceGap){-->
<!--            if(e.target.className === "range-min"){-->
<!--                rangeInput[0].value = maxVal - priceGap-->
<!--            }else{-->
<!--                rangeInput[1].value = minVal + priceGap;-->
<!--            }-->
<!--          }else{-->
<!--            priceInput[0].value = minVal;-->
<!--            priceInput[1].value = maxVal;-->
<!--            range.style.left = ((minVal / rangeInput[0].max) * 100) + "%";-->
<!--            range.style.right = 100 - (maxVal / rangeInput[1].max) * 100 + "%";-->
<!--      }-->
<!--    });-->
<!--  });-->

<!--</script>-->
