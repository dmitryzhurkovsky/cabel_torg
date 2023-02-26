<script setup lang='ts'>
  import { useStore } from '../store';
  import { ActionTypes } from '../store/action-types';
  import { MutationTypes } from '../store/mutation-types';
  import {ref, computed, onMounted, watch} from 'vue'
  import BaseTable from '@/components/Table/BaseTable.vue'
  import Button from '@/components/UI/Button.vue'
  import PhotoUploader from '@/components/UI/PhotoUploader.vue';
  import { IDeliveryType } from '../types';
  import { helpers, minLength, required } from '@vuelidate/validators';
  import { useVuelidate } from '@vuelidate/core';

  const store = useStore()

  const tableHeads = [
    {db: 'id', name: 'Id'},
    {db: 'image', name: 'Логотип', type: 'image', src: 'image'}, 
    {db: '', name: ''},
  ]
  const tableData = ref([] as Array<IDeliveryType>)
  const tableSizeColumns = '30px 1fr 40px 40px'

  const isFormOpen = ref(false)
  const files = ref<Array<File>>([])
  const idField = ref()
  const formType = ref(true)

  const sendDataRequest = async () => {
    await store.dispatch(ActionTypes.GET_PARTNERS_DATA, null)
  };

  watch(() => store.getters.partnersData,
    (curr, prev) => {
      tableData.value = [...curr];
      store.commit(MutationTypes.SET_IS_LOADING, false)
  });

  onMounted(() => {
    store.commit(MutationTypes.SET_IS_LOADING, true)
    sendDataRequest()
  })

  const onSetIsFormOpen = (val: boolean) => {
    isFormOpen.value = val
  }

  const onEditButtonClick = (rowData: IDeliveryType) => {
    idField.value = rowData.id
    formType.value = false
    onSetIsFormOpen(true)
  } 

  const onAddButtonClick = () => {
    idField.value = null
    // imageField.value = '' as string
    formType.value = true
    onSetIsFormOpen(true)
  }

  const onDeleteArticle = async (rowData: IDeliveryType) => {
    store.commit(MutationTypes.SET_IS_LOADING, true)
    await store.dispatch(ActionTypes.DELETE_PARTNER, rowData.id as number)
    isFormOpen.value = false
  }

  const submitForm = async () => {
    if (!files.value.length) return
    store.commit(MutationTypes.SET_IS_LOADING, true)
    const data = new FormData()
    data.append('file', files.value[0])
    await store.dispatch(ActionTypes.ADD_PARTNER, data)

    files.value =[]
    isFormOpen.value = false
    store.commit(MutationTypes.SET_IS_LOADING, false)
  }

</script>

<template>
  <h2 class="heading-2">Партнеры</h2>

  <div class="form-container" v-if="isFormOpen">
    <h3 class="heading-3">Новый (лого) партнер</h3>

    <form @submit.prevent="submitForm">
      <PhotoUploader v-model="files" />
      <div class="form-buttons">
        <Button label="Создать" color="primary" v-if="formType"></Button>
        <Button label="Сохранить" color="primary" v-if="!formType"></Button>
        <Button label="Отменить" color="warning" @click="onSetIsFormOpen(false)"></Button>
      </div>
    </form>
  </div>

  <base-table
    :head="tableHeads"
    :columnTemplates="tableSizeColumns"
    :tableData="tableData"
    :editButton=false
    @openForm="onAddButtonClick"
    @editRow="onEditButtonClick"
    @deleteRow="onDeleteArticle"
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
