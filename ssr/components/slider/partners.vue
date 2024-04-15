<template>
  <div class="partners" v-if="PARTNERS">
    <div class="partners__wrapper">
      <div class="partners__content _container">
        <div class="partners__body">

          <h3>Наши партнеры</h3>
          <div class="partners__items flex-center">
            <swiper
                :slides-per-view = quantity
                :space-between="15"
                :speed="500"
                :autoplay="{
                    delay: 5000,
                }"
            >

              <swiper-slide v-for="partner in PARTNERS" :key = "partner.id">
                <div class="parnters__item">
                  <UiCardImage :images = "'/' + partner.image" />
                </div>
              </swiper-slide>


              <div class="swiper-pagination"></div>

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
  import "swiper/components/pagination/pagination.min.css"
  import { mapGetters, mapActions } from 'vuex';
  SwiperCore.use([Navigation, Pagination]);

  export default {
    name: 'Partners',

    data: function(){
      return {
        quantity: 5.5,
      }
    },
  
    components: {
      Swiper, SwiperSlide
    },

    computed: {
      ...mapGetters("header", ["DEVICE_VIEW_TYPE"]),
      ...mapGetters("main", ["PARTNERS"]),
    },

    watch: {
      DEVICE_VIEW_TYPE: function() {
        this.setQuantity();
      },  
    },

    async mounted(){
      await this.GET_PARTNERS();
      this.setQuantity();
    },

    methods:{
      ...mapActions('main', ["GET_PARTNERS"]),

      setQuantity() {
        let quantity = 0;
        if (this.DEVICE_VIEW_TYPE===1) quantity = 5.5
        if (this.DEVICE_VIEW_TYPE===2) quantity = 4.5
        if (this.DEVICE_VIEW_TYPE===3) quantity = 3.5
        this.quantity = Math.min(this.PARTNERS.length, quantity);
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