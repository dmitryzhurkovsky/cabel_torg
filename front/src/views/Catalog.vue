<template>
  <div class="catalog" @click.stop = "clearSearchString()">
    <div class="catalog__wrapper">
      <div class="catalog__content _container">
        <div class="catalog__body">

          <div class="catalog__block">

<!--        # SIDEBAR-->
            <div v-if ="!isMobileVersion" class="catalog__sidebar filter">
              <FilterPanel />
            </div>
<!--        # CONTENT-->
            <div class="content-block">
              <div class="content-block__subcategory recomendation__nav" v-if = "LastCategory.length && !isMobileVersion">
                  <div 
                    :class="[category.id == this.CATEGORY_ID ? 'recomendation__nav__item active' : 'recomendation__nav__item']"
                    v-for = "category in LastCategory[0].subItems"
                    :key = "category.id"
                    @click.stop = setActiveCategory(category.id)
                  >
                    {{ category.name }}
                  </div>
              </div>
              <div v-if = "LastCategory.length && isMobileVersion">
                <swiper
                  :slides-per-view="1.7"
                  :space-between="12"
                  :speed="500"
                  :autoplay="{
                      delay: 5000,
                  }"
                  :pagination= "{
                    el: '.swiper-pagination',
                    clickable: true,
                    type: 'bullets',
                    bulletClass: 'swiper-pagination-bullet',
                    bulletElement: 'span'
                  }"
                >

                  <swiper-slide v-for="category in LastCategory[0].subItems" :key="category.id">
                    <div class="recomendation__nav__item" @click=setActiveCategory(category.id)>
                      {{ category.name }}
                    </div>
                  </swiper-slide>

                  <div class="swiper-pagination"></div>
                </swiper>
              </div>  
              <div v-if = "isMobileVersion" class="btn mobile-filter mb-20" @click.stop="setIsFilterPanelOpen(!isFilterPanelOpen)">Фильтры</div>
              <div v-if ="isMobileVersion&&isFilterPanelOpen">
                <PriceSlider />
                <SortPanel />
                <LimitPanel />
                <!-- <ViewPanel /> -->
              </div>
              <div v-if = "!isMobileVersion" class="content-block__topfilter topfilter">
                <SortPanel />
                <div class="topfilter__right flex-center">
                  <LimitPanel />
                  <ViewPanel />
                </div>
              </div>
              <div class="content-block__list">
                <div class="content-block__item product-row" v-if = "ITEMS_LIST.length !== 0 && VIEW_TYPE === 'row'">
                  <ListItem 
                    v-for   = "item in ITEMS_LIST"
                    :key    = "item.id"
                    :card   = item
                  />
                </div>  
                <div class="content-block__item product-table" v-if = "ITEMS_LIST.length !== 0 && VIEW_TYPE === 'table'">
                  <CardItem 
                    v-for   = "item in ITEMS_LIST"
                    :key    = "item.id"
                    :card   = item
                  />
                </div>  
              </div>
              <PaginationPanel class="content-block__pagination" />

            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

  import FilterPanel from '@/components/catalog/filter-panel.vue';
  import CardItem from '@/components/catalog/card-item.vue';
  import ListItem from '@/components/catalog/list-item.vue';
  import LimitPanel from '@/components/catalog/limit-panel.vue';
  import ViewPanel from '@/components/catalog/view-panel.vue';
  import PaginationPanel from '@/components/catalog/pagination-panel.vue';
  import SortPanel from '@/components/catalog/sort-panel.vue';
  import PriceSlider from '@/components/catalog/price-slider.vue';

  import { Swiper } from "swiper/vue";
  import { SwiperSlide } from "swiper/vue";
  import SwiperCore, { Pagination, Navigation } from "swiper";
  import "swiper/swiper.min.css";
  SwiperCore.use([Navigation, Pagination]);

  import { mapGetters, mapActions, mapMutations } from 'vuex'

  export default {
    name: 'Catalog',

    props: {
      id: null,
    },

    components:
    {
      FilterPanel, ListItem, CardItem, LimitPanel, ViewPanel, PaginationPanel, SortPanel, PriceSlider, Swiper, SwiperSlide,
    },

    data(){
      return {
        isFilterPanelOpen : false,
      }
    },

    watch: {
      ChangeParameters: async function() {
        await this.getData(this.CATEGORY_ID);
        this.setBreabcrumbs();
      },

      DEVICE_VIEW_TYPE: function(){
        console.log('View pannel ', this.DEVICE_VIEW_TYPE);
        if (this.DEVICE_VIEW_TYPE !== 1) {
          this.SET_VIEW_TYPE('table');
        }
      }
    },

    computed: {
        ...mapGetters("header", ["TOP_CATEGORIES_ITEM_ACTIVE", "SUB_CATEGORIES_ITEM_ACTIVE", "LAST_CATEGORIES_ITEM_ACTIVE", "SUB_CATEGORIES", "DEVICE_VIEW_TYPE", "ALL_CATEGORIES"]),
        ...mapGetters("catalog", ["ITEMS_LIST", "CATALOG_SEARCH_STRING"]),
        ...mapGetters("query", ["LIMIT", "OFFSET", "VIEW_TYPE", "TYPE_OF_PRODUCT", "CATEGORY_ID", "MIN_PRICE", "MAX_PRICE", "SORT_TYPE", "SORT_DIRECTION"]),
        ...mapGetters("breadcrumb", ["STACK"]),

        LastCategory(){
            let result = [];
            if (this.SUB_CATEGORIES_ITEM_ACTIVE && this.SUB_CATEGORIES) {
                result = this.SUB_CATEGORIES.filter(item => item.id === this.SUB_CATEGORIES_ITEM_ACTIVE);
            }
            return result;
        },

        ChangeParameters(){
          return String(this.LIMIT) + String(this.OFFSET) + String(this.TYPE_OF_PRODUCT) + String(this.MIN_PRICE) + String(this.SORT_DIRECTION) + 
                  String(this.MAX_PRICE) + String(this.CATEGORY_ID) + this.CATALOG_SEARCH_STRING + this.VIEW_TYPE + String(this.SORT_TYPE);
                  //  +
                  // JSON.stringify(this.STACK);
        },

        isMobileVersion(){
          if (this.DEVICE_VIEW_TYPE===1) return false;
          if (this.DEVICE_VIEW_TYPE===2) return true;
          if (this.DEVICE_VIEW_TYPE===3) return true;
        }

    },

    methods: {
      ...mapActions("catalog", ["GET_CATALOG_ITEMS", "GET_ALL_CATALOG_ITEMS"]),
      ...mapActions("header", ["SET_ALL_CURRENT_CATEGORIES"]),
      ...mapMutations("query", ["SET_SEARCH_STRING", "SET_CATEGORY_ID", "SET_OFFSET", "SET_LIMIT", "SET_MIN_PRICE", "SET_MAX_PRICE", "SET_TYPE_OF_PRODUCT", "SET_SORT_TYPE", 
        "SET_SORT_DIRECTION", "SET_VIEW_TYPE"]),
      ...mapMutations("catalog", ["SET_CATALOG_SEARCH_STRING"]),
      ...mapMutations("notification", ["SET_IS_LOADING"]),

      async getData() {
        this.SET_IS_LOADING(true);
        if (this.CATEGORY_ID) {
          if (this.CATALOG_SEARCH_STRING) {
            await this.GET_ALL_CATALOG_ITEMS();
          } else {
            await this.GET_CATALOG_ITEMS(this.CATEGORY_ID);
          }
        } else {
          await this.GET_ALL_CATALOG_ITEMS();
        }
        this.SET_IS_LOADING(false);
      },

      getCatalogUrl(){
        let url = "/catalog?";
        url = url + this.getLastPartOfUrl();
        return url;
      },

      getCategoryUrl(id){
        let url = "/category/";
        if (id) url = url + id + "?";
        url = url + this.getLastPartOfUrl();
        return url;
      },

      getLastPartOfUrl(){
        let url = "offset=" + this.OFFSET + 
          "&limit=" + this.LIMIT + 
          "&price_gte=" + this.MIN_PRICE + 
          "&price_lte=" + this.MAX_PRICE;
        url = url + "&ordering=" + this.SORT_DIRECTION + this.SORT_TYPE;
        url = url + '&type_of_product=' + this.TYPE_OF_PRODUCT;
        url = url + "&q=" + this.CATALOG_SEARCH_STRING;
        return url;        
      },


      setActiveCategory(id){
        this.SET_CATALOG_SEARCH_STRING('');
        if (id) {
          this.$router.push(this.getCategoryUrl(id));
        } else {
          this.$router.push(this.getCatalogUrl());
        }  
      },

      clearSearchString(){
        this.SET_SEARCH_STRING('');
        this.SET_CATALOG_SEARCH_STRING('');
      },

      setIsFilterPanelOpen(data) {
        this.isFilterPanelOpen = data;
      },

      setBreabcrumbs() {
        if (!this.$props.id) {
          this.SET_ALL_CURRENT_CATEGORIES({
            mainCategory: null,
            middleCategory: null,
            lastCategory: null,
          });
          return;
        }
        const categoryStack = [];
        categoryStack.push(Number(this.$props.id));
        let curLevel = this.ALL_CATEGORIES.filter(item => item.id == this.$props.id)[0];
        while (curLevel.parent_category_id) {
          const parent_category_id = curLevel.parent_category_id;
          categoryStack.push(parent_category_id);
          curLevel = this.ALL_CATEGORIES.filter(item => item.id == parent_category_id)[0];
        }
        if (categoryStack.length === 3) {
          this.SET_ALL_CURRENT_CATEGORIES({
            mainCategory: categoryStack[2],
            middleCategory: categoryStack[1],
            lastCategory: categoryStack[0],
          });
        };
        if (categoryStack.length === 2) {
          this.SET_ALL_CURRENT_CATEGORIES({
            mainCategory: categoryStack[1],
            middleCategory: categoryStack[0],
            lastCategory: null,
          });
        };
        if (categoryStack.length === 1) {
          this.SET_ALL_CURRENT_CATEGORIES({
            mainCategory: categoryStack[0],
            middleCategory: null,
            lastCategory: null,
          });
        }; 
      },

      setParametersFromURL(){
        // console.log('Set parameters ', this.id);
        if (this.CATEGORY_ID !== this.id) this.SET_CATEGORY_ID(this.id);
        if (this.$route.query.limit && this.LIMIT !== this.$route.query.limit) this.SET_LIMIT(this.$route.query.limit);
        if (this.$route.query.offset && this.OFFSET !== this.$route.query.offset) this.SET_OFFSET(this.$route.query.offset);
        if (this.$route.query.price_gte && this.MIN_PRICE !== this.$route.query.price_gte) this.SET_MIN_PRICE(this.$route.query.price_gte);
        if (this.$route.query.price_lte && this.MAX_PRICE !== this.$route.query.price_lte) this.SET_MAX_PRICE(this.$route.query.price_lte);
        if (this.CATALOG_SEARCH_STRING !== this.$route.query.q) {
          this.SET_CATALOG_SEARCH_STRING(this.$route.query.q);
          this.SET_SEARCH_STRING(this.$route.query.q);
        }
        if (this.$route.query.type_of_product && this.TYPE_OF_PRODUCT !== this.$route.query.type_of_product) this.SET_TYPE_OF_PRODUCT(this.$route.query.type_of_product);
        if (this.$route.query.ordering) {
          const total = this.$route.query.ordering;
          let direction = '';
          let type = ''
          if (total[0] === '-') {
            direction = '-';
            type = total.slice(1);
          } else {
            direction = '';
            type = total;
          }
          // console.log('Set parameters ', direction, '  -   ', type);
          if (this.SORT_TYPE !== type) this.SET_SORT_TYPE(type)
          if (this.SORT_DIRECTION !== direction) this.SET_SORT_DIRECTION(direction);
        };
      }
    },

    async beforeUpdate(){
      console.log('BeforeUpdate', this.$route.query);
      this.setParametersFromURL();
    },

    async mounted() {
      console.log('Mount', this.$route.query,);
      this.setParametersFromURL();
    }    
  }
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
    // @media (max-width:$md2+px) {
    //   display: none;
    // }
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
    max-width: 100px;
    background: #FFFFFF;
    color: #423E48;
    opacity: 0.5;
    border: 1px solid rgba(0, 0, 0, 0.05);
    border-radius: 50px;


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
.recomendation__nav__item{
  background: #FFFFFF;
  border: 1px solid rgba(0, 0, 0, 0.05);
  border-radius: 50px;
  font-size: 12px;
  line-height: 24px;
  text-align: center;
  opacity: 0.5;
  margin-right: 10px;
  padding: 5px 20px;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
  max-width: 200px;
  transition: all 0.5s ease;
  cursor: pointer;
}
</style>