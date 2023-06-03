<template>
  <div class="images">
    <swiper
      :slides-per-view = 1
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
      @slideChange="onSlideChange"
    >

      <swiper-slide v-for="banner in filteredBanners" :key = "banner.id">
        <div class="images__wrapper" 
          :style = "{
            backgroundImage     : 'url(' + getPath(banner.image) + ')',
            backgroundRepeat    : 'no-repeat',
            backgroundPosition  : 'center',
            backgroundSize      : 'cover',
          }"
        >
        </div>
      </swiper-slide>
      <div class="swiper-pagination"></div>
    </swiper>

  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex';
  import { Swiper } from "swiper/vue";
  import { SwiperSlide } from "swiper/vue";
  import SwiperCore, { Pagination } from "swiper";
  import "swiper/swiper.min.css";
  import "swiper/components/pagination/pagination.min.css"
  SwiperCore.use([Pagination]);

  export default {
    name: 'Images',
  
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
        let path = useRuntimeConfig().public.NUXT_APP_IMAGES + item;
        return path;
      },

      onSlideChange() {
        console.log('slide change');
      },

    },

    async mounted(){
      await this.GET_BANNERS();
    },

  }
</script>

<style scoped lang="scss">

.swiper-pagination, .swiper-pagination-clickable, .swiper-pagination-bullets, .swiper-pagination-horizontal {
  //position: unset;
  //margin-bottom: 3%;
  display: flex;
  position: inherit;
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

.images {
}

</style>