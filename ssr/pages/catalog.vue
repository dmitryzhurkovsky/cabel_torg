<template>
  <Breadcrumb/>
  <div class="catalog app__content" @click.stop = "clearSearchString()">
    <div class="catalog__wrapper">
      <div class="catalog__content _container">
        <div class="catalog__body">

          <div class="catalog__block">

            <div v-if ="viewType == 1" class="catalog__sidebar filter">
              <CatalogFilterPanel 
                  @onFilterChanged="loadCards"
              />
            </div>
            <div class="content-block slider_subcategory__block">
              <h1 class="content-block__title"> Каталог </h1>
              <div v-if = "viewType != 1" class="mobile-filter" @click.stop="setIsFilterPanelOpen(!isFilterPanelOpen)">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" data-v-50a3755b=""><line x1="2" y1="17.1133" x2="23" y2="17.1133" stroke="#423E48" stroke-width="1.25" data-v-50a3755b=""></line><line x1="23" y1="7.50391" x2="2" y2="7.5039" stroke="#423E48" stroke-width="1.25" data-v-50a3755b=""></line><circle cx="16.6619" cy="16.911" r="3.08088" fill="white" stroke="#423E48" stroke-width="1.25" data-v-50a3755b=""></circle><circle cx="8.33806" cy="7.70623" r="3.08088" transform="rotate(-180 8.33806 7.70623)" fill="white" stroke="#423E48" stroke-width="1.25" data-v-50a3755b=""></circle></svg>
              </div>
              <div v-if ="viewType != 1&&isFilterPanelOpen">
                <CatalogPriceSlider
                    @onPriceChanged="loadCards"
                />
                <CatalogFilterPanel 
                    @onFilterChanged="loadCards"
                />
                <CatalogSortPanel 
                    @onSortChanged="loadCards"
                />
                <CatalogLimitPanel 
                    @onLimitChanged="loadCards"
                />
              </div>
              <div v-if = "viewType == 1" class="content-block__topfilter topfilter">
                <CatalogSortPanel 
                    @onSortChanged="loadCards"
                />
                <div class="topfilter__right flex-center">
                  <CatalogLimitPanel 
                      @onLimitChanged="loadCards"
                  />
                  <CatalogViewPanel/>
                </div>
              </div>
              <div class="content-block__list">
                <div class="content-block__item product-row" v-if = "itemsList?.length && catalogViewType === 'row'">
                  <CatalogListItem 
                    v-for   = "item in itemsList"
                    :key    = "item.id"
                    :card   = item
                  />
                </div>  
                <div class="content-block__item product-table" v-if = "itemsList?.length && catalogViewType === 'table'">
                  <CatalogCardItem 
                    v-for   = "item in itemsList"
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
  import { ref, computed } from 'vue';
  import { useQueryStore } from '@/stores/query';
  import { useHeaderStore } from '@/stores/header';
  import { useCatalogStore } from '@/stores/catalog';

  const route = useRoute();
  const config = useRuntimeConfig();
  
  const queryStore = useQueryStore();
  const headerStore = useHeaderStore();
  const catalogStore = useCatalogStore();

  const isFilterPanelOpen = ref(false);

  const { catalogViewType, categoryId, typeOfProduct, offset, limit, sortType, sortDirection, minPrice, maxPrice } = storeToRefs(queryStore);
  const { viewType } = storeToRefs(headerStore);
  const { itemsList, catalogSearchString, activePage, totalPages } = storeToRefs(catalogStore);

  const setIsFilterPanelOpen = (data) => {
    isFilterPanelOpen.value = data
  };

  const prevLink = computed(() => {
    let href = null;
    if (activePage.value > 1) {
      const newOffset = (activePage.value - 2) * limit.value;
      href = queryStore.createUrl(newOffset);
    }
    return href ? config.public.NUXT_APP_DOCUMENTS.slice(0, -1) + href: null;
  })

  const nextLink = computed(() => {
    let href = null;
    if (activePage.value < totalPages.value) {
      const newOffset = (activePage.value) * limit.value;
      href = queryStore.createUrl(newOffset);
    }
    return  href ? config.public.NUXT_APP_DOCUMENTS.slice(0, -1) + href: null;
  })

  const createCanonicalLink = computed(() => {
    return config.public.NUXT_APP_DOCUMENTS.slice(0, -1) + '/catalog';
  });

  const clearSearchString= () => {
    queryStore.setSearchString('');
    catalogStore.setCatalogSearchString('')
  }

  const setParametersFromURL = () => {
    let isFailInParams = false
    const currRoute = useRoute()
    const { query } = currRoute
    queryStore.setCategoryID(null);

    if (query.limit) {
      if (limit.value !== query.limit) queryStore.setLimit(query.limit)
    } else {
      queryStore.setLimit(12);
      isFailInParams = true
    }
    if (query.offset) {
      if (offset.value !== query.offset) queryStore.setOffset(query.offset)
    } else {
      queryStore.setOffset(0);
      isFailInParams = true
    }
    if (query.actual_price_gte) {
      if (minPrice.value != query.actual_price_gte) {
        queryStore.setMinPrice(Number(query.actual_price_gte))
      }
    } else {
      isFailInParams = true
      queryStore.setMinPrice(0)
    }
    if (query.actual_price_lte) {
      if (maxPrice.value != query.actual_price_lte) {
        // console.log('Before set MAX from URL ', Number(query.actual_price_lte));
        queryStore.setMaxPrice(Number(query.actual_price_lte))
        // console.log('Max is not equal, set it', maxPrice.value);
      }
    } else {
      isFailInParams = true
      queryStore.setMaxPrice(80000);
    }
    if (query.q) {
      if (catalogSearchString.value !== query.q) {
        catalogStore.setCatalogSearchString(query.q);
        queryStore.setSearchString(query.q);
      } 
    } else {
      catalogStore.setCatalogSearchString('');
      queryStore.setSearchString('');
      isFailInParams = true;
    }
    if (query.type_of_product) {
      if (typeOfProduct.value !== query.type_of_product) queryStore.setTypeOfProduct(query.type_of_product);
    } else {
      queryStore.setTypeOfProduct('all');
      isFailInParams = true;
    }
    if (query.ordering) {
      const total = query.ordering;
      let direction = '';
      let type = '';
      if (total[0] === '-') {
        direction = '-'
        type = total.slice(1);
      } else {
        direction = '';
        type = total;
      }
      if (sortType.value !== type) queryStore.setSortType(type);
      if (sortDirection.value !== direction) queryStore.setSortDirection(direction);
    } else {
      queryStore.setSortType('created_at');
      queryStore.setSortDirection('-');
      isFailInParams = true;
    }
  }

  const setBreabcrumbs = () => {
    headerStore.setAllCurrentCategories({
      mainCategory: null,
      middleCategory: null,
      lastCategory: null,
    });
    return;
  };

  const loadCards = async () => {
    await catalogStore.getAllCatalogItems();
    setBreabcrumbs();
  };

  const redirectToNotFound = () => {
    console.log('Redirecting...');
    if (process.server) {
      console.log('From server');
      router.push('/404', { redirectCode: 404 });
    } else {
      console.log('From client');
      navigateTo(route.fullPath, { redirectCode: 404 });
    }
  }

  await useAsyncData(
    async () => {
      setParametersFromURL();
      if (!categoryId.value) {
        await catalogStore.getAllCatalogItems();
      } else {
        redirectToNotFound();
      }
      setBreabcrumbs();
      return itemsList.value
    }, {
      watch: [route]
    }
  );

  useHead({
    title: 'Каталог',
    meta: [
      { name: 'description', content: 'Каталог товаров' },
    ],
    link: [
      ...(prevLink.value ? [{ rel: 'prev', href: prevLink.value }] : []),
      ...(nextLink.value ? [{ rel: 'next', href: nextLink.value }] : []),
      { rel: 'canonical', href: createCanonicalLink.value },
    ],
  });

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

      @media (max-width: $md2+px) {
          background: #dedede;
          padding: 2px 0;
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


  }

}

.topfilter{

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
.content-block__title{
  font-size: 30px;
}

</style>