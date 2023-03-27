<template>
  <div class="_container">
    <div class="one-news__block" v-if="oneNewData">
      <a class="one-news__item">
        <CardImage :images = "oneNewData.image" />
        <div class="one-news__title ">{{ oneNewData.title }}</div>
        <div class="one-news__content">
          <div v-html = "oneNewData.content"></div>
        </div>
      </a>

    </div>

  </div>
</template>

<script>
  import axios from 'axios';
  import { mapMutations, mapActions } from 'vuex' 
  import CardImage from '@/components/UI/card-image.vue'

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
    },

    methods: {
      ...mapMutations("breadcrumb", ["ADD_BREADCRUMB", ]),
      ...mapActions("breadcrumb", ["CHANGE_BREADCRUMB", ]),
    },

    async mounted(){
      this.CHANGE_BREADCRUMB(0);
      try {
          const response = await axios.get(process.env.VUE_APP_API_URL + 'service_entities/articles/' + this.id);
          this.oneNewData = response.data;
      } catch (e) {
          console.log(e);
          this.ADD_MESSAGE({name: "Не возможно загрузить рекомендованные товары ", icon: "error", id: '1'})
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
  }
</script>

<style lang="scss" scoped>
.one-news{
  &__title{
    font-weight: 500;
    font-size: 24px;
    line-height: 140%;
    color: #423E48;

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

}
</style>
