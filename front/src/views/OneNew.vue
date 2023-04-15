<template>
  <div class="_container">
    <div class="one-news__block" v-if="oneNewData">
      <a class="one-news__item">
          <div class="one-news__img">
              <CardImage :images = "oneNewData.image" />
          </div>

          <div class="one-news__title ">{{ oneNewData.title }}</div>
          <div class="one-news__content">
              <div v-html = "oneNewData.content"></div>
          </div>
      </a>

      <div class="one-news__btns">
        <div class="btn empty" @click.stop="onMoveToAllNews">Все новости</div>
      </div>

      <News/>


    </div>

  </div>
</template>

<script>
  import axios from 'axios';
  import { mapMutations, mapActions } from 'vuex' 
  import CardImage from '@/components/UI/card-image.vue'
  import News from "@/components/about/News.vue";

  export default {
    name: 'OneNew',

    props: {
      id: null,
    },

    data(){
      return {
        oneNewData: null,
      }
    },

    components: {
      CardImage,
      News,
    },

    watch: {
      id: async function() {
        this.onGetNewsData();
      },
    },

    methods: {
      ...mapMutations("breadcrumb", ["ADD_BREADCRUMB", ]),
      ...mapActions("breadcrumb", ["CHANGE_BREADCRUMB", ]),

      onMoveToAllNews() {
        this.$router.push('/news');
      },

      async onGetNewsData (){
        this.CHANGE_BREADCRUMB(0);
        try {
            const response = await axios.get(process.env.VUE_APP_API_URL + 'service_entities/articles/' + this.id);
            this.oneNewData = response.data;
        } catch (e) {
            console.log(e);
            this.ADD_MESSAGE({name: "Не возможно загрузить новость ", icon: "error", id: '1'})
        }

        const mainBreadCrumb = {
          name: 'Новости',
          path: '/news',
          type: 'global',
          class: '',
        }
        this.ADD_BREADCRUMB(mainBreadCrumb);

        this.ADD_BREADCRUMB({
          name: this.oneNewData.title,
          path: this.$router.currentRoute.value.path,
          type: "global",
          class: ""
        });
      },
    },

    // async onBeforeUpdate(){
    //   await this.onGetNewsData();
    // },

    async mounted(){
      await this.onGetNewsData();
    }
  }
</script>

<style lang="scss" scoped>
.one-news{
  &__img{
    height: 200px;
    display: block;
    margin: 20px 0;
    img{
      width: 100%;
    }
  }
  &__title{
    font-weight: 500;
    font-size: 24px;
    line-height: 140%;
    color: #423E48;
    margin-bottom: 20px;

  }
  &__content{
    font-weight: 300;
    font-size: 18px;
    line-height: 140%;
    color: #423E48;
    p{
      margin: 5px 0;
    }
  }
  &__btns{
    width: 100%;
    margin: 10px 0;
    .empty{
      width: 120px;
      margin: 0 auto;
    }
  }

}
</style>

<style lang="scss">
.one-news__img img{
  width: 100%;

}
</style>