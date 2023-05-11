<template>
  <div class="product" v-if="cartItemData && id">
    <div class="product__wrapper">
      <div class="product__content _container">
        <div class="product__body">
          <div class="product__box flex-center">
              <div class="product__main-img">
                  <CardImage :images=cartItemData.images />
              </div>
              <div class="product__info">
                  <div class="desc-product__title"> {{ cartItemData.name }}</div>
                  <div class="desc-product__article  _label">Артикул: <span>{{ cartItemData.vendor_code }}</span></div>
                  <div class="desc-product__status icon-done-color _label" v-if = "cartItemData.status === 'A'">В наличии</div>
                  <div class="desc-product__status icon-on-the-way " v-if = "cartItemData.status === 'W'">В пути на склад</div>
                  <div class="desc-product__status if_status_on_the_way _label" v-if = "cartItemData.status === 'W'">Доставим в течение 14 дней</div>
                  <div class="desc-product__status icon-out-of-stock _label" v-if = "cartItemData.status === 'O'">Нет в наличии</div>

                  <div class="desc-product__count">
                      <span class="_label">Количество</span>
                      <span class="icon-minus" @click.stop="minusQuantityLocal"></span>
                      <input class="desc-product__input"  type="number" v-model="quantityLocal" @click.stop="" @input="checkQuantityLocal">
                      <span class="icon-plus" @click.stop="plusQuantityLocal"></span>
                  </div>

                  <div class="desc-product__price">
                      <div class="price__left">
                          <div class="_label">Ваша цена:</div>
                          <div class="current_price">
                          <span v-if="cartItemData.price_with_discount_and_tax && cartItemData.price_with_tax !== cartItemData.price_with_discount_and_tax"
                                class="old_price"
                          >{{ cartItemData.price_with_tax }}
                          </span>
                          <span :class="[cartItemData.price_with_discount_and_tax && cartItemData.price_with_discount_and_tax !== cartItemData.price_with_tax ? 'price_w_discount' : '']">
                            {{ cartItemData.price_with_discount_and_tax && cartItemData.price_with_discount_and_tax !== cartItemData.price_with_tax
                              ? cartItemData.price_with_discount_and_tax
                              : cartItemData.price_with_tax
                            }}
                          </span>BYN
                              <!-- cartItemData.price  -->
                              <span class="current_price_item">/{{ cartItemData.base_unit.full_name }}</span>
                          </div>
                      </div>
                      <div class="price__right">
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
                                  <span class="price__value">
                                    {{ cartItemData.price_with_discount_and_tax && cartItemData.price_with_discount_and_tax !== cartItemData.price_with_tax
                                      ? cartItemData.price_with_discount_and_tax
                                      : cartItemData.price_with_tax
                                    }}
                                  </span>BYN
                                  <span>/шт</span>
                              </div>

                          </div>
                      </div>
                  </div>
                  <div class="product__label">*Все цены указаны с учетом НДС.</div>
                  <div class="product__button flex-center">
                      <div v-if="quantity !== 0" class="btn empty_black" @click.stop="onOperationWithCartItem(cartItemData, 'set')">В корзине</div>
                      <div v-if="quantity === 0 && cartItemData.status !== 'O'" class="btn black" @click.stop="onOperationWithCartItem(cartItemData, 'set')">В корзину</div>
                      <div v-if="quantity === 0 && cartItemData.status === 'O'" class="btn empty_black popup-btn" @click.stop="onCreatePopUp(true, cartItemData.id)">Узнать о поступлении</div>

                      <div
                              @click.stop="onWishClick()"
                              :class="[isWish === false ? 'product__favorite icon-favorite' : 'product__favorite icon-favorite-choosed']"

                      >
                      </div>
                  </div>
                  <a class="product__link _link" href="/how_to_work">Как оформить заказ ></a>



            </div> <!-- product__info -->
          </div>  <!-- product__box -->


        </div>
      </div>
    </div>
  </div>
  <div v-if="cartItemData && id" class="tab__description _container">
      <!-- Tab links -->
      <div class="tab ">
          <button :class="[infoBlock === 0 ? 'tablinks active' : 'tablinks']" @click="onChangeInfoBlock(0)">Описание</button>
          <button :class="[infoBlock === 1 ? 'tablinks active' : 'tablinks']" @click="onChangeInfoBlock(1)">Характеристики</button>
          <button :class="[infoBlock === 2 ? 'tablinks active' : 'tablinks']" @click="onChangeInfoBlock(2)">Документация</button>
      </div>
      <!-- Tab content Описание  -->
      <div v-if="infoBlock === 0" class="tabcontent">
<!--          <h3>Описание</h3>-->
          <p>{{ cartItemData.description }}</p>
      </div>
      <!-- Tab content Характеристики  -->
      <div v-if="infoBlock === 1" class="tabcontent">
<!--          <h3>Характеристики</h3>-->
          <div class="tabcontent__row table__items"
            v-for = "option in cartItemData.attributes"
            :key = option.id
          >
            <div class="table__item">
              <span>{{ option?.name?.payload }}</span>
              <span>{{ option?.value?.payload }}</span>
            </div>
          </div>
      </div>
      <!-- Tab content Документация  -->
      <div v-if="infoBlock === 2" class="tabcontent">
          <h3>Документация</h3>
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

  <Recomendation 
    :isShowFilter = false
    :isShowFollow = false
  />

  <ShownItems/>
  
</template>

<script>
  import axios from 'axios';
  import { mapGetters, mapMutations, mapActions } from 'vuex' 
  import CardImage from '@/components/UI/card-image.vue'
  import Recomendation from '@/components/about/Recomendation.vue';
  import ShownItems from '@/components/card/shown_cards.vue';

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
        infoBlock: 0
      }
    },

    components: {
      CardImage,
      Recomendation,
      ShownItems,
    },

   computed: {
      ...mapGetters("order", ["ORDERS"]),
      ...mapGetters("favorite", ["FAVORITES"]),
      ...mapGetters("header", ["ALL_CATEGORIES"]),
      ...mapGetters("catalog", ["SHOWN_ITEMS_LIST"]),

      ChangeParameters(){
        return JSON.stringify(this.ORDERS) + JSON.stringify(this.FAVORITES);
      },
    },

    watch: {
      ChangeParameters: function() {
        this.countQuantity();
        this.checkIsWish();
      },
      id: function() {
        this.onGetCartData();
      }
    },

    methods: {
      ...mapMutations("notification", ["ADD_MESSAGE"]),
      ...mapActions("order", ["UPDATE_ITEMS_IN_CART"]),
      ...mapActions("favorite", ["UPDATE_IS_WISH_IN_CART"]),
      ...mapActions("breadcrumb", ["CHANGE_BREADCRUMB"]),
      ...mapMutations("breadcrumb", ["ADD_BREADCRUMB"]),
      ...mapMutations("query", ["SET_SEARCH_STRING"]),
      ...mapMutations("header", ["SET_IS_POPUP_OPEN", "SET_POPUP_ACTION", "SET_POPUP_ADDITIONAL_DATA", "SET_REQUEST_CALL_TYPE"]),
      ...mapMutations("catalog", ["SET_SHOWN_ITEMS_LIST"]),

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

      onChangeInfoBlock(num){
        this.infoBlock = num;
      },

      updateShowItems(id){
        if (!id) return
        let itemsInLocalStorage = [];
        const isItemsFromLocalStore = localStorage.getItem("shownCards");
        if (isItemsFromLocalStore) itemsInLocalStorage = JSON.parse(isItemsFromLocalStore);
        if (!itemsInLocalStorage.length) {
          itemsInLocalStorage.push({id, time: new Date().getTime()});
        } else {
          const filtered = itemsInLocalStorage.filter(item => item.id !== id);
          filtered.push({id, time: new Date().getTime()});
          const sorted = filtered.sort((a,b) => b.time - a.time);
          itemsInLocalStorage = [...sorted];
        }
        localStorage.setItem("shownCards", JSON.stringify(itemsInLocalStorage));
        this.SET_SHOWN_ITEMS_LIST(itemsInLocalStorage);
      },

      async onGetCartData(){
        this.updateShowItems(this.id);
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

    },

    async mounted(){
      this.onGetCartData();
    },

  }


</script>

<style scoped lang="scss">

.product {

  &__wrapper{}
  &__content{}

  &__body{
    .if_status_on_the_way{
      font-size: 12px;
      margin-left: 25px;
      @media (max-width: $md3+px) {
        font-size: 11px;
        margin:0 0 10px 0;
      }
    }
  }
  &__box{
    display: flex;
    margin-bottom: 40px;
    @media (max-width: $md3+px) {
      flex-direction: column;
      font-size: 11px;
      margin-bottom: 10px;
    }

  }
  &__main-img{
    flex-basis: 40%;
    text-align: center;
  }
  &__info{
    flex-basis: 60%;
    padding: 0 0 0 10px;
    position: relative;
    @media (max-width: $md3+px) {
      width: 100%;
      padding: 0 0 0 0;
      display: flex;
      flex-direction: column;
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

      &:nth-child(2){}
    }
  }
  &__label{
      font-size: 12px;
      line-height: 20px;
      text-align: right;
      margin-bottom: 20px;
      @media (max-width: $md3+px) {
        font-size: 8px;
        margin-bottom: 5px;
      }
  }
  &__btn{
    background: #423E48;
    font-weight: 400;
    padding: 13px 40px;

  }
  &__button{
    margin-bottom: 20px;
    @media (max-width: $md3+px) {
      position: absolute;
      right: 0;
      bottom: 52px;
      margin-bottom: 0;
      .btn{
        min-width: auto;
      }

    }

  }


  &__favorite{
    cursor: pointer;
    margin-left: 20px;
    @media (max-width: $md3+px) {
      position: absolute;
      right: 39px;
      bottom: 70px;
      font-size: 20px;
    }

  }
  &__link{
    opacity: 0.7;
    @media (max-width: $md3+px) {
      font-size: 11px;
    }
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
    margin-bottom: 8px;
    @media (max-width: $md3+px) {
      font-size: 16px;
    }
  }

  &__article{
    margin-bottom: 16px;
     @media (max-width: $md2+px) {
       margin-bottom: 5px;
       font-size: 11px;
    }

  }
  &__status{
    line-height: 20px;
    &:before{
      margin-right: 10px;
    }
    @media (max-width: $md3+px) {
      order: -1;
      font-size: 11px;
      margin-top: 10px;

    }
  }

  &__count{
    margin: 30px 0;
    @media (max-width: $md2+px) {
      margin: 10px 0;
    }
      span{
        cursor: pointer;
        &:nth-child(1){
          margin-right: 10px;
        }
      }

  }
  &__price{
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #F9F9F9;
    padding: 22px 18px 20px 18px;
    font-size: 14px;
    font-weight: 300;
    @media (max-width: $md3+px) {
      flex-direction: column-reverse;
      align-items: stretch;
      padding: 22px 18px 0 0;
      font-size: 11px;
      background: none;
      .price__left{
        margin-top: 20px;
        background: #F9F9F9;
        padding: 10px 0 5px 10px;
        margin: 20px -10px 0 -10px;

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

  &__favorive{
    cursor: pointer;
    &:hover{
    }
  }



}

.current_price{
  font-weight: 500;
  font-size: 24px;
  line-height: 36px;
  &_item{
    font-weight: 300;
  }
  @media (max-width: $md3 + px){
    font-size: 14px;
  }
  .old_price {
    text-decoration-line: line-through;
    opacity: 0.4;
    white-space: nowrap;
    font-weight: 300;
    font-size: 18px;
  }
  span{
    margin-right: 10px;
    // &:nth-child(2){
    //   font-weight: 300;
    // }
  }
}

.retail_price, .opt_price{
  display: flex;
  align-items: center;
  justify-content: space-between;
  @media (max-width: $md3+px) {
    justify-content: flex-start;
  }
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
      font-size: 11px;
    }
  }
  p{

  }
}

.tab__description{
  /* Style the tab */
  .tab {
    overflow: hidden;
    margin-bottom: -2px;
    margin-left: 12px;

  }

  /* Style the buttons inside the tab */
  .tab button {
    background-color: inherit;
    float: left;
    border: none;
    outline: none;
    cursor: pointer;
    padding: 14px 16px;
    transition: 0.3s;
    font-size: 17px;
    @media (max-width: $md3+px) {
        font-size: 12px;
        padding: 10px 10px;
    }
  }

  /* Change background color of buttons on hover */
  .tab button:hover {
    color: #4275D8;
  }

  /* Create an active/current tablink class */
  .tab button.active {
    color: #4275D8;
    font-weight: 500;
    border-bottom: 2px solid #4275D8;
  }

  /* Style the tab content */
  .tabcontent{
    padding: 20px 20px;
    border: 2px solid #EEEEEE;
    border-radius: 8px;
    min-height: 200px;
    @media (max-width: $md3+px) {
      font-size: 12px;
    }
    &__row{
      border: 1px solid #eee;
      .table__item{
        display: flex;
        flex-direction: row;
        flex-wrap: nowrap;
        justify-content: space-between;
        padding: 7px 10px;
      }
      &:nth-child(2n+1){
        background: #fbfbfb;
      }
    }

  }
  .tabcontent p{
    font-weight: 300;
    font-size: 16px;
    line-height: 140%;
    color: #423E48;
    margin: 8px 0;
    @media (max-width: $md3+px) {
      font-size: 12px;
    }

  }

  /* Style the close button */
  .topright {
    float: right;
    cursor: pointer;
    font-size: 28px;
  }

  .topright:hover {color: red;}

}

</style>

