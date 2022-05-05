<template>
  <div class="product">
    <div class="product__wrapper">
      <div class="product__content _container">
        <div class="product__body">

          <div class="grid ">
            <div class="grid__item" tabindex="1">
              <div class="product__main-img">
                <img src="../assets/catalog/card1.png" alt="">
              </div>
            </div>
            <div class="grid__item" tabindex="2">
              <div class="product__add-img add-img">
                <!--                <img class="add-img__item" src="../assets/catalog/card1.png" alt="">-->
                <!--                <img class="add-img__item" src="../assets/catalog/card1.png" alt="">-->
              </div>
            </div>
            <div class="grid__item" tabindex="3">
              <div class="desc-product__title">Вилка RJ-45 cat 6 UTP для витой пары 8P8C (100 шт)</div>
            </div>
            <div class="grid__item" tabindex="4">
              <div class="desc-product__article  _label">Артикул: <span>331003</span></div>
            </div>
            <div class="grid__item" tabindex="5">
              <ul class="breadcrumb">
                <li><a href="#">Главная</a></li>
                <li class="breadcrumb__separater icon-arrow-l"></li>
                <li><a href="#">Раздел</a></li>
                <li class="breadcrumb__separater icon-arrow-l"></li>
                <li><a href="#">Подраздел</a></li>
                <li class="breadcrumb__separater icon-arrow-l"></li>
                <li class="active">Название товара</li>
              </ul>
            </div>
            <div class="grid__item" tabindex="6">
              <div class="status-row__link icon-share"><span>Поделиться</span></div>
            </div>
            <div class="grid__item" tabindex="7">
              <div class="desc-product__status icon-done-color _label">В наличии</div>
            </div>
            <div class="grid__item" tabindex="8">
              <div class="price-product__block">
                <div class="_label">Ваша цена:</div>
                <div class="current_price">
                  <span>70</span>BYN
                  <span>/шт</span>
                </div>
              </div>
            </div>
            <div class="grid__item" tabindex="9">
              <div class="product__favorite icon-favorite"></div>
            </div>
            <div class="grid__item" tabindex="10">
              <div class="price-product__block">
                <div class="retail_price">
                  <div>Розничная цена: </div>
                  <div>
                    <span>70</span>BYN
                    <span>/шт</span>
                  </div>

                </div>
                <div class="opt_price">
                  <div>Оптовая цена: </div>
                  <div>
                    <span>70</span>BYN
                    <span>/шт</span>
                  </div>

                </div>
              </div>
            </div>
            <div class="grid__item" tabindex="11">
              <div class="product__btn btn">В корзину</div>
            </div>

            <div class="grid__item" tabindex="12">
              <div class="desc-product__count">
                <span class="_label">Количество</span>
                <span class="icon-minus"></span>
                <input class="desc-product__input" type="text">
                <span class="icon-plus"></span>
              </div>
            </div>
            <div class="grid__item" tabindex="13">
              <a class="product__link">Как оформить заказ ></a>
            </div>
          </div>


          <div class="product__status-row status-row">
            <ul class="breadcrumb">
              <li><a href="#">Главная</a></li>
              <li class="breadcrumb__separater icon-arrow-l"></li>
              <li><a href="#">Раздел</a></li>
              <li class="breadcrumb__separater icon-arrow-l"></li>
              <li><a href="#">Подраздел</a></li>
              <li class="breadcrumb__separater icon-arrow-l"></li>
              <li class="active">Название товара</li>
            </ul>
            <div class="status-row__link icon-share"><span>Поделиться</span></div>
          </div>


          <div class="product__block">
            <div class="_block">
              <div class="product__main-img">
                <img src="../assets/catalog/card1.png" alt="">
              </div>
              <div class="product__add-img add-img">
<!--                <img class="add-img__item" src="../assets/catalog/card1.png" alt="">-->
<!--                <img class="add-img__item" src="../assets/catalog/card1.png" alt="">-->
              </div>
            </div>
            <div class="_block product__desc desc-product">
              <div class="desc-product__title">Вилка RJ-45 cat 6 UTP для витой пары 8P8C (100 шт)</div>
              <div class="desc-product__article  _label">Артикул: <span>331003</span></div>
              <div class="desc-product__status icon-done-color _label">В наличии</div>
              <div class="desc-product__count">
                <span class="_label">Количество</span>
                <span class="icon-minus"></span>
                <input class="desc-product__input" type="text">
                <span class="icon-plus"></span>
              </div>
              <div class="desc-product__price price-product">
                <div class="price-product__block">
                  <div class="_label">Ваша цена:</div>
                  <div class="current_price">
                    <span>70</span>BYN
                    <span>/шт</span>
                  </div>
                </div>
                <div class="price-product__block">
                  <div class="retail_price">
                    <span>Розничная цена: </span>
                    <div>
                      <span>70</span>BYN
                      <span>/шт</span>
                    </div>

                  </div>
                  <div class="opt_price">
                    <span>Оптовая цена: </span>
                    <div>
                      <span>70</span>BYN
                      <span>/шт</span>
                    </div>

                  </div>
                </div>


              </div>
              <div class="_footnote">* Все цены указаны с учетом НДС.</div>
              <div class="product__action flex-center">
                <div class="product__btn btn">В корзину</div>
                <div class="product__favorite icon-favorite"></div>
              </div>

              <a class="product__link">Как оформить заказ ></a>

           </div> <!-- desc-product-->
            
            
          </div>







        </div>
      </div>
    </div>
  </div>
</template>

<script>

  export default {
    name: 'Card_product_grid',
  }
</script>

<style scoped lang="scss">

.grid {
  display: grid;
  align-items: start;
  justify-items: start;
  //grid-gap: 1.5vw;
  //min-height: 100vh;
  //padding: 1.5vw;
  &__item{
    padding: 5px 0;
  }
}

.grid {
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows:auto;

  grid-template-areas:
      "breadcrumb breadcrumb"
      "photo   photo"
      "status   status"
      "title   title"
      "arcticle arcticle"
      "add_price wishlist"
      "count count"
      "price cart_button"
      "link link";
}
.grid .item:nth-child(6){
  display: none;
}

@media screen and (min-width: $md2+px) {
  .grid {
    grid-template-columns: repeat(5, 1fr);
    grid-template-rows: auto;

    grid-template-areas:
        "breadcrumb breadcrumb breadcrumb breadcrumb breadcrumb "
        "title title  title title title"
        "photo photo photo arcticle status"
        "photo photo photo add_price add_price"
        "photo photo photo count count"
        "photo photo photo price price"
        "photo photo photo cart_button wishlist"
        "big1 big1 big1 link link";
  }
  .grid .item:nth-child(6){
    display: none;
  }
}

@media screen and (min-width: $md1+px) {
  .grid {
    grid-template-columns: repeat(6, 1fr);
    grid-template-rows: auto;
    grid-template-areas:
      "breadcrumb breadcrumb  breadcrumb breadcrumb share  share"
      "photo photo photo title title title"
      "photo photo photo arcticle arcticle arcticle"
      "photo photo photo status status status"
      "photo photo photo count count count"
      "photo photo photo price add_price add_price"
      "big1 big1 big1 cart_button cart_button wishlist"
      "big1 big1 big1 link link link";
  }
}

.grid__item:nth-child(1)  { grid-area: photo; }
.grid__item:nth-child(2)  { grid-area: big1; }
.grid__item:nth-child(3)  { grid-area: title; }
.grid__item:nth-child(4)  { grid-area: arcticle; }
.grid__item:nth-child(5)  { grid-area: breadcrumb; }
.grid__item:nth-child(6)  { grid-area: share; }
.grid__item:nth-child(7)  { grid-area: status; }
.grid__item:nth-child(8)  { grid-area: price; }
.grid__item:nth-child(9)  { grid-area: wishlist; }
.grid__item:nth-child(10) { grid-area: add_price; }
.grid__item:nth-child(11) { grid-area: cart_button; }
.grid__item:nth-child(12) { grid-area: count; }
.grid__item:nth-child(13) { grid-area: link; }




.product {

  &__wrapper{


  }
  &__content{

  }

  &__body{


  }
  &__status-row{

    display: flex;
    align-items: center;
    justify-content: space-between;
    @media (max-width: $md3+px) {
      flex-direction: column;
      align-items: flex-start;
    }

    .status-row__link{
      font-weight: 300;
      font-size: 12px;
      line-height: 16px;

      @media (max-width: $md3+px) {
        text-align: right;
        width: 100%;
        span{
          display: none;
        }
      }
    }
  }
  &__block {
    display: flex;
    align-items: flex-start;
    @media (max-width: $md3+px) {
      flex-direction: column;
    }


    ._block{
      flex-basis: 50%;

      &:nth-child(1){
        display: flex;
        flex-direction: column;

      }

      &:nth-child(2){

      }


    }
  }
  &__main-img{

    flex-basis: 80%;
    img{
      width: 100%;
    }


  }
  &__add-img{

    flex-basis: 20%;
    img{
      width: 100%;
    }


  }
  &__btn{
    background: #423E48;
    margin-right: 20px;
    font-weight: 400;
    padding: 13px 40px;


  }
  &__favorite{
    cursor: pointer;

  }
  &__link{
    font-size: 14px;
    opacity: 0.7;
  }
  &__action{
    margin:30px 0 20px 0;
  }

}
.desc-product{
  font-size: 14px;

  &__title{
    font-weight: 500;
    font-size: 20px;
    line-height: 28px;
    color: #423E48;
  }

  &__arcticle{

  }
  &__status{
    line-height: 20px;
    &:before{
      margin-right: 10px;
    }
  }
  &__count{
      span{
        &:nth-child(1){
          margin-right: 10px;
        }
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

  &__price{
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #F9F9F9;
    padding: 22px 18px 20px 18px;
    .retail_price{

    }
  }


  &__favorive{
    cursor: pointer;
    &:hover{
      background: red;
    }
  }



}
._footnote{
  font-size: 10px;
  line-height: 20px;
  text-align: right;
  opacity: 0.5;
}
.current_price{
  font-weight: 500;
  font-size: 24px;
  line-height: 36px;
  span{
    margin-right: 10px;
    &:nth-child(2){
      font-weight: 300;
    }
  }
}

.retail_price, .opt_price{
  display: flex;
  align-items: center;
  justify-content: space-between;

}

.opt_price{
margin-top: 15px;
}

</style>