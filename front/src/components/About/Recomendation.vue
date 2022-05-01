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
              <swiper class="swaper"
                  :slides-per-view="4"
                  :slider-per-group="4"
                  :space-between="30"
                  :pagination="{ clickable: true }"
                  @swiper="onSwiper"
                  @slideChange="onSlideChange"
              >
                <swiper-slide :virtualIndex = "1"><CardItem/></swiper-slide>
                <swiper-slide :virtualIndex = "2"><CardItem/></swiper-slide>
                <swiper-slide :virtualIndex = "3"><CardItem/></swiper-slide>
                <swiper-slide :virtualIndex = "4"><CardItem/></swiper-slide>
                <swiper-slide :virtualIndex = "5"><CardItem/></swiper-slide>
                <swiper-slide :virtualIndex = "6"><CardItem/></swiper-slide>
                <swiper-slide :virtualIndex = "7"><CardItem/></swiper-slide>
              </swiper>
              <div class="swiper-pagination"></div>
              <div class="swiper-button-next" @click="nextSlide"></div>
              <div class="swiper-button-prev" @click="prevSlide"></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import CardItem from '@/components/Goods/card_item.vue'

  import { Swiper, SwiperSlide } from 'swiper/vue';
  // import { Navigation, Pagination} from 'swiper';
  import 'swiper/swiper-bundle.css';

  export default {
    name: 'Recomendation',

    components:
    {
      CardItem,
       Swiper, SwiperSlide,
    },

    data: function(){
      return{
        swiper : null,
      }
    },

    methods:{
      onSlideChange() {
         console.log('slide change');
      },

      nextSlide(){
          console.log('next');
          this.swiper.slideNext();
      },

      prevSlide(){
          console.log('next');
          this.swiper.slidePrev();
      },

      onSwiper(swiper){
        this.swiper = swiper;
        this.swiper.pagination = {
          el : '.swiper-pagination',
          clickable: true,
          dynamicBullets : true,
          bulletActiveClass : '.swiper-pagination-bullet-active',
          bulletClass : '.swiper-pagination-bullet',
          type : 'bullets',
        };
        this.swiper.navigation = {
          nextEl : '.swiper-button-next',
          prevEl : '.swiper-button-prev',
        };
      },
    },

    mounted(){
      console.log();
    },

  }
</script>

<style scoped lang="scss">
.swiper-pagination{
  width: 100%;
  height: 40px;
}
.swiper-pagination-bullet{
  width: 20px;
  height: 20px;
  line-height: 20px;
  font-size: 14px;
  background-color: #ABABAB;
}

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
