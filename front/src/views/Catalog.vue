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
                <div class="topfilter__share icon-change"> По популярности</div>
                <div class="topfilter__right flex-center">
                  <div class="topfilter__page-result">Показывать по <span>10</span> </div>
                  <div class="topfilter__box-view icon-catalog-table"></div>
                  <div class="topfilter__row-view icon-catalog-row active"></div>
                </div>
              </div>
              <div class="content-block__list">
                <CatalogItem />
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

  export default {
    name: 'Catalog',

    components:
    {
      FilterPanel, CatalogItem
    },

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
    width: 270px;
  }
  .content-block{

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
      cursor: pointer;
      &:hover{
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.08);
        color:#4275D8;
        font-weight: 500;
        opacity: 1;
      }
    }
  }

  &__topfilter{
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 0;
    font-size: 12px;
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
