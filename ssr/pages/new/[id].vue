<template>
  <div class="_container">
    <Head>
      <Title>
        КабельТорг | {{ oneNewData?.title }}
      </Title>
      <Meta name="discription" :content="oneNewData?.title" />
    </Head>

    <div class="one-news__block app__content" v-if="oneNewData">
      <a class="one-news__item">
          <div class="one-news__img">
              <UiCardImage :images = "oneNewData.image" />
          </div>

          <div class="one-news__title ">{{ oneNewData.title }}</div>
          <div class="one-news__content">
              <div v-html = "oneNewData.content"></div>
          </div>
      </a>

      <div class="one-news__btns">
        <div class="btn empty" @click.stop="onMoveToAllNews">Все новости</div>
      </div>

      <SliderNews />
    </div>

  </div>
</template>

<script setup>
  import axios from 'axios';
  import store from '@/store'

  // useHead({
  //   title: 'Кабельторг | ' + oneNewData.value.name,
  //   name: oneNewData.value.name,
  //   meta: [{
  //     name: oneNewData.value.name,
  //     content: 'Страница ' + oneNewData.value.name,
  //   }]
  // })

  const route = useRoute()
  const router = useRouter()

  const ChangeParameters = computed(() => {
    return JSON.stringify(route.query) + JSON.stringify(route.params);
  })

  const onMoveToAllNews = () => {
    router.push('/news');
  }

  const onSetBreadCrumbs = () => {
    store.dispatch('breadcrumb/CHANGE_BREADCRUMB', 0);
    const mainBreadCrumb = {
      name: 'Новости',
      path: '/news',
      type: 'global',
      class: '',
    }
    store.commit('breadcrumb/ADD_BREADCRUMB', mainBreadCrumb);

    store.commit('breadcrumb/ADD_BREADCRUMB', {
      name: oneNewData.value.title,
      path: route.path,
      type: "global",
      class: ""
    });
  }

  const { data: oneNewData } = await useAsyncData(
    'oneNewData', 
    async () => {
      store.commit('notification/SET_IS_LOADING', true)
      try {
        const response = await axios.get(useRuntimeConfig().public.NUXT_APP_API_URL + 'service_entities/articles/' + route.params.id);
        store.commit('notification/SET_IS_LOADING', false)
        return response.data;
      } catch (e) {
          console.log(e);
          // store.commit('notification/ADD_MESSAGE',{name: "Не возможно загрузить новость ", icon: "error", id: '1'})
          store.commit('notification/SET_IS_LOADING', false)
          return null
      }
    }, {
      watch: [ChangeParameters]
    }
  )

  onMounted(async () => {
    onSetBreadCrumbs()
  })

  onUpdated(() => {
    onSetBreadCrumbs()
  })

</script>

<style lang="scss" scoped>
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

<style lang="scss">
.one-news__img img{
  width: 100%;


}
.one-news__block .news__content{
  padding: 0 0;
}
</style>