
<script setup lang="ts">
  import { computed, PropType, ref } from "vue";
  import { helpers, minLength } from '@vuelidate/validators';
  import { useVuelidate } from '@vuelidate/core';
  import { IFormFields } from "../../types";

  const props = defineProps({
    formFilds: {
      type: Object as PropType<IFormFields>,
      required: true
    },
    columnTemplates: {
      type: String,
      required: false
    }
  })

  const payloadField = ref('');

  const rules = computed(() => ({
    payloadField: {
      payload: helpers.withMessage(`Минимальная длина поля 5 символов`, minLength(5)),
    },
  }))

  const v = useVuelidate(rules, {payloadField});

  const submitForm = () => {
    console.log('Submit');
    
  }
</script>

<template>
  <div class="login-container">
    <h1 class="heading-1">Login</h1>

    <form @submit.prevent="submitForm">
      <Input
        label="Your email"
        name="email"
        placeholder="Input your email"
        v-model:value="v.payloadField.$model"
        :error="v.payloadField.$errors"
      />

      <Button label="Submit" color="primary"></Button>
    </form>
  </div>
</template>
