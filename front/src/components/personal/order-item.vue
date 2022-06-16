<template lang="html">
  <div class="order__item _open">
    <div class="order__num" @click = "toggleOrder()">Заказ #  <span>65854</span></div>
    <div class="flex-center order__row">
      <div class="order__date">10 июня 2022</div>
      <div class="order__delivery">Тип доставки</div>
      <div class="order__status _status-color">Отправлен</div>
      <div class="order__price">58.40 <span>BYN</span></div>
    </div>


  </div>
  <div class="order__details" v-if = "isOpen === true">
      <div class="details-order">
        <div class="details-order__item flex-center">
          <div class="details-order__title">Вилка RJ-45 cat 5E FTP для витой пары 8P8C (100 шт) экранированная</div>
          <div class="details-order__article">арт. <span>125.125.125</span></div>
          <div class="details-order__count">10 <span>шт.</span></div>
          <div class="details-order__price"><b>20</b> BYN</div>
        </div>
        <div class="details-order__item flex-center">
          <div class="details-order__title">Вилка RJ-45 cat 5E FTP для витой пары 8P8C</div>
          <div class="details-order__article">арт. <span>125.125.125</span></div>
          <div class="details-order__count">100 <span>м.</span></div>
          <div class="details-order__price"><b>220</b> BYN</div>
        </div>

      </div>
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

    &__row{
      width: 100%;
      justify-content: space-between;
      @media (max-width: $md2+px) {
        flex-direction: column;
        align-items: flex-end;
      }
      div{
        @media (max-width: $md2+px) {
          font-size: 10px;
          margin-bottom: 4px;
        }
      }
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
      @media (max-width: $md2+px) {
        align-items: flex-start;
        padding: 12px 12px ;
      }
      ._status-color{
        color: #32A071;
        font-weight: 500;
      }

    }

    &__num{
      flex-basis: 22%;
      font-weight: 500;
      font-size: 16px;
      line-height: 24px;
      text-decoration-line: underline;
      color: #423E48;
      z-index: 4;
      @media (max-width: $md2+px) {
        flex-basis: 45%;
        font-size: 12px;
      }
      &:hover{
        color: #4275D8;
        cursor: pointer;
      }
    }
    &__date{
      @media (max-width: $md2+px) {
        order: 1;
      }
    }

    &__delivery{
      @media (max-width: $md2+px) {
        order: 2;
      }
    }

    &__status{
      @media (max-width: $md2+px) {
        order: 3;
      }
    }
    &__details{
        background: #fff;
        padding: 28px 28px;
        border: 2px solid #EEEEEE;
        border-bottom-right-radius: 8px;
        border-bottom-left-radius: 8px;
        margin-bottom: 16px;

    }



    &__price{
      font-weight: 500;
      @media (max-width: $md2+px) {
        font-weight: 600;
        font-size: 14px!important;
        line-height: 20px;
        margin-bottom: 10px!important;
        order: 0;
      }
      span{
        font-weight: 400;
      }
    }
  }


.details-order{
  font-size: 14px;

  &__item{
    justify-content: space-between;
    margin-bottom: 10px;
  }
  &__title{
    flex-basis: 55%;
    font-weight: 300;
    font-size: 14px;
    text-decoration-line: underline;
  }
  &__article{
    flex-basis: 15%;
    opacity: 0.4;
    text-align: center;
  }
  &__count{
    flex-basis: 15%;
    text-align: center;

  }
  &__price{
    flex-basis: 15%;
    text-align: right;

  }
}
._open{
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
  margin-bottom: 0;

}
</style>
