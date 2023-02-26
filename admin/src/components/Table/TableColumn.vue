<script setup lang="ts">
import { PropType } from 'vue'
import { ITableHeadItem } from '../../types'
import Img from '@/components/UI/Img.vue'

const props = defineProps({
  image: {
    type: Boolean,
    required: false,
    default: false
  },
  srcImage: {
    type: String,
    required: false,
    default: '',
  },
  columnTitle: {
    type: Object as PropType<ITableHeadItem>,
    required: false
  }
})
</script>

<template>
  <div v-if="columnTitle?.db" class="table-column">
    <span class="table-column__title" v-if="columnTitle?.db">{{columnTitle.db}}: </span>
    <slot v-if="!image"></slot>
    <div v-else class="table-column-image">
      <Img :image="srcImage" />
    </div>
  </div>
</template>

<style lang="scss" scoped>
.table-column {
  padding: 15px 0;
  position: relative;
  &-image {
    max-width: 400px;
    @media screen and (max-width: 767px) {
      max-width: 200px;
    }
  }
  &__title {
    margin-right: 5px;
    display: none;
    @media screen and (max-width: 767px) {
      display: inline-block;
    }
  }
}
</style>