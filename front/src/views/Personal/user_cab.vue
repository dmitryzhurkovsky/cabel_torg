<template>
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
                <OrderList v-if = "SCREEN === 0"/>
                <FavoriteList v-if = "SCREEN === 1"/>
                <Profile v-if = "SCREEN === 2"/>
            </div>

          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>

  import { mapGetters, mapActions, mapMutations } from "vuex";

  import OrderList from '@/components/personal/order-list.vue';
  import FavoriteList from '@/components/personal/favorite-list.vue';
  import Profile from '@/components/personal/profile.vue';

  export default {
    name: "personal",

    computed: {
      ...mapGetters("profile", ["SCREEN", "BREADCRUMB"]),
    },

    data() {
      return {
        screen: 0,
      };
    },

    components:
    {
      OrderList, FavoriteList, Profile,
    },

    methods: {
      ...mapActions("breadcrumb", ["CHANGE_BREADCRUMB"]),
      ...mapMutations("auth", ["SET_USER_DATA"]),
      ...mapMutations("profile", ["CHANGE_SCREEN"]),
      ...mapMutations("breadcrumb", ["RENAME_LAST_BREADCRUMB", "ADD_BREADCRUMB"]),

      changeScreen(screenId){
        this.CHANGE_SCREEN(screenId);
        this.RENAME_LAST_BREADCRUMB(this.BREADCRUMB[screenId]);
      },

      userLogout(){
        this.SET_USER_DATA(null);
        localStorage.removeItem("authToken");
        this.$router.push({name: "Main"});
      }
    },

    mounted(){
      this.screen = this.SCREEN;
      this.CHANGE_BREADCRUMB(0);
      this.ADD_BREADCRUMB({
        name: this.$router.currentRoute.value.meta.name,
        path: this.$router.currentRoute.value.path,
        type: "local",
        class: ""
      });
      this.ADD_BREADCRUMB({
        name: this.$router.currentRoute.value.meta.name,
        path: this.$router.currentRoute.value.path,
        type: "global",
        class: ""
      });
      this.RENAME_LAST_BREADCRUMB(this.BREADCRUMB[this.SCREEN]);
    }
  }
</script>

<style scoped lang="scss">

.user-acc {

  &__wrapper{

  }

  &__body{
  }
  &__block{
    display: flex;
    align-items: flex-start;
    min-height: 400px;

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

  &__block{

  }

  &__box{
    font-weight: 400;
    position: relative;

  }
  &__list{

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
