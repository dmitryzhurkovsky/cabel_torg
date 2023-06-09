<script setup lang='ts'>
  import { useStore } from '../store';
  import { ActionTypes } from '../store/action-types';
  import { MutationTypes } from '../store/mutation-types';
  import { ref } from 'vue'
  import Button from '@/components/UI/Button.vue'
  import PhotoUploader from '@/components/UI/PhotoUploader.vue';

  const store = useStore()

  const files = ref<Array<File>>([])

  const submitUpload = async () => {

    if (files.value.length) {
      store.commit(MutationTypes.SET_IS_LOADING, true)
      const data = new FormData()
      data.append('file', files.value[0])
      await store.dispatch(ActionTypes.UPLOAD_PRICE, data)
    } 
    files.value = []
    store.commit(MutationTypes.SET_IS_LOADING, false)
  }

</script>

<template>
  <div class="form-container">
    <h3 class="heading-3">Загрузить прайс</h3>

    <form @submit.prevent="submitUpload">
      <PhotoUploader v-model="files" isNotFoto = "true"/>
      <div class="form-buttons">
        <Button label="Сохранить" color="primary"></Button>
        <Button label="Отменить" color="warning"></Button>
      </div>
    </form>
  </div>

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
