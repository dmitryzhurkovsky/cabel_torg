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
    {db: 'id', name: 'Id'},
    {db: 'fullname', name: 'Имя'}, 
    {db: 'phone_number', name: 'Телефон'}, 
    {db: 'product_id', name: 'Товар'},
    {db: 'type', name: 'Тип запроса'}, 
    {db: '', name: ''},
  ]

  const requesrTypes = [
    {id: 'U', name: 'Запрос обратной связи'},
    {id: 'GR', name: 'Запрос о поступлении товара'}
  ]

  const tableData = ref([] as Array<IDeliveryType>)
  const tableSizeColumns = '30px 1fr 1fr 1fr 20px 40px'

  const requestType = ref('')
  const fileredData = ref([] as Array<IDeliveryType>)

  const sendDataRequest = async () => {
    await store.dispatch(ActionTypes.GET_CALL_REQUESTS_DATA, null)
  };

  watch(() => store.getters.callRequests,
    (curr) => {
      tableData.value = [...curr]
      fileredData.value = [...curr]
      store.commit(MutationTypes.SET_IS_LOADING, false)
    }
  )

  onMounted(() => {
    store.commit(MutationTypes.SET_IS_LOADING, true)
    sendDataRequest()
  })

  const onDeleteRow = async (rowData: IDeliveryType) => {
    store.commit(MutationTypes.SET_IS_LOADING, true)
    await store.dispatch(ActionTypes.DELETE_CALL_REQUEST, rowData.id as number)
  }

  const onChangeType = (id: string) => {
    requestType.value = id
    fileredData.value = tableData.value.filter(item => item.type === id)
  }

</script>

<template>
  <h2 class="heading-2">Запросы на звонок</h2>

  <div class="parameters-block">
    <Select
      v-if="requesrTypes.length"
      text = 'Выберите тип запроса'
      id   = ''
      fieldForSearch = "name"
      :data = "requesrTypes"
      @onSelectItem="onChangeType"
    />
  </div>
  <base-table
    :head="tableHeads"
    :columnTemplates="tableSizeColumns"
    :tableData="fileredData"
    :editButton=false
    :addButton=false
    @deleteRow="onDeleteRow"
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
