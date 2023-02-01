<template lang="html">
  <div class="content-block__title">История покупок</div>
   <div class="order__list"
      v-if = "ORDER_DOCUMENTS.length"
   >
     <OrderItem
         v-for   = "item in ORDER_DOCUMENTS"
        :key    = "item.id"
        :card   = item
     />
   </div>

</template>

<script>

import OrderItem from '@/components/personal/order-item';
import { mapGetters, mapActions, mapMutations } from 'vuex';

export default {
  name: 'OrderList',

  components:{
    OrderItem,
  },

  computed:{
    ...mapGetters("order", ["ORDER_DOCUMENTS", "ORDER_DELIVERY_TYPES"]),

  },

  methods:{
    ...mapMutations("order", ["CLEAR_ORDER_DOCUMENTS"]),
    ...mapActions("order", ["GET_ORDER_DOCUMENTS", "GET_ORDER_DELIVERY_TYPES", ]),
    ...mapMutations("notification", ["SET_IS_LOADING"]),

    async getData(){
      this.SET_IS_LOADING(true);
      this.GET_ORDER_DOCUMENTS();
      this.SET_IS_LOADING(false);
    }
  },

  async mounted() {
    await this.getData();
    this.GET_ORDER_DELIVERY_TYPES();
  },

  beforeUnmount() {
    this.CLEAR_ORDER_DOCUMENTS();
  }

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
