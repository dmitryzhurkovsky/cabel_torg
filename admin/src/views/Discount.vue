<script setup lang='ts'>
  import { onMounted, ref, watch } from 'vue'
  import { useStore } from '../store';
  import { ActionTypes } from '../store/action-types';
  import { MutationTypes } from '../store/mutation-types';

  const store = useStore()
  const categories = ref()

  watch(() => store.getters.categories,
    (curr, prev) => {
      categories.value = [...curr];
      store.commit(MutationTypes.SET_IS_LOADING, false)
  });

  const sendDataRequest = async () => {
    await store.dispatch(ActionTypes.GET_CATEGORIES_DATA, null)
  };
  
  onMounted(() => {
    store.commit(MutationTypes.SET_IS_LOADING, true)
    sendDataRequest()
  })


</script>

<template>
  
</template>

<style lang="scss" scoped>

</style>