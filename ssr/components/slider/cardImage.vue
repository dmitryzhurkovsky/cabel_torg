<template>
  <div class="images" v-if="swiperImages.length > 1">
    <div class="images__wrapper">
      <div class="images__content _container">
        <div class="images__body">

          <div class="images__items flex-center">
            <swiper
                :slides-per-view=2
                :space-between="15"
                :navigation = "{
                  nextEl: '.btn-next_',
                  prevEl: '.btn-prev_',
                }"
                @slideChange="onSlideChange"
            >

              <swiper-slide v-for="(image, index) in swiperImages" :key = "image">
                <div class="images__item">
                  <UiCardImage 
                    :images = "allImages" 
                    :num = "index"
                    :active = "index == activeItem"
                  />
                </div>
              </swiper-slide>
              <div class="swiper-navigation">
                <div class="btn-prev" @click="prevSlide">
                </div>
                <div class="btn-next" @click="nextSlide">
                </div>
              </div>
              </swiper>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex';
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

    computed: {
      ...mapGetters("main", ["BANNERS"]),

      filteredBanners() {
        return this.BANNERS.filter(item => item.is_active);
      }
    },

    methods: {
      ...mapActions("main", ["GET_BANNERS"]),

      getPath: function(item){
        console.log('getPath ', item);
        let path = useRuntimeConfig().public.NUXT_APP_IMAGES + item;
        return path;
      },

      onSlideChange(swiper) {
        console.log('Slider changed', swiper.realIndex);
        // this.activeSlider = swiper.realIndex
        // this.$emit('onSliderChanged', this.activeSlider);
      },

      nextSlide(){
        if (this.activeItem < this.swiperImages.length) {
          this.activeItem++;
        }
        console.log('next ', this.activeItem);
        this.$emit('changeSliderTo', this.activeItem);
      },

      prevSlide(){
        if (this.activeItem) {
          this.activeItem--;          
        }
        console.log('prev ', this.activeItem);
        this.$emit('changeSliderTo', this.activeItem);
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
  background-color: blue;
  width: 20px;
  height: 20px;
}
.btn-prev{
  background-color: blue;
  width: 20px;
  height: 20px;
}
.images {
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
    text-align: center;


  }
}

</style>