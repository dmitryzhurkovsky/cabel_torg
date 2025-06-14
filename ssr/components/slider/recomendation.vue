<template>
  <div class="recomendation">
    <div class="recomendation__wrapper">
      <div class="recomendation__content _container">
        <div class="recomendation__body">

          <div class="recomendation__section_title section_title">Рекомендации для вас</div>
          <div class="recomendation__nav" v-if="isShowFilter">
            <div 
              :class="[activePiont === 0 ? 'recomendation__nav__item active' : 'recomendation__nav__item']" 
              @click="setTypeAndOrder({ type: 'popular', order: 'discount', typeRecomendation : 0 }, '-')"
            >
              Топ продаж
            </div>
            <div 
              :class="[activePiont === 1 ? 'recomendation__nav__item active' : 'recomendation__nav__item']" 
              @click="setTypeAndOrder({ type: 'new', order: 'created_at', typeRecomendation : 1 }, '-')"
            >
              Новинки
            </div>
            <div 
              :class="[activePiont === 2 ? 'recomendation__nav__item active' : 'recomendation__nav__item']" 
              @click="setTypeAndOrder({ type: 'with_discount', order: 'discount', typeRecomendation : 2 }, '')"
            >
              Скидки
            </div>
          </div>
          <div class="recomendation__block" v-if="recomendedList?.length">
              <swiper
                  :slides-per-view="slidersInFrame"
                  :space-between="15"
                  :speed="500"
                  :autoplay="{
                    delay: 5000,
                  }"
                  :pagination= "{
                    el: '.swiper-pagination',
                    clickable: true,
                    type: 'bullets',
                    bulletClass: 'swiper-pagination-bullet',
                    bulletElement: 'span'
                  }"
              >

                <swiper-slide v-for="item in recomendedList" :key="item.id">
                  <CatalogCardItem
                      :card = "item"
                  />
                </swiper-slide>

                <div class="swiper-pagination"></div>

                <div class="swiper-navigation-container"></div>

              </swiper>
              <div v-if="isShowFollow" class="recomendation__link  _link" @click="onOpenCatalog">Смотреть все
                <svg width="16" height="8" viewBox="0 0 16 8" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M0.5 3.99935H15.0833M15.0833 3.99935L11.75 0.666016M15.0833 3.99935L11.75 7.33268" stroke="#4275D8"/>
                </svg>
              </div>

          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, computed, watch, onBeforeMount } from 'vue';

  import { useHeaderStore } from '@/stores/header';
  import { useQueryStore } from '@/stores/query';
  import { useCatalogStore } from '@/stores/catalog';

  import { Swiper } from "swiper/vue";
  import { SwiperSlide } from "swiper/vue";
  import SwiperCore, { Pagination, Navigation } from "swiper";
  import "swiper/swiper.min.css";
  import "swiper/components/pagination/pagination.min.css"

  SwiperCore.use([Navigation, Pagination]);

  const props = defineProps({
    isShowFilter:  { type: Boolean,  default: true},
    isShowFollow:  { type: Boolean,  default: true},
  });

  const router = useRouter();
  const headerStore = useHeaderStore();
  const queryStore = useQueryStore();
  const catalogStore = useCatalogStore();

  const slidersInFrame = ref(4.5);
  const activePiont = ref(1);

  const { windowWidth } = storeToRefs(headerStore);
  const { typeOfProduct, sortType, sortDirection } = storeToRefs(queryStore);
  const { recomendedList, recomendationType, recomendationOrder } = storeToRefs(catalogStore);

  const ChangeParameters = computed(() => {
    return String(recomendationType.value) + String(recomendationOrder.value);
  });

  watch(windowWidth, () => {
    setSlidersInFrame();
  });

  watch(slidersInFrame, async () => {
    await catalogStore.getRecomendedItems();
    setNewQuantity();
    if (router.currentRoute._value.path !== '/') setTimeout(() => window.scrollTo(0, 0), 0);
  });

  watch(ChangeParameters, async () => {
    catalogStore.setRecomendationQuantity(10);
    await catalogStore.getRecomendedItems();
    setNewQuantity();
    if (router.currentRoute._value.path !== '/') setTimeout(() => window.scrollTo(0, 0), 0);
  });

  const setNewQuantity = () => {
    const newQuantity = recomendedList.value.length > 9 ? 10 : recomendedList.value.length;
    catalogStore.setRecomendationQuantity(newQuantity);
  };

  const setSlidersInFrame = () => {
    if (windowWidth.value > 768.5) {
      slidersInFrame.value = 4.5;
    } else if (windowWidth.value > 540.5) {
      slidersInFrame.value = 3.5;
    } else if (windowWidth.value > 480.5) {
      slidersInFrame.value = 2.5;
    } else {
      slidersInFrame.value = 1.5;
    }
  };

  const setTypeAndOrder = (params, sort) => {
    console.log(' setTypeAndOrder ', params, '  ', sort);
    queryStore.setSortDirection(sort);
    catalogStore.setRecomendationOrder(params.order);
    catalogStore.setRecomendationType(params.type);
    activePiont.value = params.typeRecomendation;
  };

  const onOpenCatalog = () => {
    let name = 'Все товары';
    if (recomendationType.value === 'with_discount') name = 'Акции';
    if (recomendationType.value === 'available') {
      queryStore.setSortType('created_at');
      queryStore.setSortDirection('-');
      name = 'В наличии';
    }
    if (recomendationType.value === 'popular') {
      queryStore.setSortType('discount');
      queryStore.setSortDirection('-');
      name = 'Топ продаж';
    }
    queryStore.setTypeOfProduct(recomendationType.value);
    router.push('/catalog?offset=0&limit=12&type_of_product=' + typeOfProduct.value + '&ordering=' + sortDirection.value + sortType.value);
  };


  onBeforeMount( async () => {
    await catalogStore.getRecomendedItems();
    setNewQuantity();
    setSlidersInFrame();
    setTimeout(() => window.scrollTo(0, 0), 0);
  });
</script>

<style scoped lang="scss">

.swiper-pagination, .swiper-pagination-clickable, .swiper-pagination-bullets, .swiper-pagination-horizontal {
  // position: unset;
  // margin-bottom: 3%;
  display: flex;
  position: inherit;
  width: 100%;
  align-items: center;
  justify-content: center;
  gap: 10px;
  margin-top: 20px;

  span {
    //background: #7700AF;
    background:red;
  }
}
.swiper-pagination-bullet, .swiper-pagination-bullet-active{
  background: black!important

}

:root {
  --swiper-theme-color: red!important;
}



.swiper-navigation-container{
  position: relative;
  margin: 0 auto;
  width: 20%;
  height: 50px;
}
.swiper-button-next, .swiper-button-prev{
  top: -3px;

}
.swiper-button-prev::after, .swiper-button-next::after{
  content: "\e90e";
  font-family: icomoon;
  font-size: 12px;
  color: #423E48;;
}
.swiper-button-prev::after{
  transform: rotate(180deg);
}
.active{
  color:#4275D8;
  border: 2px solid #4275D8!important;;
  font-weight: 500!important;;
  opacity: 1!important;
}

.recomendation {
  margin-top: 30px;
  position: relative;

  .section_title{
    margin-bottom: 20px;
  }

  &__link{
    position: absolute;
    right: 0;
    bottom: 53px;
    cursor: pointer;
    z-index: 20;
    font-size: 14px;
    @media (max-width: $md2+px) {
      right: auto;
      left: 256px;
      top: -110px;
      bottom: auto;
    }
  }

  &__block{
    position: relative;
    &__item{
      width: 100%;
      max-width: 272px;
      margin: 0 auto;


    }

    //@media (max-width: $md3+px) {
    //  display: flex;
    //  flex-direction: column;
    //  align-items: center;
    //  gap: 20px;
    //}

  }
  &__nav{
    display: grid;
    gap: 10px;
    grid-template-columns: repeat(3, minmax(0, 170px));
    /*
    if we did this instead of the template it would be a problem:
    grid-auto-flow: column;
    */
    text-align: center;
    padding: 24px 20px 20px 0;
    @media (max-width: $md2+px) {
      gap: 8px;
    }

    &__item{

      background: #FFFFFF;
      border: 2px solid #EEEEEE;
      border-radius: 50px;
      font-size: 14px;
      font-weight: 500;
      line-height: 24px;
      text-align: center;
      opacity: 0.5;
      padding: 6px 20px;
      cursor: pointer;
      transition: all 0.3s ease;
      @media (max-width: $md2+px) {
        font-size: 10px;
        line-height: 12px;
        padding: 6px 15px;
      }

      &:hover{
        color:#4275D8;
        //border: 2px solid #4275D8;
        font-weight: 500;
        opacity: 0.8;
      }

    }
    &__link{
      position: absolute;
      right: 0;
      bottom: 0;
    }
  }

}

</style>

<style lang="scss">

.recomendation__block__item{
  .item-card__uptitle div{
    //width: 200px;
    overflow:hidden;
    white-space:nowrap;
    text-overflow: ellipsis;
  }

}
.recomendation__nav__item{
  white-space: nowrap;
}
</style>