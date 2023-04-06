<script setup lang='ts'>
  import { useStore } from '../store';
  import { ActionTypes } from '../store/action-types';
  import { MutationTypes } from '../store/mutation-types';
  import {ref, computed, onMounted, watch} from 'vue'
  import BaseTable from '@/components/Table/BaseTable.vue'
  import Button from '@/components/UI/Button.vue'
  import Input from '@/components/UI/Input.vue';
  import Select from '@/components/UI/Select.vue'
  import { IDeliveryType } from '../types';
  import { helpers, minLength, required } from '@vuelidate/validators';
  import { useVuelidate } from '@vuelidate/core';

  const store = useStore()

  const tableHeads = [
    {db: 'id', name: 'N'},
    {db: 'payload', name: 'name'}, 
    {db: 'is_pickup', name: 'Мы доставляем'}, 
    {db: '', name: ''},
    {db: '', name: ''},
  ]
  const tableData = ref([] as Array<IDeliveryType>)
  const tableSizeColumns = '30px 1fr 1fr 40px 40px'

  const isFormOpen = ref(false)
  const payloadField = ref('')
  const isPickUpField = ref(false)
  const idField = ref()
  const isPickUp = ref(1)
  const formType = ref(true)

  const rules = computed(() => ({
    payloadField: {
      requered:  helpers.withMessage(`Обязательно поле`, required),
      minLength: helpers.withMessage(`Минимальная длина поля 5 символов`, minLength(5)),
    },
    isPickUpField: {
      requered: helpers.withMessage(`Обязательно поле`, required),
    }
  }))

  const v = useVuelidate(rules, {payloadField, isPickUpField});

  const sendDataRequest = async () => {
    await store.dispatch(ActionTypes.GET_DELIVERY_TYPE, null)
  };

  watch(() => store.getters.deliveryTypesData,
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
    isPickUpField.value = rowData.is_pickup as boolean
    isPickUp.value = rowData.is_pickup ? 1 : 0
    formType.value = false
    onSetIsFormOpen(true)
    setTimeout(() => window.scrollTo(0, 0), 0);
  } 

  const onAddButtonClick = () => {
    idField.value = null
    payloadField.value = '' as string
    isPickUpField.value = false
    formType.value = true
    onSetIsFormOpen(true)
    setTimeout(() => window.scrollTo(0, 0), 0);
  }

  const onChangeType = (id: number) => {
    isPickUp.value = id
    if (id === 0) isPickUpField.value = false
    if (id === 1) isPickUpField.value = true
  }

  const onDeleteDeliveryType = async (rowData: IDeliveryType) => {
    store.commit(MutationTypes.SET_IS_LOADING, true)
    await store.dispatch(ActionTypes.DELETE_DELIVERY_TYPE, rowData.id as number)
    isFormOpen.value = false
  }

  const submitForm = async () => {
    v.value.$touch()
    if (v.value.$error) return
    if (formType.value) {
      store.commit(MutationTypes.SET_IS_LOADING, true)
      const data = {payload: payloadField.value, is_pickup: isPickUp.value === 0 ? true: false}
      await store.dispatch(ActionTypes.ADD_DELIVERY_TYPE, data)
    } else {
      store.commit(MutationTypes.SET_IS_LOADING, true)
      const data = {id: idField.value, payload: payloadField.value, is_pickup: isPickUp.value === 0 ? true: false}
      console.log(data);
      
      await store.dispatch(ActionTypes.EDIT_DELIVERY_TYPE, data)
    }
    isFormOpen.value = false
    // store.commit(MutationTypes.SET_IS_LOADING, false)
  }

</script>

<template>
  <h2 class="heading-2">Способы доставки</h2>

  <div class="form-container" v-if="isFormOpen">
    <h3 class="heading-3">Новый тип доставки</h3>

    <form @submit.prevent="submitForm">
      <Input
        label="Название"
        name="payload"
        placeholder="Укажите название"
        v-model:value="v.payloadField.$model"
        :error="v.payloadField.$errors"
      />
      <Select
        text = 'Наша доставка'
        id   = ''
        fieldForSearch = "name"
        :data = "[{id: 0, name: 'Да'}, {id: 1, name: 'Нет'}]"
        @onSelectItem="onChangeType"
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
