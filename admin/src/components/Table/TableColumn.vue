<template>
  <div class="table-column">
    <span class="table-column__title" v-if="columnTitle?.name">{{columnTitle.name}}: </span>
    <slot v-if="!image"></slot>
    <img v-else class="table-column-image" :src="srcImage" alt="">
  </div>
</template>

<script setup lang="ts">
import { PropType } from 'vue'
import { ItableHeadItem } from '../../types'

const props = defineProps({
  image: {
    type: Boolean,
    required: false
  },
  srcImage: {
    type: String,
    required: false
  },
  columnTitle: {
    type: Object as PropType<ItableHeadItem>,
    required: false
  }
})
</script>

<style lang="scss" scoped>
.table-column {
  padding: 15px 0;
  position: relative;
  &-image {
    max-width: 100%;
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