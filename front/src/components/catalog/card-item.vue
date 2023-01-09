<template lang="html">
  <div class="recomendation__block__item item-card" v-if = "card">
    <div class="item-card__tag">Хит</div>
    <div class="item-card__wishlist icon-favorite"></div>
    <a class="item-card__img" href="">
      <img class="" :src=getImagePath(card.images) alt="">
    </a>
    <div class="item-card__info">
      <div class="item-card__row flex-center">
        <div class="old_price">65.3</div>
        <div class="notice">* Цена указана с учетом НДС.</div>
      </div>

      <div class="item-card__row flex-center">
        <div class="current_price">56.5
          <span>BYN/</span>
        </div>
        <div class="item-card__buy flex-center icon-cart">
        </div>

      </div>
      <div class="item-card__title">
        <div>{{card.name}}</div>
      </div>
      <div class="item-card__uptitle">
        <div>UTP cat.5e (патч-панель) 19″</div>
      </div>




    </div>
  </div>

</template>

<script>
// import axios from "axios";

export default {
  name: "CardItem",

  props: {
    card:  null,
  },

  methods: {
    getImagePath(item) {
      const allPath = item.split(',');
      const path = process.env.VUE_APP_IMAGES + allPath[0];
      return path;
    }
  },

}


</script>

<style lang="scss" scoped>

//Карточка товара

.item-card {
  display: flex;
  flex-direction: column;
  position: relative;
  background: #FFFFFF;
  border: 2px solid #EEEEEE;
  box-sizing: border-box;
  border-radius: 8px;
  padding: 20px 22px 30px 22px;

  &__img {
    width: 100%;

    img{
      max-width: 100%;
    }

  }

  &__tag{
    background: #7700AF;
    border-radius: 2px;
    padding: 2px 11px;
    position: absolute;
    font-weight: 400;
    font-size: 12px;
    left:20px;
    top:20px;
    color: #fff;
  }
  &__wishlist{

    &.added {
      fill: #ff6f60;
      path {
        stroke: #ff6f60;
      }
    }
    //width: 18px;
    //height: 16px;
    position: absolute;
    top: 20px;
    right: 20px;
    z-index: 1;
    cursor: pointer;
    fill: none;
  }

  &__row {
  justify-content: space-between;
    &:nth-child(1){
      margin-bottom: 3px;
    }
    &:nth-child(2){
      margin-bottom: 15px;
    }
  }

  &__buy {
    &:before {
      cursor: pointer;
      padding: 10px 10px;
    }
    &:hover{
      background: #4275D8;
      border-radius: 6px;
      color: #fff;
    }


  }

  .notice{
    font-weight: 300;
    font-size: 10px;
    opacity: 0.5;
    text-align: right;
  }

  .old_price {
    font-size: 16px;
    line-height: 24px;
    text-decoration-line: line-through;
    opacity: 0.4;

  }

  .current_price {
    font-weight: 500;
    font-size: 20px;
    line-height: 24px;
    span{
      font-weight: 300;
    }

  }

  &__title {
    margin-bottom: 10px;
    a{
      font-weight: 500;
      font-size: 15px;

      color: #423E48;
    }

  }

  &__uptitle {
    a{
      font-weight: 400;
      font-size: 14px;
      line-height: 130%;
      color: #423E48;
    }

  }



}

</style>
