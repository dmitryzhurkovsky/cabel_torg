<template lang="html">
    <div class="header__search search-wrapper">
      <div class="search__box">
        <div class="search__field">
          <input type="text" name="focus" required class="search-box" autocomplete="off"
                 placeholder="Поиск товаров"
            v-model = "queryString" @input="onInput()"

          />
          <button class="icon-close" type="reset" v-if ="queryString" @click = "clearString"></button>
        </div>

      </div>
      
      <div class="dropdown__box" v-if = "FINDED_ELEMENTS.length && SEARCH_STRING !== CATALOG_SEARCH_STRING">
        <div class="dropdown__wrapper">
          <div class="dropdown__content popup-cart">
              <h3 class="">Найденые товары</h3>

                <div class="popup-cart__list">
                  <HeaderSearchItem 
                      class="row" 
                      v-for = "item in FINDED_ELEMENTS"
                      :key = "item.id"
                      :item = item
                      @click.stop = "openCardItem(item.id)"
                  />
                  <div class="search__footer" @click = "openFindedElementsInCatalg" autocomplete="off">
                    Показать все
                  </div>
                </div>

            </div>
        </div>
      </div>

    </div>
</template>

<script>
import { mapActions, mapGetters, mapMutations } from 'vuex';
import HeaderSearchItem from '@/components/header/header-search-item.vue';

export default {
  name: "HeaderSearch",

  data: function() {
    return {
        queryString : '',
      }
  },
  components: {
    HeaderSearchItem,
  },

  computed:{
    ...mapGetters("query", ["SEARCH_STRING", "FINDED_ELEMENTS", "SORT_DIRECTION", "SORT_TYPE"]),
    ...mapGetters("catalog", ["CATALOG_SEARCH_STRING"]),
    ...mapGetters("header", ["TOP_CATEGORIES_ITEM_ACTIVE", "SUB_CATEGORIES_ITEM_ACTIVE", "LAST_CATEGORIES_ITEM_ACTIVE"]),
  },

  watch: {
    SEARCH_STRING: async function(){
      this.queryString = this.SEARCH_STRING;
      if (this.SEARCH_STRING) {
        await this.FIND_ELEMENTS();
      } else {
        this.SET_FINDED_ELEMENTS({data: []});
      }
    }
  },

  methods: {
    ...mapMutations("query", ["SET_SEARCH_STRING", "SET_FINDED_ELEMENTS", "SET_CATEGORY_ID"]),
    ...mapMutations("catalog", ["SET_CATALOG_SEARCH_STRING"]),
    ...mapMutations("header", ["SET_CURRENT_TOP_CATEGORY", "SET_CURRENT_SUB_CATEGORY", "SET_CURRENT_LAST_CATEGORY"]),
    ...mapActions("query", ["FIND_ELEMENTS"]),

    onInput(){
      this.SET_SEARCH_STRING(this.queryString);
    },

    openCardItem(id) {
      this.clearString();
      const URL = '/card_product/' + id;
      this.$router.push(URL);
    },

    clearString(){
      this.queryString = '';
      this.SET_SEARCH_STRING('');
      this.SET_CATALOG_SEARCH_STRING('');
      let url = "/catalog?";
      url = url + "offset=0&limit=10&price_gte=0&price_lte=10000";
      url = url + "&ordering=" + this.SORT_DIRECTION + this.SORT_TYPE;
      url = url + '&type_of_product=all';
      url = url + "&q=" + this.CATALOG_SEARCH_STRING;
      this.$router.push(url);
    },

    openFindedElementsInCatalg(){
      this.SET_CATALOG_SEARCH_STRING(this.SEARCH_STRING);
      // this.SET_SEARCH_STRING('');
      // this.SET_CURRENT_TOP_CATEGORY(null);
      // this.SET_CURRENT_SUB_CATEGORY(null);
      // this.SET_CURRENT_LAST_CATEGORY(null);
      // const category = this.LAST_CATEGORIES_ITEM_ACTIVE || this.SUB_CATEGORIES_ITEM_ACTIVE || this.TOP_CATEGORIES_ITEM_ACTIVE + '12';
      let url = "/catalog?";
      url = url + "offset=0&limit=10&price_gte=0&price_lte=10000";
      url = url + "&ordering=" + this.SORT_DIRECTION + this.SORT_TYPE;
      url = url + '&type_of_product=all';
      url = url + "&q=" + this.CATALOG_SEARCH_STRING;
      this.$router.push(url);
    }

  },
}
</script>

<style lang="scss" scoped>
.dropdown__wrapper{
  display: block;
}
.header{
    &__search{
      position: relative;
      width: 100%;
      // background: #FFFFFF;
      // box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.08);
      // border-radius: 50px;
      // max-width: 384px;
      // height: 32px;
      // width: 100%;
      @media (max-width: $md2+px) {

      }
    }
}

//SEARCH
.search-box,.close-icon,.search-wrapper {
  position: relative;
  padding: 10px;
}
.search-wrapper {
  .dropdown__box{
    width: 100%;
    position: absolute;
    bottom: 0;
    left: 6px;

  }
  .dropdown__wrapper{
    padding: 0 16px 20px 16px;
    margin: 0 10%;
    @media (max-width: $md2+px){
      margin: 0 0;
      padding: 0 10px 10px 0;
    }
  }
}
.search__box {
  //width: 500px;
  background: #fff;
  height: 32px;
  display: flex;
  padding: 6px 16px;
  margin: 0 10%;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.08);
  border-top-right-radius: 10px;
  border-top-left-radius: 10px;

  //# hide this style when search__result open
  border-bottom-right-radius: 10px;
  border-bottom-left-radius: 10px;

  @media (max-width: $md2+px){
    margin: 0 0;
  }


}

.search__field{
  width: 100%;
  height: 100%;
  position: relative;

  input{
    width: 100%;
    height: 100%;
    border: 0px;
    padding-right: 38px;
    font-weight: 300;
    font-size: 14px;
    opacity: 0.5;

  }

  button{
    position: absolute;
    top: 4px;
    right: 0;
    font-size: 16px;
    color: #423E48;


    cursor: pointer;
  }
}

.search__result{
  position: absolute;
  top: 40px;
  left: 10px;
  width: 96%;
  background: #fff;
  min-height: 50px;
  padding: 20px 20px;
  border-bottom-left-radius:10px;
  border-bottom-right-radius:10px;
  border-top: 2px solid rgba(0, 0, 0, 0.05) ;


}
::-webkit-input-placeholder { /* Chrome/Opera/Safari */
  color: #9fa3b1;
}
::-moz-placeholder { /* Firefox 19+ */
  color: #9fa3b1;
}
:-ms-input-placeholder { /* IE 10+ */
  color: #9fa3b1;
}

.search__footer{
  background: #4275D8;
  color: #fff;
  padding: 8px 5px;
  text-align: center;
  border-radius: 6px;
  transition: all 0.3s ease;
  cursor: pointer;
  &:hover{
    background: #6291ED;
  }

}

</style>
