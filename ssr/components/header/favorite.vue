<template>
  <div class="dropdown__content popup-cart">
    <h3 class="">Избранные товары</h3>

    <div class="popup-cart__list">

      <div class="popup-cart__list" v-if = "ItemsForShow.length">
        <HeaderFavoriteItem 
            class="row" 
            v-for = "favoriteItem in ItemsForShow"
            :key = "favoriteItem.product.id"
            :favoriteItem = favoriteItem
        />
      </div>

    </div>
    <div>
      <a class="popup__link" @click.prevent="onOpenFavoritePage()">Перейти в Избранное
        <svg width="16" height="8" viewBox="0 0 16 8" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M0.5 3.99935H15.0833M15.0833 3.99935L11.75 0.666016M15.0833 3.99935L11.75 7.33268" stroke="#4275D8"/>
        </svg>
      </a>
    </div>
  </div>

</template>

<script setup>
  import { computed } from 'vue';
  import { useAuthStore } from '@/stores/auth';
  import { useFavoritesStore } from '@/stores/favorites';
  import { useProfileStore } from '@/stores/profile';

  const router = useRouter();
  const authStore = useAuthStore();
  const favoritesStore = useFavoritesStore();
  const profileStore = useProfileStore();

  const { userData } = storeToRefs(authStore);
  const { favorites } = storeToRefs(favoritesStore);

  const ItemsForShow = computed(() => {
    let result = [];
    if (favorites.value.length > 5) {
      result = favorites.value.slice(favorites.value.length - 4);
    } else {
      result = [...favorites.value];
    }
    return result;
  });

  const onOpenFavoritePage = () => {
    profileStore.changeScreen(1);
    if (userData.value) {
      authStore.setDestination('');
        if (router.path != '/user_profile') {
          router.push('/user_profile');
        }
        profileStore.changeScreen(1);
    } else {
      authStore.setDestination('/user_profile');
      router.push('/login');
    }
  };
</script>

<style lang="scss" scoped>
.popup-cart{
  text-align: center;

  h3{
    font-weight: 500;
    font-size: 20px;
    line-height: 140%;
    text-align: center;
    margin-bottom: 16px;
  }

  &__list{
    margin: 30px 0;
  }

}
.popup__link{
  color: #4275D8;
  font-weight: 400;
  font-size: 14px;
}
</style>
