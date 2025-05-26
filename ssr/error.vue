<template>
  <div id="app__component">
    <HeaderWrapper />
    <NotificationMain />
    <NuxtLoadingIndicator :color="'#FF9549'" />
    <MyHeader />
    <div class="structure app__content">
      <div class="structure__wrapper">
        <div class="structure__content _container">
          <div class="structure__body">
          </div>
          <div class="structure__block">
            <div class="structure__title">Что-то пошло не так...</div>
            <div class="structure__text">Так уж получилось, что из множества страниц нашего сайта Вы оказались как раз на той, которая уже не существует…</div>
            <button class="btn" @click ="navigateTo('/catalog')">Вернуться на главную</button>
          </div>
        </div>
      </div>
    </div>
    <MyFooter />
  </div>
</template>

<script setup>
import { onBeforeMount } from 'vue'
import { useNotificationsStore } from '@/stores/notifications';
import { useMainStore } from '@/stores/main';
import { useOrdersStore } from '@/stores/orders';
import { useAuthStore } from '@/stores/auth';
import { useHeaderStore } from '@/stores/header';
import { useFavoritesStore } from '@/stores/favorites';

const notificationsStore = useNotificationsStore();
const mainStore = useMainStore();
const oredersStore = useOrdersStore();
const authStore = useAuthStore();
const headerStore = useHeaderStore();
const favoritesStore = useFavoritesStore();

onBeforeMount(async () => {
  const nullData = [];
  if (!localStorage.getItem("carts")) localStorage.setItem("carts", JSON.stringify(nullData));
  if (!localStorage.getItem("favorites")) localStorage.setItem("favorites", JSON.stringify(nullData));
  await favoritesStore.getUserFavorite();
  await oredersStore.getUserOrder();
  if (localStorage.getItem("authToken")) {
      await authStore.getUserData();
  }
});

await useAsyncData(async () => {
  notificationsStore.setIsLoading(true);
  await headerStore.getCategories();
  await oredersStore.getOrderDeliveryTypes();
  await mainStore.getSettings();
  notificationsStore.setIsLoading(false);
  return true;
});


</script>

<style scoped lang="scss">

.structure {

  &__wrapper{



  }
  &__content{

  }

  &__body{
    background-image: url("@/assets/404.png");
    background-position: top center;
    background-repeat: no-repeat;
    min-height: 500px;

  }
  &__title{
    margin-bottom: 30px;


  }
  &__text{
    width: 50%;
    margin: 0 auto;
  }
  &__block{
    text-align: center;
    padding: 20px 0 60px 0;
    button{
      background: #423E48;
      margin-top: 30px;
    }


  }
  &__item{

  }


}


</style>
