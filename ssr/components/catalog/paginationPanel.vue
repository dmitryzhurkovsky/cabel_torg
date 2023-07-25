<template>
    <div v-if = "Pages" class="content-block__pagination">
      <a 
          :class="[item.pageNumber === getters['catalog/ACTIVE_PAGE'] ? 'pagination_link active' : 'pagination_link']"
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
  import store from '@/store'
  const { getters } = store
  const router = useRouter()

  const Pages = computed(() => {
    // console.log('Pages ', getters['catalog/ACTIVE_PAGE'], '  ',  getters['catalog/TOTAL_PAGES']);
    let result = []
    const activePage = getters['catalog/ACTIVE_PAGE']
    const totalPages = getters['catalog/TOTAL_PAGES']
    const firstLink = { name: '<', pageNumber: activePage - 1, isAvailable: activePage !== 1 }

    result.push(firstLink)
    if (totalPages > 7) {
      console.log('', totalPages, activePage);
      let left = activePage;
      let right = totalPages - activePage;
      
      if (left < 4) {
        for (let i = 1; i < left; i++){
          const curLink = {
            name: i,
            pageNumber: i,
            isAvailable: activePage !== i
          }
          result.push(curLink)
        }
      } else {
        const firstLink = {
          name: 1,
          pageNumber: 1,
          isAvailable: activePage !== 1
        }
        result.push(firstLink)
        const dots = {
          name: '...',
          pageNumber: activePage - 2,
          isAvailable: true
        }
        result.push(dots)
        const curLink = {
          name: activePage - 1,
          pageNumber: activePage - 1,
          isAvailable: true
        }
        result.push(curLink)
      }

      const center = {
        name: activePage,
        pageNumber: activePage,
        isAvailable: false
      }
      result.push(center)


      if (right > 4) {
        const firstLink = {
          name: activePage + 1,
          pageNumber: activePage + 1,
          isAvailable: true
        }
        result.push(firstLink)
        const dots = {
          name: '...',
          pageNumber: activePage + 2,
          isAvailable: true
        }
        result.push(dots)
        const curLink = {
          name: totalPages,
          pageNumber: totalPages,
          isAvailable: true
        }
        result.push(curLink)
      } else {
        for (let i = activePage + 1; i <= right ; i++){
          const curLink = {
            name: i,
            pageNumber: i,
            isAvailable: activePage !== i
          }
          result.push(curLink)
        }
      }

    } else {
      for (let i = 1; i <= totalPages; i++) {
        const curLink = {
          name: i,
          pageNumber: i,
          isAvailable: activePage !== i
        }
        result.push(curLink)
      }
    }
    const lastLink = { name: '>', pageNumber: activePage + 1, isAvailable: activePage < totalPages }
    result.push(lastLink)
    return result
  })

  const createHref = (item) =>{
    let URL = ''
    const newOffset = (item.pageNumber === 0 ? 0 : (item.pageNumber - 1)) * getters['query/LIMIT']
    if (getters['query/CATEGORY_ID']) {
      URL = getCategoryUrl(getters['query/CATEGORY_ID'], newOffset)
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
      const link = getters['header/ALL_CATEGORIES'].filter(item => item.id == id)[0].site_link
      url = url + link;
    }
    url = url + getLastPartOfUrl(offset)
    return url
  }

  const getLastPartOfUrl = (offset) => {
    let url = '?';
    if (offset != 0 || getters['query/LIMIT'] != 12) {
      url = url + "offset=" + offset + '&'
      url = url + "limit=" + getters['query/LIMIT'] + '&'
    }
    if (getters['query/MIN_PRICE'] != 0 || getters['query/MAX_PRICE'] != 80000) {
      url = url + "actual_price_gte=" + getters['query/MIN_PRICE'] + '&';
      url = url + "actual_price_lte=" + getters['query/MAX_PRICE'] + '&';
    }
    if (getters['query/SORT_DIRECTION'] !== '-' || getters['query/SORT_TYPE'] !== 'created_at') {
      url = url + "ordering=" + getters['query/SORT_DIRECTION'] + getters['query/SORT_TYPE'] + '&'
    }
    if (getters['query/TYPE_OF_PRODUCT'] !== 'all') {
      url = url + "type_of_product=" + getters['query/TYPE_OF_PRODUCT'] + '&'
    }
    if (getters['query/SEARCH_STRING']) url = url + "q=" + getters['query/SEARCH_STRING']
    const lastSymbol = url.slice(-1)
    if (lastSymbol === '&' || lastSymbol === '?') url = url.slice(0, -1)
    return url;        
  }

  const onChangePage = (data) => {
    if (data.pageNumber && data.isAvailable) {
      const newOffset = (data.pageNumber - 1) * getters['query/LIMIT']
      if (window) setTimeout(() => window.scrollTo(0, 0), 0)
      store.commit('query/SET_OFFSET', newOffset)
      if (getters['query/CATEGORY_ID']) {
        router.push(getCategoryUrl(getters['query/CATEGORY_ID'], newOffset))
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