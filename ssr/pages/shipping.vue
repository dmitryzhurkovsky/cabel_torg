<template>
  <div class="structure">
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

  definePageMeta({
    // middleware: ["auth"],
    name: 'Оплата и доставка',
  });

  export default defineNuxtComponent({
    name: 'Shipping',

    head () {
      return {
        title: 'Кабельторг | Оплата и доставка',
        meta: [{
          name: 'Оплата и доставка',
          content: 'Страница Оплата и доставка'
        }]
      }
    },

    computed: {
      ...mapGetters("order", ["ORDER_DELIVERY_TYPES"]),
    },

    mounted(){
      this.$store.commit('breadcrumb/ADD_BREADCRUMB', {
        name: this.$router.currentRoute.value.meta.name,
        path: this.$router.currentRoute.value.path,
        type: "global",
        class: ""
      });
    }
  })
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
