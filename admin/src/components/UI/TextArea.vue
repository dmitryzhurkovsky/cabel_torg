<script setup lang='ts'>
import { IDeliveryType } from '../../types';

// import { Ref } from 'vue';
const emit = defineEmits(['update:value']);
const props = defineProps({
  error: {
    type: Array<IDeliveryType>,
    required: false
  },
  value: {
    type: String,
    default: ''
  },
  name: {
    type: String,
    required: true
  },
  type: {
    type: String,
    default: 'text'
  },
  placeholder: {
    type: String,
    required: true
  },
  label: {
    type: String,
    required: true
  },
  width: {
    type: String,
    default: '300px'
  },
  height: {
    type: String,
    default: '100px'
  }
})

const updateValue = (e: Event) => {
  const target = e.target as HTMLInputElement;
  emit('update:value', target.value);
}

</script>

<template>
  <div class="form-input" :style="{width: width, height: height}">
    <textarea
      class="input-text"
      :type="type"
      :name="name"
      :id="name"
      :placeholder="placeholder"
      :value="value"
      @input="updateValue">
    </textarea>
    <label :for="name" class="input-label">{{label}}</label>
    <TransitionGroup>
      <div
        class="form-error"
        v-for="element of error"
        :key="element.$uid">
        <div class="form-error__message">{{element.$message}}</div>
      </div>
    </TransitionGroup>
  </div>
</template>

<style lang="scss" scoped>
.form {
  &-input {
    margin-bottom: 30px;
    position: relative;
  }
  &-error {
    position: absolute;
    left: 15px;
    bottom: -4px;
    padding: 0 8px 0 8px;
    font-size: 12px;
    background-color: var(--background-content);
    color: var(--danger);
    z-index: 1;
  }
}
.input {
  &-text {
  border: 1px solid var(--primary);
  padding: 0 10px;
  height: 40px;
  border-radius: 7px;
  font-size: 15px;
  width: 100%;
  height: 100%;
  position: relative;
  z-index: 1;
    &:focus {
      & + .input-label {
        z-index: 1;
        opacity: 1;
        top: -20px;
      }
    }
    &:not(:placeholder-shown) {
      & + .input-label {
        z-index: 1;
        opacity: 1;
        top: -20px;
      }
    }
  }
  &-label {
    font-weight: bold;
    display: block;
    position: absolute;
    top: 20px;
    opacity: 0;
    z-index: -1;
    transition: .2s;
    font-size: 13px;
    color: var(--primary);
  }
}

.v-enter-active,
.v-leave-active {
  transition: opacity 0.2s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}
</style>