<template>
  <div class="recomendation">
    <div class="recomendation__wrapper">
      <div class="recomendation__content _container">
        <div class="recomendation__body">

          <h3>Просмотренные товары</h3>
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

                <swiper-slide v-for="item in sliderItems" :key="item.id">
                  <CardItem
                      :card = "item"
                  />
                </swiper-slide>

                <div class="swiper-pagination"></div>

                <div class="swiper-navigation-container">
                 <!-- <div class="swiper-button-next" @click="nextSlide"></div>
                 <div class="swiper-button-prev" @click="prevSlide"></div> -->
                </div>

              </swiper>
              <!-- <div class="recomendation__link  _link" @click="onOpenCatalog">Смотреть все
                <svg width="16" height="8" viewBox="0 0 16 8" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M0.5 3.99935H15.0833M15.0833 3.99935L11.75 0.666016M15.0833 3.99935L11.75 7.33268" stroke="#4275D8"/>
                </svg>
              </div> -->

          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import { mapGetters } from 'vuex'
  import CardItem from '@/components/catalog/card-item.vue'
  import axios from 'axios';

  import { Swiper } from "swiper/vue";
  import { SwiperSlide } from "swiper/vue";
  import SwiperCore, { Pagination, Navigation } from "swiper";
  import "swiper/swiper.min.css";
  SwiperCore.use([Navigation, Pagination]);

  export default {
    name: 'ShownCards',

    components:
    {
      CardItem, Swiper, SwiperSlide,
    },

    computed: {
      ...mapGetters("header", ["DEVICE_VIEW_TYPE"]),
      ...mapGetters("catalog", ["SHOWN_ITEMS_LIST"]),

      ChangeParameters(){
        return JSON.stringify(this.SHOWN_ITEMS_LIST) + String(this.slidersInFrame) + String(this.quantity);
      },
    },

    data: function(){
      return{
        slidersInFrame : 4.5,
        sliderItems: [],
        quantity: 0,
      }
    },

    watch: {
      DEVICE_VIEW_TYPE: function() {
        this.setSlidersInFrame();
      },

      ChangeParameters: async function() {
        await this.getShownItems();
        this.setNewQuantity();
      },
    },

    methods:{

      setNewQuantity(){
        const newQuantity = this.sliderItems.length > 9 ? 10 : this.sliderItems.length;
        this.quantity = newQuantity;
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

      onOpenCatalog(){
        console.log('QQQQ');
        this.$router.push('/catalog');
      },

      getShownItems(){
        const fetchedItems = [];
        this.SHOWN_ITEMS_LIST.forEach(async item => {
          try {
            const response = await axios.get(process.env.VUE_APP_API_URL + 'products/' + item.id);
            fetchedItems.push(response.data);
            this.sliderItems = [...fetchedItems]
          } catch (e) {
            console.log(e);
            this.ADD_MESSAGE({name: "Не возможно загрузить данные товара " + item.id, icon: "error", id: item.id})
          }
        });
        setTimeout(() => window.scrollTo(0, 0), 0);
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
      await this.getShownItems();
      this.setNewQuantity();
      this.setSlidersInFrame();
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
      max-height: 368px;


    }


  }
  &__nav{
    display: grid;
    gap: 10px;
    grid-template-columns: repeat(3, minmax(0, 170px));
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