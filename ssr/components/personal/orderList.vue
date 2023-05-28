<template>
  <div>
    <div class="content-block__title">История покупок</div>
    <div class="order__list"
        v-if = "ORDER_DOCUMENTS.length"
    >
      <PersonalOrderItem
          v-for   = "item in ORDER_DOCUMENTS"
          :key    = "item.id"
          :card   = item
      />
    </div>
  </div>
</template>

<script>

import { mapGetters, mapActions, mapMutations } from 'vuex';

export default {
  name: 'OrderList',

  computed:{
    ...mapGetters("order", ["ORDER_DOCUMENTS", "ORDER_DELIVERY_TYPES"]),

  },

  methods:{
    ...mapMutations("order", ["CLEAR_ORDER_DOCUMENTS"]),
    ...mapActions("order", ["GET_ORDER_DOCUMENTS"]),
    ...mapMutations("notification", ["SET_IS_LOADING"]),

    async getData(){
      this.SET_IS_LOADING(true);
      this.GET_ORDER_DOCUMENTS();
      this.SET_IS_LOADING(false);
    }
  },

  async mounted() {
    await this.getData();
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
  min-height: 350px;
  &__title{
    font-weight: 500;
    font-size: 20px;
    line-height: 24px;
    color: #423E48;
    margin-bottom: 40px;
  }
}

</style>
