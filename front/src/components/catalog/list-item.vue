<template>
    <div class="product">
        <!-- <div class="product__tag">Хит</div> -->
        <div v-if = "InfoCardBlock === 'Хит'" class="product__taghit">{{ InfoCardBlock }}</div>
        <div v-if = "InfoCardBlock === '%'" class="product__tagdiscount">
          <img class="" src="../../assets/catalog/discount.svg" alt="">
        </div>
        <div v-if = "InfoCardBlock === 'New'" class="product__tagnew">{{ InfoCardBlock }}</div>

        <a class="product__img" @click.stop="openCardItem(card.id)">
            <CardImage :images=card.images />
        </a>
        <div class="product__info">
            <div class="product__status icon-done-color _label mb-20" v-if = "card.status === 'A'">В наличии</div>
            <div class="product__status icon-on-the-way _label mb-20" v-if = "card.status === 'W'">В пути на склад</div>
            <div class="product__status icon-out-of-stock _label mb-20" v-if = "card.status === 'O'">Нет в наличии</div>
            <div class="product__title">
                <a v-if ="card.category">{{ card.category.name }}</a>
            </div>
            <div class="product__uptitle" @click.stop="openCardItem(card.id)">
                <a >{{ card.name }}</a>
            </div>
            <div class="product__count flex-center">
                <span class="_label">Количество:</span>
                <span class="icon-minus" @click.stop="minusQuantityLocal"></span>
                <input class="product__input" type="number" v-model="quantityLocal" @click.stop="" @input="checkQuantityLocal"> 
                <span class="icon-plus" @click.stop="plusQuantityLocal"></span>
            </div>
        </div>
        <div class="product__action">
            <div class="product__article  _label mb-20">Артикул: <span>{{ card.vendor_code }}</span></div>
            <div class="product__price">
                <span  v-if = "card.price_with_discount" class="product__oldprice">{{ CardPriceWithoutDiscount }}</span>
                <span>{{ cardPriceWithDiscount }}</span> BYN
                <span> / {{ card.base_unit.full_name }}</span>
            </div>
            <div class="notice">* Цена указана с учетом НДС.</div>
            <div class="product__btn flex-center">
                <div 
                    :class="[isWish === false ? 'product__wishlist icon-favorite' : 'product__wishlist icon-favorite-choosed']"
                    @click.stop="onWishClick(card)"
                  ></div>
                <div v-if = "quantity !== 0" class="btn empty_black" @click.stop="onOperationWithCartItem(card, 'set')">В корзине {{ quantity }}</div>
                <div v-if = "quantity === 0" class="btn black" @click.stop="onOperationWithCartItem(card, 'set')">В корзину</div>
            </div>
        </div>
    </div>
</template>


<script>
import { mapGetters, mapActions } from 'vuex'
import CardImage from '@/components/UI/card-image.vue'

export default {
    name: 'ListItem',
    props: {
        card:  null,
    },

    data(){
      return {
          quantity: 0,
          quantityLocal: 1,
          isWish: false,
      }
    },

    components: {
      CardImage,
    },

    computed: {
      ...mapGetters("order", ["ORDERS"]),
      ...mapGetters("favorite", ["FAVORITES"]),

      ChangeParameters(){
        return JSON.stringify(this.ORDERS) + JSON.stringify(this.FAVORITES);
      },

      cardPriceWithDiscount(){
        return this.card.price_with_discount ? this.card.price_with_discount : this.card.price;
      },

      CardPriceWithoutDiscount(){
        return this.card.price_with_discount ? this.card.price : '';
      },

      InfoCardBlock() {
        let info = '';
        info = this.card.vendor_code === 'УТ-00000037' ? 'New' : info;
        info = this.card.vendor_code === 'УТ-00000015' ? 'Хит' : info;
        info = this.card.price_with_discount ? '%' : info;
        return info;
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
      
      openCardItem(id) {
        const URL = '/card_product/' + id;
        this.$router.push(URL);
      },

      checkQuantityLocal() {
        if (this.quantityLocal < 1) {
          this.quantityLocal = 1;
        };
        if (this.quantityLocal > 99) {
          this.quantityLocal = 99;
        }
      },

      minusQuantityLocal() {
        this.quantityLocal = this.quantityLocal > 1 ? this.quantityLocal - 1 : 1;
      },

      plusQuantityLocal() {
        this.quantityLocal = this.quantityLocal < 99 ? this.quantityLocal + 1 : 99;
      },

      async onOperationWithCartItem(card, type) {
        // if (this.quantity === 0 && this.quantityLocal === 0) { 
        //   return
        // } else {
          const itemData = {
            amount: 0,
            product: {
              id: card.id,
              vendor_code: card.vendor_code,
              name: card.name,
              price: card.price,
            },
          };
          if (type === 'set') {
            itemData.amount = Number(this.quantityLocal);
          }
          
          await this.UPDATE_ITEMS_IN_CART({itemData, type});
          if (this.quantityLocal === 0) this.quantityLocal = 1;
        // }  
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
        this.quantityLocal = this.quantity ? this.quantity : this.quantityLocal;
      },

      checkIsWish() {
        if (this.FAVORITES.length) {
          const filtered = this.FAVORITES.filter(item => item.product.id === this.card.id);
          this.isWish =  filtered.length ? true : false;
        } else {
          this.isWish = false;
        }
      },

    }

}
</script>

<style scoped lang="scss">

.product{
    display: flex;
    position: relative;
    background: #FFFFFF;
    border: 2px solid #EEEEEE;
    box-sizing: border-box;
    border-radius: 8px;
    padding: 20px 22px 20px 22px;

  ._label{
    font-size: 12px;
    line-height: 20px;
  }

  &__img {
    width: 100%;
    flex-basis: 25%;
    cursor: pointer;
    text-align: center;
    img{
      max-width: 100%;
    }
  }
  &__info{
    flex-basis: 45%;
    padding: 0 10px;

  }

  &__action{
    flex-basis: 25%;
    padding: 0 10px;
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

      cursor: pointer;
      fill: none;
      margin-right: 10px;
    }
    &__price{
      font-size: 20px;
      margin-bottom: 10px;
      text-align: right;
      span:nth-child(1){
        font-weight: 500;
        margin-right: 5px;
      }

    }
    &__oldprice {
      font-size: 16px;
      line-height: 24px;
      text-decoration-line: line-through;
      opacity: 0.4;
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
      &:before {
        cursor: pointer;
        padding: 10px 10px;
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

    &__title {
      margin-bottom: 10px;

      a{
        font-weight: 500;
        font-size: 15px;

        color: #423E48;
      }

    }

    &__uptitle {
      a{
        font-weight: 400;
        font-size: 14px;
        line-height: 130%;
        color: #423E48;
        cursor: pointer;
      }

    }
  &__status{
    &:before{
      margin-right: 10px;
    }
  }
  &__article{
    text-align: right;
  }

  &__count{
    margin: 24px 0;
    span:nth-child(1){
      margin-right: 10px;
    }

    .icon-plus, .icon-minus{
      cursor: pointer;
    }
  }

  &__input{
    width: 40px;
    height: 40px;
    padding: 9px 8px;
    background: rgba(66, 62, 72, 0.07);
    border-radius: 2px;
    border: none;
    margin: 0 10px;
    text-align: center;

  }

  &__btn{
    margin: 24px 0 ;


  }
}
</style>

