<script setup lang='ts'>
  import { computed, onMounted, ref, watch } from 'vue'
  import { useStore } from '../store'
  import { ActionTypes } from '../store/action-types'
  import { MutationTypes } from '../store/mutation-types'
  import { IDeliveryType } from '../types'
  import Input from '@/components/UI/Input.vue'
  import Button from '@/components/UI/Button.vue'
  import Select from '@/components/UI/Select.vue'
  import { helpers, required, between } from '@vuelidate/validators'
  import { useVuelidate } from '@vuelidate/core'
  import Img from '@/components/UI/Img.vue'

  const store = useStore()
  const categories = ref([] as Array<IDeliveryType>)
  const activeCategory = ref()
  const categoryDiscount= ref()
  const goods = ref()
  const activeGood = ref()
  const goodDiscount =ref()

  const itemsInPageArray = [
    {id: 10, name: '10'},
    {id: 20, name: '20'},
    {id: 50, name: '50'},
  ]

  watch(() => store.getters.categories,
    (curr, prev) => {

      let menuItems = []
      const mainLevel = curr.filter(item => item.parent_category_id === null)
      let otherItems = curr.filter(item => item.parent_category_id !== null)
      menuItems = [...mainLevel]
      menuItems.forEach(item => {
        item.selected = false
        item.filterPanel = false
        item.childrens = []
      });
      menuItems.forEach(mainItem => {
        const mainItemChildrens = otherItems.filter( item => item.parent_category_id === mainItem.id)
        otherItems = otherItems.filter(item => item.parent_category_id !== mainItem.id)
        mainItemChildrens.forEach(item => {
          item.selected = false
          item.filterPanel = false
          item.childrens = []
        });
        mainItemChildrens.forEach(middleItem => {
          const lastChildrens = otherItems.filter( item => item.parent_category_id === middleItem.id)
          otherItems = otherItems.filter(item => item.parent_category_id !== middleItem.id)
          lastChildrens.forEach(item => {
            item.selected = false
            item.filterPanel = false
            item.childrens = []
          });
          middleItem.childrens = [...lastChildrens]
        })
        mainItem.childrens = [...mainItemChildrens]
      });

      categories.value = [...menuItems]
      store.commit(MutationTypes.SET_IS_LOADING, false)
  })

  watch(() => store.getters.goods,
    (curr, prev) => {
      goods.value = [...curr]
      goods.value.sort((a: IDeliveryType, b: IDeliveryType) => a.id - b.id)
      store.commit(MutationTypes.SET_IS_LOADING, false)
   });

  watch(() => JSON.stringify(activeCategory.value),
    (curr, prev) => {
      if (curr !== prev) {
        onChangePageNumber(1)
        sendGoodsRequest()
      }
  });
  
  const sendCategoryRequest = async () => {
    await store.dispatch(ActionTypes.GET_CATEGORIES_DATA, null)
  };

  const sendGoodsRequest = async () => {
    store.commit(MutationTypes.SET_IS_LOADING, true)
    await store.dispatch(ActionTypes.GET_PRODUCTS_DATA, activeCategory.value)
    store.commit(MutationTypes.SET_IS_LOADING, false)
  };

  const rulesCategories = computed(() => ({
    categoryDiscount: {
      requered: helpers.withMessage(`Обязательно`, required),
      between: helpers.withMessage(`0 - 100`, between(0, 100)),
    },
  }))

  const rulesGoods = computed(() => ({
    goodDiscount: {
      requered:  helpers.withMessage(`Обязательно`, required),
      between: helpers.withMessage(`0 - 100`, between(0, 100)),
    },
  }))

  const vCat = useVuelidate(rulesCategories, {categoryDiscount});
  const vGood = useVuelidate(rulesGoods, {goodDiscount});

  onMounted(async () => {
    store.commit(MutationTypes.SET_IS_LOADING, true)
    await sendCategoryRequest()
  })

  const openCategory = (mainItem: IDeliveryType) => {
    activeCategory.value = mainItem
  }

  const toggleCategory = (menuItem: IDeliveryType) => {
    menuItem.filterPanel = !menuItem.filterPanel
  }

  const onSetDiscountForCategory = async () => {
    vCat.value.$touch()
    if (vCat.value.$error) return
    await store.dispatch(ActionTypes.EDIT_CATEGORY_DISCOUNT, {category: activeCategory.value, discount: Number(categoryDiscount.value)})
  }

  const onSetAciveGood = (card: IDeliveryType) => {
    activeGood.value = card
  }

  const onSetDiscountForGood = async () => {
    vGood.value.$touch()
    if (vGood.value.$error) return
    await store.dispatch(ActionTypes.EDIT_PRODUCT_DISCOUNT, {product: activeGood.value, discount: Number(goodDiscount.value)})
  }

  const cardPriceWithDiscount = (card: IDeliveryType) => {
    return card.price_with_discount_and_tax && card.price_with_discount_and_tax !== card.price_with_tax 
      ? card.price_with_discount_and_tax 
      : card.price_with_tax
  }

  const cardDiscount = (card: IDeliveryType) => {
    return card.actual_discount ? String(card.actual_discount) : '-'
  }

  const cardSyles = (card: IDeliveryType) => {
    let style = 'product '
    if (card.actual_discount) style = style + 'active'
    if (activeGood.value) {
      if (card.id === activeGood.value.id) style = 'product selected'
    }
    return style
  }

  const onChangePageNumber = (page: number) => {
    if (page === 0) return
    if (page > store.getters.totalPages) return
    store.commit(MutationTypes.SET_ACTIVE_PAGE, page)
    const offSet = store.getters.itemsInPage * (store.getters.activePage - 1)
    store.commit(MutationTypes.SET_PRODUCTS_OFSET, offSet)
    sendGoodsRequest()
  }

  const onChangeItemsInPage = async (itemsInPage: number) => {
    store.commit(MutationTypes.SET_ACTIVE_PAGE, 1)
    store.commit(MutationTypes.SET_ITEMS_IN_PAGE, itemsInPage) 
    store.commit(MutationTypes.SET_PRODUCTS_OFSET, 0)
    sendGoodsRequest()
  }
</script>

<template>
  <div class="discount-container">
    <div class="filter__block" v-if="categories.length">
        <div class="filter__discount" v-if="activeCategory">
          <div class="filter__attention flex-center">
              <div class="icon">
                  <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M9 7H11V5H9V7ZM9 15H11V9H9V15ZM9.99 20C4.47 20 0 15.52 0 10C0 4.48 4.47 0 9.99 0C15.52 0 20 4.48 20 10C20 15.52 15.52 20 9.99 20ZM10 2C5.58 2 2 5.58 2 10C2 14.42 5.58 18 10 18C14.42 18 18 14.42 18 10C18 5.58 14.42 2 10 2Z" fill="#423E48"/>
                  </svg>
              </div>
              <div class="attention__text">
                  <p>Ниже устанавливается скидка для целого раздела либо подраздела. Достаточно ввести размер дисконта и нажать "Установить", как все товары указанной категории получат установленную скидку</p>
              </div>


          </div>
          <form class="filter__setup_discount" @submit.prevent="onSetDiscountForCategory">
              <div class="filter__dbox" style="">{{ activeCategory.name }}</div>
              <div class="filter__dbox">
                  <Input
                          name="categoryDiscount"
                          width="100px"
                          v-model:value="vCat.categoryDiscount.$model"
                          :error="vCat.categoryDiscount.$errors"
                  />
              </div>
              <div class="filter__dbox" style="">
                  <Button label="Установить" color="primary"></Button>
              </div>
          </form>

        </div>
        <br>
        <div class="filter__box" 
            v-for   = "mainItem in categories"
            :key    = "mainItem.id"
        >
            <div class="sidebar_menu__title">
              <div :class = "{'active' : mainItem.filterPanel||mainItem === activeCategory}"
                  @click.stop = "openCategory(mainItem)"
              >
                {{mainItem.name}}
              </div>
              <div v-if="mainItem.childrens.length"
                  :class="[ mainItem.filterPanel ? 'sidebar_menu__open  icon-arrow-up' : 'sidebar_menu__close icon-arrow-down']"
                  @click.stop = "toggleCategory(mainItem)"
              >
                  <svg width="10" height="7" viewBox="0 0 10 7" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M4.7 6.1L0 1.4L1.4 0L4.7 3.3L8 0L9.4 1.4L4.7 6.1Z" fill="#423E48"/>
                  </svg>

              </div>
            </div >

            <div class="filter__block"  v-if = "mainItem.childrens.length && mainItem.filterPanel">

                    <div class="sidebar_menu__subtitle"
                        v-for   = "middleItem in mainItem.childrens"
                        :key    = "middleItem.id"
                    >
                      <div class="subtitle__row">
                        <div :class = "{'active' : middleItem.filterPanel||middleItem === activeCategory}"
                            @click.stop  = "openCategory(middleItem)"
                        >
                          {{middleItem.name}}
                        </div>
                        <div v-if="middleItem.childrens.length"
                            :class="[ middleItem.filterPanel ? 'sidebar_menu__open icon-arrow-up' : 'sidebar_menu__close icon-arrow-down']"
                            @click.stop = "toggleCategory(middleItem)"
                        >
                            <svg width="10" height="7" viewBox="0 0 10 7" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M4.7 6.1L0 1.4L1.4 0L4.7 3.3L8 0L9.4 1.4L4.7 6.1Z" fill="#423E48"/>
                            </svg>
                        </div>
                      </div>


                    <div class="subtitle__list "  v-if = "middleItem.childrens.length &&  middleItem.filterPanel">
                        <div class="sidebar_menu__subtitle-child"
                            v-for = "lastItem in middleItem.childrens"
                            :key  = "lastItem.id"
                            @click.stop = "openCategory(lastItem)"
                        >
                            <div class="">
                              <div :class = "{'active' : lastItem.filterPanel||lastItem === activeCategory}">
                                {{lastItem.name}}
                              </div>

                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="goods__block">
      <div class="filter__discount" v-if="activeGood">
          <div class="filter__attention flex-center">
              <div class="icon">
                  <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M9 7H11V5H9V7ZM9 15H11V9H9V15ZM9.99 20C4.47 20 0 15.52 0 10C0 4.48 4.47 0 9.99 0C15.52 0 20 4.48 20 10C20 15.52 15.52 20 9.99 20ZM10 2C5.58 2 2 5.58 2 10C2 14.42 5.58 18 10 18C14.42 18 18 14.42 18 10C18 5.58 14.42 2 10 2Z" fill="#423E48"/>
                  </svg>
              </div>
              <div class="attention__text">
                  <p>Для установки скидки на отдельный товар достаточно выбрать товар снизу и ввести необходимый размер ссылки</p>
                  <p>Обращаем внимание, что <b>приоритетной</b> является всегда скидка на единичный товар, и изменение скидки на (под)категорию не влечет изменение скидки на товар с уже установленной скидкой</p>
              </div>
          </div>
          <form class="filter__setup_discount" @submit.prevent="onSetDiscountForGood">
              <div class="filter__dbox" style="">{{ activeGood.name }}</div>
              <div class="filter__dbox">
                  <Input
                          name="goodDiscount"
                          width="100px"
                          v-model:value="vGood.goodDiscount.$model"
                          :error="vGood.goodDiscount.$errors"
                  />
              </div>
              <div class="filter__dbox" style="">
                  <Button label="Установить" color="primary"></Button>
                  <!-- <Button label="Установить" color="primary" @click="onSetDiscountForGood()"></Button> -->
              </div>
          </form>

        </div>
        <br>
        <div class="content-block__list">
          <div class="table-pagination" v-if = "goods">
              <div
                  :class="[store.getters.activePage > 1 ? 'pagination-item active' : 'pagination-item']"
                  @click="onChangePageNumber(store.getters.activePage - 1)"
              >{{ '<' }}</div>
              <div class="pagination-item news__pagenumber">{{ store.getters.activePage }}</div>
              <span>{{ '/' }}</span>
              <div class="pagination-item news__pagenumber">{{ store.getters.totalPages }}</div>
              <div 
                  :class="[store.getters.activePage < store.getters.totalPages ? 'pagination-item active' : 'pagination-item']"
                  @click="onChangePageNumber(store.getters.activePage + 1)"
              >{{ '>' }}</div>
              <div class="pagination-selector">
                <Select
                  text = "10"
                  :id   = String(store.getters.activePage)
                  fieldForSearch = "name"
                  :data = "itemsInPageArray"
                  @onSelectItem="onChangeItemsInPage"
                />
              </div>
          </div>
          <div class="content-block__item product-row" v-if = "goods">
            <div :class = cardSyles(card)
              v-for   = "card in goods"
              :key    = "card.id"
              @click = "onSetAciveGood(card)"
            >
                <a class="product__img">
                    <Img :image=card.images />
                </a>
                <div class="product__action">
                    <div class="product__article  _label mb-20"><span>{{ card.vendor_code }}</span></div>
                    <div class="product__col current_price">
                        <span class="_label">Цена, BYN / {{ card.base_unit.full_name }}</span>
                        {{ card.price_with_tax }}
                    </div>
                    <div class="product__col discount_price">
                        <span class="_label">Цена со скидкой, BYN / {{ card.base_unit.full_name }}</span>
                        {{ cardPriceWithDiscount(card) }}
                    </div>
                    <div class="product__col product__discount" >
                        <span class="_label">Размер скидки, %</span>
                       {{ cardDiscount(card) }}
                    </div>


                 </div> <!--  product__action-->

                </div><!--  product-->
            </div>

          </div>  
        </div>
    </div>

</template>

<style lang="scss" scoped>
.discount-container{
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
}
.filter{

  &__block{
    flex-basis: 40%;
    width: 100%;
    .icon-arrow-l,
    .icon-arrow-r{
      font-weight: bold;
      margin-left: 15px;

    }

  }
  &__discount{
    display: flex;
    flex-direction: column;
    flex-wrap: nowrap;
    align-items: center;
  }
  &__attention {
    width: 100%;
    font-weight: 300;
    font-size: 14px;
    line-height: 20px;
    color: #423E48;
    opacity: 0.4;
    display: flex;
    align-items: flex-start;
    justify-content: flex-start;
    min-height: 60px;
    .icon {}
    .attention__text {
      padding-left: 20px;
      p{
        margin: 0;
      }
    }
  }
  &__setup_discount{
    display: flex;
    align-items: center;
    width: 100%;
    padding: 20px 0 0 0;

  }
  &__dbox{

    height: 100%;
    &:nth-child(1){
      flex-basis: 50%;
    }
    &:nth-child(2){
      flex-basis: 25%;
      padding: 0 10px;
      .form-input{
        margin-bottom: 0;
      }

    }
    &:nth-child(3){
      flex-basis: 25%;

    }
  }
  &__checkbox{

    &__item{
      margin: 0 15px 10px 15px;
      //height: 18px;
      input{
          position: absolute;
          opacity: 0;
          z-index: -1;
      }
    }
  }
  &__box{
    font-weight: 400;
    position: relative;
    //.icon-arrow-l:before{
    //  content: ">";
    //  transform: rotate(90deg);
    //  cursor: pointer;
    //}
    //.icon-arrow-r:before{
    //  content: ">";
    //  transform: rotate(-90deg);
    //  cursor: pointer;
    //}
  }

  &__title{
    background: #F8FAFF;
    padding: 6px 8px;
    font-weight: 500;
    font-size: 14px;
    line-height: 24px;
    color: #423E48;
    margin: 12px 0;
    &:before{
        position: absolute;
        top: 12px;
        right: 10px;
        font-size: 10px;
        //transform: rotate(-90deg);
    }
  }
  &__subtitle{
    font-size: 13px;
    padding: 5px 0 5px 20px;
    cursor: pointer;
    &-child{
    }
  }
  &__field{
    flex-direction: column;
    align-items: flex-start;
      input{
        width: 100%;
        height: 100%;
        outline: none;
        font-size: 16px;
        border-radius: 5px;
        padding: 5px 10px;
        text-align: left;
        border: 1px solid #999;
        -moz-appearance: textfield;
    }
  }
  &__text{
    span{
      font-weight: 400;
      font-size: 14px;
      color: #423E48;
    }
    .active{
      color: #423E48;
      font-weight: 500;
    }
  }
}

.sidebar_menu{
  &__title{
    display: flex;
    align-items: center;
    //justify-content: space-between;
    padding: 10px 10px 10px 0;
    line-height: 1.8;
    div:first-child {
      cursor: pointer;
    }
    .active{
      color:#4275D8;
    }

  }
  &__subtitle{
    .subtitle__row{
      div:first-child {
        cursor: pointer;
      }
      .active{
        color:#4275D8;
      }
      display: flex;
      align-items: center;
      //justify-content: space-between;
      padding: 10px 10px 10px 5px;
      font-size: 14px;
    }
    .subtitle__list{
      padding-left: 10px;
    }
    &-child{
      cursor: pointer;
      font-size: 13px;
      line-height: 1.2;
      padding: 5px 5px;
      opacity: 0.8;
      .active{
        color:#4275D8;
      }
    }
  }
}
.sidebar_menu{

  &__open {
    font-size: 12px;
    margin-left: 15px;
    transform: rotate(180deg);
    color:#4275D8;
    cursor: pointer;
    svg path{
      fill:#4275D8;
    }
    > div{
      color: red;
    }
  }
  &__close {
    font-size: 12px;
    margin-left: 15px;
    cursor: pointer;

  }
}

.content-block{
  &__item{
    display: flex;
    flex-direction: column;
    gap:16px;
  }
}
.product{

  display: flex;
  position: relative;
  background: #FFFFFF;
  border: 2px solid #EEEEEE;
  box-sizing: border-box;
  border-radius: 8px;
  padding: 10px 12px 10px 12px;
  justify-content: space-between;

  &.active{
    border:2px solid #c87878;
  }
  &.selected{
   background: #EEEEEE;
  }


  &:hover{
    cursor: pointer;
    background: #EEEEEE;
  }
  &__img {
    width: 100%;
    flex-basis: 20%;
    text-align: center;
    max-width: 120px;
    img{
        max-width: 100%;
        object-fit: fill;
    }
  }
  &__action{
    flex-basis: 80%;
    display: flex;
    align-items: center;
    width: 100%;
    justify-content: space-between;
  }
  &__col{
    display: flex;
    flex-direction: column;
    align-items: center;
    ._label{
      margin-bottom: 10px;
      font-size: 12px;
      color: #423e48;
      opacity: 0.6;
    }
  }
  &__discount{

  }

  .discount_price{
    color: red;
    font-weight: 500;
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

.table{
  &-pagination {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    padding: 20px 0;
  }
}

.pagination{
  &-selector{
    max-width: 100px;
  }
  &-pages{
    border: 1px solid var(--primary);
    padding: 10px 10px;
    height: 40px;
    border-radius: 7px;
    font-size: 15px;
    width: 100%;
    text-align: center;
  }
  &-item{
    border: 1px solid var(--primary);
    padding: 10px 10px;
    height: 40px;
    border-radius: 7px;
    font-size: 15px;
    width: 40px;
    text-align: center;
  }
}

.active {
  cursor: pointer;

}

.goods__block{
  flex-basis: 60%;
  width: 100%;

  .table-pagination{
    padding-top: 0;
    justify-content: right;

  }

}

</style>