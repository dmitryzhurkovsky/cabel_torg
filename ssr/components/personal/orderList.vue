<template>
  <div>
    <div class="content-block__title">История покупок</div>
    <div class="order__list"
        v-if = "orderDocuments.length"
    >
      <PersonalOrderItem
          v-for   = "item in orderDocuments"
          :key    = "item.id"
          :card   = item
      />
    </div>
  </div>
</template>

<script setup>
  import { onMounted, onBeforeUnmount } from 'vue';
  import { useNotificationsStore } from '@/stores/notifications';
  import { useOrdersStore } from '@/stores/orders';

  const notificationsStore = useNotificationsStore();
  const oredersStore = useOrdersStore();

  const { orderDocuments } = storeToRefs(oredersStore);
  
  const getData = async () => {
    notificationsStore.setIsLoading(true);
    await oredersStore.getOrdersDocuments();
    notificationsStore.setIsLoading(false);
  };

  onMounted( async () =>{
    await getData();
  });

  onBeforeUnmount(() => {
    oredersStore.clearOrderDocuments();
  });

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
