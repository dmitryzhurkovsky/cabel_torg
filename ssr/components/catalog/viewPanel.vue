<template>
  <ul class="tools-view">
    <!-- list, grid -->
    <li class="tools-view__item">
      <a href="" 
        :class="['table' === catalogViewType ? 'tools-view__link icon-catalog-table active' : 'tools-view__link icon-catalog-table']"
        @click.prevent="changeView('table')"
      ></a>
    </li>
    <li class="tools-view__item">
      <a href="" 
        :class="['row' === catalogViewType ? 'tools-view__link icon-catalog-row active' : 'tools-view__link icon-catalog-row']"
        @click.prevent="changeView('row')"
      ></a>
    </li>
  </ul>
</template>

<script setup>
  import { useQueryStore } from '@/stores/query';

  const queryStore = useQueryStore();

  const { catalogViewType } = storeToRefs(queryStore);

  const changeView = (type) => {
    queryStore.setViewType(type);
  }
</script>

<style lang="scss" scoped>
.tools-view{
  float: right;
  display: flex;
  align-items: center;
  gap: 10px;
  &__item{
    .active{
      color: #423E48;
    }
  }
  a{
    font-size: 20px;
    color: #ddd;
    transition: all 0.3s ease;
    &:hover{
      color: #423E48;
      opacity: 0.8;
    }
  }
}
</style>