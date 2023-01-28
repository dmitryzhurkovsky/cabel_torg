<template>
    <div class="popup-cart__item row" v-if = "item">
        <div class="popup-cart__img">
            <CardImage :images = item.images />
        </div>
        <div class="popup-cart__description">
            <div class="popup-cart__title">{{ item.name }}</div>
            <div class="popup-cart__uptitle">{{ item.vendor_code }}</div>

        </div>
        <div class="popup-cart__action">
            <div class="popup-cart__price">{{ item.price }} <span>BYN</span></div>
        </div>
    </div>
</template>

<script>
import CardImage from '@/components/UI/card-image.vue'

export default {
  name: 'HeaderSearchItem',

  props: {
    item: null,
  },

  components: {
    CardImage,
  },

}
</script>

<style lang="scss" scoped>
.popup-cart{
  text-align: center;

//   h3{
//     font-weight: 500;
//     font-size: 20px;
//     line-height: 140%;
//     text-align: center;
//     margin-bottom: 16px;
//   }

  &__summary{
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 16px 0;
    font-weight: 300;
    font-size: 14px;
    line-height: 140%;
    color: #423E48;
    opacity: 0.6;
    border-top: 1px solid #F0F0F1;
    border-bottom: 1px solid #F0F0F1;

    div:nth-child(1){
      span{
        font-weight: 500;
        opacity: 1;
      }
    }
    div:nth-child(2){
      span{
        font-weight: 500;
        opacity: 1;
      }
    }
  }

  &__item{
    display: grid;
    grid-template-columns: 1fr 2fr 1fr;
    gap:10px;
    align-items: self-start;
    &:hover{
      background: #F9F9F9;
    }

  }

  &__img{
    max-width: 100%;
    img{
      width: 100%;
    }

  }

  &__description{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    font-size: 12px;
    line-height: 140%;
    color: #423E48;
    text-align: left;
  }
  &__title{
    font-weight: 500;

  }
  &_action{
    align-items: stretch;

  }

  &__price{
    font-size: 12px;
    line-height: 140%;

    color: #423E48;
    margin-bottom: 20px;
  }

  .icon-delete{
    text-align: right;
    &:hover{
      color:#4275D8;
    }
  }

  button{
    margin-bottom: 20px;
  }

  a{
    font-weight: 400;
    font-size: 14px;
    line-height: 130%;
    color: #4275D8;
  }

}

</style>