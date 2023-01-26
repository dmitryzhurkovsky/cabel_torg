<template>
  <div class="product" v-if="cartItemData && id">
    <div class="product__wrapper">
      <div class="product__content _container">
        <div class="product__body">

          <div class="grid">
            <div class="grid__item" tabindex="1">
              <div class="product__main-img">
                <img v-if = "cartItemData.images" :src=getImagePath(cartItemData.images) alt="">
                <img v-if = "!cartItemData.images" src="../assets/no_image.svg" alt="">
              </div>
            </div>
            <div class="grid__item" tabindex="2">
              <div class="product__add-img add-img">
                <!--                <img class="add-img__item" src="../assets/catalog/card1.png" alt="">-->
                <!--                <img class="add-img__item" src="../assets/catalog/card1.png" alt="">-->
              </div>
            </div>
            <div class="grid__item" tabindex="3">
              <div class="desc-product__title"> {{ cartItemData.name }}</div>
            </div>
            <div class="grid__item" tabindex="4">
              <div class="desc-product__article  _label">Артикул: <span>{{ cartItemData.vendor_code }}</span></div>
            </div>
            <div class="grid__item" tabindex="5">
            </div>
            <div class="grid__item" tabindex="6">
              <div class="status-row__link icon-share"><span>Поделиться</span></div>
            </div>
            <div class="grid__item" tabindex="7">
              <div class="desc-product__status icon-done-color _label">В наличии</div>
            </div>
            <div class="grid__item" tabindex="8">
              <div class="price-product__block">
                <div class="_label">Ваша цена:</div>
                <div class="current_price">
                  <span>{{ cartItemData.price }}</span>BYN
                  <span>/{{ cartItemData.base_unit.full_name }}</span>
                </div>
              </div>
            </div>
            <div class="grid__item" tabindex="9">
              <div 
                  @click.stop="onWishClick()"
                  :class="[isWish === false ? 'product__favorite icon-favorite' : 'product__favorite icon-favorite-choosed']" 
              >
              </div>
            </div>
            <div class="grid__item" tabindex="10">
              <div class="price-product__block">
                <div class="retail_price">
                  <div>Розничная цена: </div>
                  <div>
                    <span>70???</span>BYN
                    <span>/шт</span>
                  </div>

                </div>
                <div class="opt_price">
                  <div>Оптовая цена: </div>
                  <div>
                    <span>70???</span>BYN
                    <span>/шт</span>
                  </div>

                </div>
              </div>
            </div>
            <div class="grid__item" tabindex="11">
              <div v-if="quantity !== 0" class="btn black" @click.stop="onOperationWithCartItem(cartItemData, 'remove')">В корзине</div>
              <div v-if="quantity === 0" class="btn blue" @click.stop="onOperationWithCartItem(cartItemData, 'increase')">В корзину</div>
            </div>
            <div class="grid__item" tabindex="12">
              <div class="desc-product__count">
                <span class="_label">Количество</span>
                <span class="icon-minus" @click.stop="onOperationWithCartItem(cartItemData, 'decrease')"></span>
                <input class="desc-product__input" type="text" v-model="quantity" @input="onOperationWithCartItem(cartItemData, 'set')" @click.stop="">
                <span class="icon-plus" @click.stop="onOperationWithCartItem(cartItemData, 'increase')"></span>
              </div>
            </div>
            <div class="grid__item" tabindex="13">
              <a class="product__link">Как оформить заказ ></a>
            </div>
          </div>


        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios';
  import { mapGetters, mapMutations, mapActions } from 'vuex' 

  export default {
    name: 'CardProduct',

    props: {
      id: null,
    },

    data(){
      return {
        cartItemData: null,
        isWish: false,
        quantity: 0,
      }
    },

    computed: {
      ...mapGetters("order", ["ORDERS"]),
      ...mapGetters("favorite", ["FAVORITES"]),

      ChangeParameters(){
        return JSON.stringify(this.ORDERS) + JSON.stringify(this.FAVORITES) + String(this.isWish) + 
              this.cartItemData ? JSON.stringify(this.cartItemData) : String(this.cartItemData);
      },
    },

    watch: {
      ChangeParameters: function() {
        this.countQuantity();
        this.checkIsWish();
      },
    },

    methods: {
      ...mapMutations("notification", ["ADD_MESSAGE"]),
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

      async onOperationWithCartItem(card, type) {
        if (this.quantity == 0 && type === 'remove') {
          return
        } else if (this.quantity < 0) return

        console.log('QQQQ');
        const itemData = {
          amount: 1,
          product: {
            id: card.id,
            vendor_code: card.vendor_code,
            name: card.name,
            price: card.price,
          },
        }
        if (type === 'set') {
          itemData.amount = Number(this.quantity);
        }

        // const type = this.quantity === 0 ? 'increase' : 'remove';
        // this.quantity = this.quantity !==0 ? 0 : 1;
        await this.UPDATE_ITEMS_IN_CART({itemData, type});
        this.countQuantity();
      },

      async onWishClick() {
        const itemData = {
          product: {
            id: this.cartItemData.id,
            vendor_code: this.cartItemData.vendor_code,
            name: this.cartItemData.name,
          },
        }  
        const type = this.isWish === false ? 'set' : 'remove';
        await this.UPDATE_IS_WISH_IN_CART({ itemData, type });
        this.checkIsWish()
      },

      countQuantity() {
        if (this.ORDERS.length) {
          const filtered = this.ORDERS.filter(item => String(item.product.id) === String(this.id));
          this.quantity =  filtered.length ? filtered[0].amount : 0;
        } else {
          this.quantity = 0;
        }
      },

      checkIsWish() {
        if (this.FAVORITES.length) {
          const filtered = this.FAVORITES.filter(item => String(item.product.id) === String(this.id));
          this.isWish =  filtered.length ? true : false;
        } else {
          this.isWish = false;
        }
      },

    },

    async mounted(){
        try {
            const response = await axios.get(process.env.VUE_APP_API_URL + 'products/' + this.id);
            this.cartItemData = response.data;
        } catch (e) {
            console.log(e);
            this.ADD_MESSAGE({name: "Не возможно загрузить рекомендованные товары ", icon: "error", id: '1'})
        }
    },

  }
</script>

<style scoped lang="scss">

.grid {
  display: grid;
  align-items: start;
  justify-items: start;
  //grid-gap: 1.5vw;
  //min-height: 100vh;
  //padding: 1.5vw;
  transition: 2s;
  &__item{
    padding: 5px 0;
  }
}


.grid {
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows:auto;

  grid-template-areas:
      "photo   photo"
      "status   status"
      "title   title"
      "arcticle arcticle"
      "add_price wishlist"
      "count count"
      "price cart_button"
      "link link";
}
.grid .item:nth-child(6){
  display: none;
}

@media screen and (min-width: $md2+px) {
  .grid {
    grid-template-columns: repeat(5, 1fr);
    grid-template-rows: auto;

    grid-template-areas:
        "breadcrumb breadcrumb breadcrumb breadcrumb breadcrumb "
        "title title  title title title"
        "photo photo photo arcticle status"
        "photo photo photo add_price add_price"
        "photo photo photo count count"
        "photo photo photo price price"
        "photo photo photo cart_button wishlist"
        "big1 big1 big1 link link";
  }
  .grid .item:nth-child(6){
    display: none;
  }
}

@media screen and (min-width: $md1+px) {
  .grid {
    grid-template-columns: repeat(6, 1fr);
    grid-template-rows: auto;
    grid-template-areas:
      "breadcrumb breadcrumb  breadcrumb breadcrumb share  share"
      "photo photo photo title title title"
      "photo photo photo arcticle arcticle arcticle"
      "photo photo photo status status status"
      "photo photo photo count count count"
      "photo photo photo price add_price add_price"
      "big1 big1 big1 cart_button wishlist wishlist"
      "big1 big1 big1 link link link";
  }
}

.grid__item:nth-child(1)  { grid-area: photo; }
.grid__item:nth-child(2)  { grid-area: big1; }
.grid__item:nth-child(3)  { grid-area: title; }
.grid__item:nth-child(4)  { grid-area: arcticle; }
.grid__item:nth-child(5)  { grid-area: breadcrumb; }
.grid__item:nth-child(6)  { grid-area: share; }
.grid__item:nth-child(7)  { grid-area: status; }
.grid__item:nth-child(8)  { grid-area: price; }
.grid__item:nth-child(9)  {
  grid-area: wishlist;
  align-self: center;
  justify-content: start;
  padding-left: 20px;
;
}
.grid__item:nth-child(10) { grid-area: add_price; }
.grid__item:nth-child(11) { grid-area: cart_button; }
.grid__item:nth-child(12) { grid-area: count; }
.grid__item:nth-child(13) { grid-area: link; }




.product {

  &__wrapper{


  }
  &__content{

  }

  &__body{


  }
  &__status-row{

    display: flex;
    align-items: center;
    justify-content: space-between;
    @media (max-width: $md3+px) {
      flex-direction: column;
      align-items: flex-start;
    }

    .status-row__link{
      font-weight: 300;
      font-size: 12px;
      line-height: 16px;

      @media (max-width: $md3+px) {
        text-align: right;
        width: 100%;
        span{
          display: none;
        }
      }
    }
  }
  &__block {
    display: flex;
    align-items: flex-start;
    @media (max-width: $md3+px) {
      flex-direction: column;
    }


    ._block{
      flex-basis: 50%;

      &:nth-child(1){
        display: flex;
        flex-direction: column;

      }

      &:nth-child(2){

      }


    }
  }
  &__main-img{

    flex-basis: 80%;
    img{
      width: 100%;
    }


  }
  &__add-img{

    flex-basis: 20%;
    img{
      width: 100%;
    }


  }
  &__btn{
    background: #423E48;
    font-weight: 400;
    padding: 13px 40px;


  }
  &__favorite{
    cursor: pointer;

  }
  &__link{
    font-size: 14px;
    opacity: 0.7;
  }
  &__action{
    margin:30px 0 20px 0;
  }

}
.desc-product{
  font-size: 14px;

  &__title{
    font-weight: 500;
    font-size: 20px;
    line-height: 28px;
    color: #423E48;
  }

  &__arcticle{

  }
  &__status{
    line-height: 20px;
    &:before{
      margin-right: 10px;
    }
  }
  &__count{
      span{
        cursor: pointer;
        &:nth-child(1){
          margin-right: 10px;
        }
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

  &__price{
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #F9F9F9;
    padding: 22px 18px 20px 18px;
    .retail_price{

    }
  }


  &__favorive{
    cursor: pointer;
    &:hover{
      background: red;
    }
  }



}

.current_price{
  font-weight: 500;
  font-size: 24px;
  line-height: 36px;
  span{
    margin-right: 10px;
    &:nth-child(2){
      font-weight: 300;
    }
  }
}

.retail_price, .opt_price{
  display: flex;
  align-items: center;
  justify-content: space-between;

}

.opt_price{
margin-top: 15px;
}


.status-row__link{
  font-weight: 300;
  font-size: 12px;
  line-height: 16px;

  @media (max-width: $md3+px) {
    text-align: right;
    width: 100%;
    span{
      display: none;
    }
  }
}


</style>
