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
          :class="[!USER ? 'icon-user' : 'icon-user-login']"
      >
        <div v-if = "userHover && !USER" :class="[!userHover ? 'dropdown__wrapper' : 'dropdown__wrapper wrapper__show']">
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
        <div v-if = "userHover && USER" :class="[!userHover ? 'dropdown__wrapper' : 'dropdown__wrapper wrapper__show']">

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
        :quantity = ORDERS.length 
        :left = '10'
        :top = '10'
      />
    </div>
  </div>
</template>

<script>

import {mapActions, mapGetters, mapMutations} from 'vuex'

export default {
  name: 'TopMenuActions',

  data: function() {
      return {
          isLoading: false,
          userHover: false,
          cartHover: false,
          favoriteHover: false,
      }
  },

  computed: {
      ...mapGetters("auth", ["AUTH_TYPE", "IS_OPEN_MAIN_LOGIN", "USER"]),
      ...mapGetters("order", ["ORDERS"]),
  },

  methods: {
    ...mapMutations("auth", ["SET_TYPE"]),
    ...mapActions("auth", ["SEND_LOGOUT_REQUEST"]),
    ...mapMutations("query", ["SET_SEARCH_STRING"]),
    ...mapMutations("profile", ["CHANGE_SCREEN"]),
    ...mapMutations("header", ["UPDATE_IS_CATALOG_OPEN", "UPDATE_IS_MENU_ACTIONS_OPEN"]),
    
    handleClick (URL, screen_type) {
      const vm = this;
      setTimeout(() => vm.UPDATE_IS_CATALOG_OPEN(false), 0);
      setTimeout(() => vm.UPDATE_IS_MENU_ACTIONS_OPEN(false), 0);
      // this.SET_IS_OPEN_MAIN_LOGIN(false);
      this.cartHover = false;
      this.userHover = false;
      this.favoriteHover = false;
      if (this.$route.path != URL) {
        if (URL === '/login') {
          this.SET_TYPE(screen_type);
        } else {
          this.CHANGE_SCREEN(screen_type)
        }
        this.$router.push(URL);
      } else {
        if (URL === '/login') {
          this.SET_TYPE(screen_type);
        } else {
          this.CHANGE_SCREEN(screen_type)
        }
      }
    },

    async userLogout() {
      if (this.isLoading) return;
      this.userHover = false;
      const vm = this;
      setTimeout(() => vm.UPDATE_IS_CATALOG_OPEN(false), 0);
      setTimeout(() => vm.UPDATE_IS_MENU_ACTIONS_OPEN(false), 0);
      this.isLoading = true;
      await this.SEND_LOGOUT_REQUEST();
      this.isLoading = false;
      this.$router.push('/');
    },

    clearSearchString(){
      this.SET_SEARCH_STRING('');
    },

    onUserIconEnter(){
      this.SET_SEARCH_STRING('');
      this.UPDATE_IS_MENU_ACTIONS_OPEN(true);
      // this.SET_IS_OPEN_MAIN_LOGIN(true)
      this.favoriteHover = false;
      this.cartHover = false;
      this.userHover = true;
    },

    onCartIconEnter(){
      this.SET_SEARCH_STRING('');
      this.UPDATE_IS_MENU_ACTIONS_OPEN(true);
      this.favoriteHover = false;
      this.cartHover = true;
      this.userHover = false;
    },

    onFavoriteIconEnter() {
      this.SET_SEARCH_STRING('');
      this.UPDATE_IS_MENU_ACTIONS_OPEN(true);
      this.favoriteHover = true;
      this.cartHover = false;
      this.userHover = false;
    },

    onIconLeave() {
      this.userHover = false;
      this.cartHover = false;
      this.favoriteHover = false;
      this.UPDATE_IS_MENU_ACTIONS_OPEN(false);
    },

    onIconLeaveClick() {
      this.userHover = false;
      this.cartHover = false;
      this.favoriteHover = false;
      // const vm = this;
      setTimeout(() => this.UPDATE_IS_CATALOG_OPEN(false), 0);
      setTimeout(() => this.UPDATE_IS_MENU_ACTIONS_OPEN(false), 0);
    },
  },

}
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
