<template>
  <div class="images" v-if="swiperImages.length > 1">

          <div class="images__items flex-center">
            <swiper
                :slides-per-view=3
                :space-between="5"
                :navigation = "{
                  nextEl: '.btn-next_',
                  prevEl: '.btn-prev_',
                }"
                @swiper="onSwiper"
                @slideChange="onSlideChange"
            >

              <swiper-slide v-for="(image, index) in swiperImages" :key = "image">
                <div class="images__item">
                  <UiCardImage 
                    :images = "allImages" 
                    :num = "index"
                    :active = "index == activeItem"
                    :alt="altName + ' №' + Number(index + 1) + ' - cabel-torg'"
                    @click="changeSlideByClick(index)"
                  />
                </div>
              </swiper-slide>
              <div class="swiper-navigation">
                <div class="btn-prev" @click="prevSlide">
                  <svg width="8" height="12" viewBox="0 0 8 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M7.41 1.41L2.83 6L7.41 10.59L6 12L-2.62268e-07 6L6 2.62268e-07L7.41 1.41Z" fill="#423E48"/>
                  </svg>

                </div>
                <div class="btn-next" @click="nextSlide">
                  <svg width="8" height="12" viewBox="0 0 8 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M0.59 10.59L5.17 6L0.590001 1.41L2 -2.62268e-07L8 6L2 12L0.59 10.59Z" fill="#423E48"/>
                  </svg>

                </div>
              </div>
              </swiper>
          </div>
        </div>
</template>

<script>
  import { Swiper } from "swiper/vue";
  import { SwiperSlide } from "swiper/vue";
  import SwiperCore, { Pagination, Navigation } from "swiper";
  import "swiper/swiper.min.css";
  import "swiper/components/navigation/navigation.min.css"
  SwiperCore.use([Navigation, Pagination]);

  export default {
    name: 'Images',

    props: {
      allImages: '',
      altName: '',
    },
  
    data(){
      return {
        activeSlider: 0,
        swiperImages: [],
        activeItem: 0,
      }
    },
    components: {
      Swiper, SwiperSlide,
    },

    methods: {

      onSlideChange(swiper) {
        // console.log('Slider changed', swiper.realIndex);
        this.activeSlider = swiper.realIndex
        this.$emit('onSliderChanged', this.activeSlider);
      },

      changeSlideByClick(index){
        this.activeItem = index;
        this.$emit('changeSliderTo', this.activeItem);
      },

      nextSlide(){
        if (Math.abs(this.swiper.realIndex - this.activeItem) > 1) this.swiper.slideTo(this.activeItem -1) 
        if (this.swiper.realIndex + 1 < this.activeItem) this.swiper.slideTo(this.swiper.realIndex + 1) 
        if (this.activeItem === this.swiperImages.length - 1) this.swiper.slideTo(0)

        if (this.activeItem < this.swiperImages.length - 1) {
          this.activeItem++;
          this.$emit('changeSliderTo', this.activeItem);
        } else {
          this.activeItem = 0;
          this.$emit('changeSliderTo', this.activeItem);
        }
      },

      prevSlide(){
        if (Math.abs(this.swiper.realIndex - this.activeItem) > 1) this.swiper.slideTo(this.activeItem -1) 
        if (this.activeItem === this.swiper.realIndex) this.swiper.slideTo(this.swiper.realIndex - 1) 
        if (this.activeItem === 0) this.swiper.slideTo(this.swiperImages.length - 1)

        if (this.activeItem) {
          this.activeItem--;          
          this.$emit('changeSliderTo', this.activeItem);
        } else {
          this.activeItem = this.swiperImages.length - 1;
          this.$emit('changeSliderTo', this.activeItem);
        }
      },

      onSwiper(swiper){
          this.swiper = swiper;
      },

    },

    async mounted(){
      this.swiperImages = this.$props.allImages.split(',');
      this.activeSlider = 0;
    },

  }
</script>

<style scoped lang="scss">

.swiper-navigation, .swiper-navigation-horizontal {
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

.btn-next{
  z-index: 10;
  width: 20px;
  height: 20px;
  cursor: pointer;
}
.btn-prev{
  z-index: 10;
  width: 20px;
  height: 20px;
  cursor: pointer;

}
.images {
  .swiper-container{
    width: 100%;
    padding: 0 30px;
    position: relative;
  }
  &__wrapper{
    padding: 20px 0;

  }
  &__content{

  }

  &__body{
    h3{
      text-align: center;
      margin-bottom: 36px;
      @media (max-width: $md2+px) {
        text-align: left;

      }
    }
  }


  &__items{
  justify-content: space-around;
  }
  &__item{
    display: flex;
    text-align: center;
    width: 100px;
    height: 100px;
    cursor: pointer;
    img{
      object-fit: contain;
    }
    .active{
      border: 2px solid #dedede;
    }


  }
  .swiper-navigation{
    justify-content: space-between;
    position: absolute;
    bottom:42px;
    left: 0;
  }
}

</style>