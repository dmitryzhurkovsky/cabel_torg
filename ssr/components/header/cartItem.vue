<template>
  <div class="popup-cart__item" v-if="cartItemData">
    <div class="popup-cart__img">
        <UiCardImage 
          :images=cartItemData.images
          :alt = "cartItemData.name + ' №1 - cabel-torg'"
        />
    </div>
    <div class="popup-cart__description">
      <div class="popup-cart__title long_text">{{ cartItemData.name }}</div>
      <div class="popup-cart__uptitle">{{ cartItemData.vendor_code }}</div>

    </div>
    <div class="popup-cart__action">
      <div class="popup-cart__price">{{ props.cartItem.amount + '  X  ' + cardPriceWithDiscount }} <span>BYN</span></div>
      <button class="icon-delete" @click.stop="onRemoveItemFromCart(cartItem)"></button>
    </div>
    <!-- {{ cartItemData }} -->
  </div>
</template>

<script setup>
  import axios from "@/utils/api";
  import { ref, computed, onBeforeMount } from 'vue';
  import { useOrdersStore } from "@/stores/orders";

  const props = defineProps({
    cartItem:  { type: Object,  default: null},
  });

  const oredersStore = useOrdersStore();

  const cartItemData = ref({});

  const cardPriceWithDiscount = computed(() => {
      return cartItemData.value.price_with_discount_and_tax && cartItemData.value.price_with_discount_and_tax !== cartItemData.value.price_with_tax 
        ? cartItemData.value.price_with_discount_and_tax 
        : cartItemData.value.price_with_tax;
  });

  onBeforeMount(async () => {
    try {
        const response = await axios.get('products/' + props.cartItem.product.id);
        cartItemData.value = response.data;
    } catch (e) {
        // console.log(e);
    }
  });

  const onRemoveItemFromCart = async (itemData) => {
    await oredersStore.updateItemsInCart({ itemData, type: 'remove' });
  };
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
max-width: 150px;
font-weight: 500;

}
&__action{
min-width: 90px;
align-items: stretch;


}



&__price{
font-size: 12px;
line-height: 140%;

color: #423E48;
margin-bottom: 10px;
}

.icon-delete{
text-align: right;
&:hover{
  color:#4275D8;
}
}

}

</style>
