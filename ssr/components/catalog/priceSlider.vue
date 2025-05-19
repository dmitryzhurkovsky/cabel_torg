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

<script setup>
  import { ref, computed, watch } from 'vue';
  // import { defineEmits } from 'vue';
  import { useQueryStore } from '@/stores/query';

  const router = useRouter();
  const queryStore = useQueryStore();

  const emit = defineEmits(['onPriceChanged']);  

  const { minPrice, maxPrice } = storeToRefs(queryStore);

  const minValueRange = ref(0);
  const maxValueRange = ref(80000);
  const minValuePrice = ref(0);
  const maxValuePrice = ref(80000);
  const RangeMin = ref(0);
  const RangeMax = ref(80000);
  const priceGap = ref(100);
  const Left = ref('25%');
  const Right = ref('75%');

  const ChangeParameters = computed(() => {
    // console.log('Watch in price slider ', String(maxPrice.value) + String(minPrice.value));
    return String(maxPrice.value) + String(minPrice.value);
  });

  watch(ChangeParameters, async () => {
    minValuePrice.value = minPrice.value;
    minValueRange.value = minPrice.value;
    maxValuePrice.value = maxPrice.value;
    maxValueRange.value = maxPrice.value;
    Left.value = ((minPrice.value / RangeMax.value) * 100) + '%';
    Right.value = 100 - ((maxPrice.value /RangeMax.value) * 100) + '%';
  });

  const setUpMinPrice = () => {
    if (minValuePrice.value <= RangeMin.value) minValuePrice.value = RangeMin.value;
    if (minValuePrice.value >= maxValuePrice.value - priceGap.value) minValuePrice.value = maxValuePrice.value - priceGap.value;
    const minPrice = minValuePrice.value;
    const maxPrice = maxValuePrice.value;
    if ((maxPrice - minPrice >= priceGap.value) && (maxPrice <= maxValueRange.value)) {
      minValueRange.value = minPrice;
      Left.value = ((minPrice / RangeMax.value) * 100) + '%';
    }
  };

  const setUpMaxPrice = () => {
    if (maxValuePrice.value >= RangeMax.value) maxValuePrice.value = RangeMax.value;
    if (maxValuePrice.value <= minValuePrice.value + priceGap.value) maxValuePrice.value = Number(minValuePrice.value) + Number(priceGap.value);
    const minPrice = minValuePrice.value;
    const maxPrice = maxValuePrice.value;
    if ((maxPrice - minPrice >= priceGap.value)) {
      maxValueRange.value = maxPrice;
      Right.value = 100 - ((maxPrice / RangeMax.value) * 100) + '%';
    }
  };

  const onChangeMinPrice = () => {
    if (String(minValuePrice.value).length === 0) minValuePrice.value = minValueRange.value;
    setUpMinPrice();
    updateStore();
  };

  const onChangeMaxPrice = () => {
    if (String(maxValuePrice.value).length === 0) maxValuePrice.value = maxValueRange.value;
    setUpMaxPrice();
    updateStore();
  };

  const onChangeRange = (type) => {
    let minValue = minValueRange.value;
    const maxValue = maxValueRange.value;
    if (((maxValue - minValue) < priceGap.value)) {
      if (type === 'min') {
        minValueRange.value = maxValue - priceGap.value;
      } else {
        minValue = minValuePrice.value;
        minValueRange.value = Number(minValuePrice.value);
        maxValueRange.value = Number(minValueRange.value) + Number(priceGap);
      }
      minValuePrice.value = minValueRange.value;
      maxValuePrice.value = maxValueRange.value;
      Left.value = ((minValueRange.value / RangeMax.value) * 100) + '%';
      Right.value = 100 - ((maxValueRange.value / RangeMax.value) * 100) + '%';
    } else {
      minValuePrice.value = minValue;
      maxValuePrice.value = maxValue;
      Left.value = ((minValue / RangeMax.value) * 100) + '%';
      Right.value = 100 - ((maxValue / RangeMax.value) * 100) + '%';
    }
  };

  const onSetChangeRange = () => {
    updateStore();
  };

  // const getCatalogUrl = (min, max) => {
  //   let url = "/catalog";
  //   url = url + getLastPartOfUrl(min, max);
  //   return url;
  // };

  // const getCategoryUrl = (id, min, max) => {
  //   let url = "/category/";
  //   if (id) {
  //     const link = categories.value.filter(item => item.id == id)[0].site_link
  //     url = url + link;
  //   }
  //   url = url + getLastPartOfUrl(min, max);
  //   return url;
  // };

  // const getLastPartOfUrl = (min, max) => {
  //   let url = '?';
  //   if (offset.value != 0 || limit.value != 12) {
  //     url = url + "offset=" + offset.value + '&'
  //     url = url + "limit=" + limit.value + '&'
  //   }
  //   if (min != 0 || max != 80000) {
  //     url = url + "actual_price_gte=" + min + '&';
  //     url = url + "actual_price_lte=" + max + '&';
  //   }
  //   if (sortDirection.value !== '-' || sortType.value !== 'created_at') {
  //     url = url + "ordering=" + sortDirection.value + sortType.value + '&'
  //   }
  //   if (typeOfProduct.value !== 'all') {
  //     url = url + "type_of_product=" + typeOfProduct.value + '&'
  //   }
  //   const lastSymbol = url.slice(-1)
  //   if (lastSymbol === '&' || lastSymbol === '?') url = url.slice(0, -1)
  //   return url;        
  // };

  const updateStore = () => {
    queryStore.setOffset(0);
    if (minPrice.value !== minValuePrice.value) {
      queryStore.setMinPrice(minValuePrice.value);
      const url = queryStore.createUrl();
      router.push(url);
    } 
    if (maxPrice.value !== maxValuePrice.value) {
      queryStore.setMaxPrice(maxValuePrice.value);
      const url = queryStore.createUrl();
      router.push(url);
    }
    console.log('updsteStore priceSlider');
    emit('onPriceChanged');
  }

  onBeforeMount(() => {
    // console.log('Mount price slider ', minPrice.value, '  ', maxPrice.value);
    minValuePrice.value = minPrice.value;
    maxValuePrice.value = maxPrice.value;
    setUpMinPrice();
    setUpMaxPrice();
  });

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
