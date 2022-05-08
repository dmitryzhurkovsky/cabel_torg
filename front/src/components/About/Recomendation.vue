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
          <!-- :navigation= "true" -->
          <div class="recomendation__block" v-if = "VIEW_TYPE === 1">
              <swiper
                  :slides-per-view="4"
                  :space-between="30"
                  :pagination= "{
                    el: '.swiper-pagination',
                    clickable: true,
                    type: 'bullets',
                    bulletClass: 'swiper-pagination-bullet',
                    bulletElement: 'span'
                  }"
                  @swiper="onSwiper"
                  @slideChange="onSlideChange"
              >

                <swiper-slide v-for="n in 10" :key="n"><CardItem/></swiper-slide>

                <div class="swiper-pagination"></div>

                <div class="swiper-navigation-container">
                  <div class="swiper-button-next" @click="nextSlide"></div>
                  <div class="swiper-button-prev" @click="prevSlide"></div>
                </div>

              </swiper>

          </div>
          // Сдесь надо 2 строки в 3 столбика
          <div class="recomendation__block" v-if = "VIEW_TYPE === 2">
            <CardItem/>
            <CardItem/>
            <CardItem/>
            <CardItem/>
            <CardItem/>
            <CardItem/>
          </div>
          // Сдесь надо 2 строки в 2 столбика
          <div class="recomendation__block" v-if = "VIEW_TYPE === 3">
            <CardItem/>
            <CardItem/>
            <CardItem/>
            <CardItem/>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import {mapGetters} from 'vuex'
  import CardItem from '@/components/Goods/card_item.vue'

  import { Swiper } from "swiper/vue/swiper";
  import { SwiperSlide } from "swiper/vue/swiper-slide";
  import SwiperCore, { Pagination, Navigation } from "swiper";
  // Import Swiper styles
  import "swiper/swiper.min.css";
  // import "swiper/modules/pagination/pagination.min.css";
  // import "swiper/modules/navigation/navigation.min.css";
  SwiperCore.use([Navigation, Pagination]);

  export default {
    name: 'Recomendation',

    components:
    {
      CardItem, Swiper, SwiperSlide,
    },

    computed: {
      ...mapGetters("header", ["VIEW_TYPE"]),
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

.swiper-pagination, .swiper-pagination-clickable, .swiper-pagination-bullets, .swiper-pagination-horizontal {
  //position: unset;
  //margin-bottom: 3%;
  bottom: 17px;

  span {
    background: #7700AF;
  }
}
.swiper-pagination-bullet, .swiper-pagination-bullet-active{
  background: red;
}




.swiper-navigation-container{
  position: relative;
  margin: 0 auto;
  width: 20%;
  height: 50px;
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
