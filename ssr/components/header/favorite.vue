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

<script>

import { mapGetters, mapMutations } from 'vuex'

export default {
  name: "HeaderFavorite",

  computed: {
    ...mapGetters("favorite", ["FAVORITES"]),
    ...mapGetters("auth", ["USER"]),

    ItemsForShow(){
      let result = [];
      if (this.FAVORITES.length > 5) {
        result = this.FAVORITES.slice(this.FAVORITES.length - 4);
      } else {
        result = [...this.FAVORITES];
      }
      return result;
    },
  },

  methods: {
    ...mapMutations("auth", ["SET_DESTINATION"]),
    ...mapMutations("profile", ["CHANGE_SCREEN"]),

    onOpenFavoritePage() {
      this.CHANGE_SCREEN(1);
      if (this.USER) {
            this.SET_DESTINATION('');
            if (this.$router.path != '/user_profile') {
              this.$router.push('/user_profile');
            }
            this.CHANGE_SCREEN(1);              
        } else {
            this.SET_DESTINATION('/user_profile');
            this.$router.push('/login');
        }
    }
  }
  
}
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
