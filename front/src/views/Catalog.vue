<template>
  <div class="catalog">
    <div class="catalog__wrapper">
      <div class="catalog__content _container">
        <div class="catalog__body">

          <div class="catalog__block">

<!--        # SIDEBAR-->
            <div class="catalog__sidebar filter">
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
<!--            # PRICE SLIDER-->
                <div class="filter__box">
                  <div class="filter__title icon-arrow-up">Диапазон цен:</div>
                  <div class="price-input">
                    <div class="field">
                      <span>Min</span>
                      <input type="number" class="input-min" value="2500">
                    </div>
                    <div class="separator">-</div>
                    <div class="field">
                      <span>Max</span>
                      <input type="number" class="input-max" value="7500">
                    </div>
                  </div>
                  <div class="slider">
                    <div class="progress"></div>
                  </div>
                  <div class="range-input">
                    <input type="range" class="range-min" min="0" max="10000" value="2500" step="100">
                    <input type="range" class="range-max" min="0" max="10000" value="7500" step="100">
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
                <div class="content-block__item product-row">
                  <div class="product">
                    <div class="product__tag">Хит</div>
                    <a class="product__img" href="">
                      <img class="" src="../assets/image44.png" alt="">
                    </a>
                    <div class="product__info">
                      <div class="product__status icon-done-color _label mb-20">В наличии</div>
                      <div class="product__title">
                        <a  href="">Коммуникационный кабель</a>
                      </div>
                      <div class="product__uptitle">
                        <a  href="">UTP cat.5e (патч-панель) 19″</a>
                      </div>
                      <div class="product__count flex-center">
                        <span class="_label">Количество:</span>
                        <span class="icon-minus"></span>
                        <input class="product__input" type="text">
                        <span class="icon-plus"></span>
                      </div>




                    </div>
                    <div class="product__action">
                      <div class="product__article  _label mb-20">Артикул: <span>331003</span></div>
                      <div class="product__price">
                        <span>70</span>BYN
                        <span>/шт</span>
                      </div>
                      <div class="notice">* Цена указана с учетом НДС.</div>
                      <div class="product__btn flex-center">
                        <div class="product__wishlist icon-favorite"></div>
                        <div class="btn black">В корзину</div>
                      </div>

                    </div>
                  </div>
                </div>
                <div class="content-block__item product-row">
                  <div class="product">
                    <div class="product__tag">Хит</div>
                    <a class="product__img" href="">
                      <img class="" src="../assets/image44.png" alt="">
                    </a>
                    <div class="product__info">
                      <div class="product__status icon-done-color _label mb-20">В наличии</div>
                      <div class="product__title">
                        <a  href="">Коммуникационный кабель</a>
                      </div>
                      <div class="product__uptitle">
                        <a  href="">UTP cat.5e (патч-панель) 19″</a>
                      </div>
                      <div class="product__count flex-center">
                        <span class="_label">Количество:</span>
                        <span class="icon-minus"></span>
                        <input class="product__input" type="text">
                        <span class="icon-plus"></span>
                      </div>




                    </div>
                    <div class="product__action">
                      <div class="product__article  _label mb-20">Артикул: <span>331003</span></div>
                      <div class="product__price">
                        <span>70</span>BYN
                        <span>/шт</span>
                      </div>
                      <div class="notice">* Цена указана с учетом НДС.</div>
                      <div class="product__btn flex-center">
                        <div class="product__wishlist icon-favorite"></div>
                        <div class="btn black">В корзину</div>
                      </div>

                    </div>
                  </div>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

  export default {
    name: 'Catalog',
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
