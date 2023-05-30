<template>
  <div class="catalog" @click.stop = "clearSearchString()">
    <div class="catalog__wrapper">
      <div class="catalog__content _container">
        <div class="catalog__body">

          <div class="catalog__block">

            <div v-if ="!isMobileVersion" class="catalog__sidebar filter">
              <CatalogFilterPanel />
            </div>
            <div class="content-block slider_subcategory__block">
              <div v-if = "isMobileVersion" class="mobile-filter" @click.stop="setIsFilterPanelOpen(!isFilterPanelOpen)">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" data-v-50a3755b=""><line x1="2" y1="17.1133" x2="23" y2="17.1133" stroke="#423E48" stroke-width="1.25" data-v-50a3755b=""></line><line x1="23" y1="7.50391" x2="2" y2="7.5039" stroke="#423E48" stroke-width="1.25" data-v-50a3755b=""></line><circle cx="16.6619" cy="16.911" r="3.08088" fill="white" stroke="#423E48" stroke-width="1.25" data-v-50a3755b=""></circle><circle cx="8.33806" cy="7.70623" r="3.08088" transform="rotate(-180 8.33806 7.70623)" fill="white" stroke="#423E48" stroke-width="1.25" data-v-50a3755b=""></circle></svg>
              </div>
              <div v-if ="isMobileVersion&&isFilterPanelOpen">
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
              <div class="content-block__list">
                <div class="content-block__item product-row" v-if = "catalogData?.length && store.getters['query/VIEW_TYPE'] === 'row'">
                  <CatalogListItem 
                    v-for   = "item in catalogData"
                    :key    = "item.id"
                    :card   = item
                  />
                </div>  
                <div class="content-block__item product-table" v-if = "catalogData.length && store.getters['query/VIEW_TYPE'] === 'table'">
                  <CatalogCardItem 
                    v-for   = "item in catalogData"
                    :key    = "item.id"
                    :card   = item
                  />
                </div>  
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

  import store from '@/store'

  const route = useRoute()
  const { getters } = store
  const isFilterPanelOpen = ref(false)
  const isMobileVersion = ref(false)

  useHead({
    title: 'Каталог',
    name: 'Каталог',
    meta: [{
      name: 'Каталог',
      content: 'Каталог товаров'
    }]
  })

  const setIsFilterPanelOpen = (data) => {
    isFilterPanelOpen.value = data
  };

  watch(() => getters['header/DEVICE_VIEW_TYPE'],
    (curr, prev) => {
      setViewType(curr);
  });

  const setViewType = (curr) => {
      if (curr > 1) {
        isMobileVersion.value = true
      } else {
        isMobileVersion.value = false
      }
  }

  const ChangeParameters = computed(() => {
    return JSON.stringify(route.query) + JSON.stringify(store.getters['catalog/ITEMS_LIST'])
  })

  const clearSearchString= () => {
    store.commit("query/SET_SEARCH_STRING", '')
    store.commit("catalog/SET_CATALOG_SEARCH_STRING", '')
  }

  let isFerstRender = true;

  const setParametersFromURL = () => {
    let isFailInParams = false
    const currRoute = useRoute()
    const { query } = currRoute
    if (query.limit) {
      if (getters['query/LIMIT'] !== query.limit) store.commit('query/SET_LIMIT', query.limit)
    } 
    else {
      isFailInParams = true
    }
    if (query.offset) {
      if (getters['query/OFFSET'] !== query.offset) store.commit('query/SET_OFFSET', query.offset)
    } else {
      isFailInParams = true
    }
    if (query.actual_price_gte) {
      if (getters['query/MIN_PRICE'] !== query.actual_price_gte) store.commit('query/SET_MIN_PRICE', query.actual_price_gte)
    } else {
      isFailInParams = true
    }
    if (query.actual_price_lte) {
      if (getters['query/MAX_PRICE'] !== query.actual_price_lte) store.commit('query/SET_MAX_PRICE', query.actual_price_lte)
    } else {
      isFailInParams = true
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
      isFailInParams = true
    }
    if (query.ordering) {
      const total = query.ordering;
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
      // store.commit('query/SET_SORT_TYPE', getters['query/SORT_TYPE'])
      // store.commit('query/SET_SORT_DIRECTION', getters['query/SORT_DIRECTION'])
      isFailInParams = true
    }
    isFerstRender = false
  }

  const setBreabcrumbs = () => {
    store.dispatch('header/SET_ALL_CURRENT_CATEGORIES', {
      mainCategory: null,
      middleCategory: null,
      lastCategory: null,
    });
    return;
  }

  const { data: catalogData } = await useAsyncData(
    'posts', 
    async () => {
      console.log('UseAsyncData catalog ');
      if (isFerstRender) {
        setParametersFromURL()
      }
      await store.dispatch('catalog/GET_ALL_CATALOG_ITEMS')
      return store.getters['catalog/ITEMS_LIST']
    }, {
      watch: [ChangeParameters]
    }
  )

  onBeforeMount(async () => {
    setParametersFromURL()
    await store.dispatch('catalog/GET_ALL_CATALOG_ITEMS')
    setViewType(getters['header/DEVICE_VIEW_TYPE'])
    setBreabcrumbs()
  })

  onBeforeUpdate(async () => {
    setParametersFromURL()
    await store.dispatch('catalog/GET_ALL_CATALOG_ITEMS')
    setBreabcrumbs()
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
  @media (max-width: $md2+px) {
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

}
.recomendation__nav .active {
  color: #4275D8;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.08);
  opacity: 1;
  font-weight: 600;

}
</style>