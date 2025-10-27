<template>
    <div v-if="cartItemData && quantity !==0">
      <div class="product__wrapper">
        <a class="product__img" :href="createHref(cartItemData.vendor_code)" @click.stop.prevent="openCardItem(cartItemData.vendor_code)">
            <UiCardImage 
              :images=cartItemData.images 
              :alt = "cartItemData.name + ' №1 - cabel-torg'"
            />
        </a>
        <div class="product__info">
            <div class="product__article  _label mb-20">Артикул: <span>{{ cartItemData.vendor_code }}</span></div>
            <a  :href="createHref(cartItemData.vendor_code)" class="product__title" @click.stop.prevent="openCardItem(cartItemData.vendor_code)"> {{ cartItemData.name }}</a>
            <div class="icon__row mt-20">
                <span 
                    :class="[isWish === false ? 'icon icon-favorite' : 'icon icon-favorite-choosed']" 
                    @click.stop="onWishClick(cartItemData)"
                >В избранное</span>
                <span v-if ="!isMobileVersion" class="icon icon-delete" @click.stop="onOperationWithCartItem(cartItemData, 'remove')">Удалить</span>
                <span v-if ="isMobileVersion" class="icon icon-close delete-goods flex-center" @click.stop="onOperationWithCartItem(cartItemData, 'remove')"></span>
            </div>
        </div>
      </div>

        <div class="product__wrapper">
          <div class="product__count flex-center">
            <div class="_label mb-20">Количество:</div>
            <div class="flex-center">
              <span class="icon-minus" @click.stop="onOperationWithCartItem(cartItemData, 'decrease')"></span>
              <input class="product__input" type="number" v-model="quantity"  @input="onOperationWithCartItem(cartItemData, 'set')" @click.stop="">
              <span class="icon-plus" @click.stop="onOperationWithCartItem(cartItemData, 'increase')"></span>
            </div>
          </div>
          <div class="product__price">
            <div class="_label mb-20">Стоимость (с учетом НДС):</div>
            <div class="old_price" v-if="cartItemData.price_with_tax !== cardPriceWithDiscount">
              <span>{{ cartItemData.price_with_tax }}</span>BYN
              <span>/{{ cartItemData?.base_unit?.full_name }}</span>
            </div>
            <div class="current_price">
              <span v-if="!type">{{ cardPriceWithDiscount }}</span>
              <span v-if="type">{{ (cardPriceWithDiscount * quantity).toFixed(2) }}</span>
              BYN
            </div>
          </div>
        </div>
    </div>
</template>

<script setup>
  import axios from "@/utils/api";
  import { ref, computed, watch, onMounted } from 'vue';
  import { useNotificationsStore } from '@/stores/notifications';
  import { useHeaderStore } from '@/stores/header';
  import { useFavoritesStore } from '@/stores/favorites';
  import { useOrdersStore } from "@/stores/orders";

  const notificationsStore = useNotificationsStore();
  const headerStore = useHeaderStore();
  const favoritesStore = useFavoritesStore();
  const oredersStore = useOrdersStore();

  const router = useRouter()

  const props = defineProps({
    cartItem  : { type: String,  default: null},
    type      : { type: Boolean, default: false},
  });

  const cartItemData = ref({});
  const quantity = ref(0);
  const lastQuantity = ref(0);
  const isWish = ref(false);

  const { viewType } = storeToRefs(headerStore);
  const { favorites } = storeToRefs(favoritesStore);

  onMounted( async () => {
    notificationsStore.setIsLoading(true);
    try {
      const response = await axios.get('products/' + props.cartItem.product.id);
      cartItemData.value = response.data;
      quantity.value = props.cartItem.amount;
      lastQuantity.value = props.cartItem.amount;
    } catch (e) {
      console.log(e);
      // notificationsStore.addMessage({ name: "Не возможно загрузить товары", icon: "error", id: '1' });
    }
    checkIsWish();
    notificationsStore.setIsLoading(false);
  });

  const ChangeParameters = computed(() => {
    return JSON.stringify(favorites.value);
  });

  const cardPriceWithDiscount = computed(() => {
    return cartItemData.value.price_with_discount_and_tax && cartItemData.value.price_with_discount_and_tax !== cartItemData.value.price_with_tax 
      ? cartItemData.value.price_with_discount_and_tax 
      : cartItemData.value.price_with_tax;
  });

  const isMobileVersion = computed(() => {
    if (viewType.value === 1) return false
    if (viewType.value === 2) return true
    if (viewType.value === 3) return true
  });

  watch(ChangeParameters, () => {
    checkIsWish();
  });

  const onOperationWithCartItem = async (card, type) => {
    
    if (!quantity.value) {
        quantity.value = lastQuantity.value;
    } else {
      const itemData = {
        amount: 0,
        product: {
          id: card.id,
          vendor_code: card.vendor_code,
          name: card.name,
          discont: card.discont,
          price_with_discount_and_tax: card.price_with_discount_and_tax,
          price_with_tax: card.price_with_tax,
        },
      };
      if (type === 'decrease' && quantity.value === 1) {
        itemData.amount = Number(quantity.value);
        return;
      };
      if (quantity.value < 1) {
        quantity.value = lastQuantity.value;
        itemData.amount = Number(quantity.value);
        return
      };
      if (quantity.value > 10000) {
        quantity.value = lastQuantity.value;
        itemData.amount = Number(quantity.value);
        return;
      };
      if (type === 'set') {
        itemData.amount = Number(quantity.value);
        await oredersStore.updateItemsInCart({ itemData, type });
      }

      if (type === 'increase') {
        if (quantity.value < 10000) {
          quantity.value++;
          await oredersStore.updateItemsInCart({ itemData, type });
        }
      } else if (type === 'decrease') {
        quantity.value--;
        await oredersStore.updateItemsInCart({ itemData, type });
      };
      lastQuantity.value = quantity.value; 
    }
  };

  const onWishClick = async (card) => {
    const itemData = {
      product: {
        id: card.id,
        vendor_code: card.vendor_code,
        name: card.name,
      },
    }  
    const type = isWish.value === false ? 'set' : 'remove';
    await favoritesStore.updateIsWishInCart({ itemData, type });
  };

  const checkIsWish = () => {
    if (favorites.value.length) {
      const filtered = favorites.value.filter(item => item.product.id === cartItemData.value.id);
      isWish.value =  filtered.length ? true : false;
    } else {
      isWish.value = false;
    }
  };

  const openCardItem = (id) => {
    // console.log(id);
    const URL = '/card_product/' + id;
    router.push(URL);
  };

  const createHref = (card) => {
    const URL = '/card_product/' + card;
    return URL;
  };
</script>

<style scoped lang="scss">
.product{

    &__img {
        width: 100%;
        flex-basis: 20%;
        text-align: center;
        img{
            max-width: 100%;
            object-fit: fill;
        }
    }
    &__info{
      width: 100%;padding-left: 10px;

    .icon{
        font-size: 10px;
        line-height: 20px;
        color: #423E48;
        opacity: 0.6;
        &:before{
        margin-right: 5px;
        }
        &:nth-child(1){
        margin-right: 15px;
        }
        &:hover{
        opacity: 1;
        cursor: pointer;
        }
    }
      .delete-goods, .icon-close{
        @media (max-width: $md2 + px){
          position: absolute;
          top: -9px;
          right: -9px;
          font-weight: 700;
          background:#423E48;
          color:#fff;
          border-radius: 6px;
          width: 20px;
          height: 20px;
          opacity: 1;
          justify-content: center;
          &:before{
            font-size: 10px!important;
            font-weight: 700;
            margin-right: 0;
          }
        }

      }
    }

    &__title{
        font-size: 14px;
        line-height: 24px;
        text-decoration-line: underline;
        color: #423E48;
    }

    &__wrapper{
      width: 100%;
      display: flex;
      align-items: center;
      justify-content: space-between;
      &:nth-child(2){
        @media (max-width: $md2 + px){
          padding-left: 100px;
          margin-top: 20px;
        }
      }


    }
    &__count{
        flex-direction: column;
        //margin: 24px 0;
        .icon-plus, .icon-minus{
            cursor: pointer;
        }
    }
    &__input{
        width: 70px;
        height: 40px;
        padding: 9px 8px;
        background: rgba(66, 62, 72, 0.07);
        border-radius: 2px;
        border: none;
        margin: 0 10px;
        text-align: center;
      &::-webkit-outer-spin-button,
      &::-webkit-inner-spin-button
      {
        -webkit-appearance: none;
        margin: 0;
      }
    }

    &__price{
        display: flex;
        flex-direction: column;
        align-items: flex-end;

        .old_price{
            font-size: 14px;
            line-height: 20px;
            text-decoration-line: line-through;
            opacity: 0.4;
            margin-bottom: 5px;
            min-height: 20px;

        }
        .current_price{
            font-size: 20px;
            line-height: 20px;
            color: #423E48;
            font-weight: 500;
        }

    }
}


</style>