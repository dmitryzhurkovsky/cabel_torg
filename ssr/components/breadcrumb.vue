<template>
  <div class="breadcrumb__wrapper _container" v-if = "ELEMENTS.length">
    <ul class="breadcrumb">
      <li
          v-for=" (element, index) in ELEMENTS"
          :key="element.id"
          :class="element.class"
      >
        <a class="breadcrumb__link"
            v-if="element.type !=='service'"
            :href="createHref(element)"
            @click.prevent="changePage(element)"
            :style = "[ ELEMENTS.length -1 === index ? 'color : #4275D8' : '']"
        >
          {{ element.name }}
        </a>
      </li>
    </ul>
  </div>
</template>

<script>

import { mapActions, mapMutations, mapGetters } from "vuex";

export default {
  name: "breadcrumb",

  computed: {
    ...mapGetters("breadcrumb", ["STACK"]),
    ...mapGetters("query", ["LIMIT", "OFFSET", "TYPE_OF_PRODUCT", "MIN_PRICE", "MAX_PRICE", "SORT_TYPE",  "SORT_DIRECTION", "LIMIT_ITEMS"]),
    ...mapGetters("catalog", ["CATALOG_SEARCH_STRING"]),

    // watch: {
    //   STACK: function() {
    //     console.log('watch');
    //     this.ELEMENTS()
    //   },
    // },

    ELEMENTS(){
      if (this.STACK.length > 1){
        let result = [];
        this.STACK.forEach((item, i) => {
          let menuItem = {};
          menuItem.name = item.name;
          menuItem.path = item.path;
          menuItem.type = item.type;
          menuItem.class = item.class;
          menuItem.index = i;
          result.push(menuItem);
          if (i !== this.STACK.length - 1){
            result.push({name: '', type: 'service', class: 'breadcrumb__separater icon-arrow-l'})
          }
        });
        return result;
      } else {
        return [];
      }
    },
  },

  methods: {
    ...mapActions("breadcrumb", ["MOVE_TO_SELECT_PATH"]),
    ...mapMutations("query", ["SET_SEARCH_STRING", "SET_CATEGORY_ID", "SET_DEFAULT_PRICES"]),
    
    changePage(item){
      // console.log('BreadCrumb-   ', item);
      let url = '';
      if (item.path.includes('category') || item.path.includes('catalog')) {
        // console.log('breadcrumb ', item);
        if (item.path.includes('catalog')) {
          this.SET_CATEGORY_ID(null);
        }
        this.SET_DEFAULT_PRICES();
        // url = url + "?offset=" + this.OFFSET + 
        // "&limit=" + this.LIMIT;
        // if (this.MIN_PRICE != 0 || this.MAX_PRICE != 80000) {
        //   url = url + "&actual_price_gte=" + this.MIN_PRICE; 
        //   url = url + "&actual_price_lte=" + this.MAX_PRICE;
        // }
        // url = url + "&ordering=" + this.SORT_DIRECTION + this.SORT_TYPE;
        // url = url + '&type_of_product=' + this.TYPE_OF_PRODUCT;
        // url = url + "&q=" + this.CATALOG_SEARCH_STRING;
        this.SET_SEARCH_STRING('');
        this.MOVE_TO_SELECT_PATH(item.index);
        // console.log('Url   ', item.path + url, this);
        this.$router.push(item.path + url);
      } else {
        this.SET_SEARCH_STRING('');
        this.MOVE_TO_SELECT_PATH(item.index);
        this.$router.push(item.path);
      }
      // this.MOVE_TO_SELECT_PATH(item.index);
      // this.$router.push(item.path);
    },

    createHref(item){
      let url = ''
      if (item.path.includes('category') || item.path.includes('catalog')) {
        url = url = item.path
        //  + "?";

        // if (this.OFFSET != 0 || this.LIMIT != 12) {
        //   url = url + "offset=" + this.OFFSET + '&'
        //   url = url + "limit=" + this.LIMIT + '&'
        // }
        // if (this.MIN_PRICE != 0 || this.MAX_PRICE != 80000) {
        //   url = url + "actual_price_gte=" + this.MIN_PRICE + '&';
        //   url = url + "actual_price_lte=" + this.MAX_PRICE + '&';
        // }
        // if (this.SORT_DIRECTION !== '-' || this.SORT_TYPE !== 'created_at') {
        //   url = url + "ordering=" + this.SORT_DIRECTION + this.SORT_TYPE + '&'
        // }
        // if (this.TYPE_OF_PRODUCT !== 'all') {
        //   url = url + "type_of_product=" + this.TYPE_OF_PRODUCT + '&'
        // }
        // const lastSymbol = url.slice(-1)
        // if (lastSymbol === '&' || lastSymbol === '?') url = url.slice(0, -1)
      } else {
        url = url + item.path;
      }
      return url;
    },
  },
}
</script>

<style lang="scss" scoped>


.active__breadcrumb {
  color: blue;
}
.breadcrumb{
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  padding: 20px 0 30px 0;
  @media (max-width: $md3+px){
    padding: 10px 0 10px 0;
  }

  &__wrapper{
    width: 100%;
    text-align: left;
  }

  li{
    white-space: nowrap;
    overflow: hidden;
    &:last-child{
      a{
        opacity: 0.5;
        cursor: auto;
        color: #423E48!important;
      }

    }
    a{
      font-weight: 300;
      font-size: 12px;
      line-height: 2;
      text-align: center;
      color: #423E48;
      cursor: pointer;
      @media (max-width: $md3+px){
        font-size: 10px;
      }
    }

  }
  .active{
    font-weight: 300;
    font-size: 12px;
    line-height: 16px;
    text-align: center;
    opacity: 0.5;

  }
  &__separater{
    font-size: 8px;
    margin: 0 12px;
  }

}
</style>
