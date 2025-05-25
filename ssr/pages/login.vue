<template>
  <Breadcrumb/>
  <div class="app__content">
    <div class="_container">
      <div v-if = "authType === 1" class="popup__reg full-open">
        <div>Вход</div>
        <div class="sign-in-htm">
          <div class="group">
            <label for="user" class="label">Электронная почта</label>
            <input type="email" class="input" :class="{ 'is-invalid': authErrors.email }" id="email" v-model="email">
            <div class="error-message" v-if="authErrors.email"> {{ authErrors.email }} </div>
          </div>
          <div class="group">
            <label for="pass" class="label">Пароль</label>
            <input type="password" class="input" :class="{ 'is-invalid': authErrors.password }" id="password" v-model="password">
            <div class="error-message" v-if="authErrors.password"> {{ authErrors.password }} </div>
          </div>

          <div class="center-text">
            <button @click = "userLogin()" type="submit" class="btn black">Войти</button>
          </div>

          <div @click = "changeScreen(2)" class="foot-lnk mt-20">Не помню пароль</div>
          <div @click = "changeScreen(3)" class="bottom-link mt-20">Зарегистрироваться</div>
        </div>
      </div>
      <div v-if = "authType === 2" class="popup__reg full-open">
        <div>Восстановление пароля</div>
        <div class="reset-pass">
          <div class="group">
            <label for="user" class="label">Электронная почта</label>
            <input type="email" class="input" :class="{ 'is-invalid': authErrors.email }" id="email" v-model="email">
            <div class="error-message" v-if="authErrors.email"> {{ authErrors.email }} </div>
          </div>
          <div class="center-text">
            <button @click = "restorePassword()" type="submit" class="btn black">Восстановить</button>
          </div>
          <div @click = "changeScreen(1)" class="foot-lnk mt-20">
            Войти
          </div>
          <div @click = "changeScreen(3)" class="bottom-link mt-20">
            Зарегистрироваться
          </div>
        </div>
      </div>
      <div v-if = "authType === 3" class="popup__reg full-open">
        <div>Регистрация для юрлица</div>
        <div class="register">
          <div class="group">
            <label for="email" class="label">Электронная почта</label>
            <input id="email" type="email" class="input" :class="{ 'is-invalid': authErrors.email }" v-model="email" autocomplete=off>
            <div class="error-message" v-if="authErrors.email"> {{ authErrors.email }} </div>
          </div>
          <div class="group">
            <label for="password" class="label">Пароль</label>
            <input id="password" type="password" class="input" :class="{ 'is-invalid': authErrors.password }" v-model="password" autocomplete=off>
            <div class="error-message" v-if="authErrors.password"> {{ authErrors.password }} </div>
          </div>
          <div class="group">
            <label for="confirm" class="label">Подтверждение пароля</label>
            <input id="confirm" type="password" class="input" :class="{ 'is-invalid': authErrors.confirm }" v-model="confirm" autocomplete=off>
            <div class="error-message" v-if="authErrors.confirm"> {{ authErrors.confirm }} </div>
          </div>
          <div class="group">
            <label for="username" class="label">Имя</label>
            <input id="username" type="text" class="input" :class="{ 'is-invalid': authErrors.username }" v-model="username" autocomplete=off>
            <div class="error-message" v-if="authErrors.username"> {{ authErrors.username }} </div>
          </div>
          <div class="group">
            <label for="phone" class="label">Телефон</label>
            <input id="phone" type="tel" class="input" :class="{ 'is-invalid': authErrors.phone }" v-model="phone" autocomplete=off>
            <div class="error-message" v-if="authErrors.phone"> {{ authErrors.phone }} </div>
          </div>
          <div class="group">
            <label for="company" class="label">Компания</label>
            <input id="company" type="text" class="input" :class="{ 'is-invalid': authErrors.company }" v-model="company" autocomplete=off>
            <div class="error-message" v-if="authErrors.company"> {{ authErrors.company }} </div>
          </div>
          <div class="group">
            <label for="unp" class="label">УНП</label>
            <input id="unp" type="text" class="input" :class="{ 'is-invalid': authErrors.unp }" v-model="unp" autocomplete=off>
            <div class="error-message" v-if="authErrors.unp"> {{ authErrors.unp }} </div>
          </div>
          <div class="">
            <button @click = "userRegister" type="submit" class="btn black">Регистрация</button>
          </div>
          <div @click = "changeScreen(1)" class="foot-lnk mb-20 mt-20">Войти</div>
<!--            <div @click = "changeScreen(2)" class="foot-lnk mt-20">Не помню пароль</div>-->
        </div>
      </div>
      <div v-if = "authType === 4" class="popup__reg full-open">
        <div>Проверьте ваш email</div>
        <div class="reset-pass">
          <div class="group">
            <p>Мы отправили ссылку для <b>восстановления пароля</b> к вашей учетной записи.</p>
          </div>
          <div class="">
            <button @click = "changeScreen(1)" type="submit" class="btn empty">Вернуться на сайт</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { isValidEmail } from "@/common/validation";
  import { useHead } from 'nuxt/app';
  import { ref, onMounted } from 'vue';
  import { useNotificationsStore } from '@/stores/notifications';
  import { useAuthStore } from '@/stores/auth';
  import { useHeaderStore } from "@/stores/header";
  import { useBreadCrumbStore } from '@/stores/breadcrumb';
  import { useProfileStore } from '@/stores/profile';

  definePageMeta({
    middleware: 'auth',
  });

  const router = useRouter();
  const notificationsStore = useNotificationsStore();
  const authStore = useAuthStore();
  const headerStore = useHeaderStore();
  const breadCrumbStore = useBreadCrumbStore();
  const profileStore = useProfileStore();

  const { userData, authErrors, authType, redirectAfterLogin } = storeToRefs(authStore);

  const email = ref('');
  const password = ref('');
  const confirm = ref('');
  const username = ref('');
  const phone = ref('');
  const company = ref('');
  const unp = ref('');
  const isLoading = ref(false);

  useHead({
    title: 'Авторизация',
    meta: [{
      name: 'Авторизация',
      content: 'Страница Авторизация'
    }]
  });

  onMounted( async () => {
    breadCrumbStore.changeBreadCrumb(0);
    breadCrumbStore.addBreadCrumb({
      name: router.currentRoute.value.meta.name,
      path: router.currentRoute.value.path,
      type: "global",
      class: ""
    });
  });

  onBeforeUnmount( async () => {
    authStore.setErrors({});
  });

  // useAsyncData(() => {
  //   console.log('authToken: ', localStorage.getItem("authToken"));
    
  //   if (localStorage.getItem("authToken")) {
  //     navigateTo('/user_profile');      
  //   }
  // });

  const changeScreen = (auth_type) => {
    authStore.setAuthType(auth_type);
    const errorsInData = {};
    authStore.setErrors(errorsInData);
  };

  const userLogin = async () => {
    if (isLoading.value) return;

    notificationsStore.setIsLoading(true);
    isLoading.value = true;
    const errorsInData = {};
    authStore.setErrors(errorsInData);

    if (!isValidEmail(email.value)) {
      errorsInData.email = 'Укажите валидный адрес эл. почты'
    }
    if (!password.value || password.value.length < 8) {
      errorsInData.password = 'Пароль должен быть больше 8 символов'
    }
    if (Object.keys(errorsInData).length) {
      authStore.setErrors(errorsInData);
      notificationsStore.setIsLoading(false);
    } else {
      const loginData = new FormData();
      loginData.append('username', email.value);
      loginData.append('password', password.value);
      await authStore.sendLoginRequest(loginData);
      notificationsStore.setIsLoading(false);

      if (userData.value) {
        if (redirectAfterLogin.value) {
          router.push(redirectAfterLogin.value);
        } else {
          router.push("/user_profile");
        }
      }
    }  
    isLoading.value = false;
  };

  const userRegister = async () => {
    if (isLoading.value) return;

    notificationsStore.setIsLoading(true);
    isLoading.value = true;
    const errorsInData = {};
    authStore.setErrors(errorsInData);

    if (!isValidEmail(email.value)) {
      errorsInData.email = 'Укажите валидный адрес эл. почты'
    }
    if (!password.value || password.value.length < 8) {
      errorsInData.password = 'Пароль должен быть больше 8 символов'
    }
    if (password.value !== confirm.value) {
      errorsInData.confirm = 'Пароли не совпадают'
    }
    if (!username.value) { 
      errorsInData.username = 'Укажите имя'
    }
    if (!phone.value) {
      errorsInData.phone = 'Укажите номер телефона'
    }
    if (!company.value) {
      errorsInData.company = 'Укажите название компании'
    }
    if (!unp.value || unp.value.toString().length !== 9) {
      errorsInData.unp = 'Укажите валидное УНП'
    }
    if (Object.keys(errorsInData).length) {
      authStore.setErrors(errorsInData);
      notificationsStore.setIsLoading(false);
    } else {
      const data = {
        email: email.value,
        full_name: username.value,
        phone_number: phone.value,
        company_name: company.value,
        unp: unp.value,
        password: password.value
      };
      await authStore.sendRegisterRequest(data)
      notificationsStore.setIsLoading(false);
      if (Object.keys(authErrors.value).length === 0) {
        if (typeof window !== 'undefined') window.scrollTo(0, 0);
        profileStore.changeScreen(2);
        headerStore.setIsPopUpOpen(true);
        headerStore.setPopUpAction('ShowCompleteMsg');
        const msg ={};
          msg.main = 'Спасибо за регистрацию на CabelTorg.';
          msg.bolt = '';
          msg.sub = 'Желаем Вам приятных покупок!'
        headerStore.setPopUpMessage(msg);
        router.push("/user_profile");
      }
    }
    isLoading.value = false;
  };

  const restorePassword = async () => {
    if (isLoading.value) return;

    notificationsStore.setIsLoading(true);
    isLoading.value = true;
    const errorsInData = {};
    authStore.setErrors(errorsInData);

    if (!isValidEmail(email.value)) {
        errorsInData.email = 'Укажите валидный адрес эл. почты'
    }
    if (Object.keys(errorsInData).length) {
      notificationsStore.setIsLoading(false);
      authStore.setErrors(errorsInData);
    } else {
      const data = {
        email: email.value,
      };
      await authStore.sendRestorePasswordRequest(data);
      notificationsStore.setIsLoading(false);
      if (Object.keys(authErrors.value).length === 0) {
        changeScreen(4);
      }
    }  
    isLoading.value = false;
  };
</script>

<style lang="scss" scoped>
.popup__reg{

  .sign-in-htm{
    text-align: center;
    margin: 0 auto;
  }


  h3{
    margin-bottom: 24px;
  }
  .group{
    //width: 100%;
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    margin-bottom: 15px;
    text-align: center;
    justify-content: center;
  }
  label{
    text-align: left;
    font-size: 12px;
    line-height: 140%;
    color: #423E48;
    opacity: 0.6;
  }
  p{
    font-size: 14px;
    line-height: 140%;
    text-align: center;
    color: #423E48;
  }

  input{
    width: 100%;
    background: #FFFFFF;
    border: 1px solid rgba(66, 62, 72, 0.2);
    border-radius: 8px;
    padding: 10px 16px;
  }
  .is-invalid{
    border: 1px solid #E30044;
  }
  .error-message {
    position: absolute;
    left: 15px;
    bottom: -4px;
    padding: 0 8px 0 8px;
    font-size: 12px;
    background-color: #fff;
    color: #E30044;

  }
  button{
    text-align: center;
  }
  .foot-lnk{
      font-size: 12px;
      text-align: center;
      text-decoration-line: underline;
      opacity: 0.6;
      cursor: pointer;
    &:nth-child(2){
        opacity: 1;
    }
  }
  .bottom-link{
    font-weight: 400;
    font-size: 14px;
    line-height: 130%;
    color: #4275D8;
    text-decoration: none;
    cursor: pointer;
  }
}
.full-open{
  max-width: 500px;
  margin: 0 auto;
  text-align: center;
  min-height: 400px;
}
.center-text{
  width: 100%;
  text-align: center;
}
</style>
