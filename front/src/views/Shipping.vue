<template>
  <div class="structure">
    <div class="structure__wrapper">
      <div class="structure__content _container">
        <div class="structure__body">
          <ul class="breadcrumb">
            <li><a href="#">Главная</a></li>
            <li><a href="#">Покупателям</a></li>
            <li class="active">Оплата и доставка</li>
          </ul>
          <div class="structure__block">
            <h3 class="structure__title">Доставка</h3>
            <p class="structure__text">Для оптовых покупателей из РБ мы предлагаем несколько различных способов получения заказа:</p>
            <li class="structure__list__item">Самовывоз со склада Брест с 09:00 до 18:00 (бесплатно)</li>
            <li class="structure__list__item">Самовывоз со склада Минск с 09:00 до 18:00 (бесплатно)</li>
            <li class="structure__list__item">Бесплатная доставка по РБ от 500 рублей (бесплатно)</li>
            <li class="structure__list__item">Доставка по РБ  в любую точку (платно за счет клиента). Обсуждается индивидуально с менеджером.</li>
            <h3  class="structure__title">Оплата</h3>
            <p>Для оптовых покупателей из РБ доступен только безналичный расчет.</p>
          </div>






        </div>
      </div>
    </div>
  </div>
</template>

<script>

  export default {
    name: 'Shipping',
  }
</script>

<style lang="scss">

.structure {

  &__wrapper{


  }
  &__content{

  }

  &__body{


  }
  &__title{
   margin: 30px 0;

  }
  &__block{
    padding: 0px 0 60px 0;
    h3{


    }



  }

  &__list{
    &__item{
      line-height: 30px;
      &:last-child{
        margin-bottom: 30px;
      }

    }

  }

  &__text{
    font-weight: 300;
    font-size: 18px;
    line-height: 140%;
    color: #423E48;
    margin-bottom: 20px;

  }


}


</style>
