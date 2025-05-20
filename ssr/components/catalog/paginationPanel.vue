<template>
    <div v-if = "Pages.length" class="content-block__pagination">
      <a 
          :class="[item.pageNumber === activePage ? 'pagination_link active' : 'pagination_link']"
          v-for = "item in Pages"
          :key = "item.name"
          @click.prevent="onChangePage(item)"
          :href = createHref(item)
      >
        {{ item.name }}
      </a>
    </div>   
</template>

<script setup>
  import { computed } from 'vue';
  import { useCatalogStore } from '@/stores/catalog';
  import { useQueryStore } from '@/stores/query';
  import { useHeaderStore } from '@/stores/header';

  const router = useRouter();

  const queryStore = useQueryStore();
  const catalogStore = useCatalogStore();
  const headerSore = useHeaderStore();

  const { categoryId, typeOfProduct, limit, sortType, sortDirection, minPrice, maxPrice, searchString } = storeToRefs(queryStore);
  const { activePage, totalPages } = storeToRefs(catalogStore);
  const { categories } = storeToRefs(headerSore);

  const Pages = computed(() => {
    // console.log('Pages ', activePage.value, '  ',  totalPages.value);
    let result = []
    const firstLink = { name: '<', pageNumber: activePage.value - 1, isAvailable: activePage.value !== 1 }

    result.push(firstLink)
    if (totalPages.value > 7) {
      // console.log('', totalPages, activePage);
      let left = activePage.value;
      let right = totalPages.value - activePage.value;
      
      if (left < 4) {
        for (let i = 1; i < left; i++){
          const curLink = {
            name: i,
            pageNumber: i,
            isAvailable: activePage.value !== i
          }
          result.push(curLink)
        }
      } else {
        const firstLink = {
          name: 1,
          pageNumber: 1,
          isAvailable: activePage.value !== 1
        }
        result.push(firstLink)
        const dots = {
          name: '...',
          pageNumber: activePage.value - 2,
          isAvailable: true
        }
        result.push(dots)
        const curLink = {
          name: activePage.value - 1,
          pageNumber: activePage.value - 1,
          isAvailable: true
        }
        result.push(curLink)
      }

      const center = {
        name: activePage.value,
        pageNumber: activePage.value,
        isAvailable: false
      }
      result.push(center)


      if (right > 4) {
        const firstLink = {
          name: activePage.value + 1,
          pageNumber: activePage.value + 1,
          isAvailable: true
        }
        result.push(firstLink)
        const dots = {
          name: '...',
          pageNumber: activePage.value + 2,
          isAvailable: true
        }
        result.push(dots)
        const curLink = {
          name: totalPages.value,
          pageNumber: totalPages.value,
          isAvailable: true
        }
        result.push(curLink)
      } else {
        for (let i = activePage.value + 1; i <= right ; i++){
          const curLink = {
            name: i,
            pageNumber: i,
            isAvailable: activePage.value !== i
          }
          result.push(curLink)
        }
      }

    } else {
      for (let i = 1; i <= totalPages.value; i++) {
        const curLink = {
          name: i,
          pageNumber: i,
          isAvailable: activePage.value !== i
        }
        result.push(curLink)
      }
    }
    const lastLink = { name: '>', pageNumber: activePage.value + 1, isAvailable: activePage.value < totalPages.value }
    result.push(lastLink)
    return result
  })

  const createHref = (item) =>{
    let URL = ''
    const newOffset = (item.pageNumber === 0 ? 0 : (item.pageNumber - 1)) * limit.value
    if (categoryId.value) {
      URL = getCategoryUrl(categoryId.value, newOffset)
    } else {
      URL = getCatalogUrl(newOffset)
    }
    return URL
  }

  const getCatalogUrl = (offset) => {
    let url = "/catalog"
    url = url + getLastPartOfUrl(offset)
    return url
  }

  const getCategoryUrl = (id, offset) => {
    let url = "/category/"
    if (id) {
      const link = categories.value.filter(item => item.id == id)[0].site_link
      url = url + link;
    }
    url = url + getLastPartOfUrl(offset)
    return url
  }

  const getLastPartOfUrl = (offset) => {
    // console.log(minPrice.value, '   ', maxPrice.value);
    let url = '?';
    if (offset != 0 || limit.value != 12) {
      url = url + "offset=" + offset + '&'
      url = url + "limit=" + limit.value + '&'
    }
    if (minPrice.value != 0 || maxPrice.value != 80000) {
      url = url + "actual_price_gte=" + minPrice.value + '&';
      url = url + "actual_price_lte=" + maxPrice.value + '&';
    }
    if (sortDirection.value !== '-' || sortType.value !== 'created_at') {
      url = url + "ordering=" + sortDirection.value + sortType.value + '&'
    }
    if (typeOfProduct.value !== 'all') {
      url = url + "type_of_product=" + typeOfProduct.value + '&'
    }
    if (searchString.value) url = url + "q=" + searchString.value;
    const lastSymbol = url.slice(-1)
    if (lastSymbol === '&' || lastSymbol === '?') url = url.slice(0, -1)
    return url;        
  }

  const onChangePage = (data) => {
    if (data.pageNumber && data.isAvailable) {
      const newOffset = (data.pageNumber - 1) * limit.value
      if (window) setTimeout(() => window.scrollTo(0, 0), 0);
      queryStore.setOffset(newOffset);
      if (categoryId.value) {
        router.push(getCategoryUrl(categoryId.value, newOffset))
      } else {
        router.push(getCatalogUrl(newOffset));
      }
    }
  }

</script>

<style scoped lang="scss">
.pagination_link{
    width: 40px;
    height: 40px;
    background: rgba(66, 62, 72, 0.07);
    border-radius: 2px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #423E48;
    transition: all 0.3s ease;
    &:hover{
      border: 1.2px solid #4275D8;
      cursor: pointer;
    }
  }
  .active{
    background: #4275D8;
    color: #fff;
  }
</style>