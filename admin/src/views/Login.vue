<script setup lang="ts">
import {ref, computed} from 'vue'
import useVuelidate from '@vuelidate/core'
import {helpers, minLength, maxLength, numeric, email, sameAs} from '@vuelidate/validators'
import { useStore } from '../store'
import { ActionTypes } from '../store/action-types'
import { MutationTypes } from '../store/mutation-types'
import Input from '@/components/UI/Input.vue'
import Button from '@/components/UI/Button.vue'
import { router } from '../router'
import Header from "../components/Layout/Header.vue";

const emailField = ref('')
const passwordField = ref('')
const store = useStore()

const rules = computed(() => ({
  emailField: {
    email: helpers.withMessage('Вы ввели неверный email', email)
  },
  passwordField: {
    password: helpers.withMessage(`Минимальная длина пароля 8 символов`, minLength(8)),
  },
}))

const v = useVuelidate(rules, {emailField, passwordField})

const sendLoginRequest = async (data: FormData) => {
  const result = await store.dispatch(ActionTypes.SEND_USER_REQUEST, data)
  store.commit(MutationTypes.SET_IS_LOADING, false)
  router.push('/')
}

const submitForm = () => {
  v.value.$touch()
  if (v.value.$error) return
  store.commit(MutationTypes.SET_IS_LOADING, true)
  const data = new FormData()
  data.append('username', emailField.value)
  data.append('password', passwordField.value)
  sendLoginRequest(data)
}
</script>

<template>
  <div class="login-container">

    <a href="http://localhost:8080" class="admin__logo">
        <img src="@/assets/admin_logo.svg" alt="CabelTorg">
    </a>

    <form @submit.prevent="submitForm">
      <Input
        label="Ваш email"
        name="email"
        placeholder="Укажите Ваш email"
        v-model:value="v.emailField.$model"
        :error="v.emailField.$errors"
      />
      <Input
        label="Пароль"
        name="password"
        placeholder="Укажите Ваш password"
        v-model:value="v.passwordField.$model"
        type="password"
        :error="v.passwordField.$errors"
      />

      <Button label="Вход" color="primary"></Button>
    </form>
  </div>
</template>

<style lang="scss" scoped>
.login-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-left: -250px;
}
.content{
  margin-left: 0;
}
.admin__logo{
  margin-bottom: 40px;
}
.btn_primary{
  width: 100%;
  margin: 0;
}
</style>
