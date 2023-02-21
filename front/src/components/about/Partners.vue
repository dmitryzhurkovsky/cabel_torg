<template>
  <div class="partners">
    <div class="partners__wrapper">
      <div class="partners__content _container">
        <div class="partners__body">

          <h3>Наши партнеры</h3>
          <div class="partners__items flex-center">
            <swiper
                :slides-per-view=quantity
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

<script>
  import { Swiper } from "swiper/vue";
  import { SwiperSlide } from "swiper/vue";
  import SwiperCore, { Pagination, Navigation } from "swiper";
  import "swiper/swiper.min.css";
  import { mapGetters } from 'vuex';
  SwiperCore.use([Navigation, Pagination]);

  export default {
    name: 'Partners',

    data: function(){
      return {
        quantity: 5,
      }
    },
  
    components:
    {
      Swiper, SwiperSlide,
    },

    computed: {
      ...mapGetters("header", ["DEVICE_VIEW_TYPE"]),
    },

    watch: {
      DEVICE_VIEW_TYPE: function() {
        this.setQuantity();
      },  
    },

    mounted(){
      this.setQuantity();
    },

    methods:{
      setQuantity(){
        if (this.DEVICE_VIEW_TYPE===1) this.quantity = 5
        if (this.DEVICE_VIEW_TYPE===2) this.quantity = 4
        if (this.DEVICE_VIEW_TYPE===3) this.quantity = 3
      }
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
    text-align: center;


  }
  &__link{

}

}
.swiper-container{
  width: 100%;
}
.swiper-wrapper {
  justify-content: space-between;
}
</style>