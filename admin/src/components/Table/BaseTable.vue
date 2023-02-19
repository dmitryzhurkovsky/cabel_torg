<template>
  <div class="table-wrapper">
    <div class="table">
      <div
        class="table-head"
        :style="{'grid-template-columns': columnTemplates}">
        <div
          class="table-head__name"
          v-for="(element) of head"
          :key="element.db"
          @click="clickOnHead(element.db)">
          {{element.name}}
        </div>
      </div>
      <slot></slot>
    </div>
  </div>
</template>

<script setup lang="ts">
import {PropType} from 'vue';
import { ITableHead } from '../../types';

const props = defineProps({
  head: {
    type: Object as PropType<ITableHead>,
    required: true
  },
  columnTemplates: {
    type: String,
    required: false
  }
})

const emit = defineEmits(['sorting'])

const clickOnHead = (name: string) => {
  emit('sorting', name.toLowerCase())
}
</script>


<style lang="scss" scoped>
.table {
  background-color: #fff;
  width: 100%;
  margin-bottom: 40px;
  margin-top: 15px;
  &-wrapper {
    display: flex;
    justify-content: center;
  }
  &-head {
    padding: 5px 16px;
    display: grid;
    column-gap: 10px;
    align-items: center;
    border-bottom: 2px solid #EEEFF4;
    background: #fff;
    &__name {
      display: flex;
      justify-content: flex-start;
      align-items: center;
      color: #999;
      cursor: pointer;
    }
    @media screen and (max-width: 767px) {
      display: none;
    }
  }
}
</style>