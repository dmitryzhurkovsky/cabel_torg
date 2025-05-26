<template>
  <div class="partners" v-if="partners">
    <div class="partners__wrapper">
      <div class="partners__content _container">
        <div class="partners__body">

          <div class="partners__section_title section_title">Наши партнеры</div>
          <div class="partners__items flex-center">
            <swiper
                :slides-per-view = quantity
                :space-between="15"
                :speed="500"
                :autoplay="{
                    delay: 5000,
                }"
            >

              <swiper-slide v-for="partner in partners" :key = "partner.id">
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

<script setup>
  import { ref, watch } from 'vue';
  import { useMainStore } from '@/stores/main';
  import { useHeaderStore } from '@/stores/header';

  import { Swiper } from "swiper/vue";
  import { SwiperSlide } from "swiper/vue";
  import SwiperCore, { Pagination, Navigation } from "swiper";
  import "swiper/swiper.min.css";
  import "swiper/components/pagination/pagination.min.css"
  
  const mainStore = useMainStore();
  const headerStore = useHeaderStore();

  const { partners } = storeToRefs(mainStore);
  const { viewType } = storeToRefs(headerStore);

  SwiperCore.use([Navigation, Pagination]);

  const quantity = ref(5.5);

  watch(viewType, () => {
    setQuantity();
  });
  
  await useAsyncData(
    async () => {
      await mainStore.getPartners();
      setQuantity();
      return true;
    }
  );
  
  // async mounted(){
  //   await mainStore.getPartners();
  //   this.setQuantity();
  // },

  const setQuantity = () => {
    let newQuantity = 0;
    if (viewType.value === 1) newQuantity = 5.5
    if (viewType.value === 2) newQuantity = 4.5
    if (viewType.value ===3 ) newQuantity = 3.5
    quantity.value = Math.min(partners.length, newQuantity);
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
    .section_title{
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