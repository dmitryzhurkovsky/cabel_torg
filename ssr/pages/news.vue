<template>
  <Breadcrumb/>
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
        <div v-if = "paginatedNews.length > itemsInPage" class="news__pagination">
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

<script setup>
  import { useHead } from 'nuxt/app';
  import { ref, computed } from 'vue';
  import { useMainStore } from '@/stores/main';
  import { useBreadCrumbStore } from '@/stores/breadcrumb';

  const router = useRouter();
  const route = useRoute();
  const config = useRuntimeConfig();

  const mainStore = useMainStore();
  const breadCrumbStore = useBreadCrumbStore();

  const { news } = storeToRefs(mainStore);

  const pageNumber = ref(1);
  const totalPages = ref(1);
  const itemsInPage = ref(20);

  const createCanonicalLink = computed(() => {
    return config.public.NUXT_APP_DOCUMENTS.slice(0, -1) + route.path;
  });

  useHead({
    title: 'Кабельторг | Новости',
    meta: [{
      name: 'Новости',
      content: 'Страница Новости'
    }],
    link: [
      { rel: 'canonical', href: createCanonicalLink.value },
    ],
  });
    
  const paginatedNews = computed(() => {
    const startPosition = (pageNumber.value - 1) * itemsInPage.value;
    return news.value.slice(startPosition, startPosition + itemsInPage.value);
  });

  const setPages = () => {
    totalPages.value = Math.ceil(news.value.length / itemsInPage.value);
  };

  const onChangePage = (page) => {
    if (page < 1) return
    if (page > totalPages.value) return
    pageNumber.value = page;
    setTimeout(() => window.scrollTo(0, 0), 0);
  };

  await useAsyncData(
    async () => {
      breadCrumbStore.changeBreadCrumb(0);
      breadCrumbStore.addBreadCrumb({
        name: 'Новости',
        path: router.currentRoute.value.path,
        type: "global",
        class: ""
      });

      await mainStore.getNews();
      setPages();
      return news;
    }
  )
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
