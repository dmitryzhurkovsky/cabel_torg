<template>
  <a class="news__item" v-if = "data">
    <div class="_block">
      <!-- <img src="../../assets/news/1.png" alt=""> -->
      <CardImage :images = "data.image"/>
    </div>
    <div class="_block">
      <div class="news__date">???????? Дата?</div>
      <div class="news__title"  @click.prevent="onOpenOneNew(data.id)">{{ data.title }}</div>
      <div class="news__description" v-html="data.preview_text"></div>
    </div>
  </a>
</template>
<script>
import CardImage from '@/components/UI/card-image.vue'

export default {
  name: "NewsItem",

  props: {
    data:  null,
  },

  components: {
    CardImage,
  },

  methods: {
    onOpenOneNew(id){
      this.$router.push('/new/' + id);
    }
  }
}

</script>

<style lang="scss" scoped>
.news {
  &__item{
    display: flex;
    align-items: flex-start;
    height: 100%;

    ._block{
      flex-basis: 50%;
      &:nth-child(1){
        img{
          width: 100%;
        }
      }
      &:nth-child(2){
        display: flex;
        flex-direction: column;
        padding: 20px 20px;
        @media (max-width: $md3+px) {
          padding: 0 20px 20px 20px;
        }
      }
    }
  }
  &__date{
    font-size: 14px;
    line-height: 130%;
    opacity: 0.4;
  }
  &__title{
    font-weight: 500;
    font-size: 20px;
    line-height: 24px;
    letter-spacing: 0.44px;
    margin: 16px 0;
    cursor: pointer;
    height: 100%;
    max-height: 50px;
  }

  &__description{
    font-size: 14px;
    line-height: 130%;
    opacity: 0.4;
    height: 100%;
    max-height: 60px;
  }

}
</style>