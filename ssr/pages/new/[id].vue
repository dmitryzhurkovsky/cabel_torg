<template>
  <Breadcrumb/>
  <div class="news-content">
    <div class="one-news__block app__content _container" v-if="data">
      <a class="one-news__item">
          <div class="one-news__img">
              <UiCardImage :images = "'/' + data.image" />
          </div>

          <div class="one-news__title ">{{ data.title }}</div>
          <div class="one-news__content">
            <ClientOnly>
              <div v-html = "data.content"></div>
            </ClientOnly>
          </div>
      </a>
      <div class="one-news__btns">
        <div class="btn empty" @click.stop="onMoveToAllNews">Все новости</div>
      </div>
    </div>
    <!-- <SliderNews /> -->
  </div>
</template>

<script setup>
  import axios from '@/utils/api';
  import { useNotificationsStore } from '@/stores/notifications';
  import { useBreadCrumbStore } from '@/stores/breadcrumb';

  const route = useRoute();
  const router = useRouter();
  const config = useRuntimeConfig();

  const notificationsStore = useNotificationsStore();
  const breadCrumbStore = useBreadCrumbStore();

  const oneNewData = ref(null);

  const ChangeParameters = computed(() => {
    return JSON.stringify(route.query) + JSON.stringify(route.params);
  });

  const createCanonicalLink = computed(() => {
    return config.public.NUXT_APP_DOCUMENTS.slice(0, -1) + '/new/' + route.params.id;
  });

  const onMoveToAllNews = () => {
    router.push('/news');
  };

  const setBreadCrumbs = () => {
    breadCrumbStore.changeBreadCrumb(0);
    const mainBreadCrumb = {
      name: 'Новости',
      path: '/news',
      type: 'global',
      class: '',
    }
    breadCrumbStore.addBreadCrumb(mainBreadCrumb);

    breadCrumbStore.addBreadCrumb({
      name: oneNewData.value.title,
      path: route.path,
      type: "global",
      class: ""
    });
  };



  const redirectToNotFound = async () => {
    console.log('Redirecting...');
    if (process.server) {
      console.log('From server');
      router.push('/404', { redirectCode: 404 });
    } else {
      console.log('From client');
      navigateTo(route.fullPath, { redirectCode: 404 });
    }
  }

  const oneGetData = async () => {
    notificationsStore.setIsLoading(true);
    try {
      const response = await axios.get(useRuntimeConfig().public.NUXT_APP_API_URL + 'service_entities/articles/' + route.params.id);
      console.log('response ', response);
      
      oneNewData.value = response.data;
      notificationsStore.setIsLoading(false);
    } catch (e) {
      console.log(e);
      notificationsStore.setIsLoading(false);
      await redirectToNotFound();
    }
  } 

  const { data } = await useAsyncData(
    async () => {
      await oneGetData();
      setBreadCrumbs();
      return oneNewData.value
    }, {
      watch: [ChangeParameters]
    }
  )

  useHead({
    title: ' КабельТорг | ' + data?.value?.title,
    meta: [
      { name: 'description', content: data?.value?.title },
    ],
    link: [
      { rel: 'canonical', href: createCanonicalLink.value },
    ],
  });
</script>

<style lang="scss" scoped>
.news-content{
  flex-grow: 1;
}
.one-news{
  &__img{
    height: 200px;
    display: block;
    margin: 20px 0;
    img{
      width: 100%;
      object-fit: cover;
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
