<template>
  <Breadcrumb/>
  <div class="user-acc">
    <div class="user-acc__wrapper">
      <div class="user-acc__content _container">
        <div class="user-acc__body">

          <div class="user-acc__block">
<!--        # SIDEBAR-->
            <div class="user-acc__sidebar filter">
              <div class="filter__block">
                <div class="filter__box">
                  <div class="filter__title icon-arrow-up">Личный кабинет</div>

                  <ul class="filter__list">
                     <li class="filter__item icon-order" @click="changeScreen(0)">Мои заказы</li>
                     <li class="filter__item icon-favorite-choosed" @click="changeScreen(1)">Избранные товары</li>
                     <li class="filter__item icon-setting" @click="changeScreen(2)">Настройки аккаунта</li>
                  </ul>
                  <hr class="hr"/>
                  <div class="icon-exit filter__item" @click="userLogout">Выйти из аккаунта</div>
                </div>

              </div>
            </div>
<!--        # CONTENT-->
            <div class="user-acc__content-block content-block" >
                <PersonalOrderList v-if = "profileScreen === 0"/>
                <PersonalFavoriteList v-if = "profileScreen === 1"/>
                <PersonalProfile v-if = "profileScreen === 2"/>
            </div>

          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { onBeforeMount, onBeforeUpdate, onMounted } from 'vue';
  import { useAuthStore } from '@/stores/auth';
  import { useBreadCrumbStore } from '@/stores/breadcrumb';
  import { useProfileStore } from '@/stores/profile';

  definePageMeta({
    middleware: 'auth',
  });

  const router = useRouter();
  const authStore = useAuthStore();
  const breadCrumbStore = useBreadCrumbStore();
  const profileStore = useProfileStore();

  const { breadcrumb, profileScreen } = storeToRefs(profileStore);

  const changeScreen = (screenId) => {
    profileStore.changeScreen(screenId)
    breadCrumbStore.renameLastBreadCrumb(breadcrumb.value[screenId]);
  };

  const userLogout = () =>{
    authStore.clearUserData();
    router.push("/");
  };

  // onBeforeUpdate(()=> {
  //   if (!localStorage.getItem("authToken")) {
  //     navigateTo('/login');      
  //   }
  // });

  onMounted(() => {
    if (!localStorage.getItem("authToken")) router.push('/login');
    breadCrumbStore.changeBreadCrumb(0);
    breadCrumbStore.addBreadCrumb({
      name: router.currentRoute.value.meta.name,
      path: router.currentRoute.value.path,
      type: "local",
      class: ""
    });
    breadCrumbStore.renameLastBreadCrumb(breadcrumb.value[profileScreen.value]);
  });
</script>

<style scoped lang="scss">

.user-acc {

  &__block{
    display: flex;
    align-items: flex-start;
    min-height: 350px;
  }
  &__sidebar{
    width: 270px;
    @media (max-width: $md2+px){
      display: none;
    }
  }
  &__content-block{
    width: 100%;
    padding-left: 20px;
    padding-bottom: 20px;
    min-height: 350px;
    @media (max-width: $md2+px){
      padding-left: 0px;
    }
  }

}
.filter{

  &__box{
    font-weight: 400;
    position: relative;
  }
  .hr{
    height:2px;
    margin:24px 0 24px 0;
    background:#F0F0F1;
  }

  &__item{
    font-size: 14px;
    line-height: 24px;
    color: #423E48;
    margin-bottom: 8px;

    &:hover{
      color:#4275D8;
      cursor: pointer;
    }
    &:before{
      margin-right: 10px;
    }
  }

  &__title{
    background: #eceef1;
    padding: 6px 8px;
    font-weight: 500;
    font-size: 14px;
    line-height: 24px;
    color: #423E48;
    margin: 0 0 12px 0;
    &:before{
      position: absolute;
      top: 16px;
      right: 10px;
      font-size: 6px;
      //transform: rotate(-90deg);
    }
  }
  &__text{
    span{
      font-weight: 400;
      font-size: 14px;
      color: #423E48;
    }
  }
}
</style>
