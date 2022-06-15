<template lang="html">
  <div class="order__item">
    <div class="order__num" @click = "toggleOrder()">Заказ #  <span>65854</span></div>
    <div class="order__date">10 июня 2022</div>
    <div class="order__delivery">Тип доставки</div>
    <div class="order__status _status-color">Отправлен</div>
    <div class="order__price">58.40 <span>BYN</span></div>
  </div>
  <div v-if = "isOpen === true">
      Тут будет информация о заказе
  </div>
</template>

<script>
export default {
  name: 'OrderItem',

  data() {
    return {
      isOpen  : false,
    };
  },

  methods:{
    toggleOrder(){
      this.isOpen = !this.isOpen;
    }
  }
}
</script>

<style lang="scss" scoped>
  .order{

    &__list{

    }
    &__item{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 30px 18px 30px 28px;
      background: #FFFFFF;
      border: 2px solid #EEEEEE;
      border-radius: 8px;
      margin-bottom: 16px;
      ._status-color{
        color: #32A071;
        font-weight: 500;
      }
    }
    &__num{
      font-weight: 500;
      font-size: 16px;
      line-height: 24px;
      text-decoration-line: underline;
      color: #423E48;
      z-index: 4;
      &:hover{
        color: #4275D8;
        cursor: pointer;
      }
    }
    &__date{

    }

    &__delivery{

    }

    &__status{

    }



    &__price{
      font-weight: 500;
      span{
        font-weight: 400;
      }
    }
  }
</style>
