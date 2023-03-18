<template>
  <div class="recomendation">
    <div class="recomendation__wrapper">
      <div class="recomendation__content _container">
        <div class="recomendation__body">

          <h3>Рекомендации для вас</h3>
          <div class="recomendation__nav">
            <div class="recomendation__nav__item" @click="setTypeAndOrder({ type: 'available', order: 'price' })">Топ продаж</div>
            <div class="recomendation__nav__item" @click="setTypeAndOrder({ type: 'available', order: 'created_at' })">Новинки</div>
            <div class="recomendation__nav__item" @click="setTypeAndOrder({ type: 'with_discount', order: 'discount' })">Скидки</div>
          </div>
          <!-- :navigation= "true" -->
          <div class="recomendation__block" v-if = "DEVICE_VIEW_TYPE === 1 || DEVICE_VIEW_TYPE === 2">
              <swiper
                  :slides-per-view="slidersInFrame"
                  :space-between="15"
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

                <swiper-slide v-for="item in RECOMENDED_ITEMS" :key="item.id">
                  <CardItem
                      :card = "item"
                  />
                </swiper-slide>

                <div class="swiper-pagination"></div>

                <div class="swiper-navigation-container">
                  <div class="swiper-button-next" @click="nextSlide"></div>
                  <div class="swiper-button-prev" @click="prevSlide"></div>
                </div>

              </swiper>

          </div>
          <div class="recomendation__block" v-if = "DEVICE_VIEW_TYPE === 3">

            <CardItem v-for="item in RECOMENDED_ITEMS" :key="item.id"
              :card = "item"
            />
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import { mapGetters, mapActions, mapMutations } from 'vuex'
  import CardItem from '@/components/catalog/card-item.vue'

  import { Swiper } from "swiper/vue";
  import { SwiperSlide } from "swiper/vue";
  import SwiperCore, { Pagination, Navigation } from "swiper";
  import "swiper/swiper.min.css";
  SwiperCore.use([Navigation, Pagination]);

  export default {
    name: 'Recomendation',

    components:
    {
      CardItem, Swiper, SwiperSlide,
    },

    computed: {
      ...mapGetters("header", ["DEVICE_VIEW_TYPE"]),
      ...mapGetters("catalog", ["RECOMENDED_ITEMS", "RECOMENDATION_QUANTITY", "RECOMENDATION_TYPE", "RECOMENDATION_ORDER"]),

      ChangeParameters(){
        return String(this.RECOMENDATION_TYPE) + String(this.RECOMENDATION_ORDER);
      },
    },

    data: function(){
      return{
        slidersInFrame : 4,
      }
    },

    watch: {
      DEVICE_VIEW_TYPE: function() {
        this.slidersInFrame = this.DEVICE_VIEW_TYPE === 1 ? 4 : 3;
      },

      slidersInFrame: async function() {
        await this.GET_RECOMENDED_ITEMS();
        this.setNewQuantity();
      },

      ChangeParameters: async function() {
        this.SET_RECOMENDATION_QUANTITY(10);
        await this.GET_RECOMENDED_ITEMS();
        this.setNewQuantity();
      }
    },

    methods:{
      ...mapActions("catalog", ["GET_RECOMENDED_ITEMS"]),
      ...mapMutations("catalog", ["SET_RECOMENDATION_TYPE", "SET_RECOMENDATION_QUANTITY", "SET_RECOMENDATION_ORDER"]),
      
      setNewQuantity(){
        const newQuantity = this.RECOMENDED_ITEMS.length > 9 ? 10 : this.RECOMENDED_ITEMS.length;
        this.SET_RECOMENDATION_QUANTITY(newQuantity);
      },

      setTypeAndOrder(params){
        this.SET_RECOMENDATION_ORDER(params.order);
        this.SET_RECOMENDATION_TYPE(params.type);
      },

      onSlideChange() {
        //  console.log('slide change');
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

    async mounted(){
      await this.GET_RECOMENDED_ITEMS();
    }
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



.swiper-navigation-container{
  position: relative;
  margin: 0 auto;
  width: 20%;
  height: 50px;
}
.swiper-button-next, .swiper-button-prev{
  top: -3px;

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
  margin-top: 30px;

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

    @media (max-width: $md3+px) {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 20px;
    }

  }
  &__nav{
    display: grid;
    gap: 10px;
    grid-template-columns: repeat(3, minmax(0, 170px));
    /*
    if we did this instead of the template it would be a problem:
    grid-auto-flow: column;
    */
    text-align: center;
    padding: 24px 20px 20px 0;
    @media (max-width: $md2+px) {
      gap: 8px;
    }

    &__item{

      background: #FFFFFF;
      border: 2px solid #EEEEEE;
      border-radius: 50px;
      font-size: 14px;
      font-weight: 500;
      line-height: 24px;
      text-align: center;
      opacity: 0.5;
      padding: 6px 20px;
      cursor: pointer;
      transition: all 0.3s ease;
      @media (max-width: $md2+px) {
        font-size: 10px;
        line-height: 12px;
        padding: 6px 15px;
      }

      &:hover{
        color:#4275D8;
        border: 2px solid #4275D8;
        font-weight: 500;
        opacity: 1;
      }

    }
  }


  &__item{

  }
  &__link{

}

}

</style>

<style lang="scss">

.recomendation__block__item{
  .item-card__uptitle div{
    //width: 200px;
    overflow:hidden;
    white-space:nowrap;
    text-overflow: ellipsis;
  }

}
</style>