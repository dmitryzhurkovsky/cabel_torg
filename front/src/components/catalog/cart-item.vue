<template>
    <div v-if="cartItemData && quantity !==0">
      <div class="product__wrapper">
        <a class="product__img" href="" @click.stop.prevent="openCardItem(cartItemData.id)">
            <CardImage :images=cartItemData.images />
        </a>
        <div class="product__info">
            <div class="product__article  _label mb-20">Артикул: <span>{{ cartItemData.vendor_code }}</span></div>
            <a  class="product__title" href="" @click.stop.prevent="openCardItem(cartItemData.id)"> {{ cartItemData.name }}</a>
            <div class="icon__row mt-20">
                <span 
                    :class="[isWish === false ? 'icon icon-favorite' : 'icon icon-favorite-choosed']" 
                    @click.stop="onWishClick(cartItemData)"
                >В избранное</span>
                <span v-if ="!isMobileVersion" class="icon icon-delete" @click.stop="onOperationWithCartItem(cartItemData, 'remove')">Удалить</span>
                <span v-if ="isMobileVersion" class="icon icon-close" @click.stop="onOperationWithCartItem(cartItemData, 'remove')"></span>
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
            <div class="old_price">
              <span>{{ CardPriceWithoutDiscount }}</span>BYN
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

<script>
  import axios from "axios";
  import {mapGetters, mapActions, mapMutations} from 'vuex'
  import CardImage from '@/components/UI/card-image.vue'

  export default {
    name: 'CartItem',
  
    props: {
        cartItem: null,
        type: false,
    },

    data(){
        return {
            cartItemData: {},
            quantity: 0,
            lastQuantity: 0,
            isWish: false,
        }
    },

    components: {
        CardImage,
    },

    async mounted(){
        this.SET_IS_LOADING(true);
        try {
            const response = await axios.get(process.env.VUE_APP_API_URL + 'products/' + this.cartItem.product.id);
            this.cartItemData = response.data;
            this.quantity = this.cartItem.amount;
            this.lastQuantity = this.cartItem.amount;
        } catch (e) {
            console.log(e);
            this.ADD_MESSAGE({name: "Не возможно загрузить рекомендованные товары ", icon: "error", id: '1'})
        }
        this.checkIsWish();
        this.SET_IS_LOADING(false);
    },

    computed: {
        ...mapGetters("favorite", ["FAVORITES"]),
        ...mapGetters("header", ["VIEW_TYPE"]),

        ChangeParameters(){
            return JSON.stringify(this.FAVORITES);
        },

        cardPriceWithDiscount(){
            return this.cartItemData.price_with_discount ? this.cartItemData.price_with_discount : this.cartItemData.price;
        },

        CardPriceWithoutDiscount(){
            return this.cartItemData.price_with_discount ? this.cartItemData.price : '';
        },

        isMobileVersion(){
            if (this.VIEW_TYPE===1) return false
            if (this.VIEW_TYPE===2) return true
            if (this.VIEW_TYPE===3) return true
        }
    },

    watch: {
        ChangeParameters: async function() {
            this.checkIsWish();
        },
    },

    methods:{
        ...mapMutations("notification", ["ADD_MESSAGE"]),
        ...mapActions("order", ["UPDATE_ITEMS_IN_CART"]),
        ...mapActions("favorite", ["UPDATE_IS_WISH_IN_CART"]),
        ...mapMutations("notification", ["SET_IS_LOADING"]),

        async onOperationWithCartItem(card, type) {
          if (!this.quantity ) {
              this.quantity = this.lastQuantity;
          } else {
            if (type === 'decrease' && this.quantity === 1) {
              return;
            };
            if (this.quantity < 1) {
              this.quantity = this.lastQuantity;
            };
            if (this.quantity >99) {
              this.quantity = this.lastQuantity;
              return;
            };
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
                itemData.amount = Number(this.quantity);
            }
            
            await this.UPDATE_ITEMS_IN_CART({itemData, type});
            if (type === 'increase') {
                if (this.quantity < 99) {
                  this.quantity++;
                }
            } else if (type === 'decrease') {
                this.quantity--;
            };
            this.lastQuantity = this.quantity; 
          }
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

        checkIsWish() {
            if (this.FAVORITES.length) {
                const filtered = this.FAVORITES.filter(item => item.product.id === this.cartItemData.id);
                this.isWish =  filtered.length ? true : false;
            } else {
                this.isWish = false;
            }
        },

        openCardItem(id) {
            const URL = '/card_product/' + id;
            this.$router.push(URL);
        }


    }

  }
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
      width: 100%;

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
      .icon-delete, .icon-close{
        @media (max-width: $md2 + px){
          position: absolute;
          top: 0;
          right: 0;
        }

      }
    }

    &__article{

    }
    &__title{
        font-size: 14px;
        line-height: 24px;
        text-decoration-line: underline;
        color: #423E48;
    }
    &__status{

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
        width: 40px;
        height: 40px;
        padding: 9px 8px;
        background: rgba(66, 62, 72, 0.07);
        border-radius: 2px;
        border: none;
        margin: 0 10px;
        text-align: center;
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