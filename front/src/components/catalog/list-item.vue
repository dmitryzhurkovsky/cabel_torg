<template>
    <div class="product">
        <div class="product__tag">Хит</div>
        <a class="product__img" href="">
            <img v-if = "card.images" class="" :src=getImagePath(card.images) alt="">
            <img v-if = "!card.images" class="" src="../../assets/no_image.jpg" alt="">
        </a>
        <div class="product__info">
            <div class="product__status icon-done-color _label mb-20">В наличии</div>
            <div class="product__title">
                <a  href="" v-if ="card.category">{{ card.category.name }}</a>
            </div>
            <div class="product__uptitle">
                <a  href="">{{ card.name }}</a>
            </div>
            <div class="product__count flex-center">
                <span class="_label">Количество:</span>
                <span class="icon-minus" @click="removeItemFromCart(card)"></span>
                <span class="product__input">{{ quantity }}</span>
                <span class="icon-plus" @click="addItemToCart(card)"></span>
            </div>
        </div>
        <div class="product__action">
            <div class="product__article  _label mb-20">Артикул: <span>{{ card.vendor_code }}</span></div>
            <div class="product__price">
                <span>{{ card.price }}</span>BYN
                <span> / {{ card.base_unit.full_name }}</span>
            </div>
            <div class="notice">* Цена указана с учетом НДС.</div>
            <div class="product__btn flex-center">
                <div class="product__wishlist icon-favorite"></div>
                <div class="btn black">В корзину</div>
            </div>
        </div>
    </div>
</template>


<script>
  import { mapGetters, mapMutations } from 'vuex'

  export default {
    name: 'ListItem',

    props: {
        card:  null,
    },

    data(){
      return {
          quantity: 0,
      }
    },

    computed: {
      ...mapGetters("order", ["ORDERS"]),

      ChangeParameters(){
        return JSON.stringify(this.ORDERS);
      },
    },

    watch: {
      ChangeParameters: async function() {
        this.countQuantity();
      },
    },

    mounted(){
      this.countQuantity();
    },

    
    methods: {
      ...mapMutations("order", ["ADD_ITEM_TO_CART", "REMOVE_ITEM_FROM_CART"]),

      getImagePath(item) {
        let path = null;
        if (item) {
          const allPath = item.split(',');
          path = process.env.VUE_APP_IMAGES + allPath[0];
        }
        return path;
      },

      addItemToCart(card){
        const itemToAdd = {
          amount: 1,
          product: {
            id: card.id,
            vendor_code: card.vendor_code,
            name: card.name,
          },
        }
        this.ADD_ITEM_TO_CART(itemToAdd);
        this.quantity++;
      },

      removeItemFromCart(card) {
        const itemToAdd = {
            amount: -1,
            product: {
              id: card.id,
              vendor_code: card.vendor_code,
              name: card.name,
            },
        }
        if (this.quantity > 1) {
          this.ADD_ITEM_TO_CART(itemToAdd);
          this.quantity--;
        } else if (this.quantity === 1) {
          this.REMOVE_ITEM_FROM_CART(itemToAdd);
          this.quantity--;
        }
      },

      countQuantity(){
        if (this.ORDERS.length) {
          const filtered = this.ORDERS.filter(item => item.product.id === this.card.id);
          this.quantity =  filtered.length ? filtered[0].amount : 0;
        } else {
          this.quantity = 0;
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
      flex-basis: 30%;
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
  }

  &__btn{
    margin: 24px 0 ;


  }
}
</style>

