<template>
  <div class="news">
    <div class="news__wrapper">
      <div class="news__content _container">
        <div class="news__body">

          <h3>Новости CabelTorg</h3>
          <!-- <div class="news__block" v-if="NEWS"> -->

            <swiper
                :slides-per-view="slidersInFrame"
                :space-between="12"
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
            >

              <swiper-slide v-for="oneNew in filteredNews" :key="oneNew.id">
                <a class="news__item" @click="onOpenNew(oneNew.id)">
                  <div class="news__item__box">
                    <CardImage :images = "oneNew.image" />
                  </div>
                  <div class="news__title long-text">{{ oneNew.title }}</div>
                  <div class="news__desc">
                    <div v-html = "oneNew.preview_text"></div>
                  </div>
                </a>
              </swiper-slide>

              <div class="swiper-pagination"></div>

              <div class="swiper-navigation-container">
              </div>

            </swiper>

          <!-- </div> -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex';
  import CardImage from '@/components/UI/card-image.vue';

  import { Swiper } from "swiper/vue";
  import { SwiperSlide } from "swiper/vue";
  import SwiperCore, { Pagination, Navigation } from "swiper";
  import "swiper/swiper.min.css";
  SwiperCore.use([Navigation, Pagination]);

  export default {
    name: 'News',

    components: {
      CardImage, Swiper, SwiperSlide,
    },

    data: function(){
      return{
        slidersInFrame : 4.5,
      }
    },

    computed: {
      ...mapGetters("main", ["NEWS"]),
      ...mapGetters("header", ["DEVICE_VIEW_TYPE"]),

      filteredNews() {
        return this.NEWS.slice(-10);
      }
    },

    watch: {
      DEVICE_VIEW_TYPE: function() {
        this.setQuantityInSlider();
      },
    },

    methods: {
      ...mapActions("main", ["GET_NEWS"]),

      onOpenNew(id) {
        this.$router.push('/new/' + id);
      },

      setQuantityInSlider() {
        if (this.DEVICE_VIEW_TYPE === 1) this.slidersInFrame = 4.5
        if (this.DEVICE_VIEW_TYPE === 2) this.slidersInFrame = 2.5
        if (this.DEVICE_VIEW_TYPE === 3) this.slidersInFrame = 1.5
      }
    },

    async mounted(){
      await this.GET_NEWS();
      this.setQuantityInSlider();
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
:root {
  --swiper-theme-color: red!important;
}
.news {

  &__wrapper{
    padding: 20px 0;
  }

  &__body{
    h3{
      margin-bottom: 20px ;
    }
  }

  // &__block{
  //   display:grid;
  //   grid-template-columns: repeat(4, 1fr);
  //   grid-template-rows:auto;
  //   gap: 12px;
  //   width: 100%;
  //   @media (max-width: $md2+px) {
  //     grid-template-columns: repeat(2, 1fr);
  //   }

  // }


  &__item{
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: space-between;
    cursor: pointer;
    &__box{
     width: 100%;
     height: 150px;
      @media (max-width: $md3+px) {
        height: 250px;
      }

    }
    img{
      width: 100%;
      max-height: 100%;
    }
    ._block{
      &:nth-child(2){
        padding: 0 20px 20px 20px;
        background: red;
      }
    }

  }
  &__title{
    margin: 12px 0;
    font-weight: 500;
    font-size: 20px;
    line-height: 24px;
    letter-spacing: 0.44px;
    color: $mainColor;
    height: 100%;
    max-height: 50px;
    overflow: hidden;

  }
  &__desc{
    font-size: 14px;
    line-height: 130%;
    color: $mainColor;
    opacity: 0.4;
    height: 100%;
    max-height: 70px;
    overflow: hidden;

  }


}

</style>
<style lang="scss">
.news__item__box img{
  width: 100%;
}

</style>