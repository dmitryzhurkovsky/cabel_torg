<template>
  <div class="partners">
    <div class="partners__wrapper">
      <div class="partners__content _container">
        <div class="partners__body">

          <h3>Наши партнеры</h3>
          <div class="partners__items flex-center">
            <swiper
                :slides-per-view="5"
                :space-between="15"
                @swiper="onSwiper"
                @slideChange="onSlideChange"
            >

              <swiper-slide>
                <div class="parnters__item">
                  <img src="../../assets/partners/11.png" alt="partners">
                </div>
              </swiper-slide>

              <swiper-slide>
                <div class="parnters__item">
                  <img src="../../assets/partners/12.png" alt="partners">
                </div>
              </swiper-slide>

              <swiper-slide>
                <div class="parnters__item">
                  <img src="../../assets/partners/13.png" alt="partners">
                </div>
              </swiper-slide>

              <swiper-slide>
                <div class="parnters__item">
                  <img src="../../assets/partners/14.png" alt="partners">
                </div>
              </swiper-slide>

              <swiper-slide>
                <div class="parnters__item">
                  <img src="../../assets/partners/12.png" alt="partners">
                </div>
              </swiper-slide>

              <swiper-slide>
                <div class="parnters__item">
                  <img src="../../assets/partners/11.png" alt="partners">
                </div>
              </swiper-slide>

              <div class="swiper-pagination"></div>

              <div class="swiper-navigation-container">
                <div class="swiper-button-next" @click="nextSlide"></div>
                <div class="swiper-button-prev" @click="prevSlide"></div>
              </div>

            </swiper>

          </div>


        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import { Swiper } from "swiper/vue";
  import { SwiperSlide } from "swiper/vue";
  import SwiperCore, { Pagination, Navigation } from "swiper";
  import "swiper/swiper.min.css";
  SwiperCore.use([Navigation, Pagination]);

  export default {
    name: 'Partners',
  
    components:
    {
      Swiper, SwiperSlide,
    },

    methods:{
      nextSlide(){
          this.swiper.slideNext();
      },
      prevSlide(){
          this.swiper.slidePrev();
      },
      onSwiper(swiper){
          this.swiper = swiper;
      },
    },
}
</script>

<style scoped lang="scss">

.partners {


  &__wrapper{
    padding: 20px 0;

  }
  &__content{

  }

  &__body{
    h3{
      text-align: center;
      margin-bottom: 36px;
    }
  }


  &__items{
  justify-content: space-around;
  }
  &__item{


  }
  &__link{

}

}

</style>