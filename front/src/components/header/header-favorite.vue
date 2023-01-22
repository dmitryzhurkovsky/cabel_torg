<template lang="html">
  <div class="dropdown__content popup-cart">
    <h3 class="">Избранные товары</h3>

    <div class="popup-cart__list">

      <div class="popup-cart__list" v-if = "FAVORITES.length">
        <HeaderFavoriteItem 
            class="row" 
            v-for = "favoriteItem in FAVORITES"
            :key = "favoriteItem.product.id"
            :favoriteItem = favoriteItem
        />
      </div>

    </div>
    <div>
      <a class="" @click="onOpenFavoritePage($event)">Перейти в Избранное
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M3 12H20.5M20.5 12L16.5 8M20.5 12L16.5 16" stroke="white"/>
        </svg>
      </a>
    </div>
  </div>

</template>

<script>

import { mapGetters, mapMutations } from 'vuex'

import HeaderFavoriteItem from '@/components/header/header-favorite-item.vue'

export default {
  name: "HeaderFavorite",

  components: {
    HeaderFavoriteItem,
  },

  computed: {
    ...mapGetters("favorite", ["FAVORITES"]),
    ...mapGetters("auth", ["USER"]),
  },

  methods: {
    ...mapMutations("auth", ["SET_DESTINATION"]),
    ...mapMutations("profile", ["CHANGE_SCREEN"]),

    onOpenFavoritePage(e) {
      e.preventDefault();
      e.stopPropagation();
      this.CHANGE_SCREEN(1);
      if (this.USER) {
            this.SET_DESTINATION('');
            if (this.$router.path != '/user-cab') {
                this.$router.push('/user-cab');
            }
        } else {
            this.SET_DESTINATION('/user-cab');
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

</style>
