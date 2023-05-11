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
    if (activePage !== 1 && totalPages >= 5) {
      const goTopLink = { name: '1', pageNumber: 1, isAvailable: activePage !== 1 }
      result.push(goTopLink)
      const dots = {
          name: '...',
          pageNumber: null,
          isAvailable: false
        }
        result.push(dots)
    }
    if (totalPages >= 5) {
      if (totalPages - activePage < 5) {
        for (let i = 4; i >= 0; i--) {
          const curLink = {
            name: totalPages - i,
            pageNumber: totalPages - i,
            isAvailable: activePage !== i
          }
          result.push(curLink)
        }
      } else {
        for (let i = 0; i < 3; i++) {
          const curLink = {
            name: activePage + i,
            pageNumber: activePage + i,
            isAvailable: activePage + i !== activePage
          };
          result.push(curLink);
        }
        const dots = {
          name: '...',
          pageNumber: null,
          isAvailable: false
        }
        result.push(dots);
        const afterDots = {
          name: totalPages,
          pageNumber: totalPages,
          isAvailable: totalPages !== activePage
        }
        result.push(afterDots)
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
    const lastLink = { name: '>', pageNumber: activePage + 1, isAvailable: activePage !== totalPages }
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
    if (id) url = url + id + "?"
    url = url + getLastPartOfUrl(offset)
    return url
  }

  const getLastPartOfUrl = (offset) => {
    let url = "offset=" + offset + 
      "&limit=" + getters['query/LIMIT'] + 
      "&price_gte=" + getters['query/MIN_PRICE'] + 
      "&price_lte=" + getters['query/MAX_PRICE']
    url = url + "&ordering=" + getters['query/SORT_DIRECTION'] + getters['query/SORT_TYPE']
    url = url + '&type_of_product=' + getters['query/TYPE_OF_PRODUCT']
    url = url + "&q=" + getters['query/SEARCH_STRING']
    return url
  }

  const onChangePage = (data) => {
    if (data.pageNumber && data.isAvailable) {
      const newOffset = (data.pageNumber - 1) * getters['query/LIMIT']
      if (window) setTimeout(() => window.scrollTo(0, 0), 0)
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