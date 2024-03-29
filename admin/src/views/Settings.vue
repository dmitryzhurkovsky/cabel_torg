<script setup lang='ts'>
  import useVuelidate from '@vuelidate/core';
  import { email, helpers, maxLength, minLength, numeric, required } from '@vuelidate/validators';
  import { computed, onMounted, ref, watch } from 'vue'
  import { useStore } from '../store';
  import { ActionTypes } from '../store/action-types';
  import { MutationTypes } from '../store/mutation-types';
  import Button from '@/components/UI/Button.vue'
  import Input from '@/components/UI/Input.vue';

  const store = useStore()
  const id = ref('')
  const phone = ref('')
  const mail = ref('')
  const director_fullname = ref('')
  const unp = ref('')
  const OKPO = ref('')
  const legal_address = ref('')
  const postal_address = ref('')
  const phone_and_fax = ref('')
  const serving_bank = ref('')
  const serving_bank_short = ref('')
  const IBAN = ref('')
  const RUR = ref('')
  const instagram_url = ref('')
  const facebook_url = ref('')
  const vk_url = ref('')
  const telegram_url = ref('')
  const twitter_url = ref('')
  const tiktok_url = ref('')
  const youtube_url = ref('')

  const rules = computed(() => ({
    phone: {
      requered:  helpers.withMessage(`Обязательно поле`, required),
      minLength: helpers.withMessage(`Минимальная длина поля 7 символов`, minLength(7)),
    },
    mail: {
      requered:  helpers.withMessage(`Обязательно поле`, required),
      email: helpers.withMessage(`укажите валидный E-Mail`, email),
    },
    director_fullname: {
      requered:  helpers.withMessage(`Обязательно поле`, required),
    },
    unp: {
      requered:  helpers.withMessage(`Обязательно поле`, required),
      minLength: helpers.withMessage(`Длина поля 9 символов`, minLength(9)),
      maxLength: helpers.withMessage(`Длина поля 9 символов`, maxLength(9)),
      numeric: helpers.withMessage(`Это числовое поле`, numeric)
    },
    OKPO: {
      requered:  helpers.withMessage(`Обязательно поле`, required),
      numeric: helpers.withMessage(`Это числовое поле`, numeric)
    },
    legal_address: {
      requered:  helpers.withMessage(`Обязательно поле`, required),
    },
    postal_address: {
      requered:  helpers.withMessage(`Обязательно поле`, required),
    },
    phone_and_fax: {
      requered:  helpers.withMessage(`Обязательно поле`, required),
      minLength: helpers.withMessage(`Минимальная длина поля 7 символов`, minLength(7)),
    },
    serving_bank: {
      requered:  helpers.withMessage(`Обязательно поле`, required),
    },
    serving_bank_short: {
      requered:  helpers.withMessage(`Обязательно поле`, required),
    },
    IBAN: {
      requered:  helpers.withMessage(`Обязательно поле`, required),
      minLength: helpers.withMessage(`Длина поля 9 символов`, minLength(28)),
      maxLength: helpers.withMessage(`Длина поля 9 символов`, maxLength(28)),
    },
    RUR: {
      requered:  helpers.withMessage(`Обязательно поле`, required),
    },
    instagram_url: {
      requered:  helpers.withMessage(`Обязательно поле`, required),
    },
    facebook_url: {
      requered:  helpers.withMessage(`Обязательно поле`, required),
    },
    vk_url: {
      requered:  helpers.withMessage(`Обязательно поле`, required),
    },
    telegram_url: {
      requered:  helpers.withMessage(`Обязательно поле`, required),
    },
    twitter_url: {
      requered:  helpers.withMessage(`Обязательно поле`, required),
    },
    tiktok_url: {
      requered:  helpers.withMessage(`Обязательно поле`, required),
    },
    youtube_url: {
      requered:  helpers.withMessage(`Обязательно поле`, required),
    },
  }))

  const v = useVuelidate(rules, {
    phone, mail, director_fullname, unp, OKPO, legal_address, postal_address, phone_and_fax, serving_bank, serving_bank_short, IBAN,
    RUR, instagram_url, facebook_url, vk_url, telegram_url, twitter_url, tiktok_url, youtube_url,
  });

  watch(() => store.getters.settings,
    (curr, prev) => {
      id.value = curr.id
      phone.value = curr.phone
      mail.value = curr.email
      director_fullname.value = curr.director_fullname
      unp.value = curr.unp
      OKPO.value = curr.OKPO
      legal_address.value = curr.legal_address
      postal_address.value = curr.postal_address
      phone_and_fax.value = curr.phone_and_fax
      serving_bank.value = curr.serving_bank
      serving_bank_short.value = curr.serving_bank_short
      IBAN.value = curr.IBAN
      RUR.value = curr.RUR
      instagram_url.value = curr.instagram_url
      facebook_url.value = curr.facebook_url
      vk_url.value = curr.vk_url
      telegram_url.value = curr.telegram_url
      twitter_url.value = curr.twitter_url
      tiktok_url.value = curr.tiktok_url
      youtube_url.value = curr.youtube_url
      store.commit(MutationTypes.SET_IS_LOADING, false)
  });

  const sendDataRequest = async () => {
    await store.dispatch(ActionTypes.GET_SETTINGS_DATA, null)
  };
  
  onMounted(() => {
    store.commit(MutationTypes.SET_IS_LOADING, true)
    sendDataRequest()
  })

  const submitForm = async () => {
    v.value.$touch()
    if (v.value.$error) return
    store.commit(MutationTypes.SET_IS_LOADING, true)
    const data = {
      id : id.value,
      phone : phone.value, 
      email : mail.value, 
      director_fullname: director_fullname.value, 
      unp : unp.value, 
      OKPO : OKPO.value, 
      legal_address : legal_address.value, 
      postal_address : postal_address.value, 
      phone_and_fax : phone_and_fax.value, 
      serving_bank : serving_bank.value, 
      serving_bank_short : serving_bank_short.value, 
      IBAN : IBAN.value,
      RUR: RUR.value, 
      instagram_url : instagram_url.value, 
      facebook_url : facebook_url.value, 
      vk_url :vk_url.value, 
      telegram_url : telegram_url.value, 
      twitter_url : twitter_url.value, 
      tiktok_url : tiktok_url.value, 
      youtube_url : youtube_url.value,
    }
    await store.dispatch(ActionTypes.EDIT_SETTINGS_DATA, data)
  }

</script>

<template>
  <h2 class="heading-2">Настройки сайта</h2>

  <div class="form-container">
    <h3 class="heading-3">Изменение настроек</h3>

    <form @submit.prevent="submitForm">
      <Input
        label="Телефон"
        name="phone"
        width="600px"
        placeholder="Укажите телефон"
        v-model:value="v.phone.$model"
        :error="v.phone.$errors"
      />
      <Input
        label="E-Mail"
        name="mail"
        width="600px"
        placeholder="Укажите E-Mail"
        v-model:value="v.mail.$model"
        :error="v.mail.$errors"
      />
      <Input
        label="Директор"
        name="director_fullname"
        width="600px"
        placeholder="Укажите директора"
        v-model:value="v.director_fullname.$model"
        :error="v.director_fullname.$errors"
      />
      <Input
        label="УНП"
        name="unp"
        width="600px"
        placeholder="Укажите УНП"
        v-model:value="v.unp.$model"
        :error="v.unp.$errors"
      />
      <Input
        label="ОКПО"
        name="OKPO"
        width="600px"
        placeholder="Укажите ОКПО"
        v-model:value="v.OKPO.$model"
        :error="v.OKPO.$errors"
      />
      <Input
        label="Юридический адрес"
        name="legal_address"
        width="600px"
        placeholder="Укажите Юридический адрес"
        v-model:value="v.legal_address.$model"
        :error="v.legal_address.$errors"
      />
      <Input
        label="Почтовый адрес"
        name="postal_address"
        width="600px"
        placeholder="Укажите Почтовый адрес"
        v-model:value="v.postal_address.$model"
        :error="v.postal_address.$errors"
      />
      <Input
        label="Факс"
        name="phone_and_fax"
        width="600px"
        placeholder="Укажите факс"
        v-model:value="v.phone_and_fax.$model"
        :error="v.phone_and_fax.$errors"
      />
      <Input
        label="Обслужвающий банк"
        name="serving_bank"
        width="600px"
        placeholder="Укажите обслужвающий банк"
        v-model:value="v.serving_bank.$model"
        :error="v.serving_bank.$errors"
      />
      <Input
        label="Обслужвающий банк короткое"
        name="serving_bank_short"
        width="600px"
        placeholder="Укажите обслужвающий банк короткое"
        v-model:value="v.serving_bank_short.$model"
        :error="v.serving_bank_short.$errors"
      />
      <Input
        label="IBAN"
        name="IBAN"
        width="600px"
        placeholder="Укажите IBAN"
        v-model:value="v.IBAN.$model"
        :error="v.IBAN.$errors"
      />
      <Input
        label="RUR"
        name="RUR"
        width="600px"
        placeholder="Укажите RUR"
        v-model:value="v.RUR.$model"
        :error="v.RUR.$errors"
      />
      <Input
        label="Instagram"
        name="instagram_url"
        width="600px"
        placeholder="Укажите instagram"
        v-model:value="v.instagram_url.$model"
        :error="v.instagram_url.$errors"
      />
      <Input
        label="Facebook"
        name="facebook_url"
        width="600px"
        placeholder="Укажите Facebook"
        v-model:value="v.facebook_url.$model"
        :error="v.facebook_url.$errors"
      />
      <Input
        label="VK"
        name="vk_url"
        width="600px"
        placeholder="Укажите VK"
        v-model:value="v.vk_url.$model"
        :error="v.vk_url.$errors"
      />
      <Input
        label="Telegram"
        name="telegram_url"
        width="600px"
        placeholder="Укажите telegram"
        v-model:value="v.telegram_url.$model"
        :error="v.telegram_url.$errors"
      />
      <Input
        label="Twitter"
        name="twitter_url"
        width="600px"
        placeholder="Укажите twitter"
        v-model:value="v.twitter_url.$model"
        :error="v.twitter_url.$errors"
      />
      <Input
        label="Tiktok"
        name="tiktok_url"
        width="600px"
        placeholder="Укажите tiktok"
        v-model:value="v.tiktok_url.$model"
        :error="v.tiktok_url.$errors"
      />
      <Input
        label="Youtube"
        name="youtube_url"
        width="600px"
        placeholder="Укажите youtube"
        v-model:value="v.youtube_url.$model"
        :error="v.youtube_url.$errors"
      />
      <div class="form-buttons">
        <Button label="Сохранить" color="primary" ></Button>
      </div>
    </form>
  </div>

</template>

<style lang="scss" scoped>
  .form{
    &-container {
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: baseline;
      margin: 15px 0;
      background-color: var(--background-content);
    }
    &-buttons {
      display: flex;
      justify-content: space-around;
    }
  }

</style>