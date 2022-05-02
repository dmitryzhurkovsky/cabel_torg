<template>
  <div class="product">
    <div class="product__wrapper">
      <div class="product__content _container">
        <div class="product__body">
          <ul class="breadcrumb">
            <li><a href="#">Главная</a></li>
            <li class="breadcrumb__separater icon-arrow-l"></li>
            <li><a href="#">Раздел</a></li>
            <li class="breadcrumb__separater icon-arrow-l"></li>
            <li><a href="#">Подраздел</a></li>
            <li class="breadcrumb__separater icon-arrow-l">-</li>
            <li class="active">Название товара</li>
          </ul>
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
                <span _label>Количество</span>
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
                    <span>70</span>BYN
                    <span>/шт</span>
                  </div>
                  <div class="opt_price">
                    <span>Оптовая цена: </span>
                    <span>70</span>BYN
                    <span>/шт</span>
                  </div>
                </div>


              </div>
              <div _footnote>* Все цены указаны с учетом НДС.</div>
              <div class="product__btn btn">Заказать</div>
              <div class="_label icon-favorite"></div>
              <a class="product__link">Как оформить заказ ></a>

            </div>
            
            
          </div>







        </div>
      </div>
    </div>
  </div>
</template>

<script>

  export default {
    name: 'Card_product',
  }
</script>

<style scoped lang="scss">

.product {

  &__wrapper{


  }
  &__content{

  }

  &__body{


  }
  &__header{


  }
  &__block {
    display: flex;
    align-items: flex-start;


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


}
.desc-product{
  font-size: 14px;

  &__title{
    font-weight: 500;
    font-size: 20px;
    line-height: 28px;
    color: #423E48;
    margin: 8px 0;
  }

  &__arcticle{

  }
  &__status{
    line-height: 20px;
    padding: 18px 0 20px 0;
  }
  &__count{


  }

  &__input{
    width: 50px;
    height: 50px;
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
  }

  &__btn{
    background: #423E48;
  }

  &__link{

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

}


</style>