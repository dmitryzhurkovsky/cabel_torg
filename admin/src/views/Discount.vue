<script setup lang='ts'>
  import { computed, onMounted, ref, watch } from 'vue'
  import { useStore } from '../store';
  import { ActionTypes } from '../store/action-types';
  import { MutationTypes } from '../store/mutation-types';
  import { IDeliveryType } from '../types';
  import Input from '@/components/UI/Input.vue';
  import Button from '@/components/UI/Button.vue'
  import { helpers, required } from '@vuelidate/validators';
  import { useVuelidate } from '@vuelidate/core';
  import Img from '@/components/UI/Img.vue'

  const store = useStore()
  const categories = ref([] as Array<IDeliveryType>)
  const activeCategory = ref()
  const categoryDiscount= ref()
  const goods = ref()
  const activeGood = ref()
  const goodDiscount =ref()

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
      store.commit(MutationTypes.SET_IS_LOADING, false)
   });

  watch(() => activeCategory.value,
    (curr, prev) => {
      if (curr !== prev) {
        sendGoodsRequest()
      }
  });
  
  const sendCategoryRequest = async () => {
    await store.dispatch(ActionTypes.GET_CATEGORIES_DATA, null)
  };

  const sendGoodsRequest = async () => {
    store.commit(MutationTypes.SET_IS_LOADING, true)
    await store.dispatch(ActionTypes.GET_GOODS_DATA, activeCategory.value)
    store.commit(MutationTypes.SET_IS_LOADING, false)
  };

  const rules = computed(() => ({
    categoryDiscount: {
      requered:  helpers.withMessage(`Обязательно поле`, required),
    },
    goodDiscount: {
      requered:  helpers.withMessage(`Обязательно поле`, required),
    },
  }))

  const v = useVuelidate(rules, {categoryDiscount, goodDiscount});

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

  const onSetDiscountForCategory = () => {
    console.log('Сдесь установить скидку для категории: ', categoryDiscount.value);
  }

  const onSetDiscountForGood = () => {
    console.log('Сдесь установить скидку для товара: ', categoryDiscount.value);
  }

  const CardPriceWithoutDiscount = () => {

  }

  const cardPriceWithDiscount = () => {

  }
</script>

<template>
  <div class="discount-container">
    <div class="filter__block" v-if="categories.length">
        <div class="filter__discount" v-if="activeCategory">
          <div class="filter__dbox" style="margin-bottom: 30px;">{{ activeCategory.name }}</div>
          <div class="filter__dbox">
            <Input
              name="categoryDiscount"
              width="100px"
              v-model:value="v.categoryDiscount.$model"
            />
          </div>
          <div class="filter__dbox" style="margin-bottom: 30px;">
            <Button label="Установить" color="primary" @click="onSetDiscountForCategory()"></Button>
          </div>
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
                  :class="[ mainItem.filterPanel ? 'sidebar_menu__open  icon-arrow-r' : 'sidebar_menu__close icon-arrow-l']"
                  @click.stop = "toggleCategory(mainItem)"
              >
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
                            :class="[ middleItem.filterPanel ? 'sidebar_menu__open icon-arrow-r' : 'sidebar_menu__close icon-arrow-l']"
                            @click.stop = "toggleCategory(middleItem)"
                        >
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
          <div class="filter__dbox" style="margin-bottom: 30px;">{{ activeGood.name }}</div>
          <div class="filter__dbox">
            <Input
              name="categoryDiscount"
              width="100px"
              v-model:value="v.goodDiscount.$model"
            />
          </div>
          <div class="filter__dbox" style="margin-bottom: 30px;">
            <Button label="Установить" color="primary" @click="onSetDiscountForGood()"></Button>
          </div>
        </div>
        <br>
        <div class="content-block__list">
          <div class="content-block__item product-row" v-if = "goods">
            <div class="product"
              v-for   = "card in goods"
              :key    = "card.id"
            >
                <a class="product__img">
                    <Img :image=card.images />
                </a>
                <div class="product__action">
                    <div class="product__article  _label mb-20">Артикул: <span>{{ card.vendor_code }}</span></div>
                    <div class="product__price">
                        <span  v-if = "card.price_with_discount_and_tax" class="product__oldprice">{{ CardPriceWithoutDiscount }}</span>
                        <span>{{ cardPriceWithDiscount }}</span> BYN
                        <span> / {{ card.base_unit.full_name }}</span>
                    </div>
                    <div class="notice">* Цена указана с учетом НДС.</div>
                </div>
            </div>

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
  }
  &__discount{
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    align-items: center;
  }
  &__dbox{
    flex-basis: 33%;
    height: 100%;
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
    .icon-arrow-l:before{
      content: ">";
      transform: rotate(90deg);
      cursor: pointer;
    }
    .icon-arrow-r:before{
      content: ">";
      transform: rotate(-90deg);
      cursor: pointer;
    }
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
    justify-content: space-between;
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
      justify-content: space-between;
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

  transition: all 0.3s ease;
  &__open {
    font-size: 12px;
    transform: rotate(-90deg);
    color:#4275D8;
    > div{
      color: red;
    }
  }
  &__close {
    font-size: 12px;
    transform: rotate(90deg);
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
  padding: 20px 22px 20px 22px;
  justify-content: space-between;

  // &__container {
  //   display: flex;
  //   align-items: flex-start;
  //   justify-content: space-between;
  //   padding: 24px 20px;
  //   background: #FFFFFF;
  //   border: 2px solid #EEEEEE;
  //   border-radius: 8px;
  //   margin-bottom: 16px;
  //   ._label{
  //     font-weight: 300;
  //     font-size: 12px;
  //     line-height: 20px;

  //   }
  // }

  &__img {
    width: 100%;
    flex-basis: 20%;
    text-align: center;
    img{
        max-width: 100%;
        object-fit: fill;
    }
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