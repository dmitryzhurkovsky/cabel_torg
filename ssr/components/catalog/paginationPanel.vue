<template>
    <div v-if = "Pages" class="content-block__pagination">
      <a 
          :class="[item.pageNumber === getters['catalog/ACTIVE_PAGE'] ? 'pagination_link active' : 'pagination_link']"
          v-for = "item in Pages"
          :key = "item.name"
          @click="onChangePage(item)"
      >
        {{ item.name }}
      </a>
    </div>   
</template>

<script setup>
  import store from '@/store'
  const { getters } = store
  const router = useRouter()


  const ChangeParameters = computed(() => {
    return String(getters['query/LIMIT']) + String(getters['query/OFFSET'])
  })

  watch(() => ChangeParameters,
    () => {
      Pages
  })


  const Pages = computed(() => {
    let result = []
    const activePage = getters['catalog/ACTIVE_PAGE']
    const totalPages = getters['catalog/TOTAL_PAGES']
    const firstLink = { name: '<', pageNumber: activePage - 1, isAvailable: activePage !== 1 }

    result.push(firstLink)
    // if (activePage !== 1 && totalPages >= 5) {
    //   const goTopLink = { name: '1', pageNumber: 1, isAvailable: activePage !== 1 }
    //   result.push(goTopLink)
    //   const dots = {
    //       name: '...',
    //       pageNumber: null,
    //       isAvailable: false
    //     }
    //     result.push(dots)
    // }
    console.log('totalPage - ', totalPages);
    if (totalPages > 7) {
      console.log('totalPage >= 7 - ', totalPages, activePage);
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

  const getCatalogUrl = (offset) => {
    let url = "/catalog?"
    url = url + getLastPartOfUrl(offset)
    return url
  }

  const getCategoryUrl = (id, offset) => {
    let url = "/category/"
    if (id) {
      const link = getters['header/ALL_CATEGORIES'].filter(item => item.id == id)[0].site_link
      url = url + link + "?";
    }
    url = url + getLastPartOfUrl(offset)
    return url
  }

  const getLastPartOfUrl = (offset) => {
    let url = "offset=" + offset + 
      "&limit=" + getters['query/LIMIT'] + 
      "&actual_price_gte=" + getters['query/MIN_PRICE'] + 
      "&actual_price_lte=" + getters['query/MAX_PRICE']
    url = url + "&ordering=" + getters['query/SORT_DIRECTION'] + getters['query/SORT_TYPE']
    url = url + '&type_of_product=' + getters['query/TYPE_OF_PRODUCT']
    url = url + "&q=" + getters['query/SEARCH_STRING']
    return url
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