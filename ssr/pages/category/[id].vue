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
              <h1 class="content-block__title"> {{ categoryData.name }} </h1>
              <div class="content-block__subcategory recomendation__nav" v-if = "LastCategory?.length && viewType == 1">
                  <div class="slider_subcategory__row"
                    :class="[quickCategory.id == categoryId ? 'recomendation__nav__item active' : 'recomendation__nav__item']"
                    v-for = "quickCategory in LastCategory[0].subItems"
                    :key = "quickCategory.id"
                    @click.stop = setActiveCategory(quickCategory)
                  >
                    {{ quickCategory.name }}
                  </div>
              </div>
              <div v-if = "LastCategory?.length && viewType != 1">
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
              <div v-if = "viewType != 1" class="mobile-filter" @click.stop="setIsFilterPanelOpen(!isFilterPanelOpen)">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" data-v-50a3755b=""><line x1="2" y1="17.1133" x2="23" y2="17.1133" stroke="#423E48" stroke-width="1.25" data-v-50a3755b=""></line><line x1="23" y1="7.50391" x2="2" y2="7.5039" stroke="#423E48" stroke-width="1.25" data-v-50a3755b=""></line><circle cx="16.6619" cy="16.911" r="3.08088" fill="white" stroke="#423E48" stroke-width="1.25" data-v-50a3755b=""></circle><circle cx="8.33806" cy="7.70623" r="3.08088" transform="rotate(-180 8.33806 7.70623)" fill="white" stroke="#423E48" stroke-width="1.25" data-v-50a3755b=""></circle></svg>
              </div>
              <div v-if ="viewType != 1 && isFilterPanelOpen" class="mobile-filter__block">
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
              <div class="content-block__list" v-if = "itemsList">
                <div class="content-block__item product-row" v-if = "itemsList.length && catalogViewType === 'row'">
                  <CatalogListItem 
                    v-for   = "item in itemsList"
                    :key    = "item.id"
                    :card   = item
                  />
                </div>  
                <div class="content-block__item product-table" v-if = "itemsList.length && catalogViewType === 'table'">
                  <CatalogCardItem 
                    v-for   = "item in itemsList"
                    :key    = "item.id"
                    :card   = item
                  />
                </div>  
              </div>
              <div class="content-block__list" v-if = "!itemsList">
                <div class="empty_catalog">По вашему запросу ничего не найдено</div>
              </div>
              <div class="content-block__pagination">
                <CatalogPaginationPanel />
              </div>
              <div class="content-block__category_description" v-if = categoryData.site_page_seo_description>
                  <p v-safe-html = "categoryData.site_page_seo_description"></p>
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
  import { useQueryStore } from '@/stores/query';
  import { useHeaderStore } from '@/stores/header';
  import { useCatalogStore } from '@/stores/catalog';

  SwiperCore.use([Navigation, Pagination])

  const router = useRouter();
  const route = useRoute();
  const config = useRuntimeConfig();
  
  const queryStore = useQueryStore();
  const headerStore = useHeaderStore();
  const catalogStore = useCatalogStore();

  const isFilterPanelOpen = ref(false)

  const { catalogViewType, categoryId, typeOfProduct, offset, limit, sortType, sortDirection, minPrice, maxPrice } = storeToRefs(queryStore);
  const { viewType, categories, subCategories, subCategoriesItemActive } = storeToRefs(headerStore);
  const { itemsList, catalogSearchString, activePage, totalPages, category } = storeToRefs(catalogStore);

  const LastCategory = computed(() => {
    let result = [];
    if (subCategoriesItemActive.value && subCategories.value) {
        result = subCategories.value.filter(item => item.id === subCategoriesItemActive.value);
    }
    return result;
  });

  const categoryData = computed(() => {
    const category = categories.value.filter(item => item.id == categoryId.value)[0];
    return category ? category: null;
  });

  const prevLink = computed(() => {
    let href = null;
    if (activePage.value > 1) {
      const newOffset = (activePage.value - 2) * limit.value;
      href = queryStore.createUrl(newOffset);
    }
    return href ? config.public.NUXT_APP_DOCUMENTS.slice(0, -1) + href: null;
  });

  const nextLink = computed(() => {
    let href = null;
    if (activePage.value < totalPages.value) {
      const newOffset = (activePage.value) * limit.value;
      href = queryStore.createUrl(newOffset);
    }
    return  href ? config.public.NUXT_APP_DOCUMENTS.slice(0, -1) + href: null;
  });

  const createCanonicalLink = computed(() => {
    return config.public.NUXT_APP_DOCUMENTS.slice(0, -1) + '/category/' + categoryData?.value?.site_link
  });

  const setIsFilterPanelOpen = (data) => {
    isFilterPanelOpen.value = data
  };

  const clearSearchString= () => {
    queryStore.setSearchString('');
    catalogStore.setCatalogSearchString('');
    const url = queryStore.createUrl();
    router.push(url);
  };

  const setActiveCategory = (category) => {
    catalogStore.setCatalogSearchString('');
    queryStore.setDefaultPrices();
    queryStore.setTypeOfProduct('all');
    queryStore.setCategoryID(category.id);
    headerStore.setCurrentLastCategory(category.id);
    queryStore.setOffset(0);
    const url = queryStore.createUrl();
    router.push(url);
  }

  const redirectToNotFound = async () => {
    // console.log('Redirecting from category... ');
    if (process.server) {
      // console.log('From server');
      await router.push('/404', { redirectCode: 404 });
    } else {
      // console.log('From client');
      await navigateTo(route.fullPath, { redirectCode: 404 });
    }
  }

  const setParametersFromURL = async () => {
    let isFailInParams = false
    const currRoute = useRoute();
    const { query } = currRoute
    if (currRoute.params.id) {
      const isCategoryByLink = categories.value.filter(item => item.site_link?.toLowerCase() == currRoute.params.id)
      if (!isCategoryByLink.length) {
        await redirectToNotFound();
      } else {
        queryStore.setCategoryID(isCategoryByLink[0].id) 
      }
    } else {
      queryStore.setCategoryID(null) 
      await redirectToNotFound();
    }
    // console.log('After SetFromUrl ', categoryId.value);
    if (query.limit) {
      if (limit.value !== query.limit) queryStore.setLimit(query.limit);
    } else {
      queryStore.setLimit(12);
      isFailInParams = true
    }
    if (query.offset) {
      if (offset.value !== query.offset) queryStore.setOffset(query.offset);
    } else {
      queryStore.setOffset(0);
      isFailInParams = true;
    }
    if (query.actual_price_gte) {
      if (minPrice.value != query.actual_price_gte) {
        queryStore.setMinPrice(Number(query.actual_price_gte));
      }
    } else {
      isFailInParams = true
      queryStore.setMinPrice(0);
    }
    if (query.actual_price_lte) {
      if (maxPrice.value != query.actual_price_lte) {
        queryStore.setMaxPrice(Number(query.actual_price_lte));
      }
    } else {
      isFailInParams = true
      queryStore.setMaxPrice(80000);
    }
    if (query.q) {
      if (catalogSearchString.value !== query.q) {
        catalogStore.setCatalogSearchString(query.q);
        queryStore.setSearchString(query.q)
      } 
    } else {
      catalogStore.setCatalogSearchString('');
      queryStore.setSearchString('');
      isFailInParams = true
    }
    if (query.type_of_product) {
      if (typeOfProduct.value !== query.type_of_product) queryStore.setTypeOfProduct(query.type_of_product)
    } else {
      queryStore.setTypeOfProduct('all')
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
      if (sortType.value !== type) queryStore.setSortType(type);
      if (sortDirection.value !== direction) queryStore.setSortDirection(direction);
    } else {
      queryStore.setSortType('created_at');
      queryStore.setSortDirection('-');
      isFailInParams = true
    }
    // isFirstRender = false
  }

  const setBreabcrumbs = () => {
    if (categoryId.value === null) {
      return;
    }

    const categoryStack = [];

    let category = null
    if (categoryId.value) category = categories.value.filter(item => item.id == categoryId.value)[0].id;
    
    if (category) {
      categoryStack.push(category)

      let curLevel = categories.value.filter(item => item.id == category)[0]
      while (curLevel.parent_category_id) {
        const parent_category_id = curLevel.parent_category_id
        categoryStack.push(parent_category_id)
        curLevel = categories.value.filter(item => item.id == parent_category_id)[0]
      }
      // console.log('categoryStack ', categoryStack);
      
      if (categoryStack.length === 3) {
        headerStore.setAllCurrentCategories({
          mainCategory: categoryStack[2],
          middleCategory: categoryStack[1],
          lastCategory: categoryStack[0],
        });
      };
      if (categoryStack.length === 2) {
        headerStore.setAllCurrentCategories({
          mainCategory: categoryStack[1],
          middleCategory: categoryStack[0],
          lastCategory: null,
        });
      };
      if (categoryStack.length === 1) {
        headerStore.setAllCurrentCategories({
          mainCategory: categoryStack[0],
          middleCategory: null,
          lastCategory: null,
        });
      }; 
    }  
  }

  const loadCards = async () => {
    await catalogStore.getCatalogItems(categoryId.value);
    setBreabcrumbs();
  };

  await useAsyncData(
    async () => {
      // console.log('category start useAsyncData');
      
      await setParametersFromURL();
      if (categoryId.value) {
        await catalogStore.getCatalogItems(categoryId.value);
      } else {
        await redirectToNotFound();
      }
      setBreabcrumbs();
      return {
        catalogData: itemsList.value,
        category: category.value,
      }
    }, {
      watch: [route]
    }
  );

  useHead({
    title: categoryData?.value?.site_page_title,
    meta: [
      { name: 'description', content: categoryData?.value?.site_page_description },
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

  &__title{
    font-size: 30px;
  }

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
  &__category_description{
    margin-bottom: 20px;
    font-size: 0.875rem;
    line-height: 20px;

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