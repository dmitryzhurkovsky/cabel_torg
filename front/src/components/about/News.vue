<template>
  <div class="news">
    <div class="news__wrapper">
      <div class="news__content _container">
        <div class="news__body">

          <h3>Новости CabelTorg</h3>
          <div class="news__block" v-if="NEWS">
            <a class="news__item" v-for="oneNew in filteredNews" :key="oneNew.id">
              <CardImage :images = "oneNew.image" />
              <!-- <img src="../../assets/news/new1.png" alt=""> -->
              <div class="news__title">{{ oneNew.title }}</div>
              <div class="news__desc">{{ oneNew.content }}</div>
            </a>

          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex';
  import CardImage from '@/components/UI/card-image.vue';

  export default {
    name: 'News',

    components: {
      CardImage,
    },

    computed: {
      ...mapGetters("main", ["NEWS"]),

      filteredNews() {
        return this.NEWS.slice(-4);
      }
    },

    methods: {
      ...mapActions("main", ["GET_NEWS"]),
    },

    async mounted(){
      await this.GET_NEWS();
    },

  }

</script>

<style scoped lang="scss">

.news {

  &__wrapper{
    padding: 20px 0;

  }
  &__content{

  }

  &__body{
    h3{
      margin-bottom: 20px ;
    }
  }

  &__block{
    display:grid;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows:auto;
    gap: 12px;
    width: 100%;
    @media (max-width: $md2+px) {
      grid-template-columns: repeat(2, 1fr);
    }

  }


  &__item{
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: space-between;
    cursor: pointer;
    img{
      max-width: 100%;
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
  }
  &__desc{
    font-size: 14px;
    line-height: 130%;
    color: $mainColor;
    opacity: 0.4;

  }


}

</style>