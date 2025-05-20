<template>
  <div class="popup-cart__item row">
      <div class="popup-cart__img">
          <UiCardImage 
            :images=favoriteItemData.images 
            :alt = "favoriteItemData.name + ' №1 - cabel-torg'"
          />
      </div>
      <div class="popup-cart__description">
          <div class="popup-cart__title long_text">{{ favoriteItemData.name }}</div>
          <div class="popup-cart__uptitle">{{ favoriteItemData.vendor_code }}</div>

      </div>
      <div class="popup-cart__action">
          <div class="popup-cart__price">{{ cardPriceWithDiscount }} <span>BYN</span></div>
          <button class="icon-delete" @click.stop="onRemoveItemFromFavorite(favoriteItem)"></button>
      </div>
  </div>
</template>

<script setup>

  import axios from "axios";
  import { ref, computed, onMounted } from 'vue';
  import { useFavoritesStore } from "@/stores/favorites";

  const favoritesStore = useFavoritesStore();

  const props = defineProps({
    favoriteItem:  { type: Object,  default: null},
  });

  const favoriteItemData = ref({});

  const cardPriceWithDiscount =computed(() => {
      return favoriteItemData.value.price_with_discount_and_tax && favoriteItemData.value.price_with_discount_and_tax !== favoriteItemData.value.price_with_tax 
        ? favoriteItemData.value.price_with_discount_and_tax 
        : favoriteItemData.value.price_with_tax;
  });

  onMounted( async () => {
    try {
        const response = await axios.get(useRuntimeConfig().public.NUXT_APP_API_URL + 'products/' + props.favoriteItem.product.id);
        favoriteItemData.value = response.data;
    } catch (e) {
        console.log(e);
    }
  })

  const onRemoveItemFromFavorite = async (itemData) => {
    await favoritesStore.updateIsWishInCart({ itemData, type: 'remove' });
  };

</script>

<style lang="scss" scoped>
.popup-cart{
text-align: center;

&__summary{
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 0;
  font-weight: 300;
  font-size: 14px;
  line-height: 140%;
  color: #423E48;
  opacity: 0.6;
  border-top: 1px solid #F0F0F1;
  border-bottom: 1px solid #F0F0F1;

  div:nth-child(1){
    span{
      font-weight: 500;
      opacity: 1;
    }
  }
  div:nth-child(2){
    span{
      font-weight: 500;
      opacity: 1;
    }
  }
}

&__item{
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
  gap:10px;
  align-items: center;
  &:hover{
    background: #F9F9F9;
  }

}

&__img{
  max-width: 100%;
  img{
    width: 100%;
  }

}

&__description{
  display: flex;
  text-align: left;
  flex-direction: column;
  justify-content: space-between;
  font-size: 12px;
  line-height: 140%;
  color: #423E48;
}
&__title{
  max-width: 150px;
  font-weight: 500;


}
&_action{
  align-items: stretch;
  text-align: right;

}

&__price{
  font-size: 12px;
  line-height: 140%;
  white-space: nowrap;
  color: #423E48;
  margin-bottom: 10px;
}

.icon-delete{
  text-align: right;
  &:hover{
    color:#4275D8;
  }
}

button{
  margin-bottom: 20px;
}

a{
  font-weight: 400;
  font-size: 14px;
  line-height: 130%;
  color: #4275D8;
}

}

</style>