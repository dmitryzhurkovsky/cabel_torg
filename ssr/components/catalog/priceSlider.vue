<template>
  <div>
    <div class="filter__title">Диапазон цен:</div>
    <div class="filter__slider">
      <div class="filter__progress" :style = "{left: Left, right: Right}"></div>
    </div>
    <div class="range-input">
      <input type="range" class="range-min" 
        :min="RangeMin" 
        :max="RangeMax" 
        v-model="minValueRange" 
        step="10" 
        v-on:input="onChangeRange('min')"
        v-on:change="onSetChangeRange()"
      >
      <input type="range" class="range-max" 
        :min="RangeMin" 
        :max="RangeMax" 
        v-model="maxValueRange" 
        step="10" 
        v-on:input="onChangeRange('max')"
        v-on:change="onSetChangeRange()"
      >
    </div>
    <div class="price-input">
      <div class="filter__field">
        <span>от</span>
        <input type="number" class="input-min" v-model="minValuePrice" v-on:change="onChangeMinPrice()">
      </div>

      <div class="filter__field">
        <span>до</span>
        <input type="number" class="input-max" v-model="maxValuePrice" v-on:change="onChangeMaxPrice()">
      </div>
    </div>
  </div>
</template>

<script>

import {mapMutations, mapGetters} from 'vuex'

export default {
  name: 'PriceSlider',

  data(){
    return {
      minValueRange: 0,
      maxValueRange: 80000,
      minValuePrice: 0,
      maxValuePrice: 80000,
      RangeMin: 0,
      RangeMax: 80000,
      priceGap: 100,
      Left: '25%',
      Right: '75%',
    }
  },

  watch: {
    ChangeParameters: async function() {
      this.minValuePrice = this.MIN_PRICE;
      this.minValueRange = this.MIN_PRICE;
      this.maxValuePrice = this.MAX_PRICE;
      this.maxValueRange = this.MAX_PRICE;
      this.Left = ((this.MIN_PRICE / this.RangeMax) * 100) + '%';
      this.Right = 100 - ((this.MAX_PRICE / this.RangeMax) * 100) + '%';
    }  
  },

  computed: {
    ...mapGetters("query", ["LIMIT", "OFFSET", "VIEW_TYPE", "TYPE_OF_PRODUCT", "CATEGORY_ID", "MIN_PRICE", "MAX_PRICE", "SORT_TYPE", "SORT_ORDER", "SORT_DIRECTION", "LIMIT_ITEMS"]),
    ...mapGetters("catalog", ["CATALOG_SEARCH_STRING"]),
    ...mapGetters("header", ["ALL_CATEGORIES"]),

    ChangeParameters(){
      return String(this.MAX_PRICE) + String(this.MIN_PRICE);
    }
  },

  methods: {
    ...mapMutations("query", ["SET_MIN_PRICE", "SET_MAX_PRICE", "SET_OFFSET"]),

    setUpMinPrice(){
      if (this.minValuePrice <= this.RangeMin) this.minValuePrice = this.RangeMin;
      if (this.minValuePrice >= this.maxValuePrice - this.priceGap) this.minValuePrice = this.maxValuePrice - this.priceGap;
      const minPrice = this.minValuePrice;
      const maxPrice = this.maxValuePrice;
      if ((maxPrice - minPrice >= this.priceGap) && (maxPrice <= this.maxValueRange)) {
        this.minValueRange = minPrice;
        this.Left = ((minPrice / this.RangeMax) * 100) + '%';
      }
    },

    setUpMaxPrice(){
      if (this.maxValuePrice >= this.RangeMax) this.maxValuePrice = this.RangeMax;
      if (this.maxValuePrice <= this.minValuePrice + this.priceGap) this.maxValuePrice = Number(this.minValuePrice) + Number(this.priceGap);
      const minPrice = this.minValuePrice;
      const maxPrice = this.maxValuePrice;
      if ((maxPrice - minPrice >= this.priceGap)) {
        this.maxValueRange = maxPrice;
        this.Right = 100 - ((maxPrice / this.RangeMax) * 100) + '%';
      }
    },

    onChangeMinPrice(){
      if (String(this.minValuePrice).length === 0) this.minValuePrice = this.minValueRange;
      this.setUpMinPrice();
      this.updateStore();
    },

    onChangeMaxPrice() {
      if (String(this.maxValuePrice).length === 0) this.maxValuePrice = this.maxValueRange;
      this.setUpMaxPrice();
      this.updateStore();
    },

    onChangeRange(type) {
      let minValue = this.minValueRange;
      const maxValue = this.maxValueRange;
      if (((maxValue - minValue) < this.priceGap)) {
        if (type === 'min') {
          this.minValueRange = maxValue - this.priceGap;
        } else {
          minValue = this.minValuePrice;
          this.minValueRange = Number(this.minValuePrice);
          this.maxValueRange = Number(this.minValueRange) + Number(this.priceGap);
        }
        this.minValuePrice = this.minValueRange;
        this.maxValuePrice = this.maxValueRange;
        this.Left = ((this.minValueRange / this.RangeMax) * 100) + '%';
        this.Right = 100 - ((this.maxValueRange / this.RangeMax) * 100) + '%';
      } else {
        this.minValuePrice = minValue;
        this.maxValuePrice = maxValue;
        this.Left = ((minValue / this.RangeMax) * 100) + '%';
        this.Right = 100 - ((maxValue / this.RangeMax) * 100) + '%';
      }
    },

    onSetChangeRange(){
      this.updateStore();
    },

    getCatalogUrl(min, max){
      let url = "/catalog";
      url = url + this.getLastPartOfUrl(min, max);
      return url;
    },

    getCategoryUrl(id, min, max){
      let url = "/category/";
      if (id) {
        const link = this.ALL_CATEGORIES.filter(item => item.id == id)[0].site_link
        url = url + link;
      }
      url = url + this.getLastPartOfUrl(min, max);
      return url;
    },

    getLastPartOfUrl(min, max){
      let url = '?';
      if (this.OFFSET != 0 || this.LIMIT != 12) {
        url = url + "offset=" + this.OFFSET + '&'
        url = url + "limit=" + this.LIMIT + '&'
      }
      if (min != 0 || max != 80000) {
        url = url + "actual_price_gte=" + min + '&';
        url = url + "actual_price_lte=" + max + '&';
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

    updateStore(){
      this.SET_OFFSET(0);
      if (this.MIN_PRICE !== this.minValuePrice) {
        this.SET_MIN_PRICE(this.minValuePrice);
        if (this.CATEGORY_ID) {
          this.$router.push(this.getCategoryUrl(this.CATEGORY_ID, this.minValuePrice, this.MAX_PRICE));
        } else {
          this.$router.push(this.getCatalogUrl(this.minValuePrice, this.MAX_PRICE));
        }
      } 
      if (this.MAX_PRICE !== this.maxValuePrice) {
        this.SET_MAX_PRICE(this.maxValuePrice);
        if (this.CATEGORY_ID) {
          this.$router.push(this.getCategoryUrl(this.CATEGORY_ID, this.MIN_PRICE, this.maxValuePrice));
        } else {
          this.$router.push(this.getCatalogUrl(this.MIN_PRICE, this.maxValuePrice));
        }
      }
    }
  },

  beforeMount(){
    this.minValuePrice = this.MIN_PRICE;
    this.maxValuePrice = this.MAX_PRICE;
    this.setUpMinPrice();
    this.setUpMaxPrice();
  },

  // beforeUpdate(){
  //   this.minValuePrice = this.MIN_PRICE;
  //   this.maxValuePrice = this.MAX_PRICE;
  //   this.setUpMinPrice();
  //   this.setUpMaxPrice();
  // }
}
</script>

<style lang="scss" scoped>
.filter {
    &__title{
        background: #F8FAFF;
        padding: 6px 8px;
        font-weight: 500;
        font-size: 14px;
        line-height: 24px;
        color: #423E48;
        margin: 12px 0;
        &:before{
            position: absolute;
            top: 12px;
            right: 10px;
            font-size: 10px;
            //transform: rotate(-90deg);
        }
    }
    &__slider {
        height: 4px;
        position: relative;
        background: #ddd;
        border-radius: 5px;
    }
    &__progress{
        height: 100%;
        left: 25%;
        right: 25%;
        position: absolute;
        border-radius: 5px;
        background: #4275D8;
    }
}

.price-input{
  width: 100%;
  display: flex;
  margin: 30px 0 35px;
  gap: 10px;
}
.price-input .filter__field{
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 45px;
  align-items: flex-start;
  gap: 10px;
}

input[type="number"]::-webkit-outer-spin-button,
input[type="number"]::-webkit-inner-spin-button {
  -webkit-appearance: none;
}


.range-input{
  position: relative;
}
.range-input input{
  position: absolute;
  width: 100%;
  height: 4px;
  top: -5px;
  background: none;
  border: none;
  padding: 0;
  pointer-events: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}
input[type="range"]::-webkit-slider-thumb{
  height: 20px;
  width: 20px;
  border-radius: 50%;
  border: 2px solid #4275D8;

  background: #fff;
  pointer-events: auto;
  -webkit-appearance: none;
  box-shadow: 0 0 6px rgba(0,0,0,0.05);
}
input[type="range"]::-moz-range-thumb{
  height: 20px;
  width: 20px;
  border: 2px solid #4275D8;
  border-radius: 50%;
  background: #fff;
  pointer-events: auto;
  -moz-appearance: none;
  box-shadow: 0 0 6px rgba(0,0,0,0.05);
}

</style>>
