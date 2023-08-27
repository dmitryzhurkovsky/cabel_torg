<script setup lang='ts'>
  import { useStore } from '../store';
  import { ActionTypes } from '../store/action-types';
  import { MutationTypes } from '../store/mutation-types';
  import {ref, computed, onMounted, watch} from 'vue'
  import BaseTable from '@/components/Table/BaseTable.vue'
  import Button from '@/components/UI/Button.vue'
  import Input from '@/components/UI/Input.vue';
  import { IDeliveryType } from '../types';
  import { helpers, minLength, numeric, required } from '@vuelidate/validators';
  import { useVuelidate } from '@vuelidate/core';

  const store = useStore()

  const tableHeads = [
    {db: 'id', name: 'N'},
    {db: 'title', name: 'заголовок'},
    {db: 'payload', name: 'описание'}, 
    {db: '', name: ''},
    {db: '', name: ''},
  ]
  const tableData = ref([] as Array<IDeliveryType>)
  const tableSizeColumns = '30px 1fr 1fr 40px 40px'

  const isFormOpen = ref(false)
  const payloadField = ref('')
  const titleField = ref('')
  const vendorField = 1
  const idField = ref()
  const formType = ref(true)

  const rules = computed(() => ({
    payloadField: {
      requered:  helpers.withMessage(`Обязательно поле`, required),
    },
    titleField: {
      requered:  helpers.withMessage(`Обязательно поле`, required),
    },
  }))

  const v = useVuelidate(rules, {payloadField, titleField});

  const sendDataRequest = async () => {
    await store.dispatch(ActionTypes.GET_STOCKS_DATA, null)
  };

  watch(() => store.getters.stocks,
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
    payloadField.value = rowData.payload as string
    titleField.value = rowData.title as string
    formType.value = false
    onSetIsFormOpen(true)
    setTimeout(() => window.scrollTo(0, 0), 0);
  } 

  const onAddButtonClick = () => {
    idField.value = null
    payloadField.value = '' as string
    titleField.value = '' as string
    formType.value = true
    onSetIsFormOpen(true)
    setTimeout(() => window.scrollTo(0, 0), 0);
  }

  const onDeleteDeliveryType = async (rowData: IDeliveryType) => {
    store.commit(MutationTypes.SET_IS_LOADING, true)
    await store.dispatch(ActionTypes.DELETE_STOCK, rowData.id as number)
    isFormOpen.value = false
  }

  const submitForm = async () => {
    v.value.$touch()
    if (v.value.$error) return
    const data = {
      payload: payloadField.value,
      title: titleField.value,
      vendor_info_id: vendorField,
    } as IDeliveryType
    if (formType.value) {
      store.commit(MutationTypes.SET_IS_LOADING, true)
      await store.dispatch(ActionTypes.ADD_STOCK, data)
    } else {
      store.commit(MutationTypes.SET_IS_LOADING, true)
      data.id = idField.value
      await store.dispatch(ActionTypes.EDIT_STOCK, data)
    }
    isFormOpen.value = false
    store.commit(MutationTypes.SET_IS_LOADING, false)
  }

</script>

<template>
  <h2 class="heading-2">Способы доставки</h2>

  <div class="form-container" v-if="isFormOpen">
    <h3 class="heading-3">Новый тип доставки</h3>

    <form @submit.prevent="submitForm">
      <Input
        label="Название"
        name="title"
        placeholder="Укажите название"
        v-model:value="v.titleField.$model"
        :error="v.titleField.$errors"
      />
      <Input
        label="Адрес склада"
        name="payload"
        placeholder="Адрес склада"
        v-model:value="v.payloadField.$model"
        :error="v.payloadField.$errors"
      />
      <div class="form-buttons">
        <Button label="Создать" color="primary" v-if="formType"></Button>
        <Button label="Сохранить" color="primary" v-if="!formType"></Button>
        <Button label="Отменить" color="warning"  @click="onSetIsFormOpen(false)"></Button>
      </div>
    </form>
  </div>

  <base-table
    :head="tableHeads"
    :columnTemplates="tableSizeColumns"
    :tableData="tableData"
    @openForm="onAddButtonClick"
    @editRow="onEditButtonClick"
    @deleteRow="onDeleteDeliveryType"
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
