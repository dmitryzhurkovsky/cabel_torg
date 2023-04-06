<template>
  <div class="banner">
    <swiper
      :slides-per-view = 1
      :space-between="15"
      :pagination= "{
        el: '.swiper-pagination',
        clickable: true,
        type: 'bullets',
        bulletClass: 'swiper-pagination-bullet',
        bulletElement: 'span'
      }"
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
              <button class="btn btn-banner" @click="onButtonClick(banner.button_link)">{{ banner.button_name }}
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M3 12H20.5M20.5 12L16.5 8M20.5 12L16.5 16" stroke="white"/>
                </svg>
              </button>


            </div>
          </div>
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
  SwiperCore.use([Pagination]);

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
        let path = process.env.VUE_APP_IMAGES + item;
        return path;
      },

      onButtonClick(link) {
        this.$router.push(link);
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

.banner {
  &__body{
    max-width: 427px;
    padding: 60px 0;
    @media (max-width: $md2+px){
      padding: 10px 0;
    }
    h1{
      margin-bottom: 20px;
     @media (max-width: $md2+px){
       font-size: 18px;
       margin-bottom: 10px;
       line-height: 1.4;
       max-width: 200px;
     }
      //@include adaptiv-value("line-height",43,20,43);
      //@include adaptiv-font(36, 18, 36);
    }

    p{
      font-weight: 300;
      font-size: 12px;
      line-height: 14px;
      display: flex;
      align-items: center;
      color: #423E48;
      @media (max-width: $md2+px){
        font-size: 10px;
        max-width: 200px;
      }
    }
    button{
      margin-top: 30px;
      font-weight: 400;
      font-size: 14px;
      color: #FFFFFF;
      display: flex;
      align-items: center;
      @media (max-width: $md2+px){
        margin-top: 10px;
        min-width: auto;
      }
      svg{
        margin-left: 10px;
      }
    }
  }
}

</style>