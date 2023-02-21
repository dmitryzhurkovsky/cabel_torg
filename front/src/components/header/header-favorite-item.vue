<template>
    <div class="popup-cart__item row">
        <div class="popup-cart__img">
            <CardImage :images=favoriteItemData.images />
        </div>
        <div class="popup-cart__description">
            <div class="popup-cart__title long_text">{{ favoriteItemData.name }}</div>
            <div class="popup-cart__uptitle">{{ -favoriteItemData.vendor_code }}</div>

        </div>
        <div class="popup-cart__action">
            <div class="popup-cart__price">{{ cardPriceWithDiscount }} <span>BYN</span></div>
            <button class="icon-delete" @click.stop="onRemoveItemFromFavorite(favoriteItem)"></button>
        </div>
    </div>
</template>

<script>

import axios from "axios";
import {mapMutations, mapActions } from 'vuex'
import CardImage from '@/components/UI/card-image.vue'

export default {
  name: 'HeaderFavoriteItem',

  props: {
    favoriteItem: null,
  },

  components: {
    CardImage,
  },

  data(){
    return {
        favoriteItemData: {},
    }
  },

  computed: {
    cardPriceWithDiscount(){
        return this.favoriteItemData.price_with_discount ? this.favoriteItemData.price_with_discount : this.favoriteItemData.price;
    },
  },

  async mounted(){
    try {
        const response = await axios.get(process.env.VUE_APP_API_URL + 'products/' + this.favoriteItem.product.id);
        this.favoriteItemData = response.data;
    } catch (e) {
        console.log(e);
        this.ADD_MESSAGE({name: "Не возможно загрузить рекомендованные товары ", icon: "error", id: '1'})
    }
  },

  methods:{
    ...mapMutations("notification", ["ADD_MESSAGE"]),
    ...mapActions("favorite", ["UPDATE_IS_WISH_IN_CART"]),

    async onRemoveItemFromFavorite(itemData){
        await this.UPDATE_IS_WISH_IN_CART({ itemData, type: 'remove' });
    }
  }

}
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