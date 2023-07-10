<template>
  <div class="tools-pages">
    <div class="tools-pages__header">Показывать по: </div>
    <ul class="tools-pages__body">
      <li class="tools-pages__item" 
        v-for = "limitItem in LIMIT_ITEMS" 
        :key = limitItem
      >
        <a href=""  
          :class="[limitItem == LIMIT ? 'tools-pages__link active' : 'tools-pages__link']"
          @click.prevent="setLimit(limitItem)"
        >{{ limitItem }}</a>
      </li>
    </ul>
  </div>    
</template>

<script>

  import {mapGetters, mapMutations} from 'vuex'


  export default {
    name: 'LimitPanel',

    computed: {
      ...mapGetters("query", ["LIMIT", "OFFSET", "VIEW_TYPE", "TYPE_OF_PRODUCT", "CATEGORY_ID", "MIN_PRICE", "MAX_PRICE", "SORT_TYPE",  "SORT_DIRECTION", "LIMIT_ITEMS", "MAX_PRICE_FROM_DB"]),
      ...mapGetters("catalog", ["CATALOG_SEARCH_STRING"]),
      ...mapGetters("header", ["ALL_CATEGORIES"]),
    },

    methods: {
      ...mapMutations("query", ["SET_LIMIT"]),

      getCatalogUrl(){
        let url = "/catalog";
        url = url + this.getLastPartOfUrl();
        return url;
      },

      getCategoryUrl(id){
        let url = "/category/";
        if (id) {
          const link = this.ALL_CATEGORIES.filter(item => item.id == id)[0].site_link
          url = url + link;
        }
        url = url + this.getLastPartOfUrl();
        return url;
      },

      getLastPartOfUrl(){
        let url = '?';
        if (this.OFFSET != 0 || this.LIMIT != 12) {
          url = url + "offset=" + this.OFFSET + '&'
          url = url + "limit=" + this.LIMIT + '&'
        }
        if (this.MIN_PRICE != 0 || this.MAX_PRICE != this.MAX_PRICE_FROM_DB) {
          url = url + "actual_price_gte=" + this.MIN_PRICE + '&';
          url = url + "actual_price_lte=" + this.MAX_PRICE + '&';
        }
        if (this.SORT_DIRECTION !== '-' || this.SORT_TYPE !== 'created_at') {
          url = url + "ordering=" + this.SORT_DIRECTION + this.SORT_TYPE + '&'
        }
        if (this.TYPE_OF_PRODUCT !== 'all') {
          url = url + "type_of_product=" + this.TYPE_OF_PRODUCT + '&'
        }
        const lastSymbol = url.slice(-1)
        if (lastSymbol === '&' || lastSymbol === '?') url = url.slice(0, -1)
        return url;        
      },

      setLimit(limit) {
        this.SET_LIMIT(limit);
        if (this.CATEGORY_ID) {
          this.$router.push(this.getCategoryUrl(this.CATEGORY_ID));
        } else {
          this.$router.push(this.getCatalogUrl());
        }
      },
    },
  }

</script>

<style scoped lang="scss">
.tools-pages {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-right: 20px;
    @media (max-width: $md3+px){
        display: none;
    }
  &__item{
    .active{
      color: #423E48;
      font-weight: 500;
    }

  }
  &__header {
    margin-right: 15px;
  }
  &__body {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-right: 20px;
  }
  a{
    font-size: 12px;
    color:#000;
    opacity: 0.8;
    transition: all ease 1ms;
    &:hover{
      color: #423E48;
      opacity: 0.8;
    }
  }

}
</style>