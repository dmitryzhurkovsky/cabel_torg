<template>
  <div class="recomendation">
    <div class="recomendation__wrapper">
      <div class="recomendation__content _container">
        <div class="recomendation__body">

          <div>Просмотренные товары</div>
          <div class="recomendation__block" v-if="ItemsForSlider.length">
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
                <!-- @swiper="onSwiper"
                @slideChange="onSlideChange" -->

                <swiper-slide v-for="item in ItemsForSlider" :key="item.id">
                  <CatalogCardItem
                      :card = "item"
                  />
                </swiper-slide>

                <div class="swiper-pagination"></div>

                <!-- <div class="swiper-navigation-container">
                 <div class="swiper-button-next" @click="nextSlide"></div>
                 <div class="swiper-button-prev" @click="prevSlide"></div>
                </div> -->

              </swiper>

          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import axios from 'axios';
  import { ref, computed, watch, onBeforeMount, onMounted } from 'vue';
  import { useNotificationsStore } from '@/stores/notifications';
  import { useHeaderStore } from '@/stores/header';
  import { useCatalogStore } from '@/stores/catalog';

  import { Swiper, SwiperSlide } from "swiper/vue";
  import SwiperCore, { Pagination, Navigation } from "swiper";
  import "swiper/swiper.min.css";
  import "swiper/components/pagination/pagination.min.css";

  SwiperCore.use([Navigation, Pagination]);

  const notificationsStore = useNotificationsStore();
  const headreStore = useHeaderStore();
  const catalogStore = useCatalogStore();

  const slidersInFrame = ref(4.5);
  const sliderItems = ref([]);
  const quantity = ref(0);

  const ChangeParameters = computed(() => {
    return JSON.stringify(sliderItems.value) + String(slidersInFrame.value) + String(quantity.value);
  });

  const ItemsForSlider = computed(() => {
    const sliders = sliderItems.value.slice(0, 10);
    return sliders;
  });


  watch(() => headreStore.windowWidth, () => {
    setSlidersInFrame();
  });

  watch(() => ChangeParameters, async () => {
    getShownItems();
    setNewQuantity();
  });

  const setNewQuantity = () => {
    const newQuantity = sliderItems.value.length > 9 ? 10 : sliderItems.value.length;
    quantity.value = newQuantity;
  };

  const setSlidersInFrame = () => {
    if (headreStore.windowWidth > 768.5) {
      slidersInFrame.value = 4.5;
    } else if (headreStore.windowWidth > 540.5) {
      slidersInFrame.value = 3.5;
    } else if (headreStore.windowWidth > 480.5) {
      slidersInFrame.value = 2.5;
    } else {
      slidersInFrame.value = 1.5;
    }
  };

  // const onOpenCatalog = () => {
  //   router.push('/catalog');
  // };

  const getShownItems = async () => {
    const fetchedItems = [];
    catalogStore.shownItemslist.forEach(async item => {
      try {
        const response = await axios.get(useRuntimeConfig().public.NUXT_APP_API_URL + 'products/' + item.id);
        fetchedItems.push(response.data);
        sliderItems.value = [...fetchedItems];
      } catch (e) {
        console.log(e);
        notificationsStore.addMessage({ name: "Не возможно загрузить данные товара " + item.id, icon: "error", id: item.id });
      }
    });
    // setTimeout(() => window.scrollTo(0, 0), 0);
  };

  // const onSlideChange = () => {
  //    console.log('slide change');
  // };
  // const nextSlide = () => {
  //   swiper.slideNext();
  // };
  // const prevSlide = () => {
  //   swiper.slidePrev();
  // };

  // const onSwiper = (swiper) => {
  //   // swiper.value = swiper;
  //   console.log('swiper:  ', swiper);
  //   // console.log('swp:  ', swp);
  // };

  onBeforeMount(async () => {
    await getShownItems();
    setNewQuantity();
    setSlidersInFrame();
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
.swiper-pagination-bullet-active{
  background: red!important;
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
.recomendation {
  margin-top: 30px;
  position: relative;

  h3{
    margin-bottom: 20px;
  }

  &__link{
    position: absolute;
    right: 0;
    bottom: 43px;
    cursor: pointer;
    z-index: 90;
    @media (max-width: $md3+px) {
      display: none;
    }
  }

  &__block{
    position: relative;
    &__item{
      width: 100%;
      max-width: 272px;
      margin: 0 auto;
      max-height: 368px;


    }


  }
  &__nav{
    display: grid;
    gap: 10px;
    grid-template-columns: repeat(3, minmax(0, 170px));
    text-align: center;
    padding: 24px 20px 20px 0;
    @media (max-width: $md2+px) {
      gap: 8px;
    }

    &__item{

      background: #dedede;
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
        border: 2px solid #4275D8;
        font-weight: 500;
        opacity: 1;
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