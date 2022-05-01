<template>
  <div class="recomendation">
    <div class="recomendation__wrapper">
      <div class="recomendation__content _container">
        <div class="recomendation__body">

          <h3>Рекомендации для вас</h3>
          <div class="recomendation__nav flex-center">
            <div class="recomendation__nav__item">Топ продаж</div>
            <div class="recomendation__nav__item">Новинки</div>
            <div class="recomendation__nav__item">Скидки</div>
          </div>
          <div class="recomendation__block">
            <!-- <CardItem/> -->
              <swiper
                :modules="modules"
                :slides-per-view="2"
                :space-between="50"
                navigation
                :pagination="{ clickable: true }"
                :scrollbar="{ draggable: true }"
                @swiper="onSwiper"
                @slideChange="onSlideChange"              >
                <swiper-slide><CardItem/></swiper-slide>
                <swiper-slide><CardItem/></swiper-slide>
                <swiper-slide><CardItem/></swiper-slide>
              </swiper>


          </div>


        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import CardItem from '@/components/Goods/card_item.vue'

  // Import Swiper Vue.js components
  import { Swiper, SwiperSlide } from 'swiper/vue';
  import { Navigation, Pagination, Scrollbar, A11y } from 'swiper';
  // // Import Swiper styles
  import 'swiper/swiper-bundle.css';
  // import 'swiper/css/swiper.css';

  export default {
    name: 'Recomendation',

    components:
    {
      CardItem,
       Swiper, SwiperSlide,
    },

    setup() {
      const onSwiper = (swiper) => {
        console.log(swiper);
      };
      const onSlideChange = () => {
        console.log('slide change');
      };
      return {
        onSwiper,
        onSlideChange,
        modules: [Navigation, Pagination, Scrollbar, A11y],
      };
    },

  }
</script>

<style scoped lang="scss">


.recomendation {

  &__wrapper{

  }
  &__content{

  }

  &__body{
  }

  &__block{
    &__item{
      width: 100%;
      max-width: 272px;
    }

  }
  &__nav{
    padding: 10px 0;
    justify-content: flex-start;
    &__item{

      background: #FFFFFF;
      border: 1px solid rgba(0, 0, 0, 0.05);
      border-radius: 50px;
      font-size: 14px;
      line-height: 24px;
      text-align: center;
      opacity: 0.5;
      margin-right: 10px;
      padding: 6px 40px;
      cursor: pointer;
      &:hover{
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.08);
        color:#4275D8;
        font-weight: 500;
      }

    }
  }


  &__item{

  }
  &__link{

}

}
</style>
