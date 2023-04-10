<template>
  <div class="product" v-if="cartItemData && id">
    <div class="product__wrapper">
      <div class="product__content _container">
        <div class="product__body">

          <div class="grid">
            <div class="grid__item" tabindex="1">
              <div class="product__main-img">
                <CardImage :images=cartItemData.images />
              </div>
            </div>
            <div class="grid__item" tabindex="2">
              <div class="product__add-img add-img">
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
<!--              <div class="status-row__link icon-share"><span>Поделиться</span></div>-->
            </div>
            <div class="grid__item" tabindex="7">
              <div class="desc-product__status icon-done-color _label" v-if = "cartItemData.status === 'A'">В наличии</div>
              <div class="desc-product__status icon-on-the-way " v-if = "cartItemData.status === 'W'">В пути на склад</div>
              <div class="desc-product__status if_status_on_the_way _label" v-if = "cartItemData.status === 'W'">Доставим в течение 14 дней</div>
              <div class="desc-product__status icon-out-of-stock _label" v-if = "cartItemData.status === 'O'">Нет в наличии</div>
            </div>
            <div class="grid__item" tabindex="8">
              <div class="price-product__block">
                <div class="_label">Ваша цена:</div>
                <div class="current_price">
                  <span>
                    {{ cartItemData.price_with_discount_and_tax && cartItemData.price_with_discount_and_tax !== cartItemData.price_with_tax 
                          ? cartItemData.price_with_discount_and_tax 
                          : cartItemData.price_with_tax 
                    }}
                  </span>BYN
                  <!-- cartItemData.price  -->
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
                  <div>Первоначальная цена: </div>
                  <div>
                    <span class="price__value"> {{ cartItemData.price_with_tax }}</span>
                      BYN
                    <span>/шт</span>
                  </div>

                </div>
                <div class="opt_price">
                  <div>Цена со скидкой: </div>
                  <div>
                    <span class="price__value">{{ 
                        cartItemData.price_with_discount_and_tax && cartItemData.price_with_discount_and_tax !== cartItemData.price_with_tax 
                          ? cartItemData.price_with_discount_and_tax 
                          : cartItemData.price_with_tax }}</span>BYN
                    <span>/шт</span>
                  </div>

                </div>
              </div>
            </div>
            <div class="grid__item" tabindex="11">
              <div v-if="quantity !== 0" class="btn empty_black" @click.stop="onOperationWithCartItem(cartItemData, 'set')">В корзине</div>
              <div v-if="quantity === 0 && cartItemData.status !== 'O'" class="btn black" @click.stop="onOperationWithCartItem(cartItemData, 'set')">В корзину</div>
              <div v-if="quantity === 0 && cartItemData.status === 'O'" class="btn empty_black popup-btn" @click.stop="onCreatePopUp(true, cartItemData.id)">Узнать о поступлении</div>
            </div>
            <div class="grid__item" tabindex="12">
              <div class="desc-product__count">
                <span class="_label">Количество</span>
                <span class="icon-minus" @click.stop="minusQuantityLocal"></span>
                <input class="desc-product__input"  type="number" v-model="quantityLocal" @click.stop="" @input="checkQuantityLocal">
                <span class="icon-plus" @click.stop="plusQuantityLocal"></span>
              </div>
            </div>
            <div class="grid__item" tabindex="13">
              <a class="product__link _link" href="/how_to_work">Как оформить заказ ></a>
            </div>
          </div>


        </div>
      </div>
    </div>
  </div>
  <div class="product__attention flex-center _container">
    <div class="icon"><svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M9 7H11V5H9V7ZM9 15H11V9H9V15ZM9.99 20C4.47 20 0 15.52 0 10C0 4.48 4.47 0 9.99 0C15.52 0 20 4.48 20 10C20 15.52 15.52 20 9.99 20ZM10 2C5.58 2 2 5.58 2 10C2 14.42 5.58 18 10 18C14.42 18 18 14.42 18 10C18 5.58 14.42 2 10 2Z" fill="#423E48"/>
    </svg>
    </div>
    <div class="attention__text">
      <p>Уважаемые покупатели.</p>
      <p>Обращаем Ваше внимание, что производитель оставляет за собой право изменять внешний вид, технические характеристики и комплектацию без уведомления.</p>
    </div>


  </div>
</template>

<script>
  import axios from 'axios';
  import { mapGetters, mapMutations, mapActions } from 'vuex' 
  import CardImage from '@/components/UI/card-image.vue'

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
        quantityLocal: 1,
      }
    },

    components: {
      CardImage,
    },

   computed: {
      ...mapGetters("order", ["ORDERS"]),
      ...mapGetters("favorite", ["FAVORITES"]),
      ...mapGetters("header", ["ALL_CATEGORIES"]),

      ChangeParameters(){
        return JSON.stringify(this.ORDERS) + JSON.stringify(this.FAVORITES);
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
      ...mapActions("breadcrumb", ["CHANGE_BREADCRUMB"]),
      ...mapMutations("breadcrumb", ["ADD_BREADCRUMB"]),
      ...mapMutations("query", ["SET_SEARCH_STRING"]),
      ...mapMutations("header", ["SET_IS_POPUP_OPEN", "SET_POPUP_ACTION", "SET_POPUP_ADDITIONAL_DATA", "SET_REQUEST_CALL_TYPE"]),

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
        }
        if (type === 'set') {
          itemData.amount = Number(this.quantityLocal);
        }

        await this.UPDATE_ITEMS_IN_CART({itemData, type});
        if (this.quantityLocal === 0) this.quantityLocal = 1;
      },

      onCreatePopUp(status, cardID) {
        this.SET_IS_POPUP_OPEN(status);
        this.SET_POPUP_ACTION('RequestCall');
        this.SET_REQUEST_CALL_TYPE('GR');
        this.SET_POPUP_ADDITIONAL_DATA({cardID});
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
        this.quantityLocal = this.quantity ? this.quantity : this.quantityLocal;
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
        this.countQuantity();
        this.checkIsWish();
        this.SET_SEARCH_STRING('');
        this.CHANGE_BREADCRUMB(0);
        try {
            const response = await axios.get(process.env.VUE_APP_API_URL + 'products/' + this.id);
            this.cartItemData = response.data;
        } catch (e) {
            console.log(e);
            this.ADD_MESSAGE({name: "Не возможно загрузить рекомендованные товары ", icon: "error", id: '1'})
        }

        const mainBreadCrumb = {
          name: 'Каталог',
          path: '/catalog',
          type: 'global',
          class: '',
          category: 1,
          level: 'root',
        }
        this.ADD_BREADCRUMB(mainBreadCrumb);

        const chein = [];
        const category = this.cartItemData.category;
        chein.push(category);
        if (category.parent_category_id) {
          const category1 = this.ALL_CATEGORIES.filter(item => item.id === category.parent_category_id)[0];
          chein.push(category1);
          if (category1.parent_category_id) {
            const category2 = this.ALL_CATEGORIES.filter(item => item.id === category1.parent_category_id )[0];
            chein.push(category2);
          }
        }

        const level = ['last', 'sub', 'top'];

        for (let i = 0; i < chein.length; i++) {
          // console.log(chein[i]);
          const currBreadCrumb  = {
            name: chein[chein.length - 1 - i].name,
            path: '/category/' + chein[chein.length - 1 - i].id,
            type: 'global',
            class: '',
            category: chein[chein.length - 1 - i].id,
            level: level[chein.length - 1 - i],
          };
          this.ADD_BREADCRUMB(currBreadCrumb);
        }

        this.ADD_BREADCRUMB({
          name: this.cartItemData.name,
          path: this.$router.currentRoute.value.path,
          type: "global",
          class: ""
        });
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
        "photo photo photo arcticle arcticle"
        "photo photo photo status status"
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
    grid-template-columns: repeat(7, 1fr);
    grid-template-rows: auto;
    gap: 5px;
    grid-template-areas:
      "breadcrumb breadcrumb  breadcrumb breadcrumb breadcrumb share  share"
      "photo photo photo title title title title"
      "photo photo photo arcticle arcticle arcticle arcticle"
      "photo photo photo status status status status"
      "photo photo photo count count count count"
      "photo photo photo price price add_price add_price"
      "big1 big1 big1 cart_button cart_button wishlist wishlist"
      "big1 big1 big1 link link link link";
  }
}

.grid__item:nth-child(1)  {
  grid-area: photo;
  grid-row: 1/9;
  align-self: center;
  justify-self: center;
  @media (max-width: $md2+px){
    grid-row: 1;
  }
}
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
.grid__item:nth-child(11) {
  grid-area: cart_button;
  align-self: center;
  @media (max-width: $md2+px){

  }
}
.grid__item:nth-child(12) { grid-area: count; }
.grid__item:nth-child(13) { grid-area: link; }




.product {

  &__wrapper{


  }
  &__content{

  }

  &__body{
    .if_status_on_the_way{
      font-size: 12px;
      margin-left: 25px;
    }

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

  &__article{


     @media (max-width: $md2+px) {
       margin-bottom: 20px;
    }

  }
  &__status{
    line-height: 20px;
    &:before{
      margin-right: 10px;
    }
  }

  &__count{
    @media (max-width: $md2+px) {
      margin: 20px 0;
    }
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
  @media (max-width: $md3 + px){

  }
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
  .price__value{
    margin: 0 5px;
    font-weight: 600;
  }
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
.product__attention{
  width: 100%;
  font-weight: 300;
  font-size: 14px;
  line-height: 20px;
  color: #423E48;
  opacity: 0.4;
  padding-top: 20px;
  padding-bottom: 20px;

  align-items: flex-start;
  justify-content: flex-start;
  .icon{

  }
  .attention__text{
    padding-left: 20px;
    max-width: 60%;
    @media (max-width: $md3+px) {
      max-width: 100%;
    }
  }
  p{

  }
}

</style>
