<template>
  <div class="cart">
    <div class="cart__wrapper">
      <div class="cart__content _container">
        <div class="cart__body">
          <ul class="breadcrumb">
            <li><a href="#">Главная</a></li>
            <li class="breadcrumb__separater icon-arrow-l"></li>
            <li><a href="#">Корзина</a></li>

          </ul>

          <div class="cart__block">
            <h3>Корзина <span>(4)</span></h3>

<!--            Если корзина пуста то это выводится, и сверху ноль возле Корзины-->
            <div class="cart__list">
              <div class="cart__empty__item">Ваша корзина пуста</div>
              <a class="_link">
                <svg width="16" height="8" viewBox="0 0 16 8" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M15.5 3.99935H0.916666M0.916666 3.99935L4.25 0.666016M0.916666 3.99935L4.25 7.33268" stroke="#4275D8"/>
                </svg>
                Вернуться к покупкам
              </a>
            </div>
            <!-- Если в корзине есть товар, и сверху число товаров возле Корзины-->

            <div class="cart__list">
              <div class="cart__item">
                  <a class="product__img" href="">
                    <img class="" src="../../assets/image44.png" alt="">
                  </a>
                  <div class="product__info">
                    <div class="product__article  _label mb-20">Артикул: <span>331003</span></div>
                    <a  class="product__title" href="">Вилка RJ-45 cat 5E FTP для витой пары 8P8C (100 шт) экранированная</a>
                    <div class="icon__row mt-20">
                      <span class="icon icon-favorite">В избранное</span>
                      <span class="icon icon-delete">Удалить</span>
                    </div>
                  </div>
                  <div class="product__count flex-center">
                    <div class="_label mb-20">Количество:</div>
                    <div class="flex-center">
                      <span class="icon-minus"></span>
                      <input class="product__input" type="text">
                      <span class="icon-plus"></span>
                    </div>

                  </div>


                  <div class="product__price">
                    <div class="_label mb-20">Стоимость (с учетом НДС):</div>
                    <div class="old_price">
                      <span>70</span>BYN
                      <span>/шт</span>
                    </div>
                    <div class="current_price">
                      <span>59.5</span> BYN

                    </div>
                  </div>
                </div>
              <div class="cart__item">
                <a class="product__img" href="">
                  <img class="" src="../../assets/image44.png" alt="">
                </a>
                <div class="product__info">
                  <div class="product__article  _label mb-20">Артикул: <span>331003</span></div>
                  <a  class="product__title" href="">Вилка RJ-45 cat 5E FTP для витой пары 8P8C (100 шт) экранированная</a>
                  <div class="icon__row mt-20">
                    <span class="icon icon-favorite">В избранное</span>
                    <span class="icon icon-delete">Удалить</span>
                  </div>
                </div>
                <div class="product__count flex-center">
                  <div class="_label mb-20">Количество:</div>
                  <div class="flex-center">
                    <span class="icon-minus"></span>
                    <input class="product__input" type="text">
                    <span class="icon-plus"></span>
                  </div>

                </div>


                <div class="product__price">
                  <div class="_label mb-20">Стоимость (с учетом НДС):</div>
                  <div class="old_price">
                    <span>70</span>BYN
                    <span>/шт</span>
                  </div>
                  <div class="current_price">
                    <span>59.5</span> BYN

                  </div>
                </div>
              </div>
            </div>
            <div class="cart__footer flex-center">
              <div class="group cart-promo">
                <label for="promo" class="label">Промокод</label>
                <div class="input__box">
                  <input id="promo" type="text" class="input">
                  <button class="btn black">Применить</button>
                </div>
              </div>
              <div class="cart__summary">
                <div class="_footnote">* Сумма указана с учетом НДС</div>
                <div class="label flex-center ">
                  Общая стоимость:
                  <span>102.8</span>
                   BYN
                </div>
                <div class="">
                  <button class="btn">Оформить заказ</button>
                </div>
              </div>
            </div>
          </div>

          <!-- Появляется если есть товар в корзине  и человек наживаем кнопку оформить заказ -->

          <div class="cart__order ">
            <h3>Оформление заказа </h3>
            <div class="about__paragraph">
              <div class="about__paragraph__title">
                <span>Доставка</span>
              </div>
              <div class="about__paragraph__box flex-center">
                <div class="group table3x">
                  <label for="city" class="label">Город / населенный пункт</label>
                  <input id="city" type="text" class="input">
                </div>
                <div class="radio__list table3x">
                  <div class="radio">
                    <input id="radio-1" name="radio" type="radio" checked>
                    <label for="radio-1" class="radio-label">Самовывоз со склада в г. Минск (9:00-18:00), <b>бесплатно</b></label>
                  </div>

                  <div class="radio">
                    <input id="radio-2" name="radio" type="radio">
                    <label  for="radio-2" class="radio-label">Самовывоз со склада в г. Брест (9:00-18:00), <b>бесплатно</b></label>
                  </div>

                  <div class="radio">
                    <input id="radio-3" name="radio" type="radio">
                    <label  for="radio-3" class="radio-label">Доставка по РБ при заказе от 500 рублей, <b>бесплатно</b></label>
                  </div>

                  <div class="radio">
                    <input id="radio-4" name="radio" type="radio">
                    <label  for="radio-4" class="radio-label">Платная доставка, стоимость обсуждается индивидуально</label>
                  </div>

                </div>

                <div class="table3x">
                  <div class="group">
                    <label for="city" class="label">Улица</label>
                    <input id="city" type="text" class="input">
                  </div>
                  <div class="group__row flex-center">
                    <div class="group">
                      <input id="city" type="text" class="input">
                    </div>
                    <div class="group">
                      <input id="city" type="text" class="input">
                    </div>
                  </div>

                </div>
              </div>
            </div>
            <div class="about__paragraph">
              <div class="about__paragraph__title">
                <span>Контактная информация</span>
              </div>
              <div class="about__paragraph__box flex-center group__row">
                <div class="group ">
                  <label for="" class="label">ФИО</label>
                  <input id="" type="text" class="input">
                </div>
                <div class="group ">
                  <label for="" class="label">Номер телефона</label>
                  <input id="" type="text" class="input">
                </div>
                <div class="group ">
                  <label for="" class="label">Email</label>
                  <input id="" type="text" class="input">
                </div>


                </div>
              </div>
            <div class="about__paragraph">
              <div class="about__paragraph__title">
                <span>Данные оптового клиента</span>
              </div>
              <div class="about__paragraph__box ">

                  <div class="group__row flex-center">
                    <div class="group">
                      <label for="city" class="label">Наименование компании</label>
                      <input id="city" type="text" class="input">
                    </div>
                    <div class="group">
                      <label for="city" class="label">Расчетный счет IBAN</label>
                      <input id="city" type="text" class="input">
                    </div>
                  </div>

                <div class="group__row flex-center">
                  <div class="group">
                    <label for="city" class="label">Наименование компании</label>
                    <input id="city" type="text" class="input">
                  </div>
                  <div class="group">
                    <label for="city" class="label">Расчетный счет IBAN</label>
                    <input id="city" type="text" class="input">
                  </div>
                </div>

                <div class="group__row flex-center">
                  <div class="group">
                    <label for="city" class="label">УНП</label>
                    <input id="city" type="text" class="input">
                  </div>
                  <div class="group">
                    <label for="city" class="label">БИК</label>
                    <input id="city" type="text" class="input">
                  </div>
                </div>
                <div class="group__row flex-center">
                  <div class="group">
                    <label for="city" class="label">Юридический адрес</label>
                    <input id="city" type="text" class="input">
                  </div>
                  <div class="group">
                    <label for="city" class="label">Обслуживающий банк</label>
                    <input id="city" type="text" class="input">
                  </div>
                </div>

                </div>
              </div>
            <div class="about__paragraph">
              <div class="about__paragraph__title">
                <span>Оплата</span>
              </div>
              <div class="about__paragraph__box flex-center">

                <div class="radio__list">
                  <div class="radio">
                    <input id="radio-6" name="radio-1" type="radio" checked>
                    <label for="radio-6" class="radio-label">Безналичный расчет</label>
                  </div>
                  <p>После оформления заказа мы отправим счет для оплаты на ваш адрес электронной почты. Также наш
                    специалист свяжется с вами для подтверждения заказа.</p>
                </div>
                <div class="cart__summary">
                  <div class="summary__item">Стоимость товаров: <span>192.90</span>BYN</div>
                  <div class="summary__item">Стоимость доставки: <span>0.0</span>BYN</div>
                  <div class="summary__item">Скидка по промокоду: <span>2.0</span>BYN</div>
                  <div class="summary__item">Итоговая стоимость: <span><b>192.90</b></span>BYN</div>
                  <div class="_footnote">* Сумма указана с учетом НДС</div>
                  <button class="btn">Оформить заказ</button>

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
    name: 'cart',
  }
</script>

<style scoped lang="scss">

.cart {
  h3{
    margin-bottom: 45px;
  }
  &__content-block{
    width: 100%;
    padding: 0 16px;
  }

  &__block{ }
  &__empty__item{
    margin-bottom: 20px;
    font-size: 14px;

  }

  &__item{
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    padding: 24px 20px;
    background: #FFFFFF;
    border: 2px solid #EEEEEE;
    border-radius: 8px;
    margin-bottom: 16px;
    ._label{
      font-weight: 300;
      font-size: 12px;
      line-height: 20px;
    }

  }
  &__list{
      ._link{
        margin-top: 20px;
        cursor: pointer;
      }
  }
  &__footer{
    align-items: flex-start;
    padding: 40px 0;

    input{
      width:241px;
      border-bottom-right-radius: 0;
      border-top-right-radius: 0;
    }
    .black{
      border-bottom-left-radius: 0;
      border-top-left-radius: 0;
    }
  }
  &__summary{
    flex-basis: 50%;
    text-align: right;
    .label{
      justify-content: flex-end;
      margin-top: 15px;
      align-items: flex-end;
    }

    span{
      font-weight: 600;
      font-size: 20px;
      line-height: 20px;
      &:nth-child(1){
        margin: 0 10px 0 10px;
      }
    }
    .btn{
      margin-top: 20px;
    }


  }
  &__order{
    .summary__item{
      font-size: 14px!important;
      line-height: 20px;
      opacity: 1!important;
      margin-bottom: 12px;
      &:nth-child(3){
        margin-bottom: 30px;
      }

      span{
        font-size: 16px;
        margin: 0 5px 0 10px;
      }


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

.product{

  &__img {
    width: 100%;
    flex-basis: 20%;
    img{
      max-width: 100%;
      object-fit: fill;
    }
  }
  &__info{

    .icon{
      font-size: 10px;
      line-height: 20px;
      color: #423E48;
      opacity: 0.6;
      &:before{
        margin-right: 5px;
      }
      &:nth-child(1){
        margin-right: 15px;
      }
      &:hover{
        opacity: 1;
        cursor: pointer;
      }
    }
  }

  &__article{

  }
  &__title{
    font-size: 14px;
    line-height: 24px;
    text-decoration-line: underline;
    color: #423E48;
  }
  &__status{

  }
  &__count{
    flex-direction: column;
    //margin: 24px 0;


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

  &__price{
    display: flex;
    flex-direction: column;
    align-items: flex-end;

    .old_price{
      font-size: 14px;
      line-height: 20px;
      text-decoration-line: line-through;
      opacity: 0.4;
      margin-bottom: 5px;
    }
    .current_price{
      font-size: 20px;
      line-height: 20px;
      color: #423E48;
      font-weight: 500;
    }

  }



}

.about__paragraph{
  margin-bottom: 60px;

  &__title{
    position: relative;
    height: 20px;
    background: rgba(66, 117, 216, 0.1);
    border-radius: 4px;
    span{

      font-weight: 500;
      position: absolute;
      top: -10px;
      left: 10px;
      font-size: 20px;
      line-height: 24px;
      color: #4275D8;
    }


  }
  &__box{
    padding: 24px 0 30px 0;
    align-items: flex-start;
  }
  &__text{

    p{
      margin: 10px 0;
      font-size: 18px;
      line-height: 140%;
    }
  }
  .radio__list{
    p{
      font-size: 14px;
      line-height: 16px;
      opacity: 0.4;
    }
  }
}


</style>