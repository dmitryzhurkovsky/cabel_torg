<template>
  <a class="news__item" v-if = "data">
    <div class="_block">
      <UiCardImage :images = "data.image"/>
    </div>
    <div class="_block">
      <div class="news__date">{{ data.created_at.slice(0,10) }}</div>
      <div class="news__title"  >{{ data.title }}</div>
      <div class="news__description" v-html="data.preview_text"></div>
      <a class="news__link _link" @click.prevent="onOpenOneNew(data.id)">Читать
        <svg width="16" height="8" viewBox="0 0 16 8" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M0.5 3.99935H15.0833M15.0833 3.99935L11.75 0.666016M15.0833 3.99935L11.75 7.33268" stroke="#4275D8"></path>
        </svg>
      </a>

    </div>
  </a>
</template>
<script>
// import CardImage from '@/components/UI/card-image.vue'
// import Header from "@/App.vue";

export default {
  name: "NewsItem",

  props: {
    data:  null,
  },

  // components: {
  //   Header,
  //   CardImage,
  // },
  methods: {
    onOpenOneNew(id){
      setTimeout(() => window.scrollTo(0, 0), 0);
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
    border: 2px solid #EEEEEE;
    border-radius: 8px;

    ._block{
      flex-basis: 50%;
      height: 189px;

      &:nth-child(1){
        img{
          width: 100%;
          max-height: 100%;
          height: 100%;
          object-fit: cover;
        }
      }
      &:nth-child(2){
        display: flex;
        flex-direction: column;
        padding: 20px 20px;
        @media (max-width: $md3+px) {
          //padding: 0 20px 20px 20px;
        }
      }
    }
  }
  &__date{
    font-size: 14px;
    line-height: 130%;
    opacity: 0.4;
    margin-bottom: 5px;
  }
  &__title{
    font-weight: 500;
    font-size: 18px;
    line-height: 22px;
    letter-spacing: 0.44px;
    //margin: 16px 0;
    cursor: pointer;
    height: 50px;
    overflow: hidden;
  }

  &__description{
    font-size: 14px;
    line-height: 130%;
    opacity: 0.4;
    height: 60px;
    margin-top: 5px;
    overflow: hidden;
    margin-bottom: 5px;

  }
  &__link{
    cursor: pointer;
  }

}
</style>

<style lang="scss">

.news__item img{
  height: 100%;
}
</style>