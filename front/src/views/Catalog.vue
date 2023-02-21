<template>
  <div class="catalog" @click.stop = "clearSearchString()">
    <div class="catalog__wrapper">
      <div class="catalog__content _container">
        <div class="catalog__body">

          <div class="catalog__block">

<!--        # SIDEBAR-->
            <div class="catalog__sidebar filter">
              <FilterPanel />
            </div>
<!--        # CONTENT-->
            <div class="content-block">
              <div class="content-block__subcategory recomendation__nav" v-if = "LastCategory.length">
                  <div 
                    class="recomendation__nav__item"
                    v-for = "category in LastCategory[0].subItems"
                    :key = "category.id"
                    @click.stop = setActiveCategory(category.id)
                  >
                    {{ category.name }}
                  </div>
              </div>
              <div class="content-block__topfilter topfilter">
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

  import { mapGetters, mapActions, mapMutations } from 'vuex'

  export default {
    name: 'Catalog',

    components:
    {
      FilterPanel, ListItem, CardItem, LimitPanel, ViewPanel, PaginationPanel, SortPanel,
    },

    watch: {
      ChangeParameters: async function() {
        await this.getData();
      },

      CATEGORY_ID: function() {
        this.SET_CATALOG_SEARCH_STRING('');
      },
    },

    computed: {
        ...mapGetters("header", ["TOP_CATEGORIES_ITEM_ACTIVE", "SUB_CATEGORIES_ITEM_ACTIVE", "LAST_CATEGORIES_ITEM_ACTIVE", "SUB_CATEGORIES"]),
        ...mapGetters("catalog", ["ITEMS_LIST", "CATALOG_SEARCH_STRING"]),
        ...mapGetters("query", ["LIMIT", "OFFSET", "VIEW_TYPE", "TYPE_OF_PRODUCT", "CATEGORY_ID", "MIN_PRICE", "MAX_PRICE", "SEARCH_STRING", "SORT_TYPE", "SORT_DIRECTION"]),

        LastCategory(){
            let result = [];
            if (this.SUB_CATEGORIES_ITEM_ACTIVE && this.SUB_CATEGORIES) {
                result = this.SUB_CATEGORIES.filter(item => item.id === this.SUB_CATEGORIES_ITEM_ACTIVE);
            }
            return result;
        },

        ChangeParameters(){
          return String(this.LIMIT) + String(this.OFFSET) + JSON.stringify(this.TYPE_OF_PRODUCT) + String(this.MIN_PRICE) + String(this.SORT_DIRECTION) +
                  String(this.MAX_PRICE) + String(this.CATEGORY_ID) + this.CATALOG_SEARCH_STRING + this.VIEW_TYPE + JSON.stringify(this.SORT_TYPE);
        }
    },

    methods: {
      ...mapActions("catalog", ["GET_CATALOG_ITEMS", "GET_ALL_CATALOG_ITEMS"]),
      ...mapActions("header", ["SET_ALL_CURRENT_CATEGORIES"]),
      ...mapMutations("query", ["SET_CATEGORY_ID", "SET_OFFSET"]),
      ...mapMutations("query", ["SET_SEARCH_STRING"]),
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
          // await this.GET_CATALOG_ITEMS(this.CATEGORY_ID);
        } else {
          await this.GET_ALL_CATALOG_ITEMS();
        }
        this.SET_IS_LOADING(false);
      },

      setActiveCategory(id){
        this.SET_ALL_CURRENT_CATEGORIES({
            mainCategory: this.TOP_CATEGORIES_ITEM_ACTIVE,
            middleCategory: this.SUB_CATEGORIES_ITEM_ACTIVE,
            lastCategory: id,
        });
        this.SET_CATEGORY_ID(id);
      },

      clearSearchString(){
        this.SET_SEARCH_STRING('');
      },

    },

    async mounted() {
      await this.getData();
      if (!this.CATEGORY_ID) {
        this.$store.dispatch("breadcrumb/CHANGE_BREADCRUMB", 0);
        this.$store.commit('breadcrumb/ADD_BREADCRUMB', {
          name: this.$router.currentRoute.value.meta.name,
          path: this.$router.currentRoute.value.path,
          type: "global",
          class: ""
        });
      }
    }    
  }
</script>

<style scoped lang="scss">

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

</style>