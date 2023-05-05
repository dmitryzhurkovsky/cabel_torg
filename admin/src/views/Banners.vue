<script setup lang='ts'>
  import { useStore } from '../store';
  import { ActionTypes } from '../store/action-types';
  import { MutationTypes } from '../store/mutation-types';
  import {ref, computed, onMounted, watch} from 'vue'
  import BaseTable from '@/components/Table/BaseTable.vue'
  import Button from '@/components/UI/Button.vue'
  import TextArea from '@/components/UI/TextArea.vue';
  import Input from '@/components/UI/Input.vue';
  import Select from '@/components/UI/Select.vue'
  import PhotoUploader from '@/components/UI/PhotoUploader.vue';
  import { IDeliveryType } from '../types';
  import { helpers, required } from '@vuelidate/validators';
  import { useVuelidate } from '@vuelidate/core';

  const store = useStore()

  const tableData = ref([] as Array<IDeliveryType>)
  const files = ref<Array<File>>([])
  
  const tableSizeColumns = '30px 1fr 1fr 1fr 1fr 1fr 50px 40px 40px 40px'

  const isFormOpen = ref(false)
  const isUploadOpen = ref(false)
  const titleField = ref('')
  const buttonNameField = ref('')
  const buttonLinkField = ref('')
  const subtitleField = ref('')
  const textField = ref('')
  const isActiveField = ref()
  const isActiveNameField = ref('') 
  const isActiveValue = ref()
  const idField = ref()
  const formType = ref(true)
  const isActiveData = [
    {name: 'Активен', id: '0', value: true},
    {name: 'Не активен', id: '1', value: false}
  ]
  const tableHeads = [
    {db: 'id', name: 'Id'},
    {db: 'title', name: 'Заголовок'}, 
    {db: 'subtitle', name: 'Контент',}, 
    {db: 'button_name', name: 'Кнопка',}, 
    {db: 'button_link', name: 'Переход',}, 
    // {db: 'text', name: 'Контент', type: 'v-html', src: 'text'}, 
    {db: 'image', name: 'Картинка', type: 'image', src: 'image'}, 
    {db: 'is_active', name: 'Актив.'}, 
    {db: '', name: ''},
    {db: '', name: ''},
    {db: '', name: ''},
  ]

  const rules = computed(() => ({
    titleField: {
      requered:  helpers.withMessage(`Обязательно поле`, required),
    },
    subtitleField: {
      requered:  helpers.withMessage(`Обязательно поле`, required),
    },
    isActiveField: {
      requered:  helpers.withMessage(`Обязательно поле`, required),
    },
    buttonNameField: {     
     requered:  helpers.withMessage(`Обязательно поле`, required),
    },
    buttonLinkField: {
      requered:  helpers.withMessage(`Обязательно поле`, required),
    },
  }))

  const v = useVuelidate(rules, {titleField, subtitleField, isActiveField, buttonNameField, buttonLinkField});

  const sendDataRequest = async () => {
    await store.dispatch(ActionTypes.GET_BANNERS_DATA, null)
  };

  watch(() => store.getters.bannersData,
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
    titleField.value = rowData.title
    subtitleField.value = rowData.subtitle
    textField.value = rowData.text
    buttonNameField.value = rowData.button_name
    buttonLinkField.value = rowData.button_link
    isActiveField.value = rowData.is_active ? 0 : 1
    isActiveNameField.value = rowData.is_active ? isActiveData[0].name : isActiveData[1].name
    isActiveValue.value = rowData.is_active ? true : false
    formType.value = false
    onSetIsFormOpen(true)
    onSetIsUploadOpen(false)
    setTimeout(() => window.scrollTo(0, 0), 0);
  } 

  const onAddButtonClick = () => {
    idField.value = null
    titleField.value = ''
    subtitleField.value = ''
    textField.value = ''
    buttonNameField.value = ''
    buttonLinkField.value = ''
    isActiveField.value = isActiveData[0].id
    isActiveNameField.value = isActiveData[0].name
    isActiveValue.value = true
    formType.value = true
    onSetIsFormOpen(true)
    onSetIsUploadOpen(false)
    setTimeout(() => window.scrollTo(0, 0), 0);
  }

  const onDeleteArticle = async (rowData: IDeliveryType) => {
    store.commit(MutationTypes.SET_IS_LOADING, true)
    await store.dispatch(ActionTypes.DELETE_BANNER, rowData.id as number)
    isFormOpen.value = false
  }

  const onSetNewStatus = (id: string) => {
    isActiveValue.value = isActiveData.filter(item => item.id === id)[0].value
    isActiveNameField.value = isActiveData.filter(item => item.id === id)[0].name
    isActiveField.value = isActiveData.filter(item => item.id === id)[0].id
  }

  const submitUpload = async () => {
    if (files.value.length) {
      const data = new FormData()
      data.append('file', files.value[0])
      await store.dispatch(ActionTypes.UPLOAD_BANNER_PHOTO, { id: idField.value, data: data })
    } 
    files.value = []
    onSetIsUploadOpen(false)
  }

  const submitForm = async () => {
    v.value.$touch()
    if (v.value.$error) return
    const data = {
      title: titleField.value,
      subtitle: subtitleField.value,
      text: textField.value,
      button_name: buttonNameField.value,
      button_link: buttonLinkField.value,
      is_active: isActiveValue.value,
    } as IDeliveryType
    console.log(data);
    
    if (formType.value) {
      store.commit(MutationTypes.SET_IS_LOADING, true)
      await store.dispatch(ActionTypes.ADD_BANNER, data)
    } else {
      store.commit(MutationTypes.SET_IS_LOADING, true)
      data.id = idField.value
      await store.dispatch(ActionTypes.EDIT_BANNER, data)
    }
    onSetIsFormOpen(false)
    // store.commit(MutationTypes.SET_IS_LOADING, false)
  }

</script>

<template>
  <h2 class="heading-2">Банеры</h2>

  <div class="form-container">
    <h3 class="heading-3">Данные банера</h3>

    <form @submit.prevent="submitUpload"  v-if="isUploadOpen">
      <PhotoUploader v-model="files" />
      <div class="form-buttons">
        <Button label="Сохранить" color="primary" ></Button>
        <Button label="Отменить" color="warning" @click="onSetIsUploadOpen(false)"></Button>
      </div>
    </form>

    <form @submit.prevent="submitForm" v-if="isFormOpen" class="form">
        <div  class="textarea__block">
            <TextArea
                    label="Заголовок"
                    name="title"
                    placeholder="Укажите заголовок"
                    v-model:value="v.titleField.$model"
                    :error="v.titleField.$errors"
                    height="200px"
            />
            <TextArea
                    label="Контент"
                    name="subtitle"
                    placeholder="Укажите контент"
                    v-model:value="v.subtitleField.$model"
                    :error="v.subtitleField.$errors"
                    height="200px"
            />
            <div class="banner__column">
                <Select
                        v-if="isActiveData.length"
                        :text = "isActiveNameField"
                        :id  = "String(isActiveField)"
                        fieldForSearch = "name"
                        :data = "isActiveData"
                        @onSelectItem="onSetNewStatus"
                        height="100%"
                />
                <Input
                        label="Название кнопки"
                        name="buttonNameField"
                        placeholder="Название кнопки"
                        v-model:value="v.buttonNameField.$model"
                        :error="v.buttonNameField.$errors"
                />
                <Input
                        label="Линк кнопки"
                        name="buttonLinkField"
                        placeholder="Линк кнопки"
                        v-model:value="v.buttonLinkField.$model"
                        :error="v.buttonLinkField.$errors"
                />
            </div>

        </div>


      <!-- <QuillEditor 
        theme="snow" 
        v-model:content = "textField" 
        contentType = "html" 
      /> -->


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
.heading-3{
  margin-bottom: 10px;
}
.form{
  margin-top: 20px;
  &-container {
    display: flex;
    flex-direction: column;
    align-items: baseline;
    margin: 15px 0;
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
.banner__column{
  display: flex;
  flex-direction: column;
  gap: 40px;

}
.form-input{
  margin-bottom: 0;
}

.edit_separator{
  height: 2px;
  width: 100%;
  background: #3c3f45;
}

</style>
