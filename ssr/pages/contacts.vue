<template>
  <Breadcrumb/>
  <div class="contacts app__content">
    <div class="contacts__wrapper">
      <div class="contacts__content _container">
        <div class="contacts__body">
          <h3>Контактная информация</h3>
          <p>Если у вас возникнут какие-либо вопросы по работе нашего интернет-магазина или понадобится консультация
            относительно ассортимента, обратитесь к нам любым удобным для вас способом. Мы обязательно поможем!</p>
          <div class="contacts__block flex-center">

            <div class="contacts__block__item">
                <div class="block__item flex-center">
                  <img  class="_icon" src="@/assets/svg/phone.svg" alt="Phone">
                  <a class="_title"  :href="'tel:' + String(settings.phone).replace(/ /g,'')">{{ settings.phone }}</a>
                </div>
                <div class="block__item flex-center">
                  <img class="_icon" src="@/assets/svg/round-place.svg" alt="Address">
                  <div>
                    <div class="_title">Наш адрес:</div>
                    <div>{{ settings.legal_address }}</div>
                  </div>
                </div>
                <div class="block__item flex-center" 
                  v-for = "address in settings.addresses" 
                  :key ="address.id"
                >
                  <img class="_icon" src="@/assets/svg/round-place.svg" alt="Address">
                  <div>
                    <div class="_title">{{ address.title }}:</div>
                    <div>{{ address.payload }}</div>
                  </div>
                </div>
            </div>
            <div class="contacts__block__item">
              <form class="contacts__form form-contacts">
                <div class="form-contacts__title mb-20 ">Напишите нам</div>
                <div class="group">
                    <input type="text" class="input mb-20" placeholder="ФИО" v-model="fullname">
                    <div class="error-message" v-if="authErrors.fullname"> {{ authErrors.fullname }} </div>
                </div>
                <!-- <input type="text" class="input mb-20" placeholder="ФИО" v-model="fullname"> -->
                <div class="form-contacts__row flex-center mb-20">
                  <div class="group">
                    <input type="text" class="input" placeholder="Email" v-model="email">
                    <div class="error-message" v-if="authErrors.email"> {{ authErrors.email }} </div>
                  </div>
                  <div class="group">
                    <input type="text" class="input" placeholder="Телефон" v-model="phone_number">
                    <div class="error-message" v-if="authErrors.phone_number"> {{ authErrors.phone_number }} </div>
                  </div>
                </div>
                <div class="group mb-20">
                  <textarea class="textarea " placeholder="Сообщение" v-model="message"></textarea>
                  <div class="error-message" v-if="authErrors.message"> {{ authErrors.message }} </div>
                </div>
                <button class="btn" @click.prevent = "sendRequest($event)">Отправить</button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue';
  import { useHead } from 'nuxt/app';
  import { isValidEmail } from "@/common/validation";
  import { useMainStore } from '@/stores/main';
  import { useAuthStore } from '@/stores/auth';
  import { useHeaderStore } from '@/stores/header';
  import { useBreadCrumbStore } from '@/stores/breadcrumb';

  const router = useRouter();
  const route = useRoute();
  const config = useRuntimeConfig();

  const mainStore = useMainStore();
  const authStore = useAuthStore();
  const headerStore = useHeaderStore();
  const breadCrumbStore = useBreadCrumbStore();

  const { settings } = storeToRefs(mainStore);
  const { authErrors } = storeToRefs(authStore);

  const fullname = ref('');
  const phone_number = ref('');
  const email = ref('');
  const message = ref('');
  const isLoading = ref(false);

  const createCanonicalLink = computed(() => {
    return config.public.NUXT_APP_DOCUMENTS.slice(0, -1) + route.path;
  });

  useHead({
    title: 'Кабельторг | Контакты',
    meta: [{
      name: 'Контакты',
      content: 'Страница Контакты'
    }],
    link: [
      { rel: 'canonical', href: createCanonicalLink.value },
    ],
  });

  onMounted(() => {
    breadCrumbStore.changeBreadCrumb(0);
    breadCrumbStore.addBreadCrumb({
      name: "Контакты",
      path: router.currentRoute.value.path,
      type: "global",
      class: ""
    });
  });

  const sendRequest = async (event) => {
    event.preventDefault();
    if (isLoading.value) return;

    isLoading.value = true;
    const errorsInData = {};
    authStore.setErrors(errorsInData);
    if (!fullname.value) {
      errorsInData.fullname = 'Укажите валидное имя'
    }
    if (!phone_number.value) {
      errorsInData.phone_number = 'Укажите номер телефона'
    }
    if (!isValidEmail(email.value)) {
      errorsInData.email = 'Укажите email'
    }
    if (!message.value) {
      errorsInData.message = 'Укажите текст сообщения'
    }
    if (Object.keys(errorsInData).length) {
      authStore.setErrors(errorsInData);
    } else {
      const data = {
          fullname: fullname.value,
          phone_number: phone_number.value,
          email: email.value,
          message: message.value,
      };
      // Тут посылаем на бэк запрос и ждем ответа, по результатам фомируем окно с ответом
      await headerStore.sendRequestFeedback(data);
      fullname.value = '';
      phone_number.value = '';
      fullnaemailme.value = '';
      email.value = '';
      message.value = '';
    }
    isLoading.value = false;
  }
</script>

<style scoped lang="scss">
  .error-message {
    position: absolute;
    left: 15px;
    bottom: -4px;
    padding: 0 8px 0 8px;
    font-size: 12px;
    background-color: #fff;
    color: #E30044;

  }

.contacts {

  &__wrapper{


  }
  &__content{

  }

  &__body{
    padding: 0 0 60px 0;
    h3{
      margin-bottom: 28px;
    }
    p{
      font-weight: 400;
      font-size: 18px;
      line-height: 140%;
    }


  }
  &__form{
    background: #FFFFFF;
    box-shadow: 0px 4px 20px rgba(51, 51, 51, 0.1);
    border-radius: 16px;
    padding: 32px 28px;
    input{
      width: 100%;
      background: #FFFFFF;
      border: 1px solid rgba(66, 62, 72, 0.2);
      box-sizing: border-box;
      border-radius: 8px;
      font-size: 16px;
      line-height: 16px;
      display: flex;
      align-items: center;
      padding: 14px 16px;
      color: #423E48;
      position: relative;
    }


  }
  &__block{
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    margin-top: 30px;
    @media (max-width: $md2+px) {
      flex-direction: column;
    }

    &__item{
      align-items: flex-start;
      width: 100%;
      &:nth-child(1){
        flex-basis: 35%;
        padding-right: 10px;
      }

      &:nth-child(2){
        flex-basis: 65%;


      }
      .block__item{
        margin-bottom: 30px;
        align-items: flex-start;
        &:nth-child(1){
          color:#4275D8;
          cursor: pointer;


        }
      }
    }




  }
  &__paragraph{
    margin-bottom: 60px;

    &__title{
      position: relative;
      height: 20px;
      background: rgba(66, 117, 216, 0.1);
      border-radius: 4px;
      span{

        font-weight: 500;
        position: absolute;
        top: -10px;
        left: 10px;
        font-size: 20px;
        line-height: 24px;
        color: #4275D8;
      }


    }
    &__text{

      p{
        margin: 10px 0;
        font-size: 18px;
        line-height: 140%;
      }
    }
  }

}
.form-contacts{
  text-align: center;
  &__title{

  }
  .group{
    width: 100%;
    position: relative;
  }


  &__row{
    width: 100%;
    gap: 10px;

    @media (max-width: $md2+px) {
      flex-direction: column;
    }
    .input:nth-child(1){
      margin-right: 20px;
      @media (max-width: $md2+px) {
        margin-right: 0px;
        margin-bottom: 20px;
      }
    }

  }
  textarea{
    background: #FFFFFF;
    border: 1px solid rgba(66, 62, 72, 0.2);
    box-sizing: border-box;
    border-radius: 8px;
    width: 100%;
    max-height: 400px;
    padding: 14px 16px;
    resize: vertical;
    position: relative;
    min-height: 80px;
  }
  button{

  }
}
</style>
