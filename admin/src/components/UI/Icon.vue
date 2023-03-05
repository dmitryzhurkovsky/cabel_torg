<script setup lang='ts'>
import { ref } from "vue";

const props = defineProps({
  icon: {
    type: String,
    required: false
  },
  color: {
    type: String,
    default: 'primary'
  },
  disabled: {
    type: Boolean,
    required: false
  },
})

const emit = defineEmits(['click'])

const clickOnButton = () => {
  emit('click')
}

</script>

<template>
  <font-awesome-icon 
    :class="['btn', `btn_${color}`]"
    :icon="`fa-regular fa-${icon}`"
    :disabled="disabled"
    @click="clickOnButton"
  />
</template>

<style lang="scss" scoped>
.btn {
  height: 40px;
  border-radius: 7px;
  border: none;
  cursor: pointer;
  font-size: 15px;
  transition: .2s;
  &:disabled {
    opacity: .6;
    cursor: default;
  }
  &_primary {
    color: var(--primary);
    &:enabled:hover {
      color: var(--primary-hover);
    }
  }
  &_second {
    color: var(--second);
    &:enabled:hover {
      color: var(--second-hover);
    }
  }
  &_success {
    color: var(--success);
    &:enabled:hover {
      color: var(--success-hover);
    }
  }
  &_info {
    color: var(--info);
    &:enabled:hover {
      color: var(--info-hover);
    }
  }
  &_warning {
    color: var(--warning);
    &:enabled:hover {
      color: var(--warning-hover);
    }
  }
  &_danger {
    color: var(--danger);
    &:enabled:hover {
      color: var(--danger-hover);
    }
  }
}
</style>