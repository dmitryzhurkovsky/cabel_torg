<template>
  <div class="recomendation">
    <div class="recomendation__wrapper">
      <div class="recomendation__content _container">
        <div class="recomendation__body">

          <h3>Рекомендации для вас</h3>
          <div class="recomendation__nav flex-center">
            <div class="recomendation__nav__item">Топ продаж</div>
            <div class="recomendation__nav__item">Новинки</div>
            <div class="recomendation__nav__item">Скидки</div>
          </div>
          <div class="recomendation__block">
            <div class="recomendation__block__item item-card">
              <div class="item-card__label">Хит</div>
              <div class="item-card__img">
                <img class="" src="../../assets/image44.png" alt="">
              </div>
              <div class="item-card__info">
                <div class="item-card__row flex-center">
                  <div class="old_price">65.3</div>
                  <div class="notice">* Цена указана с учетом НДС.</div>
                </div>

                <div class="item-card__row flex-center">
                  <div class="current_price">56.5
                    <span>BYN/шт.</span>
                  </div>
                  <div class="item-card__block flex-center">
                    <img src="../../assets/svg/cart.svg" alt="Cart">
                  </div>

                </div>

                  <div class="item-card__title">Коммуникационный кабель</div>
                  <div class="item-card__uptitle">UTP cat.5e (патч-панель) 19″</div>


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
    name: 'Recomendation',
  }
</script>

<style scoped lang="scss">

.recomendation {

  &__wrapper{

  }
  &__content{

  }

  &__body{
  }

  &__block{
    &__item{
      width: 100%;
      max-width: 272px;
    }

  }
  &__nav{
    padding: 10px 0;
    justify-content: flex-start;
    &__item{

      background: #FFFFFF;
      border: 1px solid rgba(0, 0, 0, 0.05);
      border-radius: 50px;
      font-size: 14px;
      line-height: 24px;
      text-align: center;
      opacity: 0.5;
      margin-right: 10px;
      padding: 6px 40px;
      cursor: pointer;
      &:hover{
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.08);
        color:#4275D8;
        font-weight: 500;
      }

    }
  }


  &__item{

  }
  &__link{

}

}

//Карточка товара

.item-card {
  display: flex;
  flex-direction: column;
  position: relative;
  background: #FFFFFF;
  border: 2px solid #EEEEEE;
  box-sizing: border-box;
  border-radius: 8px;
  padding: 20px 22px 30px 22px;

  &__img {
    width: 100%;

    img{
      max-width: 100%;
    }

  }

  &__label{
    background: #7700AF;
    border-radius: 2px;
    padding: 2px 11px;
    position: absolute;
    font-weight: 400;
    font-size: 12px;
    left:10px;
    top:10px;
    color: #fff;
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

  &__block {
    &:hover{
      width: 20px;
      height:20px;
      padding: 10px 10px;
      background: #4275D8;
      border-radius: 6px;
      cursor: pointer;
    }
    img{

    }

  }

  .notice{
    font-weight: 300;
    font-size: 10px;
    line-height: 20px;
    opacity: 0.5;
  }

  .old_price {
    font-size: 16px;
    line-height: 24px;
    text-decoration-line: line-through;
    opacity: 0.4;

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
    font-weight: 500;
    font-size: 15px;
    margin-bottom: 5px;
  }

  &__uptitle {
    font-weight: 400;
    font-size: 14px;
    line-height: 130%;
  }

}

</style>