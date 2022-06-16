<template lang="html">
  <div class="dropdown__content popup-cart">
    <h3 class="">Корзина</h3>
    <div class="popup-cart__summary">
      <div class="div">Товары в корзине: <span>12</span></div>
      <div>на сумму <span>123.89</span><span>BYN</span></div>
    </div>
    <div class="popup-cart__list">
      <div class="popup-cart__item row">
        <div class="popup-cart__img">
          <img src="../../assets/catalog/card1.png" alt="">
        </div>
        <div class="popup-cart__description">
          <div class="popup-cart__title">Коммуникационный кабель</div>
          <div class="popup-cart__uptitle">UTP cat.5e (патч-панель) 19″</div>

        </div>
        <div class="popup-cart__action">
          <div class="popup-cart__price">12.03 <span>BYN</span></div>
          <button class="icon-delete"></button>
        </div>

      </div>
      <div class="popup-cart__item row">
        <div class="popup-cart__img">
          <img src="../../assets/catalog/card1.png" alt="">
        </div>
        <div class="popup-cart__description">
          <div class="popup-cart__title">Коммуникационный кабель</div>
          <div class="popup-cart__uptitle">UTP cat.5e (патч-панель) 19″</div>

        </div>
        <div class="popup-cart__action">
          <div class="popup-cart__price">12.03 <span>BYN</span></div>
          <button class="icon-delete"></button>
        </div>

      </div>
    </div>
    <button class="btn">Оформить заказ</button>
    <div>
      <a class="">Перейти в корзину
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M3 12H20.5M20.5 12L16.5 8M20.5 12L16.5 16" stroke="white"/>
        </svg>
      </a>
    </div>



  </div>

</template>

<script>
export default {
  name: "HeaderCart",
}
</script>

<style lang="scss" scoped>
.popup-cart{
  text-align: center;

  h3{
    font-weight: 500;
    font-size: 20px;
    line-height: 140%;
    text-align: center;
    margin-bottom: 16px;
  }

  &__summary{
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 16px 0;
    font-weight: 300;
    font-size: 14px;
    line-height: 140%;
    color: #423E48;
    opacity: 0.6;
    border-top: 1px solid #F0F0F1;
    border-bottom: 1px solid #F0F0F1;

    div:nth-child(1){
      span{
        font-weight: 500;
        opacity: 1;
      }
    }
    div:nth-child(2){
      span{
        font-weight: 500;
        opacity: 1;
      }


    }

  }

  &__list{
    margin: 30px 0;
  }

  &__item{
    display: grid;
    grid-template-columns: 1fr 2fr 1fr;
    gap:10px;
    align-items: self-start;
    &:hover{
      background: #F9F9F9;
    }

  }

  &__img{
    max-width: 100%;
    img{
      width: 100%;
    }

  }

  &__description{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    font-size: 12px;
    line-height: 140%;
    color: #423E48;
    text-align: left;
  }
  &__title{
    font-weight: 500;

  }
  &_action{
    align-items: stretch;

  }



  &__price{
    font-size: 12px;
    line-height: 140%;

    color: #423E48;
    margin-bottom: 20px;
  }

  .icon-delete{
    text-align: right;
    &:hover{
      color:#4275D8;
    }
  }

  button{
    margin-bottom: 20px;
  }

  a{
    font-weight: 400;
    font-size: 14px;
    line-height: 130%;
    color: #4275D8;
  }


}

</style>
