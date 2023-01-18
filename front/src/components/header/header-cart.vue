<template lang="html">
  <div class="dropdown__content popup-cart">
    <h3 class="">Корзина</h3>
    <div class="popup-cart__summary">
      <div class="div">Товары в корзине: <span>{{ totalInCart }}</span></div>
      <div>на сумму <span>{{ TOTAL_ORDER_COST }}</span><span>BYN</span></div>
    </div>
    <div class="popup-cart__list" v-if = "ORDERS.length">
      <HeaderCartItem 
          class="row" 
          v-for = "cartItem in ORDERS"
          :key = "cartItem.product.id"
          :cartItem = cartItem
      />
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

import { mapGetters } from 'vuex'

import HeaderCartItem from '@/components/header/header-cart-item.vue'

export default {
  name: "HeaderCart",

  components: {
    HeaderCartItem,
  },

  computed: {
    ...mapGetters("order", ["ORDERS", "TOTAL_ORDER_COST"]),

    totalInCart(){
      let total = 0;
      this.ORDERS.forEach(item => {
        total = total + item.amount
      });
      return total;
    },
  },
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
