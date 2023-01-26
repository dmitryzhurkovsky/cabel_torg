<template lang="html">
  <div class="recomendation__block__item item-card" v-if = "card">
    <div class="item-card__tag">Хит</div>
    <div 
        :class="[isWish === false ? 'item-card__wishlist icon-favorite' : 'item-card__wishlist icon-favorite-choosed']" 
        @click.stop="onWishClick(card)"
    ></div>
    <a class="item-card__img" @click.stop="openCardItem(card.id)">
      <img v-if = "card.images" class="" :src=getImagePath(card.images) alt="">
      <img v-if = "!card.images" class="" src="../../assets/no_image.svg" alt="">
    </a>
    <div class="item-card__info">
      <div class="item-card__row flex-center">
        <div class="old_price">65.3???</div>
        <div class="notice">* Цена указана с учетом НДС.</div>
      </div>

      <div class="item-card__row flex-center">
        <div class="current_price">{{ card.price }}
          <span>BYN / {{ card.base_unit.full_name }}</span>
        </div>
        <div 
          :class="[quantity === 0 ? 'item-card__buy flex-center icon-cart' : 'item-card__buy flex-center icon-cart-chosen']"
          @click.stop="onOperationWithCartItem(card)"
        >
          <!-- <IconQuantity 
            v-if = "quantity"
            :quantity = quantity 
            :left = '18'
            :top = '18'
          /> -->
        </div>

      </div>
      <div class="item-card__title" @click.stop="openCardItem(card.id)">
        <div>{{ card.name }}</div>
      </div>
      <div class="item-card__uptitle">
        <div>UTP cat.5e (патч-панель) 19″?????</div>
      </div>
    </div>
  </div>

</template>

<script>
import { mapActions, mapGetters } from 'vuex'

// import IconQuantity from '@/components/catalog/icon-quantity.vue'

export default {
  name: "CardItem",

  props: {
    card:  null,
  },

  data(){
    return {
      quantity: 0,
      isWish: false,
    }
  },

  // components:
  // {
  //   IconQuantity,
  // },

  computed: {
    ...mapGetters("order", ["ORDERS"]),
    ...mapGetters("favorite", ["FAVORITES"]),

    ChangeParameters(){
      return JSON.stringify(this.ORDERS) + JSON.stringify(this.FAVORITES);
    },
  },

  watch: {
    ChangeParameters: async function() {
      this.countQuantity();
      this.checkIsWish();
    },
  },

  mounted(){
    this.countQuantity();
    this.checkIsWish();
  },


  methods: {
    ...mapActions("order", ["UPDATE_ITEMS_IN_CART"]),
    ...mapActions("favorite", ["UPDATE_IS_WISH_IN_CART"]),

    getImagePath(item) {
      let path = null;
      if (item) {
        const allPath = item.split(',');
        path = process.env.VUE_APP_IMAGES + allPath[0];
      }
      return path;
    },

    openCardItem(id) {
      const URL = '/card_product/' + id;
      this.$router.push(URL);
    },

    async onOperationWithCartItem(card) {
      const itemData = {
        amount: 1,
        product: {
          id: card.id,
          vendor_code: card.vendor_code,
          name: card.name,
          price: card.price,
        },
      }
      const type = this.quantity === 0 ? 'increase' : 'remove';
      this.quantity = this.quantity !==0 ? 0 : 1;
      await this.UPDATE_ITEMS_IN_CART({itemData, type});
    },

    async onWishClick(card) {
      const itemData = {
        product: {
          id: card.id,
          vendor_code: card.vendor_code,
          name: card.name,
        },
      }  
      const type = this.isWish === false ? 'set' : 'remove';
      await this.UPDATE_IS_WISH_IN_CART({ itemData, type });
    },

    countQuantity() {
      if (this.ORDERS.length) {
        const filtered = this.ORDERS.filter(item => item.product.id === this.card.id);
        this.quantity =  filtered.length ? filtered[0].amount : 0;
      } else {
        this.quantity = 0;
      }
    },

    checkIsWish() {
      if (this.FAVORITES.length) {
        const filtered = this.FAVORITES.filter(item => item.product.id === this.card.id);
        this.isWish =  filtered.length ? true : false;
      } else {
        this.isWish = false;
      }
    },

  },

}


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
  padding: 20px 22px 30px 22px;

  &__img {
    width: 100%;
    cursor: pointer;

    img{
      max-width: 100%;
    }

  }

  &__tag{
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

  &__row {
  justify-content: space-between;
    &:nth-child(1){
      margin-bottom: 3px;
    }
    &:nth-child(2){
      margin-bottom: 15px;
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
    }


  }

  .notice{
    font-weight: 300;
    font-size: 10px;
    opacity: 0.5;
    text-align: right;
  }

  .old_price {
    font-size: 16px;
    line-height: 24px;
    text-decoration-line: line-through;
    opacity: 0.4;

  }

  .current_price {
    font-weight: 500;
    font-size: 20px;
    line-height: 24px;
    span{
      font-weight: 300;
    }

  }

  &__title {
    margin-bottom: 10px;
    height: 40px;
    overflow: hidden;
    line-height: 1.26;
    font-weight: 400;
    cursor: pointer;
    a{
      font-weight: 500;
      font-size: 15px;

      color: #423E48;
    }

  }

  &__uptitle{
    font-size: 14px;
    a{
      font-weight: 400;
      font-size: 14px;
      line-height: 130%;
      color: #423E48;
    }

  }



}

</style>
