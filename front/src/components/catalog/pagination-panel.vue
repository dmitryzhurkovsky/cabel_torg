<template>
    <div v-if = "Pages" class="content-block__pagination">
      <a 
          :class="[item.pageNumber === ACTIVE_PAGE ? 'pagination_link active' : 'pagination_link']"
          v-for = "item in Pages"
          :key = "item.name"
          @click="onChangePage(item)"
      >
        {{ item.name }}
      </a>
    </div>   
</template>

<script>

  import { mapGetters, mapMutations } from 'vuex'

  export default {
    name: 'PaginationPanel',

    computed: {
      ...mapGetters("catalog", ["TOTAL_PAGES", "ACTIVE_PAGE"]),
      ...mapGetters("query", 
        ["LIMIT", "OFFSET", "VIEW_TYPE", "TYPE_OF_PRODUCT", "CATEGORY_ID", "MIN_PRICE", "MAX_PRICE", "SEARCH_STRING", "SORT_TYPE",  "SORT_DIRECTION", "LIMIT_ITEMS"
      ]),

      watch: {
        OFFSET: function(){
          this.Pages();
        },
      },

      Pages() {
        let result = []
        const firstLink = { name: '<', pageNumber: this.ACTIVE_PAGE - 1, isAvailable: this.ACTIVE_PAGE !== 1 };
        result.push(firstLink);
        if (this.ACTIVE_PAGE !== 1 && this.TOTAL_PAGES >= 5) {
          const goTopLink = { name: '1', pageNumber: 1, isAvailable: this.ACTIVE_PAGE !== 1 };
          result.push(goTopLink);
          const dots = {
              name: '...',
              pageNumber: null,
              isAvailable: false
            }
            result.push(dots);
        }
        if (this.TOTAL_PAGES >= 5) {
          if (this.TOTAL_PAGES - this.ACTIVE_PAGE < 5) {
            for (let i = 4; i >= 0; i--) {
              const curLink = {
                name: this.TOTAL_PAGES - i,
                pageNumber: this.TOTAL_PAGES - i,
                isAvailable: this.ACTIVE_PAGE !== i
              }
              result.push(curLink);
            }
          } else {
            for (let i = 0; i < 3; i++) {
              const curLink = {
                name: this.ACTIVE_PAGE + i,
                pageNumber: this.ACTIVE_PAGE + i,
                isAvailable: this.ACTIVE_PAGE + i !== this.ACTIVE_PAGE
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
              name: this.TOTAL_PAGES,
              pageNumber: this.TOTAL_PAGES,
              isAvailable: this.TOTAL_PAGES !== this.ACTIVE_PAGE
            }
            result.push(afterDots);
          }
        } else {
          for (let i = 1; i <= this.TOTAL_PAGES; i++) {
            const curLink = {
              name: i,
              pageNumber: i,
              isAvailable: this.ACTIVE_PAGE !== i
            }
            result.push(curLink);
          }
        }
        const lastLink = { name: '>', pageNumber: this.ACTIVE_PAGE + 1, isAvailable: this.ACTIVE_PAGE !== this.TOTAL_PAGES };
        result.push(lastLink);
        return result;
      }
    },

    methods: {
      ...mapMutations("query", ["SET_OFFSET"]),

      getCatalogUrl(offset){
        let url = "/catalog?";
        url = url + this.getLastPartOfUrl(offset);
        return url;
      },

      getCategoryUrl(id, offset){
        let url = "/category/";
        if (id) url = url + id + "?";
        url = url + this.getLastPartOfUrl(offset);
        return url;
      },

      getLastPartOfUrl(offset){
        let url = "offset=" + offset + 
          "&limit=" + this.LIMIT + 
          "&price_gte=" + this.MIN_PRICE + 
          "&price_lte=" + this.MAX_PRICE;
        url = url + "&ordering=" + this.SORT_DIRECTION + this.SORT_TYPE;
        url = url + '&type_of_product=' + this.TYPE_OF_PRODUCT;
        url = url + "&q=" + this.SEARCH_STRING;
        return url;        
      },

      onChangePage(data) {
        if (data.pageNumber && data.isAvailable) {
          const newOffset = (data.pageNumber - 1) * this.LIMIT;
          // this.SET_OFFSET(newOffset);
          console.log('Pagination ', this.CATEGORY_ID);
          if (this.CATEGORY_ID) {
            this.$router.push(this.getCategoryUrl(this.CATEGORY_ID, newOffset));
          } else {
            this.$router.push(this.getCatalogUrl(newOffset));
          }
        }
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