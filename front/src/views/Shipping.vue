<template>
  <div class="structure app__content">
    <div class="structure__wrapper">
      <div class="structure__content _container">
        <div class="structure__body">
          <div class="structure__block">
            <h3 class="structure__title">Доставка</h3>
            <p class="structure__text">Для оптовых покупателей из РБ мы предлагаем несколько различных способов получения заказа:</p>
            <li 
              class="structure__list__item" 
              v-for = "delivery in ORDER_DELIVERY_TYPES" 
              :key = delivery.id 
            >
              {{ delivery.payload }}
            </li>
            <!-- <li class="structure__list__item">Самовывоз со склада Брест с 09:00 до 18:00 (бесплатно)</li>
            <li class="structure__list__item">Самовывоз со склада Минск с 09:00 до 18:00 (бесплатно)</li>
            <li class="structure__list__item">Бесплатная доставка по РБ от 500 рублей (бесплатно)</li>
            <li class="structure__list__item">Доставка по РБ  в любую точку (платно за счет клиента). Обсуждается индивидуально с менеджером.</li> -->
            <h3  class="structure__title">Оплата</h3>
            <p>Для оптовых покупателей из РБ доступен только безналичный расчет.</p>
          </div>






        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import { mapGetters } from 'vuex';

  export default {
    name: 'Shipping',

    computed: {
      ...mapGetters("order", ["ORDER_DELIVERY_TYPES"]),
    },

    mounted(){
      this.$store.dispatch("breadcrumb/CHANGE_BREADCRUMB", 0);
      this.$store.commit('breadcrumb/ADD_BREADCRUMB', {
        name: this.$router.currentRoute.value.meta.name,
        path: this.$router.currentRoute.value.path,
        type: "global",
        class: ""
      });
    }
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
