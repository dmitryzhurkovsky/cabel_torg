<template>
  <div class="topmenu__right client-bar flex-center">
    <div class="topmenu__item right-direction"
        @click.stop="onFavoriteIconEnter()"
        @mouseleave="onIconLeave()"
    >
      <div class="dropdown icon-favorite">
        <div :class="[!favoriteHover ? 'dropdown__wrapper': 'dropdown__wrapper wrapper__show']">
            <div class="dropdown__inner">
                <HeaderFavorite @click.stop = "onIconLeaveClick()" />
            </div>

        </div>

      </div>
    </div>
    <div class="topmenu__item right-direction" 
        @click.stop="onUserIconEnter()"
        @mouseleave="onIconLeave()"
    >
      <div class="dropdown" 
          :class="[!userData ? 'icon-user' : 'icon-user-login']"
      >
        <div v-if = "userHover && !userData" :class="[!userHover ? 'dropdown__wrapper' : 'dropdown__wrapper wrapper__show']">
            <div class="dropdown__inner">
                <div class="dropdown__content popup-cart">
                    <div class="avatar__box">
                        <div class="avatar icon-user flex-center"></div>
                    </div>

                    <div @click.stop="handleClick('/login', 1)" class="btn black mb-20">
                        Вход
                    </div>

                    <div @click.stop="handleClick('/login', 2)" class="foot-lnk">
                        Не помню пароль
                    </div>
                    <hr class="hr">
                    <div @click.stop="handleClick('/login', 3)" class="foot-reg">
                        Зарегистрироваться
                    </div>
                </div>
            </div>

          <!-- <UserActions/> -->
        </div>
        <div v-if = "userHover && userData" :class="[!userHover ? 'dropdown__wrapper' : 'dropdown__wrapper wrapper__show']">

          <div class="dropdown__content popup-cart user-login">
            <div class="dropdown__list">
                <h3>
                  Личный кабинет
                </h3>
                <a @click.stop="handleClick('/user_profile', 0)" class="icon-go-cart">
                  Мои заказы
                </a>
                <a @click.stop="handleClick('/user_profile', 2)" class="icon-setting">
                  Настройки
                </a>
                <a @click.stop="userLogout()" class="icon-exit">
                  Выйти из аккаунта
                </a>
            </div>

          </div>
          <!-- <UserActions/> -->
        </div>

      </div>

    </div>
    <div class="topmenu__item right-direction" 
        @click.stop="onCartIconEnter()"
        @mouseleave="onIconLeave()"
    >
      <div class="dropdown icon-cart">
        <div :class="[!cartHover ? 'dropdown__wrapper': 'dropdown__wrapper wrapper__show']">
            <div class="dropdown__inner">
                <HeaderCart @click.stop = "onIconLeaveClick()" />
            </div>

        </div>
      </div>
      <CatalogIconQuantity 
        :quantity = orders.length 
        :left = '10'
        :top = '10'
      />
    </div>
  </div>
</template>

<script setup>
  import { ref } from 'vue';
  import { useAuthStore } from '@/stores/auth';
  import { useQueryStore } from '@/stores/query';
  import { useHeaderStore } from '@/stores/header';
  import { useOrdersStore } from '@/stores/orders';
  import { useProfileStore } from '@/stores/profile';

  const route = useRoute();
  const router = useRouter();

  const authStore = useAuthStore();
  const queryStore = useQueryStore();
  const headerStore = useHeaderStore();
  const oredersStore = useOrdersStore();
  const profileStore = useProfileStore();

  const isLoading = ref(false);
  const userHover = ref(false);
  const cartHover = ref(false);
  const favoriteHover = ref(false);

  const { userData } = storeToRefs(authStore);
  // const { searchString } = storeToRefs(queryStore);
  const { orders } = storeToRefs(oredersStore);

  const handleClick = (URL, screen_type) => {
    setTimeout(() => headerStore.updateIsCatalogOpen(false), 0);
    setTimeout(() => headerStore.updateIsMenuActionsOpen(false), 0);
    cartHover.value = false;
    userHover.value = false;
    favoriteHover.value = false;
    if (route.path != URL) {
      if (URL === '/login') {
        authStore.setAuthType(screen_type);
      } else {
        profileStore.changeScreen(screen_type);
      }
      router.push(URL);
    } else {
      if (URL === '/login') {
        authStore.setAuthType(screen_type);
      } else {
        profileStore.changeScreen(screen_type);
      }
    }
  };

  const userLogout = async () => {
    if (isLoading.value) return;
    userHover.value = false;
    setTimeout(() => headerStore.updateIsCatalogOpen(false), 0);
    setTimeout(() => headerStore.updateIsMenuActionsOpen(false), 0);
    isLoading.value = true;
    authStore.sendLogoutRequest();
    isLoading.value = false;
    router.push('/');
  };

  // const clearSearchString = () => {
  //   queryStore.setSearchString('');
  // };

  const onUserIconEnter = () => {
    queryStore.setSearchString('');
    headerStore.updateIsMenuActionsOpen(true);
    favoriteHover.value = false;
    cartHover.value = false;
    userHover.value = true;
  };

  const onCartIconEnter = () => {
    queryStore.setSearchString('');
    headerStore.updateIsMenuActionsOpen(true);
    favoriteHover.value = false;
    cartHover.value = true;
    userHover.value = false;
  };

  const onFavoriteIconEnter = () => {
    queryStore.setSearchString('');
    headerStore.updateIsMenuActionsOpen(true);
    favoriteHover.value = true;
    cartHover.value = false;
    userHover.value = false;
  };

  const onIconLeave = () => {
    userHover.value = false;
    cartHover.value = false;
    favoriteHover.value = false;
    headerStore.updateIsMenuActionsOpen(false);
  };

  const onIconLeaveClick = () => {
    userHover.value = false;
    cartHover.value = false;
    favoriteHover.value = false;
    setTimeout(() => headerStore.updateIsCatalogOpen(false), 0);
    setTimeout(() => headerStore.updateIsMenuActionsOpen(false), 0);
  };

</script>

<style lang="scss" scoped>

.right-direction .dropdown__wrapper{
  right: 0;
  left: unset;
}

.topmenu{
  &__item{
    // padding: 0 10px 0 10px;
    position: relative;
    z-index: 51;
  }
}

.popup-cart{
  text-align: center;
  padding: 40px 24px 40px 24px;
}
.user-login{
  min-width: 270px;
  padding: 20px 14px 20px 14px;
}

.avatar{
  justify-content: center;
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: rgba(66, 117, 216, 0.07);
  font-size: 30px;
  color: #423E48;
  font-weight: 500;
}
.avatar__box{
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 24px 0;
}

.hr{
  height:2px;
  margin:44px 0 40px 0;
  background:#F0F0F1;
}
.foot-reg{
  font-weight: 400;
  font-size: 14px;
  line-height: 130%;
  text-align: center;
  color: #4275D8;
}
.foot-lnk{
  font-size: 12px;
  text-align: center;
  text-decoration-line: underline;
  opacity: 0.6;
  color: #423E48;
}

.topmenu__right{
  gap:20px;
  @media (max-width:$md3+px) {
    margin-right: 10px;
  }

}

.dropdown__list{
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;

  a{
    display: flex;
    align-items: center;
    //justify-content: center;

    width: 100%;
    text-align: left;
    &:before{
      margin-right: 10px;
    }
  }

}

</style>
