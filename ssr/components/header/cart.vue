<template>
  <div class="dropdown__content popup-cart">
    <div class="dropdown__content__title">Корзина</div>
    <div class="popup-cart__summary">
      <div class="">Товары в корзине: <span>{{ totalOrderQuantity }}</span></div>
      <div>на сумму <span>{{ totalOrderCost }}</span><span> BYN</span></div>
    </div>
    <div class="popup-cart__list" v-if = "ItemsForShow.length">
      <HeaderCartItem 
          class="row" 
          v-for = "cartItem in ItemsForShow"
          :key = "cartItem.product.id"
          :cartItem = cartItem
      />
    </div>
    <button class="btn" @click.prevent="onPutApplication()">Оформить заказ</button>
    <div>
      <a class="" @click.prevent="onOpenCart()">Перейти в корзину
        <svg width="16" height="8" viewBox="0 0 16 8" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M0.5 3.99935H15.0833M15.0833 3.99935L11.75 0.666016M15.0833 3.99935L11.75 7.33268" stroke="#4275D8"/>
        </svg>

      </a>
    </div>
  </div>

</template>

<script setup>
  import { computed } from 'vue';
  import { useOrdersStore } from '@/stores/orders';
  import { useAuthStore } from '@/stores/auth';

  const router = useRouter();
  const oredersStore = useOrdersStore();
  const authStore = useAuthStore();

  const { orders, totalOrderCost, totalOrderQuantity } = storeToRefs(oredersStore);

  const ItemsForShow = computed(() => {
    let result = [];
    if (orders.value.length > 5) {
      result = orders.value.slice(orders.value.length - 4);
    } else {
      result = [...orders.value];
    }
    return result;
  });

  const onOpenCart = () => {
    if (router.path != '/cart') {
      router.push('/cart');
    }
  };

  const onPutApplication = () => {
    authStore.setDestination('');
    oredersStore.setIsApplicationOpen(true);
    if (router.path != '/cart') {
      router.push('/cart');
    }
  };
</script>

<style lang="scss">
.popup-cart{
  text-align: center;



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

.dropdown__content__title{
  font-size: 20px;
  line-height: 140%;
  margin-bottom: 16px;
  color: #423e48;
  font-weight: 500;
}
</style>
