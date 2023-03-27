<template>
  <div class="news">
    <div class="news__wrapper">
      <div class="news__content _container">
        <div class="news__body">
          <div class="news__block">
            <NewsItem
              v-for = "oneNew in NEWS"
              :key = "oneNew.id"
              :data = "oneNew"
            />
          </div>
        </div>
        <div class="news__button">
          <button class="btn empty_black"> Все новости</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex';
  import NewsItem from '@/components/news/news-item.vue'

  export default {
    name: 'News',

    components: {
      NewsItem,
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
      this.$store.dispatch("breadcrumb/CHANGE_BREADCRUMB", 0);
      this.$store.commit('breadcrumb/ADD_BREADCRUMB', {
        name: this.$router.currentRoute.value.meta.name,
        path: this.$router.currentRoute.value.path,
        type: "global",
        class: ""
      });
      await this.GET_NEWS();
    }
  }
</script>

<style scoped lang="scss">

.news {

  &__wrapper{


  }
  &__content{
    padding: 20px 0 30px 0;
  }

  &__body{



  }
  &__header{


  }
  &__block{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-column-gap: 20px;
    grid-row-gap: 20px;
    padding:20px 0 60px 0;

    @media (max-width: $md2+px) {
      grid-template-columns: repeat(1, 1fr);
    }

  }
  &__button{
    text-align:center ;
  }
}


</style>
