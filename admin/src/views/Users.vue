<script setup lang='ts'>
  import { useStore } from '../store';
  import { ActionTypes } from '../store/action-types';
  import { MutationTypes } from '../store/mutation-types';
  import {ref, computed, onMounted, watch} from 'vue'
  import BaseTable from '@/components/Table/BaseTable.vue'
  import Button from '@/components/UI/Button.vue'
  import Input from '@/components/UI/Input.vue';
  import { IDeliveryType } from '../types';
  import { helpers, minLength, email, required } from '@vuelidate/validators';
  import { useVuelidate } from '@vuelidate/core';

  const store = useStore()

  const tableHeads = [
    {db: 'id', name: 'N'},
    {db: 'full_name', name: 'Имя'},
    {db: 'email', name: 'EMail'}, 
    {db: '', name: ''},
    {db: '', name: ''},
  ]
  const tableData = ref([] as Array<IDeliveryType>)
  const tableSizeColumns = '30px 1fr 1fr 40px 40px'

  const isFormOpen = ref(false)
  const emailField = ref('')
  const nameField = ref('')
  const passwordField = ref('')
  const idField = ref()
  const formType = ref(true)

  const rules = computed(() => ({
    emailField: {
      requered:  helpers.withMessage(`Обязательно поле`, required),
      email: helpers.withMessage(`укажите валидный E-Mail`, email),
    },
    nameField: {
      requered:  helpers.withMessage(`Обязательно поле`, required),
    },
    passwordField: {
      requered:  helpers.withMessage(`Обязательно поле`, required),
      minLength: helpers.withMessage(`Длина поля 8 символов`, minLength(8)),
    },
  }))

  const v = useVuelidate(rules, {emailField, nameField, passwordField});

  const sendDataRequest = async () => {
    await store.dispatch(ActionTypes.GET_USERS_LIST_DATA, null)
  };

  watch(() => store.getters.usersList,
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
    emailField.value = rowData.email as string
    nameField.value = rowData.full_name as string
    formType.value = false
    onSetIsFormOpen(true)
    setTimeout(() => window.scrollTo(0, 0), 0);
  } 

  const onAddButtonClick = () => {
    idField.value = null
    emailField.value = '' as string
    nameField.value = '' as string
    passwordField.value = '' as string
    formType.value = true
    onSetIsFormOpen(true)
    setTimeout(() => window.scrollTo(0, 0), 0);
  }

  const onDeleteButtonClick = async (rowData: IDeliveryType) => {
    store.commit(MutationTypes.SET_IS_LOADING, true)
    await store.dispatch(ActionTypes.DELETE_USER, rowData.id as number)
    isFormOpen.value = false
  }

  const submitForm = async () => {
    v.value.$touch()
    if (v.value.$error) return
    const data = {
      email: emailField.value,
      full_name: nameField.value,
    } as IDeliveryType
    if (formType.value) {
      store.commit(MutationTypes.SET_IS_LOADING, true)
      data.password = passwordField.value
      data.is_admin = true
      data.phone_number = '+375 162 54-54-07'
      data.company_name = 'CabelTorg'
      data.unp = '291132270'
      await store.dispatch(ActionTypes.ADD_USER, data)
    } else {
      store.commit(MutationTypes.SET_IS_LOADING, true)
      data.id = idField.value
      console.log(data);
      
      await store.dispatch(ActionTypes.EDIT_USER, data)
    }
    isFormOpen.value = false
    store.commit(MutationTypes.SET_IS_LOADING, false)
  }

</script>

<template>
  <h2 class="heading-2">Администраторы магазина</h2>

  <div class="form-container" v-if="isFormOpen">
    <h3 class="heading-3">Администратор</h3>

    <form @submit.prevent="submitForm">
      <Input
        label="Имя"
        name="name"
        placeholder="Укажите имя"
        v-model:value="v.nameField.$model"
        :error="v.nameField.$errors"
      />
      <Input
        label="Email"
        name="email"
        placeholder="Укажите EMail"
        v-model:value="v.emailField.$model"
        :error="v.emailField.$errors"
      />
      <Input v-if = "formType"
        label="Password"
        name="password"
        placeholder="Password"
        v-model:value="v.passwordField.$model"
        :error="v.passwordField.$errors"
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
    @deleteRow="onDeleteButtonClick"
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
