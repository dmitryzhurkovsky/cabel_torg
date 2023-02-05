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
    name: 'SortSlider',

    data(){
        return {
            minValueRange: 10,
            maxValueRange: 10000,
            minValuePrice: 10,
            maxValuePrice: 10000,
            RangeMin: 10,
            RangeMax: 10000,
            priceGap: 1000,
            Left: '25%',
            Right: '75%',
        }
    },

    mounted(){
        this.onChangeMinPrice();
        this.onChangeMaxPrice();
        this.updateStore();
    },

    computed: {
        ...mapGetters("query", ["MIN_PRICE", "MAX_PRICE"]),
    },

    methods: {
        ...mapMutations("query", ["SET_MIN_PRICE", "SET_MAX_PRICE"]),

        onChangeMinPrice() {
            if (this.minValuePrice <= this.RangeMin) this.minValuePrice = this.RangeMin;
            if (this.minValuePrice >= this.maxValuePrice - this.priceGap) this.minValuePrice = this.maxValuePrice - this.priceGap;
            const minPrice = this.minValuePrice;
            const maxPrice = this.maxValuePrice;
            if ((maxPrice - minPrice >= this.priceGap) && (maxPrice <= this.maxValueRange)) {
                this.minValueRange = minPrice;
                this.Left = ((minPrice / this.RangeMax) * 100) + '%';
            }
            this.updateStore();
        },
        onChangeMaxPrice() {
            if (this.maxValuePrice >= this.RangeMax) this.maxValuePrice = this.RangeMax;
            if (this.maxValuePrice <= this.minValuePrice + this.priceGap) this.maxValuePrice = Number(this.minValuePrice) + Number(this.priceGap);
            const minPrice = this.minValuePrice;
            const maxPrice = this.maxValuePrice;
            if ((maxPrice - minPrice >= this.priceGap)) {
                this.maxValueRange = maxPrice;
                this.Right = 100 - ((maxPrice / this.RangeMax) * 100) + '%';
            }
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
                    this.minValueRange = this.minValuePrice;
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
        updateStore(){
            if (this.MIN_PRICE !== this.minValuePrice) this.SET_MIN_PRICE(this.minValuePrice);
            if (this.MAX_PRICE !== this.maxValuePrice) this.SET_MAX_PRICE(this.maxValuePrice);
        }
    }
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
