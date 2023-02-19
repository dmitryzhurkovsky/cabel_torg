<script setup lang='ts'>
  import { useStore } from '../store';
  import { ActionTypes } from '../store/action-types';
  import { MutationTypes } from '../store/mutation-types';
  import {ref, computed, onMounted, watchEffect, watch} from 'vue'
  import BaseTable from '@/components/Table/BaseTable.vue'
  import TableRow from '@/components/Table/TableRow.vue'
  import TableColumn from '@/components/Table/TableColumn.vue'
  import Button from '@/components/UI/Button.vue'
  import Input from '@/components/UI/Input.vue';
  import { router } from '../router';
  import { IDeliveryType } from '../types';
  import { helpers, minLength, required } from '@vuelidate/validators';
  import { useVuelidate } from '@vuelidate/core';

  const store = useStore()

  const tableHeads = [
    {db: 'id', name: 'N'},
    {db: 'payload', name: 'name'}, 
    {db: '', name: ''},
    {db: '', name: ''},
  ]

  const tableSizeColumns = '30px 1fr 40px 40px'

  const sortField = ref('id')
  const typeSort = ref('asc')
  const isFormOpen = ref(false)
  const tableData = ref([] as Array<IDeliveryType>)
  const payloadField = ref('')
  const idField = ref()
  const formType = ref(true)

  const tableDataSorting = computed(() => {
    return tableData.value.sort((a, b) => {
      let modifier = 1;
      if (typeSort.value === 'desc') modifier = -1
      const param = sortField.value;
      if (a[param] < b[param]) return -1 * modifier
      if (a[param] > b[param]) return 1 * modifier
      return 0
    })
  })

  const setSort = (name: string) => {
    if (sortField.value === name) {
      if (typeSort.value === 'asc') {
        typeSort.value = 'desc'
      } else {
        typeSort.value = 'asc'
      }
    } else {
      sortField.value = name
    }
  }

  const rules = computed(() => ({
    payloadField: {
      requered:  helpers.withMessage(`Обязательно поле`, required),
      minLength: helpers.withMessage(`Минимальная длина поля 5 символов`, minLength(5)),
    },
  }))

  const v = useVuelidate(rules, {payloadField});

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
    formType.value = false
    onSetIsFormOpen(true)
  } 

  const onAddButtonClick = () => {
    idField.value = null
    payloadField.value = '' as string
    formType.value = true
    onSetIsFormOpen(true)
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
      const data = {payload: payloadField.value}
      await store.dispatch(ActionTypes.ADD_DELIVERY_TYPE, data)
    } else {
      store.commit(MutationTypes.SET_IS_LOADING, true)
      const data = {id: idField.value, payload: payloadField.value}
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
      <div class="form-buttons">
        <Button label="Создать" color="primary" v-if="formType"></Button>
        <Button label="Сохранить" color="primary" v-if="!formType"></Button>
        <Button label="Отменить" color="warning"  @click="onSetIsFormOpen(false)"></Button>
      </div>
    </form>
  </div>

  <div class="table-info info">
    <span class="info-elem">Сортировка по полю: {{sortField}}</span>
    <span class="info-elem">Сортируем по направлению: {{typeSort}}</span>
    <Button label="Добавить" @click="onAddButtonClick()"></Button>
  </div>

  <base-table
    :head="tableHeads"
    :columnTemplates="tableSizeColumns"
    @sorting="setSort">
    <table-row
      v-for="rowData in tableDataSorting"
      :key="rowData.id"
      :columnTemplates="tableSizeColumns"
      >
      <table-column :columnTitle="tableHeads[0]">
        {{rowData.id}}
      </table-column>
      <table-column :columnTitle="tableHeads[1]">
        {{rowData.payload}}
      </table-column>
      <table-column>
        <Button icon="pen-to-square" @click="onEditButtonClick(rowData)"></Button>
      </table-column>
      <table-column>
        <Button icon="trash-can" color="danger" @click="onDeleteDeliveryType(rowData)"></Button>
      </table-column>
    </table-row>
  </base-table>
</template>

<style lang="scss" scoped>
  @import "../styles/table-info.scss";

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
