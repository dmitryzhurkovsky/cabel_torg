<template>
  <div class="user-acc">
    <div class="user-acc__wrapper">
      <div class="user-acc__content _container">
        <div class="user-acc__body">
          <ul class="breadcrumb">
            <li><a href="#">Главная</a></li>
            <li class="breadcrumb__separater icon-arrow-l"></li>
            <li><a href="#">Личный кабинет</a></li>
            <li class="breadcrumb__separater icon-arrow-l"></li>
            <li><a href="#">История покупок</a></li>
          </ul>

          <div class="user-acc__block">
<!--        # SIDEBAR-->
            <div class="user-acc__sidebar filter">
              <div class="filter__block">
                <div class="filter__box">
                  <div class="filter__title icon-arrow-up">Личный кабинет</div>

                  <ul class="filter__list">
                     <li class="filter__item icon-cart">Мои заказы</li>
                     <li class="filter__item icon-favorite-choosed">Избранные товары</li>
                     <li class="filter__item icon-setting">Настройки аккаунта</li>
                  </ul>
                  <hr class="hr">
                  <div class="icon-exit filter__item">Выйти из аккаунта</div>
                </div>

              </div>
            </div>
<!--        # CONTENT-->
            <div class="user-acc__content-block content-block">
              <div class="content-block__title">История покупок</div>
               <div class="order__list">
                 <div class="order__item">
                   <div class="order__num">Заказ #  <span>65854</span></div>
                   <div class="order__date">10 июня 2022</div>
                   <div class="order__delivery">Тип доставки</div>
                   <div class="order__status _status-color">Отправлен</div>
                   <div class="order__price">58.40 <span>BYN</span></div>
                 </div>

                 <div class="order__item">
                   <div class="order__num">Заказ #  <span>65854</span></div>
                   <div class="order__date">10 июня 2022</div>
                   <div class="order__delivery">Тип доставки</div>
                   <div class="order__status _status-color">Отправлен</div>
                   <div class="order__price">58.40 <span>BYN</span></div>
                 </div>

                 <div class="order__item">
                   <div class="order__num">Заказ #  <span>65854</span></div>
                   <div class="order__date">10 июня 2022</div>
                   <div class="order__delivery">Тип доставки</div>
                   <div class="order__status _status-color">Отправлен</div>
                   <div class="order__price">58.40 <span>BYN</span></div>
                 </div>

                 <div class="order__item">
                   <div class="order__num">Заказ #  <span>65854</span></div>
                   <div class="order__date">10 июня 2022</div>
                   <div class="order__delivery">Тип доставки</div>
                   <div class="order__status _status-color">Отправлен</div>
                   <div class="order__price">58.40 <span>BYN</span></div>
                 </div>

                 <div class="order__item">
                   <div class="order__num">Заказ #  <span>65854</span></div>
                   <div class="order__date">10 июня 2022</div>
                   <div class="order__delivery">Тип доставки</div>
                   <div class="order__status _status-color">Отправлен</div>
                   <div class="order__price">58.40 <span>BYN</span></div>
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
    name: 'user-cab',
  }
</script>

<style scoped lang="scss">

.user-acc {

  &__wrapper{

  }
  &__content-block{
    width: 100%;
    padding: 0 16px;
  }

  &__body{
  }
  &__block{
    display: flex;
    align-items: flex-start;

  }
  &__sidebar{
    width: 270px;
  }


  &__item{

  }
  &__link{

}

}
.filter{

  &__block{

  }

  &__box{
    font-weight: 400;
    position: relative;

  }
  &__list{

  }
  .hr{
    height:2px;
    margin:24px 0 24px 0;
    background:#F0F0F1;
  }

  &__item{
    font-size: 14px;
    line-height: 24px;
    color: #423E48;
    margin-bottom: 8px;

    &:hover{
      color:#4275D8;
      cursor: pointer;
    }
    &:before{
      margin-right: 10px;
    }
  }

  &__title{
    background: #eceef1;
    padding: 6px 8px;
    font-weight: 500;
    font-size: 14px;
    line-height: 24px;
    color: #423E48;
    margin: 0 0 12px 0;
    &:before{
      position: absolute;
      top: 16px;
      right: 10px;
      font-size: 6px;
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


.content-block{
  &__title{
    font-weight: 500;
    font-size: 20px;
    line-height: 24px;
    color: #423E48;
    margin-bottom: 40px;
  }
}
.order{

  &__list{

  }
  &__item{
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 30px 18px 30px 28px;
    background: #FFFFFF;
    border: 2px solid #EEEEEE;
    border-radius: 8px;
    margin-bottom: 16px;
    ._status-color{
      color: #32A071;
      font-weight: 500;
    }
  }
  &__num{
    font-weight: 500;
    font-size: 16px;
    line-height: 24px;
    text-decoration-line: underline;
    color: #423E48;
    z-index: 4;
    &:hover{
      color: #4275D8;
      cursor: pointer;
    }
  }
  &__date{

  }

  &__delivery{

  }

  &__status{

  }



  &__price{
    font-weight: 500;
    span{
      font-weight: 400;
    }
  }
}
</style>