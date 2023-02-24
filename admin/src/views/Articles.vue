<script setup lang='ts'>
  import { useStore } from '../store';
  import { ActionTypes } from '../store/action-types';
  import { MutationTypes } from '../store/mutation-types';
  import {ref, computed, onMounted, watch} from 'vue'
  import BaseTable from '@/components/Table/BaseTable.vue'
  import Button from '@/components/UI/Button.vue'
  import TextArea from '@/components/UI/TextArea.vue';
  import { router } from '../router';
  import { IDeliveryType } from '../types';
  import { helpers, minLength, required } from '@vuelidate/validators';
  import { useVuelidate } from '@vuelidate/core';

  const store = useStore()

  const tableHeads = [
    {db: 'id', name: 'Id'},
    {db: 'title', name: 'Заголовок'}, 
    {db: 'content', name: 'Контент'}, 
    {db: '', name: ''},
    {db: '', name: ''},
  ]
  const tableData = ref([] as Array<IDeliveryType>)
  const tableSizeColumns = '30px 1fr 2fr 40px 40px'

  const isFormOpen = ref(false)
  const titleField = ref('')
  const contentField = ref('')
  const idField = ref()
  const formType = ref(true)

  const rules = computed(() => ({
    titleField: {
      requered:  helpers.withMessage(`Обязательно поле`, required),
      minLength: helpers.withMessage(`Минимальная длина поля 5 символов`, minLength(5)),
    },
    contentField: {
      requered:  helpers.withMessage(`Обязательно поле`, required),
      minLength: helpers.withMessage(`Минимальная длина поля 5 символов`, minLength(5)),
    },
  }))

  const v = useVuelidate(rules, {titleField, contentField});

  const sendDataRequest = async () => {
    await store.dispatch(ActionTypes.GET_ARTICLE_DATA, null)
  };

  watch(() => store.getters.articlesData,
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
    titleField.value = rowData.title as string
    contentField.value = rowData.content as string
    formType.value = false
    onSetIsFormOpen(true)
  } 

  const onAddButtonClick = () => {
    idField.value = null
    titleField.value = '' as string
    contentField.value = '' as string
    formType.value = true
    onSetIsFormOpen(true)
  }

  const onDeleteArticle = async (rowData: IDeliveryType) => {
    store.commit(MutationTypes.SET_IS_LOADING, true)
    await store.dispatch(ActionTypes.DELETE_ARTICLE, rowData.id as number)
    isFormOpen.value = false
  }

  const submitForm = async () => {
    v.value.$touch()
    if (v.value.$error) return
    if (formType.value) {
      store.commit(MutationTypes.SET_IS_LOADING, true)
      const data = {
        title: titleField.value,
        content: contentField.value,
      }
      await store.dispatch(ActionTypes.ADD_ARTICLE, data)
    } else {
      store.commit(MutationTypes.SET_IS_LOADING, true)
      const data = {
        id: idField.value, 
        title: titleField.value,
        content: contentField.value,
      }
      await store.dispatch(ActionTypes.EDIT_ARTICLE, data)
    }
    isFormOpen.value = false
    // store.commit(MutationTypes.SET_IS_LOADING, false)
  }

</script>

<template>
  <h2 class="heading-2">Новости</h2>

  <div class="form-container" v-if="isFormOpen">
    <h3 class="heading-3">Новая новость</h3>

    <form @submit.prevent="submitForm">
      <TextArea
        label="Заголовок"
        name="title"
        placeholder="Укажите заголовок"
        v-model:value="v.titleField.$model"
        :error="v.titleField.$errors"
        width="600px"
        height="80px"
      />
      <TextArea
        label="Крнтент"
        name="content"
        placeholder="Укажите содержание"
        v-model:value="v.contentField.$model"
        :error="v.contentField.$errors" 
        width="600px"
        height="150px"
      />
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
