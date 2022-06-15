<template lang="html">
  <div class="content-block__title">История покупок</div>
   <div class="order__list">
     <OrderItem/>
     <OrderItem/>
     <OrderItem/>
   </div>

</template>

<script>

import OrderItem from '@/components/personal/order-item';

export default {
  name: 'OrderList',

  components:{
    OrderItem,
  },

}
</script>

<style lang="scss" scoped>
.user-acc {
  &__content-block{
    width: 100%;
    padding: 0 16px;
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

</style>
