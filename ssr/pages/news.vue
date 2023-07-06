<template>
  <div class="news app__content">
    <div class="news__wrapper">
      <div class="news__content _container">
        <div class="news__body">
          <div class="news__block">
            <NewsItem
              v-for = "oneNew in paginatedNews"
              :key = "oneNew.id"
              :data = "oneNew"
            />
          </div>
        </div>
        <div v-if = "NEWS.length > itemsInPage" class="news__pagination">
          <a 
              :class="[pageNumber > 1 ? 'news__link active' : 'news__link']"
              @click="onChangePage(pageNumber - 1)"
          >{{ '<' }}</a>
          <a class="news__link news__pagenumber">{{ pageNumber }}</a>
          <a 
              :class="[pageNumber < totalPages ? 'news__link active' : 'news__link']"
              @click="onChangePage(pageNumber + 1)"
          >{{ '>' }}</a>
        </div>   
      </div>
    </div>
  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex';

  definePageMeta({
    // middleware: ["auth"],
    name: 'Новости',
  });

  export default defineNuxtComponent({
    name: 'News',

    head () {
      return {
        title: 'Кабельторг | Новости',
        meta: [{
          name: 'Новости',
          content: 'Страница Новости'
        }]
      }
    },
    
    data: function(){
      return{
        pageNumber : 1,
        totalPages: 1,
        itemsInPage: 20,
      }
    },

    computed: {
      ...mapGetters("main", ["NEWS"]),

      paginatedNews() {
        const startPosition = (this.pageNumber - 1) * this.itemsInPage;
        return this.NEWS.slice(startPosition, startPosition + this.itemsInPage);
      }
    },

    methods: {
      ...mapActions("main", ["GET_NEWS"]),

      setPages(){
        this.totalPages = Math.ceil(this.NEWS.length / this.itemsInPage);
      },

      onChangePage(page) {
        if (page < 1) return
        if (page > this.totalPages) return
        this.pageNumber = page;
        setTimeout(() => window.scrollTo(0, 0), 0);
      }
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
      this.setPages();
    }
  })
</script>

<style scoped lang="scss">

.news {
  &__content{
    padding-bottom: 30px;
  }
  &__pagination{
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    padding: 20px 0;
  }
  &__pagenumber{
    background: #4275D8 !important;
    color: #fff;
  }
  &__link{
    width: 40px;
    height: 40px;
    background: rgba(66, 62, 72, 0.07);
    border-radius: 2px;
    display: flex;
    align-items: center;
    justify-content: center;
    // color: #423E48;
    transition: all 0.3s ease;
  }
  .active{
    background: #4275D8;
    color: #fff;
      &:hover{
        border: 1.2px solid #4275D8;
        cursor: pointer;
      }
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
