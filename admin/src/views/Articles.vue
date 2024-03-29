<script setup lang='ts'>
  import { useStore } from '../store';
  import { ActionTypes } from '../store/action-types';
  import { MutationTypes } from '../store/mutation-types';
  import {ref, computed, onMounted, watch} from 'vue'
  import BaseTable from '@/components/Table/BaseTable.vue'
  import Button from '@/components/UI/Button.vue'
  import TextArea from '@/components/UI/TextArea.vue';
  import PhotoUploader from '@/components/UI/PhotoUploader.vue';
  import { IDeliveryType } from '../types';
  import { helpers, minLength, required } from '@vuelidate/validators';
  import { useVuelidate } from '@vuelidate/core';

  const store = useStore()

  const tableData = ref([] as Array<IDeliveryType>)
  const files = ref<Array<File>>([])
  
  // const tableSizeColumns = '30px 1fr 2fr 2fr 1fr 40px 40px 40px'
  const tableSizeColumns = '30px 1fr 2fr 1fr 40px 40px 40px'

  const isFormOpen = ref(false)
  const isUploadOpen = ref(false)
  const titleField = ref('')
  const contentField = ref('')
  const contentShortField = ref('')
  const idField = ref()
  const formType = ref(true)

  const tableHeads = [
    {db: 'id', name: 'Id'},
    {db: 'title', name: 'Заголовок'}, 
    {db: 'preview_text', name: 'Контент превью', type: 'v-html', src: 'preview_text'}, 
    // {db: 'content', name: 'Контент', type: 'v-html', src: 'content'}, 
    {db: 'image', name: 'Картинка', type: 'image', src: 'image'}, 
    {db: '', name: ''},
    {db: '', name: ''},
    {db: '', name: ''},
  ]

  const rules = computed(() => ({
    titleField: {
      requered:  helpers.withMessage(`Обязательно поле`, required),
      minLength: helpers.withMessage(`Минимальная длина поля 5 символов`, minLength(5)),
    },
  }))

  const v = useVuelidate(rules, {titleField});

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

  const onSetIsUploadOpen = (val: boolean) => {
    isUploadOpen.value = val
  }

  const onUploadButtonClick = (rowData: IDeliveryType) => {
    idField.value = rowData.id
    onSetIsFormOpen(false)
    onSetIsUploadOpen(true)
  }

  const onEditButtonClick = (rowData: IDeliveryType) => {
    idField.value = rowData.id
    titleField.value = rowData.title as string
    contentField.value = rowData.content as string
    contentShortField.value = rowData.preview_text as string
    formType.value = false
    onSetIsFormOpen(true)
    onSetIsUploadOpen(false)
    setTimeout(() => window.scrollTo(0, 0), 0);
  } 

  const onAddButtonClick = () => {
    idField.value = null
    titleField.value = '' as string
    contentField.value = '' as string
    contentShortField.value = '' as string
    formType.value = true
    onSetIsFormOpen(true)
    onSetIsUploadOpen(false)
    setTimeout(() => window.scrollTo(0, 0), 0);
  }

  const onDeleteArticle = async (rowData: IDeliveryType) => {
    store.commit(MutationTypes.SET_IS_LOADING, true)
    await store.dispatch(ActionTypes.DELETE_ARTICLE, rowData.id as number)
    isFormOpen.value = false
  }

  const submitUpload = async () => {
    if (files.value.length) {
      const data = new FormData()
      data.append('file', files.value[0])
      await store.dispatch(ActionTypes.UPLOAD_ARTICLE_PHOTO, { id: idField.value, data: data })
    } 
    files.value = []
    onSetIsUploadOpen(false)
  }

  const submitForm = async () => {
    v.value.$touch()
    if (v.value.$error) return
    const data = {
        title: titleField.value,
        content: contentField.value,
        preview_text: contentShortField.value,
      } as IDeliveryType
    if (formType.value) {
      store.commit(MutationTypes.SET_IS_LOADING, true)
      await store.dispatch(ActionTypes.ADD_ARTICLE, data)
    } else {
      store.commit(MutationTypes.SET_IS_LOADING, true)
      data.id = idField.value
      await store.dispatch(ActionTypes.EDIT_ARTICLE, data)
    }
    onSetIsFormOpen(false)
    // store.commit(MutationTypes.SET_IS_LOADING, false)
  }

</script>

<template>
  <h2 class="heading-2">Новости</h2>

  <div class="form-container">
    <h3 class="heading-3">Новая новость</h3>


    <form @submit.prevent="submitUpload"  v-if="isUploadOpen">
      <PhotoUploader v-model="files" />
      <div class="form-buttons">
        <Button label="Сохранить" color="primary" ></Button>
        <Button label="Отменить" color="warning" @click="onSetIsUploadOpen(false)"></Button>
      </div>
    </form>

    <form @submit.prevent="submitForm" v-if="isFormOpen" class="form">

        <div  class="textarea__block">
            <div class="textarea__col">
                <h3 class="heading-3">Заголовок</h3>
                 <TextArea
                         name="title"
                         placeholder="Укажите заголовок"
                         v-model:value="v.titleField.$model"
                         :error="v.titleField.$errors"
                         height="80px"
                         width="100%"
                 />
            </div>

            <div class="textarea__col">
                <h3 class="heading-3">Превью новости (<i>100 символов)</i></h3>
                <QuillEditor
                        theme="snow"
                        v-model:content = "contentShortField"
                        contentType = "html"

                />
            </div>


        </div>


      <h3 class="heading-3">Новость</h3>
      <QuillEditor 
        theme="snow" 
        v-model:content = "contentField" 
        contentType = "html"
        height="300px"
      />
      <!-- <PhotoUploader v-model="files" /> -->
      <div class="form-buttons">
        <Button label="Создать" color="primary" v-if="formType"></Button>
        <Button label="Сохранить" color="primary" v-if="!formType"></Button>
        <Button label="Отменить" color="warning" @click="onSetIsFormOpen(false)"></Button>
      </div>
        <hr class="edit_separator">
    </form>
  </div>

  <base-table
    :head="tableHeads"
    :columnTemplates="tableSizeColumns"
    :tableData="tableData"
    :uploadButton=true
    @openForm="onAddButtonClick"
    @uploadRow="onUploadButtonClick"
    @editRow="onEditButtonClick"
    @deleteRow="onDeleteArticle"
  />
</template>

<style lang="scss" scoped>

.form{
  width: 100%;
  &-container {
    display: flex;
    flex-direction: column;
    align-items: baseline;
    margin: 15px 0;
    padding: 15px 20px;
    background-color: var(--background-content);
  }
  &-buttons {
    display: flex;
    justify-content: flex-start;
    margin: 20px 0;
  }
}

.textarea__block{
  width: 100%;
  display: flex;
  gap: 20px;

}
.textarea__col{
  margin-bottom: 20px;
  height: 100%;
  width: 100%;
}
.edit_separator{
  height: 2px;
  width: 100%;
  background: #3c3f45;
}
</style>
