<script setup lang='ts'>
  import { useStore } from '../store';
  import { ActionTypes } from '../store/action-types';
  import { MutationTypes } from '../store/mutation-types';
  import {ref, onMounted, watch} from 'vue'
  import BaseTable from '@/components/Table/BaseTable.vue'
  import { IDeliveryType } from '../types';

  const store = useStore()

  const tableHeads = [
    {db: 'id', name: 'Id'},
    {db: 'fullname', name: 'Имя'}, 
    {db: 'phone_number', name: 'Телефон'}, 
    {db: 'email', name: 'email'}, 
    {db: 'message', name: 'Сообщение'}, 
    {db: '', name: ''},
  ]
  const tableData = ref([] as Array<IDeliveryType>)
  const tableSizeColumns = '30px 1fr 1fr 1fr 2fr 40px'

  const idField = ref()

  const sendDataRequest = async () => {
    await store.dispatch(ActionTypes.GET_FEEDBACK_REQUESTS_DATA, null)
  };

  watch(() => store.getters.feedbackRequests,
    (curr, prev) => {
      tableData.value = [...curr];
      store.commit(MutationTypes.SET_IS_LOADING, false)
  });

  onMounted(() => {
    store.commit(MutationTypes.SET_IS_LOADING, true)
    sendDataRequest()
  })

  const onDeleteRow = async (rowData: IDeliveryType) => {
    store.commit(MutationTypes.SET_IS_LOADING, true)
    await store.dispatch(ActionTypes.DELETE_FEEDBACK_REQUEST, rowData.id as number)
  }

</script>

<template>
  <h2 class="heading-2">Запросы на звонок</h2>

  <base-table
    :head="tableHeads"
    :columnTemplates="tableSizeColumns"
    :tableData="tableData"
    :editButton=false
    @deleteRow="onDeleteRow"
  />
</template>

<style lang="scss" scoped>

  .form{
    &-container {
      display: flex;
      flex-direction: column;
      align-items: baseline;
      margin: 15px 0;
      background-color: var(--background-content);
    }
    &-buttons {
      display: flex;
      justify-content: space-around;
    }
  }
</style>
