<template>
      <div class="popup-cart__item" v-it="cartItemData">
        <div class="popup-cart__img">
            <!-- <img src="../../assets/catalog/card1.png" alt=""> -->
            <img v-if = "cartItemData.images" :src=getImagePath(cartItemData.images) alt="">
            <img v-if = "!cartItemData.images" src="../../assets/no_image.jpg" alt="">
        </div>
        <div class="popup-cart__description">
          <div class="popup-cart__title">{{ cartItemData.name }}</div>
          <div class="popup-cart__uptitle">{{ cartItemData.vendor_code }}</div>

        </div>
        <div class="popup-cart__action">
          <div class="popup-cart__price">{{ cartItem.amount + '  X  ' + cartItemData.price }} <span>BYN</span></div>
          <button class="icon-delete" @click="onRemoveItemFromCart(cartItem)"></button>
        </div>
        <!-- {{ cartItemData }} -->
      </div>
</template>

<script>
import axios from "axios";
import {mapMutations, mapActions } from 'vuex'

export default {
  name: 'HeaderCartItem',

  props: {
    cartItem: null,
  },

  data(){
    return {
        cartItemData: {},
    }
  },

  async mounted(){
    try {
        const response = await axios.get(process.env.VUE_APP_API_URL + 'products/' + this.cartItem.product.id);
        this.cartItemData = response.data;
    } catch (e) {
        console.log(e);
        this.ADD_MESSAGE({name: "Не возможно загрузить рекомендованные товары ", icon: "error", id: '1'})
    }
  },

  methods:{
    ...mapMutations("notification", ["ADD_MESSAGE"]),
    ...mapActions("order", ["UPDATE_ITEMS_IN_CART"]),

    getImagePath(item) {
      let path = null;
      if (item) {
        const allPath = item.split(',');
        path = process.env.VUE_APP_IMAGES + allPath[0];
      }
      return path;
    },

    onRemoveItemFromCart(itemData){
        this.UPDATE_ITEMS_IN_CART({ itemData, type: 'remove' });
    }
}

}
</script>

<style lang="scss" scoped>
.popup-cart{

  &__item{
    display: grid;
    grid-template-columns: 1fr 2fr 1fr;
    gap:10px;
    align-items: self-start;
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
    flex-direction: column;
    justify-content: space-between;
    font-size: 12px;
    line-height: 140%;
    color: #423E48;
    text-align: left;
  }
  &__title{
    font-weight: 500;

  }
  &__action{
    align-items: stretch;

  }



  &__price{
    font-size: 12px;
    line-height: 140%;

    color: #423E48;
    margin-bottom: 20px;
  }

  .icon-delete{
    text-align: right;
    &:hover{
      color:#4275D8;
    }
  }

}

</style>
