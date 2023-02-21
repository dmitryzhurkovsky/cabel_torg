<script setup lang='ts'>
  import Button from '@/components/UI/Button.vue';
  import { computed, onMounted, ref } from 'vue';
  import { useStore } from '../store';
  import { IArticleItem } from '../types';

  const store = useStore()
  
  const tableHeads = [
    {db: 'id', name: 'N'},
    {db: 'title', name: 'Заголовок'}, 
    {db: 'content', name: 'Контент'}, 
    {db: 'image', name: 'Картинка'}, 
    {db: '', name: ''},
    {db: '', name: ''},
  ]

  const tableSizeColumns = '30px 1fr 40px 40px'

  const sortField = ref('id')
  const typeSort = ref('asc')
  const isFormOpen = ref(false)
  const tableData = ref([] as Array<IArticleItem>)

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

  onMounted(() => {
    // store.commit(MutationTypes.SET_IS_LOADING, true)
    // sendDataRequest()
  })

</script>
<template>
  <h1 class="heading-1">News</h1>
</template>