<template>
  <Breadcrumb/>
  <div class="app__content">
    <div class="product" v-if="cartItemData && cartItemId">
      <div class="product__wrapper">
        <div class="product__content _container">
          <div class="product__body">
            <div class="product__box flex-center">
                <div class="product__main-img">
                  <div class="product__main-img--container">
                  <UiCardImage 
                    :images=cartItemData.images 
                    :num="imgNumber"
                    :alt="cartItemData.name + ' №' + Number(imgNumber + 1) + ' - cabel-torg'"
                  />
                  </div>
                  <div class="product__swaper-img">
                    <!-- <ClientOnly> -->
                      <SliderCardImage 
                        :allImages = cartItemData.images
                        :altName = cartItemData.name
                        @changeSliderTo = "changeNumber"
                      />
                    <!-- </ClientOnly> -->
                  </div>

                </div>
                <div class="product__info">
                    <h1 class="desc-product__title"> {{ cartItemData.name }}</h1>
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
                              <span v-if="!cartItemData.is_price_on_request && cartItemData.price_with_discount_and_tax && cartItemData.price_with_tax !== cartItemData.price_with_discount_and_tax"
                                    class="old_price"
                              >{{ cartItemData.price_with_tax }}
                              </span>
                              <span v-if="!cartItemData.is_price_on_request"
                                  :class="[cartItemData.price_with_discount_and_tax && cartItemData.price_with_discount_and_tax !== cartItemData.price_with_tax ? 'price_w_discount' : '']">
                                  {{ cartItemData.price_with_discount_and_tax && cartItemData.price_with_discount_and_tax !== cartItemData.price_with_tax
                                    ? cartItemData.price_with_discount_and_tax
                                    : cartItemData.price_with_tax
                                  }}
                              </span>
                              <span v-if="cartItemData.is_price_on_request">Цена по запросу</span>
                              <span class="current_price_item" v-if="!cartItemData.is_price_on_request">BYN/{{ cartItemData.base_unit.full_name }}</span>
                            </div>
                        </div>
                        <div class="price__right">
                            <div class="retail_price">
                              <div>Первоначальная цена: </div>
                              <div v-if="!cartItemData.is_price_on_request">
                                  <span class="price__value"> {{ cartItemData.price_with_tax }}</span>
                                  <span>BYN/{{ cartItemData.base_unit.full_name }}</span>
                              </div>
                              <div v-if="cartItemData.is_price_on_request">
                                  <span class="price__value"> Цена по запросу</span>
                              </div>
                            </div>
                            <div class="opt_price">
                                <div>Цена со скидкой: </div>
                                <div v-if="!cartItemData.is_price_on_request">
                                    <span class="price__value">
                                      {{ cartItemData.price_with_discount_and_tax && cartItemData.price_with_discount_and_tax !== cartItemData.price_with_tax
                                        ? cartItemData.price_with_discount_and_tax
                                        : cartItemData.price_with_tax
                                      }}
                                    </span>
                                    <span>BYN/{{ cartItemData.base_unit.full_name }}</span>
                                </div>
                                <div v-if="cartItemData.is_price_on_request">
                                    <span class="price__value">Цена по запросу</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="product__label">*Все цены указаны с учетом НДС.</div>
                    <div class="product__button flex-center">
                        <div v-if="!cartItemData.is_price_on_request && quantity !== 0" class="btn empty_black" @click.stop="onOperationWithCartItem(cartItemData, 'set')">В корзине</div>
                        <div v-if="!cartItemData.is_price_on_request && quantity === 0 && cartItemData.status !== 'O'" class="btn black" @click.stop="onOperationWithCartItem(cartItemData, 'set')">В корзину</div>
                        <div v-if="!cartItemData.is_price_on_request && quantity === 0 && cartItemData.status === 'O'" class="btn empty_black popup-btn" @click.stop="onCreatePopUp(true, cartItemData.id)">Узнать о поступлении</div>
                        <div v-if="cartItemData.is_price_on_request" class="btn empty_black popup-btn" @click.stop="onCreatePopUpRequestPrice(true, cartItemData.id)">Запросить цену</div>
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
    <div v-if="cartItemData && cartItemId" class="tab__description _container">
      <div class="tab ">
          <button :class="[infoBlock === 0 ? 'tablinks active' : 'tablinks']" @click="onChangeInfoBlock(0)">Описание</button>
          <button :class="[infoBlock === 1 ? 'tablinks active' : 'tablinks']" @click="onChangeInfoBlock(1)">Характеристики</button>
          <button :class="[infoBlock === 2 ? 'tablinks active' : 'tablinks']" @click="onChangeInfoBlock(2)">Документация</button>
      </div>
      <div v-if="infoBlock === 0" class="tabcontent">
          <p v-html = "rebuildText(cartItemData.description)"></p>
      </div>
      <div v-if="infoBlock === 1" class="tabcontent">
          <div class="tabcontent__row table__items"
            v-for = "option in cartItemData.attributes"
            :key = option.id
          >
            <div class="table__item" v-if = "option?.name?.payload !== 'Товар под заказ'">
              <span>{{ option?.name?.payload }}</span>
              <span>{{ option?.value?.payload }}</span>
            </div>
          </div>
      </div>
      <div v-if="infoBlock === 2" class="tabcontent">

          <a v-if="cartItemData.document_url" class="table__link" @click="onOpenDocumentation">
            <img src="@/assets/dok-ikon.png" alt="document">
            Документ</a>
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
    <SliderRecomendation
      :isShowFilter = false
      :isShowFollow = false
    />
    <ClientOnly>
      <SliderShownCards/>
    </ClientOnly>
  </div>
</template>

<script setup>
  import { useCatalogStore } from '@/stores/catalog';
  import { useNotificationsStore } from '@/stores/notifications';
  import { useQueryStore } from '@/stores/query';
  import { useHeaderStore } from '@/stores/header';
  import { useBreadCrumbStore } from '@/stores/breadcrumb';
  import { useFavoritesStore } from '@/stores/favorites';
  import { useOrdersStore } from '@/stores/orders';

  const route = useRoute();
  const router = useRouter();
  const config = useRuntimeConfig();

  const catalogStore = useCatalogStore();
  const notificationsStore = useNotificationsStore();
  const queryStore = useQueryStore();
  const headerStore = useHeaderStore();
  const breadCrumbStore = useBreadCrumbStore();
  const favoritesStore = useFavoritesStore();
  const oredersStore = useOrdersStore();

  const { cartItemId, cartItemData } = storeToRefs(catalogStore);
  const { categories } = storeToRefs(headerStore);
  const { favorites } = storeToRefs(favoritesStore);
  const { orders } = storeToRefs(oredersStore);

  const isWish = ref(false);
  const quantity = ref(0);
  const quantityLocal = ref(1);
  const infoBlock = ref(0);
  const imgNumber = ref(0);

  watch (orders, () => {
    countQuantity();
    checkIsWish();
  });

  watch (favorites, () => {
    countQuantity();
    checkIsWish();
  });

  const createCanonicalLink = computed(() => {
    return config.public.NUXT_APP_DOCUMENTS.slice(0, -1) + '/card_product/' + route.params.id
  });
  
  const rebuildText = (text) => {
    let newText = ''
    if (text) newText = text.replace('<br>', '&nbsp')
    return newText
  }

  const changeNumber = (newItem) => {
    imgNumber.value = newItem
  }

  const checkQuantityLocal = () => {
    if (quantityLocal.value < 1) {
      quantityLocal.value = 1
    };
    if (quantityLocal.value > 99) {
      quantityLocal.value = 99
    }
  }

  const minusQuantityLocal = () => {
    quantityLocal.value = quantityLocal.value > 1 ? quantityLocal.value - 1 : 1
  }

  const plusQuantityLocal = () => {
    quantityLocal.value = quantityLocal.value < 99 ? quantityLocal.value + 1 : 99
  }

  const onOperationWithCartItem = async (card, type) => {
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
      itemData.amount = Number(quantityLocal.value);
    }

    await oredersStore.updateItemsInCart({ itemData, type });
    if (quantityLocal.value === 0) quantityLocal.value = 1
  }

  const onCreatePopUp = (status, cardID) => {
    headerStore.setIsPopUpOpen(status);
    headerStore.setPopUpAction('RequestCall');
    headerStore.setRequestCallType('GR');
    headerStore.setPopUpAdditionalData({cardID});
  }

  const onCreatePopUpRequestPrice = (status, cardID) => {
    headerStore.setIsPopUpOpen(status);
    headerStore.setPopUpAction('RequestPrice');
    headerStore.setRequestCallType('GR');
    headerStore.setPopUpAdditionalData({cardID});
  }

  const onWishClick = async () => {
    const itemData = {
      product: {
        id: cartItemData.value.id,
        vendor_code: cartItemData.value.vendor_code,
        name: cartItemData.value.name,
      },
    }  
    const type = isWish.value === false ? 'set' : 'remove';

    await favoritesStore.updateIsWishInCart({ itemData, type });
    checkIsWish()
  }

  const countQuantity = () => {
    if (orders.value.length) {
      const filtered = orders.value.filter(item => String(item.product.vendor_code) === String(cartItemId.value))
      quantity.value =  filtered.length ? filtered[0].amount : 0
    } else {
      quantity.value = 0
    }
    quantityLocal.value = quantity.value ? quantity.value : quantityLocal.value
  }

  const checkIsWish = () => {
    if (favorites.value.length) {
      const filtered = favorites.value.filter(item => String(item.product.vendor_code) === String(cartItemId.value))
      isWish.value =  filtered.length ? true : false
    } else {
      isWish.value = false
    }
  }

  const onChangeInfoBlock = (num) => {
    infoBlock.value = num
    // console.log(cartItemData.value.document_url);
  }

  const onOpenDocumentation = () => {
    // console.log(cartItemData.value.document_url)
    if (cartItemData.value.document_url) {
      const _url = useRuntimeConfig().public.NUXT_APP_DOCUMENTS + cartItemData.value.document_url
      // console.log(useRuntimeConfig().public, _url);
      window.open(_url, '_blank');
    } 
  }

  const updateShowItems = (id) => {
    if (!id && cartItemData.value) return
    let itemsInLocalStorage = []
    const isItemsFromLocalStore = localStorage.getItem('shownCards')
    if (isItemsFromLocalStore) itemsInLocalStorage = JSON.parse(isItemsFromLocalStore)
    if (!itemsInLocalStorage.length) {
      itemsInLocalStorage.push({id, time: new Date().getTime()})
    } else {
      const filtered = itemsInLocalStorage.filter(item => item.id !== id)
      filtered.push({id, time: new Date().getTime()})
      const sorted = filtered.sort((a,b) => b.time - a.time)
      itemsInLocalStorage = [...sorted]
    }
    localStorage.setItem("shownCards", JSON.stringify(itemsInLocalStorage))
    catalogStore.setShownItemsList(itemsInLocalStorage)
  }

  const onGetCartData = async () => {
    queryStore.setSearchString('');
    // console.log('cartItemId: ', cartItemId.value);
    
    await catalogStore.getCartItemData(cartItemId.value);
    if (cartItemData.value) {
      if (typeof window !== 'undefined') updateShowItems(cartItemId.value)
      countQuantity()
      checkIsWish()
      breadCrumbStore.changeBreadCrumb(0);
      setBreabcrumbs();
    }
  }

  const setBreabcrumbs = async () => {
      breadCrumbStore.changeBreadCrumb(0);
      const mainBreadCrumb = {
      name: 'Каталог',
      path: '/catalog',
      type: 'global',
      class: '',
      category: 1,
      level: 'root',
    }
    breadCrumbStore.addBreadCrumb(mainBreadCrumb)
    // console.log(cartItemData.value.category);
    const chein = []
    const category = cartItemData.value.category
    chein.push(category)
    if (!categories.value.length) {
      await headerStore.getCategories();
    }
    if (category.parent_category_id) {
      const category1 = categories.value.filter(item => item.id === category.parent_category_id)[0]
      chein.push(category1)
      if (category1.parent_category_id) {
        const category2 = categories.value.filter(item => item.id === category1.parent_category_id )[0]
        chein.push(category2)
      }
    }

    const level = ['last', 'sub', 'top']

    for (let i = 0; i < chein.length; i++) {
      const currBreadCrumb  = {
        name: chein[chein.length - 1 - i].name,
        path: '/category/' + chein[chein.length - 1 - i].site_link,
        type: 'global',
        class: '',
        category: chein[chein.length - 1 - i].id,
        level: level[chein.length - 1 - i],
      }
      breadCrumbStore.addBreadCrumb(currBreadCrumb)
    }

    breadCrumbStore.addBreadCrumb({
      name: cartItemData.value.name,
      path: router.currentRoute.value.path,
      type: "global",
      class: ""
    })
    
  }

  const redirectToNotFound = async () => {
    // console.log('Redirecting from card_product...');
    if (process.server) {
      // console.log('From server');
      await router.push('/404', { redirectCode: 404 });
    } else {
      // console.log('From client');
      await navigateTo('/404', { redirectCode: 404 });
    }
  }
  
  await useAsyncData(
    async () => {
      // console.log('Starting get data for: ', route.fullPath);
      
      catalogStore.setCartItemId(route.params.id);
      if (cartItemId.value) {
        await onGetCartData();
        if (!cartItemData.value) {
          await redirectToNotFound();
        }
      } else {
        await redirectToNotFound();
      }
      return cartItemData.value;
    }, {
      watch: [route]
    }
  );

  useHead({
    title: cartItemData?.value?.name + ' купить в Минске, цена',
    meta: [
      { name: 'description', content: 'Предлагаем купить ' + cartItemData?.value?.name + ' в Минске по доступным ценам. Доставка по РБ, большой выбор.' },
    ],
    link: [
      { rel: 'canonical', href: createCanonicalLink.value },
    ],
  });
</script>

<style scoped lang="scss">

.product {

  &__body{
    .if_status_on_the_way{
      font-size: 12px;
      margin-left: 25px;
      @media (max-width: $md2+px) {
        font-size: 11px;
        margin:0 0 10px 0;
      }
    }
  }
  &__box{
    display: flex;
    margin-bottom: 40px;
    @media (max-width: $md2+px) {
      flex-direction: column;
      font-size: 11px;
      margin-bottom: 10px;
    }

  }
  &__main-img{
    // flex-basis: 40%;
    max-width: 40%;
    text-align: center;
    width:100%;
    display: flex;
    flex-direction: column;
    height: 480px;
    @media (max-width: $md2+px) {
      max-width: 100%;
    }
    &--container{
      flex:1;
      display: flex;
      height: calc(100% - 100px);
      justify-content: center;

    }
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
  &__swaper-img{
    flex:0
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
        font-size: 10px;
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
    @media (max-width: $md2+px) {
      flex-direction: column-reverse;
      align-items: stretch;
      padding: 22px 0 0 0;
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
    text-align: center;
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
    @media (max-width: $md3+px) {
      font-size: 13px;
    }
  }
  span{
    margin-right: 5px;
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
    @media (max-width: $md2+px) {
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
    .table__link{
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 10px;

    }
    &__row{
      border: 1px solid #eee;
      .table__item{
        display: flex;
        flex-direction: row;
        flex-wrap: nowrap;
        justify-content: space-between;
        padding: 7px 10px;
        span{
          &:nth-child(2){
            text-align: right;
          }
        }
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

.price_w_discount{
  color: #E30044;
  .old_price{
    color: #B3B2B6;
    @media (max-width: $md3+px) {
      font-size: 13px;
    }
  }
  .current_price_item{
    color: #B3B2B6;

  }
}

</style>

