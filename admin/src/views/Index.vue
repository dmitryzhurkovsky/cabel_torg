<script setup lang='ts'>
  import { useStore } from '../store';
  import { ActionTypes } from '../store/action-types';
  import { MutationTypes } from '../store/mutation-types';
  import {ref, onMounted, watch} from 'vue'
  import BaseTable from '@/components/Table/BaseTable.vue'
  import { IDeliveryType } from '../types';
  import Select from '@/components/UI/Select.vue'

  const store = useStore()

  const tableHeads = [
    {db: 'id', name: 'Номер заказа'},
    {db: 'date', name: 'Дата'}, 
    {db: 'delivery_type_name', name: 'Доставка'},
    {db: 'statusName', name: 'Статус'}, 
    {db: 'total_price', name: 'Сумма'}, 
    {db: '', name: ''},
    {db: '', name: ''},
  ]

  const orederType = ref('')
  const tableData = ref([] as Array<IDeliveryType>)
  const fileredData = ref([] as Array<IDeliveryType>)
  const tableSizeColumns = '100px 1fr 1fr 1fr 60px 40px 40px'

  const ordersRequest = async () => {
    await store.dispatch(ActionTypes.GET_ORDERS_DATA, null)
  };

  watch(() => store.getters.orders,
    () => {
      tableData.value = [...store.getters.orderList]
      onFilterData()
      store.commit(MutationTypes.SET_IS_LOADING, false)
    }
  )

  onMounted(() => {
    store.commit(MutationTypes.SET_IS_LOADING, true)
    ordersRequest()
  })

  const onFilterData = () => {
    if (orederType.value) {
      fileredData.value = tableData.value.filter(item => item.status === orederType.value)
    } else {
      fileredData.value = [...tableData.value]
    }
  }

  const onDeletOrder = async (rowData: IDeliveryType) => {
    // store.commit(MutationTypes.SET_IS_LOADING, true)
    // await store.dispatch(ActionTypes.DELETE_CALL_REQUEST, rowData.id as number)
  }

  const onChangeType = (id: string) => {
    orederType.value = id
    onFilterData()
  }

  const onEditOrder = (order: IDeliveryType) => {
    console.log(order.id);
    
  }

</script>

<template>
  <h2 class="heading-2">Список заказов</h2>

  <div class="parameters-block">
    <Select
      v-if="store.getters.orderTypes.length"
      text = 'Выберите статус заказов'
      id   = ''
      fieldForSearch = "name"
      :data = "store.getters.orderTypes"
      @onSelectItem="onChangeType"
    />
  </div>
  <base-table
    :head="tableHeads"
    :columnTemplates="tableSizeColumns"
    :tableData="fileredData"
    :addButton=false
    @deleteRow="onDeletOrder"
    @editRow="onEditOrder"
  />
</template>

<style lang="scss" scoped>

  .parameters{
    &-block{
      margin: 20px 0;
      width: 500px;
    }
  }
</style>
