<template>
  <div class="recomendation__block__item item-card" v-if = "card">
    <div v-if = "InfoCardBlock === 'Хит'" class="item-card__taghit">{{ InfoCardBlock }}</div>
    <div v-if = "InfoCardBlock === '%'" class="item-card__tagdiscount">
      <img class="" src="@/assets/catalog/discount.svg" alt="">
    </div>
    <div v-if = "InfoCardBlock === 'New'" class="item-card__tagnew">{{ InfoCardBlock }}</div>
    <div 
        :class="[isWish === false ? 'item-card__wishlist icon-favorite' : 'item-card__wishlist icon-favorite-choosed']" 
        @click.stop="onWishClick(card)"
    ></div>
    <a :href="createHref(card.vendor_code)" class="item-card__img" @click.stop.prevent="openCardItem(card.vendor_code)">
      <UiCardImage 
        :images=card.images
        :alt = "card.name + ' №1 - cabel-torg'"
      />
    </a>
    <div class="item-card__info">
      <div class="item-card__row flex-center">
        <div class="item-card__status icon-done-color _label" v-if = "card.status === 'A'">В наличии</div>
        <div class="item-card__status icon-on-the-way _label" v-if = "card.status === 'W'">В пути на склад</div>
<!--        <div class="item-card__status _label if_status_on_the_way" v-if = "card.status === 'W'">Доставим в течение 14 дней</div>-->
        <div class="item-card__status icon-out-of-stock _label" v-if = "card.status === 'O'">Нет в наличии</div>
      </div>
      <div class="item-card__row old_price__row flex-center">
        <div class="old_price" v-if="!card.is_price_on_request && card.price_with_tax !== cardPriceWithDiscount">{{ card.price_with_tax }} 
          <span>BYN/{{ card.base_unit.full_name }}</span>
        </div>
        <div class="notice" v-if="!card.is_price_on_request">* Цена указана с учетом НДС.</div>
      </div>
      <div class="item-card__row current_price__row flex-center">
        <div class="current_price" v-if="!card.is_price_on_request">{{ cardPriceWithDiscount }}
          <span>BYN/{{ card.base_unit.full_name }}</span>
        </div>
        <div class="current_price" v-if="card.is_price_on_request">{{  'Цена по запросу' }}
          <!-- <span>BYN/{{ card.base_unit.full_name }}</span> -->
        </div>
        <div v-if = "!card.is_price_on_request && quantity !== 0" @click.stop="onOperationWithCartItem(card)"
          class = "item-card__buy flex-center icon-cart-chosen"
        >
        </div>
        <div v-if = "!card.is_price_on_request && quantity === 0 && card.status !== 'O'" @click.stop="onOperationWithCartItem(card)"
          class="item-card__buy flex-center icon-cart"
        >
        </div>
        <div v-if = "!card.is_price_on_request && quantity === 0 && card.status === 'O'" @click.stop="onCreatePopUp(true, card.id)"
          class="item-card__buy flex-center icon-ring"
        >
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 22C13.105 22 14 21.105 14 20H10C10 21.105 10.895 22 12 22ZM18 16.5V11C18 7.925 16.365 5.36 13.5 4.68V4C13.5 3.17 12.83 2.5 12 2.5C11.17 2.5 10.5 3.17 10.5 4V4.68C7.635 5.36 6 7.925 6 11V16.5L4 18V18.5H20V18L18 16.5ZM16.5 17H7.5V11C7.5 8.515 9.515 6 12 6C14.485 6 16.5 8.515 16.5 11V17Z" fill="#423E48"/>
          </svg>
        </div>
        <div v-if = "card.is_price_on_request" @click.stop="onCreatePopUpRequestPrice(true, card.id)"
          class="item-card__buy flex-center icon-ring"
        >
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 22C13.105 22 14 21.105 14 20H10C10 21.105 10.895 22 12 22ZM18 16.5V11C18 7.925 16.365 5.36 13.5 4.68V4C13.5 3.17 12.83 2.5 12 2.5C11.17 2.5 10.5 3.17 10.5 4V4.68C7.635 5.36 6 7.925 6 11V16.5L4 18V18.5H20V18L18 16.5ZM16.5 17H7.5V11C7.5 8.515 9.515 6 12 6C14.485 6 16.5 8.515 16.5 11V17Z" fill="#423E48"/>
          </svg>
        </div>
      </div>
      <a :href="createHref(card.vendor_code)" class="item-card__title" @click.stop.prevent="openCardItem(card.vendor_code)">
        <span>{{ card.name }}</span>
      </a>
      <div class="item-card__uptitle">
        <div v-if ="card.category">{{ card.category.name }}</div>
      </div>
    </div>
  </div>

</template>

<script setup>
  import { ref, computed, watch, onMounted } from 'vue';
  import { useHeaderStore } from '@/stores/header';
  import { useFavoritesStore } from '@/stores/favorites';
  import { useOrdersStore } from '@/stores/orders';

  const props = defineProps({
    card:  { type: Object,  default: null},
  });

  const router = useRouter();
  const headerStore = useHeaderStore();
  const favoritesStore = useFavoritesStore();
  const oredersStore = useOrdersStore();

  const quantity = ref(0);
  const isWish = ref(false);

  const { favorites } = storeToRefs(favoritesStore);
  const { orders } = storeToRefs(oredersStore);

  const ChangeParameters = computed(() => {
    return JSON.stringify(orders.value) + JSON.stringify(favorites.value);
  });

  const cardPriceWithDiscount = computed(() => {
    return props.card.price_with_discount_and_tax && props.card.price_with_discount_and_tax !== props.card.price_with_tax 
      ? props.card.price_with_discount_and_tax 
      : props.card.price_with_tax;
  });

  const InfoCardBlock = computed(() => {
    if (props.card.price_with_discount_and_tax && props.card.price_with_discount_and_tax !== props.card.price_with_tax) return '%';
    // let info = '';
    if (props.card.is_new) return 'New'
    if (props.card.is_popular) return 'Хит'
    // info = props.card.vendor_code === 'УТ-00000037' ? 'New' : info;
    // info = props.card.vendor_code === 'УТ-00000015' ? 'Хит' : info;
    // info = props.card.price_with_discount_and_tax ? '%' : info;
    return '';
  });

  watch(ChangeParameters, async () => {
      countQuantity();
      checkIsWish();
    },
  );

  onMounted(() => {
    countQuantity();
    checkIsWish();
  });


  const onCreatePopUp = (status, cardID) => {
    headerStore.setIsPopUpOpen(status);
    headerStore.setPopUpAction('RequestCall');
    headerStore.setRequestCallType('GR');
    headerStore.setPopUpAdditionalData({cardID});
  };

  const onCreatePopUpRequestPrice = (status, cardID) => {
    headerStore.setIsPopUpOpen(status);
    headerStore.setPopUpAction('RequestPrice');
    headerStore.setRequestCallType('GR');
    headerStore.setPopUpAdditionalData({cardID});
  };

  const openCardItem = (id) => {
    const URL = '/card_product/' + id;
    router.push(URL);
  };

  const createHref = (card) => {
    const URL = '/card_product/' + card;
    return URL;
  };

  const onOperationWithCartItem = async (card) => {
    const itemData = {
      amount: 1,
      product: {
        id: card.id,
        vendor_code: card.vendor_code,
        name: card.name,
        discont: card.discont,
        price_with_discount_and_tax: card.price_with_discount_and_tax,
        price_with_tax: card.price_with_tax,
      },
    }
    const type = quantity.value === 0 ? 'increase' : 'remove';
    quantity.value = quantity.value !==0 ? 0 : 1;
    await oredersStore.updateItemsInCart({ itemData, type });
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

  const countQuantity = () => {
    if (orders.value.length) {
      const filtered = orders.value.filter(item => item.product.id === props.card.id);
      quantity.value =  filtered.length ? filtered[0].amount : 0;
    } else {
      quantity.value = 0;
    }
  };

  const checkIsWish = () => {
    if (favorites.value.length) {
      const filtered = favorites.value.filter(item => item.product.id === props.card.id);
      isWish.value =  filtered.length ? true : false;
    } else {
      isWish.value = false;
    }
  };
</script>

<style lang="scss" scoped>

//Карточка товара

// .icon-card .active {
//   // background-color: red;
//   border: 2px solid red;
// }
.item-card {
  display: flex;
  flex-direction: column;
  position: relative;
  background: #FFFFFF;
  border: 2px solid #EEEEEE;
  box-sizing: border-box;
  border-radius: 8px;
  padding: 20px 20px 30px 20px;
  @media (max-width: $md3+px){
    padding: 5px 15px 10px 15px;
  }

  &__img {
    width: 100%;
    cursor: pointer;
    text-align: center;
    min-height: 162px;
    display: flex;
    align-items: center;
    justify-content: center;

  }

  &__taghit{
    background: #7700AF;
    border-radius: 2px;
    padding: 2px 11px;
    position: absolute;
    font-weight: 400;
    font-size: 12px;
    left:20px;
    top:20px;
    color: #fff;
  }
  &__tagnew{
    background: #4275d8;;
    border-radius: 2px;
    padding: 2px 11px;
    position: absolute;
    font-weight: 400;
    font-size: 12px;
    left:20px;
    top:20px;
    color: #fff;
  }
  &__tagdiscount{
    padding: 2px 11px;
    position: absolute;
    left:10px;
    top:10px;
  }
  &__wishlist{

    &.added {
      fill: #ff6f60;
      path {
        stroke: #ff6f60;
      }
    }
    //width: 18px;
    //height: 16px;
    position: absolute;
    top: 20px;
    right: 20px;
    z-index: 1;
    cursor: pointer;
    fill: none;
  }
  &__status{
    font-size: 14px;
    margin: 5px 0;
    &:before{
      margin-right: 10px;
    }
  }

  &__row {
  justify-content: space-between;
    &:nth-child(1){
      margin-bottom: 3px;
    }
    &:nth-child(2){
      //margin-bottom: 15px;
    }
  }

  &__buy {
    position: relative;

    &:before {
      cursor: pointer;
      padding: 10px 10px;
      transition: all 0.2s ease;
    }

    &:hover{
      background: #4275D8;
      border-radius: 6px;
      color: #fff;
      @media (max-width: $md2 + px) {
        background: none;
        color:#000;
      }
    }


  }

  .notice{
    font-weight: 300;
    font-size: 10px;
    opacity: 0.5;
    text-align: right;
  }

  .old_price__row{
    min-height: 34px;
    //flex-direction: column-reverse;
    align-items: flex-start;
  }
  .current_price__row{
    min-height: 40px;
    align-items: center;
  }

  .old_price {
    font-size: 16px;
    line-height: 24px;
    text-decoration-line: line-through;
    opacity: 0.4;
    white-space: nowrap;
    span{
      font-size: 14px;
    }
    @media (max-width: $md3 + px){
      font-size: 12px;
    }

  }

  .current_price {
    font-weight: 500;
    font-size: 20px;
    //line-height: 24px;
    @media (max-width: $md3+px){
      font-size: 16px;
    }
    span{
      font-weight: 300;
      font-size: 16px;
      @media (max-width: $md3+px){
        font-size: 12px;
      }
    }

  }

  &__title {
    display: inline-block;
    margin-bottom: 10px;
    height: 40px;
    overflow: hidden;
    line-height: 1.26;
    font-weight: 400;
    color: black;
    cursor: pointer;
    @media (max-width: $md3+px){
      font-size: 13px;
      height: 33px;

    }
    a{
      font-weight: 500;
      font-size: 15px;
      color: #423E48;

    }

  }

  &__uptitle{
    font-size: 14px;
    //min-height: 42px;
    @media (max-width: $md3+px){
      font-size: 13px;
      height: 33px;

    }
    a{
      font-weight: 400;
      font-size: 14px;
      line-height: 130%;
      color: #423E48;
    }

  }
}

</style>
<style lang="scss">
.item-card__img img{
  max-height: 162px!important;
}
.icon-ring{
    width: 36px;
    height: 36px;
    justify-content: center;
    cursor: pointer;
  &:hover{

    path{
      fill:#fff;
    }

  }
}
</style>
