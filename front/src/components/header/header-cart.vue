<template lang="html">
  <div class="dropdown__content popup-cart">
    <h3 class="">Корзина</h3>
    <div class="popup-cart__summary">
      <div class="div">Товары в корзине: <span>{{ TOTAL_ORDER_QUANTITY }}</span></div>
      <div>на сумму <span>{{ TOTAL_ORDER_COST }}</span><span> BYN</span></div>
    </div>
    <div class="popup-cart__list" v-if = "ORDERS.length">
      <HeaderCartItem 
          class="row" 
          v-for = "cartItem in ORDERS"
          :key = "cartItem.product.id"
          :cartItem = cartItem
      />
    </div>
    <button class="btn" @click="onPutApplication()">Оформить заказ</button>
    <div>
      <a class="" @click="onOpenCart()">Перейти в корзину
        <svg width="16" height="8" viewBox="0 0 16 8" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M0.5 3.99935H15.0833M15.0833 3.99935L11.75 0.666016M15.0833 3.99935L11.75 7.33268" stroke="#4275D8"/>
        </svg>

      </a>
    </div>
  </div>

</template>

<script>

import { mapGetters, mapMutations } from 'vuex'

import HeaderCartItem from '@/components/header/header-cart-item.vue'

export default {
  name: "HeaderCart",

  components: {
    HeaderCartItem,
  },

  computed: {
    ...mapGetters("order", ["ORDERS", "TOTAL_ORDER_COST", "TOTAL_ORDER_QUANTITY", "IS_APPLICATION_OPEN"]),
    ...mapGetters("auth", ["USER", "REDIRECT_AFTER_LOGIN"]),
  },

  methods: {
    ...mapMutations("auth", ["SET_DESTINATION"]),
    ...mapMutations("order", ["SET_IS_APPLICATION_OPEN"]),

    onOpenCart() {
        if (this.$router.path != '/cart') {
            this.$router.push('/cart');
        }
    },

    onPutApplication() {
        if (this.USER) {
            this.SET_DESTINATION('');
            this.SET_IS_APPLICATION_OPEN(true);
            if (this.$router.path != '/cart') {
                this.$router.push('/cart');
            }
        } else {
            this.SET_DESTINATION('/cart');
            this.$router.push('/login');
        }
    }
  }
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
