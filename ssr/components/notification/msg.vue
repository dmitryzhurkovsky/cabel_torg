<template>
  <div class="popup__msg">
    <svg width="80" height="80" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path fill-rule="evenodd" clip-rule="evenodd" d="M40 70C56.5685 70 70 56.5685 70 40C70 33.3975 67.8671 27.2932 64.2528 22.3385L38.765 50.6582C37.726 51.8127 35.9776 51.9832 34.7351 51.0513L22.1333 41.6C21.2497 40.9373 21.0706 39.6837 21.7333 38.8C22.3961 37.9163 23.6497 37.7373 24.5333 38.4L36.4035 47.3027L61.6585 19.2416C56.1982 13.546 48.5132 10 40 10C23.4315 10 10 23.4315 10 40C10 56.5685 23.4315 70 40 70Z" fill="url(#paint0_linear_2011_3)"/>
      <defs>
      <linearGradient id="paint0_linear_2011_3" x1="40" y1="10" x2="40" y2="70" gradientUnits="userSpaceOnUse">
        <stop stop-color="#4275D8" stop-opacity="0.8"/>
        <stop offset="1" stop-color="#4275D8" stop-opacity="0.6"/>
      </linearGradient>
      </defs>
    </svg>
    <h3>Готово!</h3>
    <p v-if = "popUpMessage.main"> {{ popUpMessage.main }}</p>
    <p class="mt-20" v-if = "popUpMessage.sub"><b v-if = "popUpMessage.bolt">{{ popUpMessage.bolt }} </b> {{ popUpMessage.sub }}</p>
    <div class="group__row flex-center mt-20">
      <div class="center-text">
        <button @click = "returnToApp()" type="submit" class="btn black">Вернуться на сайт</button>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { useAuthStore } from '@/stores/auth';
  import { useHeaderStore } from '@/stores/header';

  const router = useRouter();
  const authStore = useAuthStore();
  const headerStore = useHeaderStore();

  const { redirectAfterLogin } = storeToRefs(authStore);
  const { popUpMessage } = headerStore;

  const returnToApp = () => {
    headerStore.setPopUpMessage({});
    headerStore.setIsPopUpOpen(false);
    headerStore.setPopUpAction('');
    if (redirectAfterLogin.value) {
      const path = redirectAfterLogin.value;
      authStore.setDestination('');
      router.push(path);
    }
  };
</script>

<style lang="scss" scoped>
.popup {
    &__msg{
        text-align: center;
        h3{
        margin: 20px 0;
        }
        p{
        font-weight: 300;
        font-size: 14px;
        line-height: 140%;
        text-align: center;
        color: #423E48;

        }
    }
}
</style>