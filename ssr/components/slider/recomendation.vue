<template>
  <div class="recomendation">
    <div class="recomendation__wrapper">
      <div class="recomendation__content _container">
        <div class="recomendation__body">

          <h3>Рекомендации для вас</h3>
          <div class="recomendation__nav" v-if="isShowFilter">
            <div 
              :class="[activePiont === 0 ? 'recomendation__nav__item active' : 'recomendation__nav__item']" 
              @click="setTypeAndOrder({ type: 'popular', order: 'discount', typeRecomendation : 0 }, '-')"
            >Топ продаж</div>
            <div 
            :class="[activePiont === 1 ? 'recomendation__nav__item active' : 'recomendation__nav__item']" 
              @click="setTypeAndOrder({ type: 'available', order: 'created_at', typeRecomendation : 1 }, '-')"
            >Новинки</div>
            <div 
            :class="[activePiont === 2 ? 'recomendation__nav__item active' : 'recomendation__nav__item']" 
              @click="setTypeAndOrder({ type: 'with_discount', order: 'discount', typeRecomendation : 2 }, '')"
            >Скидки</div>
          </div>
          <!-- :navigation= "true" -->
          <!-- <div class="recomendation__block" v-if = "DEVICE_VIEW_TYPE === 1 || DEVICE_VIEW_TYPE === 2"> -->
          <div class="recomendation__block">
              <swiper
                  :slides-per-view="slidersInFrame"
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
                  @swiper="onSwiper"
                  @slideChange="onSlideChange"
              >

                <swiper-slide v-for="item in RECOMENDED_ITEMS" :key="item.id">
                  <CatalogCardItem
                      :card = "item"
                  />
                </swiper-slide>

                <div class="swiper-pagination"></div>

                <div class="swiper-navigation-container">
                 <!-- <div class="swiper-button-next" @click="nextSlide"></div>
                 <div class="swiper-button-prev" @click="prevSlide"></div> -->
                </div>

              </swiper>
              <div v-if="isShowFollow" class="recomendation__link  _link" @click="onOpenCatalog">Смотреть все
                <svg width="16" height="8" viewBox="0 0 16 8" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M0.5 3.99935H15.0833M15.0833 3.99935L11.75 0.666016M15.0833 3.99935L11.75 7.33268" stroke="#4275D8"/>
                </svg>
              </div>

          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import { mapGetters, mapActions, mapMutations } from 'vuex'
  // import CardItem from '@/components/catalog/card-item.vue'8

  import { Swiper } from "swiper/vue";
  import { SwiperSlide } from "swiper/vue";
  import SwiperCore, { Pagination, Navigation } from "swiper";
  import "swiper/swiper.min.css";
  import "swiper/components/pagination/pagination.min.css"
  SwiperCore.use([Navigation, Pagination]);

  export default {
    name: 'Recomendation',

    props: {
      isShowFilter: true,
      isShowFollow: true,
    },

    components:
    {
      Swiper, SwiperSlide,
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
        slidersInFrame : 4.5,
        activePiont: 0,
      }
    },

    watch: {
      DEVICE_VIEW_TYPE: function() {
        this.setSlidersInFrame();
      },

      slidersInFrame: async function() {
        await this.GET_RECOMENDED_ITEMS();
        this.setNewQuantity();
        if (this.$router.currentRoute._value.path !== '/') setTimeout(() => window.scrollTo(0, 0), 0);
      },

      ChangeParameters: async function() {
        this.SET_RECOMENDATION_QUANTITY(10);
        await this.GET_RECOMENDED_ITEMS();
        this.setNewQuantity();
        if (this.$router.currentRoute._value.path !== '/') setTimeout(() => window.scrollTo(0, 0), 0);
      }
    },

    methods:{
      ...mapActions("catalog", ["GET_RECOMENDED_ITEMS"]),
      ...mapMutations("catalog", ["SET_RECOMENDATION_TYPE", "SET_RECOMENDATION_QUANTITY", "SET_RECOMENDATION_ORDER"]),
      ...mapMutations("query", ["SET_TYPE_OF_PRODUCT", "SET_SORT_DIRECTION", "SET_SORT_TYPE"]),

      setNewQuantity(){
        const newQuantity = this.RECOMENDED_ITEMS.length > 9 ? 10 : this.RECOMENDED_ITEMS.length;
        this.SET_RECOMENDATION_QUANTITY(newQuantity);
      },

      setSlidersInFrame(){
        if (this.DEVICE_VIEW_TYPE === 1) {
          this.slidersInFrame = 4.5;
        } else if (this.DEVICE_VIEW_TYPE === 2) {
          this.slidersInFrame = 3.5;
        } else {
          this.slidersInFrame = 1.5;
        }
      },

      setTypeAndOrder(params, sort){
        this.SET_SORT_DIRECTION(sort);
        this.SET_RECOMENDATION_ORDER(params.order);
        this.SET_RECOMENDATION_TYPE(params.type);
        this.activePiont = params.typeRecomendation;
      },

      onOpenCatalog(){
        // console.log(this.RECOMENDATION_TYPE);
        let name = 'Все товары';
        if (this.RECOMENDATION_TYPE === 'with_discount') name = 'Акции';
        if (this.RECOMENDATION_TYPE === 'available') {
          this.SET_SORT_TYPE({ name: 'По дате добавления', type: 'created_at' });
          this.SET_SORT_DIRECTION('-');
          name = 'В наличии';
        }
        if (this.RECOMENDATION_TYPE === 'popular') {
          this.SET_SORT_TYPE({ name: 'Топ продаж', type: 'discount' });
          this.SET_SORT_DIRECTION('-');
          name = 'Топ продаж';
        }
        this.SET_TYPE_OF_PRODUCT({name, type: this.RECOMENDATION_TYPE, selected: true});
        this.$router.push('/catalog');
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
      this.setNewQuantity();
      this.setSlidersInFrame();
      setTimeout(() => window.scrollTo(0, 0), 0);
    }
  }
</script>

<style scoped lang="scss">

.swiper-pagination, .swiper-pagination-clickable, .swiper-pagination-bullets, .swiper-pagination-horizontal {
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
.active{
  color:#4275D8;
  border: 2px solid #4275D8;
  font-weight: 500;
  opacity: 1;
}

.recomendation {
  margin-top: 30px;
  position: relative;

  h3{
    margin-bottom: 20px;
  }

  &__wrapper{

  }
  &__content{

  }

  &__link{
    position: absolute;
    right: 0;
    bottom: 43px;
    cursor: pointer;
    z-index: 90;
    @media (max-width: $md3+px) {
      display: none;
    }
  }

  &__block{
    position: relative;
    &__item{
      width: 100%;
      max-width: 272px;
      margin: 0 auto;


    }

    //@media (max-width: $md3+px) {
    //  display: flex;
    //  flex-direction: column;
    //  align-items: center;
    //  gap: 20px;
    //}

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
    &__link{
      position: absolute;
      right: 0;
      bottom: 0;
    }
  }


  &__item{

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
.recomendation__nav__item{
  white-space: nowrap;
}
</style>