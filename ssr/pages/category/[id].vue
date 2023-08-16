<template>
  <div class="catalog app__content" @click.stop = "clearSearchString()">
    <Head>
      <Title>
        КабельТорг | {{ data?.category?.site_page_title }}
      </Title>
      <Meta name="discription" :content="data?.category?.site_page_description" />
    </Head>
    <div class="catalog__wrapper">
      <div class="catalog__content _container">
        <div class="catalog__body">

          <div class="catalog__block">

            <div v-if ="!isMobileVersion" class="catalog__sidebar filter">
              <CatalogFilterPanel />
            </div>
            <div class="content-block slider_subcategory__block">
              <div class="content-block__subcategory recomendation__nav" v-if = "LastCategory?.length && !isMobileVersion">
                  <div class="slider_subcategory__row"
                    :class="[quickCategory.id == store.getters['query/CATEGORY_ID'] ? 'recomendation__nav__item active' : 'recomendation__nav__item']"
                    v-for = "quickCategory in LastCategory[0].subItems"
                    :key = "quickCategory.id"
                    @click.stop = setActiveCategory(quickCategory)
                  >
                    {{ quickCategory.name }}
                  </div>
              </div>
              <div v-if = "LastCategory?.length && isMobileVersion">
                <swiper
                  :slides-per-view="2.7"
                  :space-between="12"
                  :speed="500"
                  :autoplay="{
                      delay: 5000,
                  }"
                  :pagination= "{
                    el: '.swiper-pagination',
                    clickable: false,
                    type: 'bullets',
                    bulletClass: 'swiper-pagination-bullet',
                    bulletElement: 'span',
                  }"
                >
                  <swiper-slide v-for="quickCategory in LastCategory[0].subItems" :key="quickCategory.id">
                    <div class="recomendation__nav__item" @click=setActiveCategory(quickCategory)>
                      {{ quickCategory.name }}
                    </div>
                  </swiper-slide>
                </swiper>
              </div>  
              <div v-if = "isMobileVersion" class="mobile-filter" @click.stop="setIsFilterPanelOpen(!isFilterPanelOpen)">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" data-v-50a3755b=""><line x1="2" y1="17.1133" x2="23" y2="17.1133" stroke="#423E48" stroke-width="1.25" data-v-50a3755b=""></line><line x1="23" y1="7.50391" x2="2" y2="7.5039" stroke="#423E48" stroke-width="1.25" data-v-50a3755b=""></line><circle cx="16.6619" cy="16.911" r="3.08088" fill="white" stroke="#423E48" stroke-width="1.25" data-v-50a3755b=""></circle><circle cx="8.33806" cy="7.70623" r="3.08088" transform="rotate(-180 8.33806 7.70623)" fill="white" stroke="#423E48" stroke-width="1.25" data-v-50a3755b=""></circle></svg>
              </div>
              <div v-if ="isMobileVersion&&isFilterPanelOpen" class="mobile-filter__block">
                <CatalogPriceSlider />
                <CatalogFilterPanel />
                <CatalogSortPanel />
                <CatalogLimitPanel />
              </div>
              <div v-if = "!isMobileVersion" class="content-block__topfilter topfilter">
                <CatalogSortPanel />
                <div class="topfilter__right flex-center">
                  <CatalogLimitPanel />
                  <CatalogViewPanel />
                </div>
              </div>
              <div class="content-block__list" v-if = "data?.catalogData">
                <div class="content-block__item product-row" v-if = "data?.catalogData?.length && store.getters['query/VIEW_TYPE'] === 'row'">
                  <CatalogListItem 
                    v-for   = "item in data?.catalogData"
                    :key    = "item.id"
                    :card   = item
                  />
                </div>  
                <div class="content-block__item product-table" v-if = "data?.catalogData?.length && store.getters['query/VIEW_TYPE'] === 'table'">
                  <CatalogCardItem 
                    v-for   = "item in data?.catalogData"
                    :key    = "item.id"
                    :card   = item
                  />
                </div>  
              </div>
              <div class="content-block__list" v-if = "!data?.catalogData?.length">
                <div class="empty_catalog">По вашему запросу ничего не найдено</div>
              </div>
              <div class="content-block__pagination">
                <CatalogPaginationPanel />
              </div>

            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>

  import { Swiper } from "swiper/vue";
  import { SwiperSlide } from "swiper/vue";
  import SwiperCore, { Pagination, Navigation } from "swiper"
  import "swiper/swiper.min.css"
  import store from '@/store'
  SwiperCore.use([Navigation, Pagination])

  const route = useRoute()
  const router = useRouter()
  const { getters } = store
  const isFilterPanelOpen = ref(false)
  const isMobileVersion = ref(false)
  
  const setIsFilterPanelOpen = (data) => {
    isFilterPanelOpen.value = data
  };

  watch(() => getters['header/DEVICE_VIEW_TYPE'],
    (curr, prev) => {
      setViewType(curr);
  });

  const setViewType = (curr) => {
    // console.log('isMoblile version ', curr);
      if (curr > 1) {
        isMobileVersion.value = true
      } else {
        isMobileVersion.value = false
      }
  }

  const LastCategory = computed(() => {
    let result = [];
    if (getters['header/SUB_CATEGORIES_ITEM_ACTIVE'] && getters['header/SUB_CATEGORIES']) {
        result = getters['header/SUB_CATEGORIES'].filter(item => item.id === getters['header/SUB_CATEGORIES_ITEM_ACTIVE']);
    }
    return result;
  })

  const ChangeParameters = computed(() => {
    return JSON.stringify(route.query) + JSON.stringify(route.params) + String(getters['query/CATEGORY_ID']) + JSON.stringify(getters['query/TYPE_OF_PRODUCT']) + 
      JSON.stringify(getters['query/SORT_TYPE']) + JSON.stringify(getters['query/SORT_DIRECTION']) + String(getters['query/MIN_PRICE']) + String(getters['query/MAX_PRICE']) +
      String(getters['query/OFFSET']) + String(getters['query/LIMIT']) + getters['header/SUB_CATEGORIES_ITEM_ACTIVE'] 
      + getters['catalog/ACTIVE_PAGE'] + getters['catalog/TOTAL_PAGES'];
      //  + getters['catalog/ITEMS_LIST'];
  })

  const clearSearchString= () => {
    store.commit("query/SET_SEARCH_STRING", '')
    store.commit("catalog/SET_CATALOG_SEARCH_STRING", '')
  }

  const getCategoryUrl = (id) => {
    let url = "/category/";
    if (id) {
        const link = getters['header/ALL_CATEGORIES'].filter(item => item.id == id)[0].site_link
        url = url + link;
      }
    url = url + getLastPartOfUrl();
    return url;
  }

  const getLastPartOfUrl = () => {
    let url = '?'
    if (getters['query/OFFSET'] != 0 || getters['query/LIMIT'] != 12) {
      url = url + "offset=" + getters['query/OFFSET'] + '&'
      url = url + "limit=" + getters['query/LIMIT'] + '&'
    }
    if (getters['query/TYPE_OF_PRODUCT'] !== 'all') {
      url = url + "type_of_product=" + getters['query/TYPE_OF_PRODUCT'] + '&'
    }
    if (getters['query/MIN_PRICE'] != 0 || getters['query/MAX_PRICE'] != 80000) {
      url = url + "actual_price_gte=" + getters['query/MIN_PRICE'] + '&'
      url = url + "actual_price_lte=" + getters['query/MAX_PRICE'] + '&'
    }
    if (getters['query/SORT_DIRECTION'] !== '-' || getters['query/SORT_TYPE'] !== 'created_at') {
      url = url + "ordering=" + getters['query/SORT_DIRECTION'] + getters['query/SORT_TYPE'] + '&'
    }
    const lastSymbol = url.slice(-1)
    if (lastSymbol === '&' || lastSymbol === '?') url = url.slice(0, -1)
    return url;        
  }

  const setActiveCategory = (category) => {
    store.commit('catalog/SET_CATALOG_SEARCH_STRING','')
    store.commit('query/SET_DEFAULT_PRICES')
    store.commit('query/SET_TYPE_OF_PRODUCT', 'all')
    store.commit('query/SET_CATEGORY_ID', category.id)
    store.commit('header/SET_CURRENT_LAST_CATEGORY', category.id)
    store.commit('query/SET_OFFSET', 0)
    const link = getCategoryUrl(category.id)
    router.push(link);
  }

  let isFirstRender = true;

  const setParametersFromURL = () => {
    let isFailInParams = false
    const currRoute = useRoute()
    const { query } = currRoute
    // console.log('SetForm URL ' ,currRoute.params, '   ', query);
    if (currRoute.params.id) {
      // console.log('Есть id ', currRoute.params.id);
      const isCategoryByLink = getters['header/ALL_CATEGORIES'].filter(item => item.site_link == currRoute.params.id)
      if (!isCategoryByLink) {
        store.commit('query/SET_CATEGORY_ID', null) 
      } else {
        store.commit('query/SET_CATEGORY_ID', isCategoryByLink[0].id) 
      }
    } else {
      // console.log('Нет id ', currRoute.params.id);
      store.commit('query/SET_CATEGORY_ID', null) 
    }
    // console.log('After SetFromUrl ', getters['query/CATEGORY_ID']);
    if (query.limit) {
      if (getters['query/LIMIT'] !== query.limit) store.commit('query/SET_LIMIT', query.limit)
    } else {
      store.commit('query/SET_LIMIT', 12)
      isFailInParams = true
    }
    if (query.offset) {
      if (getters['query/OFFSET'] !== query.offset) store.commit('query/SET_OFFSET', query.offset)
    } else {
      store.commit('query/SET_OFFSET', 0)
      isFailInParams = true
    }
    if (query.actual_price_gte) {
      if (getters['query/MIN_PRICE'] != query.actual_price_gte) {
        store.commit('query/SET_MIN_PRICE', Number(query.actual_price_gte))
      }
    } else {
      isFailInParams = true
      store.commit('query/SET_MIN_PRICE', 0)
    }
    if (query.actual_price_lte) {
      if (getters['query/MAX_PRICE'] != query.actual_price_lte) {
        store.commit('query/SET_MAX_PRICE', Number(query.actual_price_lte))
      }
    } else {
      isFailInParams = true
      store.commit('query/SET_MAX_PRICE', 80000)
    }
    if (query.q) {
      if (getters['catalog/CATALOG_SEARCH_STRING'] !== query.q) {
        store.commit('catalog/SET_CATALOG_SEARCH_STRING', query.q)
        store.commit('query/SET_SEARCH_STRING', query.q)
      } 
    } else {
      store.commit('catalog/SET_CATALOG_SEARCH_STRING', '')
      store.commit('query/SET_SEARCH_STRING', '')
      isFailInParams = true
    }
    if (query.type_of_product) {
      if (getters['query/TYPE_OF_PRODUCT'] !== query.type_of_product) store.commit('query/SET_TYPE_OF_PRODUCT', query.type_of_product)
    } else {
      store.commit('query/SET_TYPE_OF_PRODUCT', 'all')
      isFailInParams = true
    }
    if (query.ordering) {
      const total = query.ordering
      let direction = ''
      let type = ''
      if (total[0] === '-') {
        direction = '-'
        type = total.slice(1)
      } else {
        direction = ''
        type = total
      }
      if (getters['query/SORT_TYPE'] !== type) store.commit('query/SET_SORT_TYPE', type)
      if (getters['query/SORT_DIRECTION'] !== direction) store.commit('query/SET_SORT_DIRECTION', direction)
    } else {
      store.commit('query/SET_SORT_TYPE', 'created_at')
      store.commit('query/SET_SORT_DIRECTION', '-')
      isFailInParams = true
    }
    isFirstRender = false
  }

  const setBreabcrumbs = () => {
    const categoryStack = []
    const currRoute = useRoute()
    let category = null
    if (currRoute.params.id) category = getters['header/ALL_CATEGORIES'].filter(item => item.site_link == currRoute.params.id)[0].id

    if (category) {
      categoryStack.push(category)

      let curLevel = getters['header/ALL_CATEGORIES'].filter(item => item.id == category)[0]
      while (curLevel.parent_category_id) {
        const parent_category_id = curLevel.parent_category_id
        categoryStack.push(parent_category_id)
        curLevel = getters['header/ALL_CATEGORIES'].filter(item => item.id == parent_category_id)[0]
      }
      if (categoryStack.length === 3) {
        store.dispatch('header/SET_ALL_CURRENT_CATEGORIES', {
          mainCategory: categoryStack[2],
          middleCategory: categoryStack[1],
          lastCategory: categoryStack[0],
        });
      };
      if (categoryStack.length === 2) {
        store.dispatch('header/SET_ALL_CURRENT_CATEGORIES', {
          mainCategory: categoryStack[1],
          middleCategory: categoryStack[0],
          lastCategory: null,
        });
      };
      if (categoryStack.length === 1) {
        store.dispatch('header/SET_ALL_CURRENT_CATEGORIES', {
          mainCategory: categoryStack[0],
          middleCategory: null,
          lastCategory: null,
        });
      }; 
    }  
  }

  const { data } = await useAsyncData(
    'posts', 
    async () => {
      if (!store.getters['header/ALL_CATEGORIES'].length) {
        await store.dispatch('header/GET_CATEGORIES')
      }
      // console.log('id useAsyncData ' + store.getters['query/CATEGORY_ID']);
      if (isFirstRender) {
        setParametersFromURL()
      }
      // console.log('id useAsyncData after setFromUrl' + store.getters['query/CATEGORY_ID']);

      if (store.getters['query/CATEGORY_ID']) {
        const isCategoryData = store.getters['header/ALL_CATEGORIES'].filter(item => item.id == store.getters['query/CATEGORY_ID'])
        
        if (isCategoryData.length) {
          store.commit('catalog/SET_CATEGORY', isCategoryData[0])
        } else {
          store.commit('catalog/SET_CATEGORY', {})
        }

        await store.dispatch('catalog/GET_CATALOG_ITEMS', getters['query/CATEGORY_ID'])
        // setBreabcrumbs()
      }
      
      return {
        catalogData: store.getters['catalog/ITEMS_LIST'],
        category: store.getters['catalog/CATEGORY'],
      }
    }, {
      watch: [ChangeParameters]
    }
  )

  onUpdated(async () => {
    // console.log('id updated ' + store.getters['query/CATEGORY_ID']);
   
    if (!store.getters['header/ALL_CATEGORIES'].length) {
      await store.dispatch('header/GET_CATEGORIES')
    }
    if (store.getters['query/CATEGORY_ID']) {
      if (isFirstRender) {
        setParametersFromURL()
        const isCategoryData = store.getters['header/ALL_CATEGORIES'].filter(item => item.id == store.getters['query/CATEGORY_ID'])
        store.commit('catalog/SET_CATEGORY', isCategoryData[0])
        await store.dispatch('catalog/GET_CATALOG_ITEMS', getters['query/CATEGORY_ID'])
      }
      setViewType(getters['header/DEVICE_VIEW_TYPE'])
      setBreabcrumbs()
    }  
    // console.log('mount category');
  })

  onBeforeMount(async () => {
    if (!store.getters['header/ALL_CATEGORIES'].length) {
      await store.dispatch('header/GET_CATEGORIES')
    }
    setParametersFromURL()
    const isCategoryData = store.getters['header/ALL_CATEGORIES'].filter(item => item.id == store.getters['query/CATEGORY_ID'])
    if (isCategoryData.length) {
      store.commit('catalog/SET_CATEGORY', isCategoryData[0])
    } else {
      store.commit('catalog/SET_CATEGORY', {})
    }
    setViewType(getters['header/DEVICE_VIEW_TYPE'])
    await store.dispatch('catalog/GET_CATALOG_ITEMS', getters['query/CATEGORY_ID'])
    setBreabcrumbs()
    // console.log('update category');
  })

</script>

<style scoped lang="scss">

.swiper-pagination, .swiper-pagination-clickable, .swiper-pagination-bullets, .swiper-pagination-horizontal {
  display: flex;
  position: inherit;
  align-items: center;
  justify-content: center;
  gap: 10px;
  margin-top: 20px;

  span {
    //background: #7700AF;
    background:red;
  }
}
.swiper-pagination-bullet, .swiper-pagination-bullet-active{
  background: black!important

}
.swiper-pagination-bullet-active{
  background: red!important;
}

.catalog {

  &__wrapper{

  }
  &__content{

  }

  &__body{
  }



  &__item{


  }
  &__block{
    display: flex;
    align-items: flex-start;

}
  &__sidebar{
    min-width: 260px;
    width: 272px;
    padding-right: 10px;
     @media (max-width:$md2+px) {
       display: none;
     }
  }

}
.content-block{
  width: 100%;

  &__subcategory{
    display: grid;
    gap: 10px;
    grid-template-columns: repeat(3, minmax(0, 300px));
    text-align: center;
    //padding: 24px 20px 20px 0;

    .recomendation__nav__item{
      background: #FFFFFF;
      border: 1px solid rgba(0, 0, 0, 0.05);
      border-radius: 50px;
      font-size: 14px;
      line-height: 24px;
      text-align: center;
      opacity: 0.5;
      margin-right: 10px;
      padding: 6px 20px;
      //max-width: 25%;
      text-overflow: ellipsis;
      white-space: nowrap;
      overflow: hidden;
      transition: all 0.5s ease;
      cursor: pointer;
      a{
        color: #423E48;
      }
      @media (max-width: $md2+px) {
        background: #dedede;
        opacity: 0.6;
      }

      &:hover{
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.08);
        color:#4275D8;
        font-weight: 500;
        opacity: 1;
      }
    }

  }
  &__pagination{
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    padding: 20px 0;
  }
  &__item{
    display: flex;
    flex-direction: column;
    gap:16px;
  }

  &__topfilter{
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 0;
    font-size: 12px;
  }

  .mobile-filter{
    border: 2px solid rgba(0, 0, 0, 0.05);
    border-radius: 50%;
    width: 40px;
    height: 40px;
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 20px 0;
    &:hover{
      background: #dedede;
    }
    &__block{
      margin-bottom: 15px;
    }


  }

  .empty_catalog{
    width: 100%;
    padding: 10px 0;
    text-align: center;
  }


}

.topfilter{

  &__right{

  }
  &__box-view{
    margin-right: 15px;
    font-size: 20px;
  }
  &__row-view{
    font-size: 20px;

  }
  .active{
    opacity: 0.5;
  }

}

.product-table{
  display: grid;
  width: 100%;
  grid-template-columns: repeat(3, minmax(242px, 272px));
  grid-template-rows: auto;
  gap: 10px;
  @media (max-width: 1089px) {
    grid-template-columns: repeat(2, minmax(142px, 272px));
  }
  .item-card{
    //min-width: 270px;
  }
}

.slider_subcategory__block{
  max-width: 100%;
}

//.slider_subcategory__row{
//  margin: 10px 0;
//}
.recomendation__nav__item{
  background: #FFFFFF;
  border: 1px solid rgba(0, 0, 0, 0.05);
  border-radius: 50px;
  font-size: 11px;
  line-height: 24px;
  text-align: center;
  opacity: 0.5;
  margin-right: 10px;
  padding: 0px 20px;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
  //max-width: 180px;
  transition: all 0.5s ease;
  cursor: pointer;
  @media (max-width: $md2+px) {
    background: #dedede;
    opacity: 0.6;
  }

}
.recomendation__nav .active {
  color: #4275D8;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.08);
  opacity: 1;
  font-weight: 600;

}
</style>