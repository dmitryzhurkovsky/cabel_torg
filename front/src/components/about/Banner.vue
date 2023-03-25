<template>
  <div class="banner">
    <swiper
      :slides-per-view=quantity
      :space-between="15"
      @swiper="onSwiper"
      @slideChange="onSlideChange"
    >

      <swiper-slide v-for="banner in filteredBanners" :key = "banner.id">
        <div class="banner__wrapper" 
          :style = "{
            backgroundImage     : 'url(' + getPath(banner.image) + ')',
            backgroundRepeat    : 'no-repeat',
            backgroundPosition  : 'center',
            backgroundSize      : 'cover',
          }"
        >
          <div class="banner__content _container">
            <div class="banner__body">
              <h1>{{ banner.title }}</h1>
              <p>{{ banner.subtitle }}</p>
              <button class="btn"> К распродаже
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M3 12H20.5M20.5 12L16.5 8M20.5 12L16.5 16" stroke="white"/>
                </svg>
              </button>


            </div>
          </div>
        </div>
      </swiper-slide>
    </swiper>

  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex';
  import { Swiper } from "swiper/vue";
  import { SwiperSlide } from "swiper/vue";
  import SwiperCore, { Pagination, Navigation } from "swiper";
  import "swiper/swiper.min.css";
  
  export default {
    name: 'Banner',
  
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
        console.log(process.env.BASE_URL);
        console.log(process.env.VUE_APP_IMAGES);
        let path = process.env.VUE_APP_IMAGES + item;
        return path;
      },
    },

    async mounted(){
      console.log('Mounted');
      await this.GET_BANNERS();
    },

  }
</script>

<style scoped lang="scss">

.banner {

  // &__wrapper{
  //   // background-image:url("../../assets/banner/1.png");
  //   // background-repeat: no-repeat;
  //   // background-position: center;
  //   // background-size: cover;
  // }
  &__content{

  }

  &__body{
    max-width: 427px;
    padding: 60px 0;
    h1{
      margin-bottom: 20px;
      @include adaptiv-value("line-height",43,20,43);
      @include adaptiv-font(36, 18, 36);
    }

    p{
      font-weight: 300;
      font-size: 12px;
      line-height: 14px;
      display: flex;
      align-items: center;

      color: #423E48;
    }
    button{
      margin-top: 30px;
      font-weight: 400;
      font-size: 14px;
      color: #FFFFFF;
      display: flex;
      align-items: center;
      svg{
        margin-left: 10px;
      }
    }
  }


  &__item{

  }
  &__link{

}

}

</style>