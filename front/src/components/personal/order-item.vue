<template lang="html">
  <div class="order__item _open" v-if = "card">
    <div class="order__num" @click = "toggleOrder()">
      Заказ #  <span>{{ card.id }}</span>
    </div>
    <div class="flex-center order__row">
      <div class="order__invoice" @click.stop = "dowwnloadInvoice"> Счет </div>
      <div class="order__date">{{ card.created_at.slice(0, 10) }}</div>
      <div class="order__delivery">{{ delivery_type }}</div>
      <div class="order__status _status-color">{{ order_status }}</div>
      <div class="order__price">{{ order_price }}<span> BYN</span></div>
    </div>


  </div>
  <div class="order__details" v-if = "isOpen === true && card">
      <div class="details-order" v-if ="card.products.length">
        <div class="details-order__item flex-center"
            v-for   = "orderProduct in card.products"
            :key    = "orderProduct.id + card.id"
        >
          <div class="details-order__title long_text">{{ orderProduct.product.name }}</div>
          <div class="details-order__article"><span>{{ orderProduct.product.vendor_code }}</span></div>
          <div class="details-order__count">{{ orderProduct.amount }}<span> {{ orderProduct.product.base_unit.full_name }}</span></div>
          <div class="details-order__price"><b>{{ (orderProduct.amount * orderProduct.product.price).toFixed(2) }}</b> BYN</div>
        </div>
      </div>
  </div>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex';
export default {
  name: 'OrderItem',

  props: {
    card:  null,
  },

  data() {
    return {
      isOpen  : false,
    };
  },

  computed:{
    ...mapGetters("order", ["ORDER_DELIVERY_TYPES"]),

    order_price(){
      let totalPrice = 0;
      this.card.products.forEach(item => {
        totalPrice = totalPrice + Number((item.amount * item.product.price).toFixed(2));
      });
      return Number(totalPrice.toFixed(2));
    },

    order_status(){
      if (this.card.status === 'P') return 'В обработке';
      if (this.card.status === 'S') return 'Отправлен';
      if (this.card.status === 'c') return 'Отменен';
      if (this.card.status === 'C') return 'Выполнен';
    },

    delivery_type(){
      const type = this.ORDER_DELIVERY_TYPES.filter(item => item.id === this.card.delivery_type_id);
      return type.length ? type[0].payload : 'unknown';
    },

    productPrice(item){
      console.log(item);
      return (item.amount * item.product.price).toFixed(2)
    }
  },

  methods:{
    ...mapMutations("notification", ["SET_IS_LOADING"]),

    toggleOrder(){
      this.isOpen = !this.isOpen;
    },

    dowwnloadInvoice(){
      this.SET_IS_LOADING(true);
      const myHeaders = new Headers();
      myHeaders.append("Content-Type", "application/x-www-form-urlencoded");
      const urlencoded = new URLSearchParams();
      const requestOptions = {
          method  : 'POST',
          headers : myHeaders,
      };
      fetch(process.env.VUE_APP_API_URL + "orders/" + this.card.id + '/invoices', requestOptions)
      .then((response) => response.blob())
      .then((blob) => {
          const _url = window.URL.createObjectURL(blob);
          window.open(_url, '_blank');
          this.SET_IS_LOADING(false);
      }).catch((err) => {
          console.log(err);
          this.SET_IS_LOADING(false);
      });

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
      flex-basis: 16%;
      font-weight: 500;
      font-size: 16px;
      line-height: 24px;
      padding-right: 5px;
      white-space: nowrap;
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
      padding: 0 5px;
      @media (max-width: $md2+px) {
        order: 1;
      }
    }

    &__delivery{
      padding: 0 5px;
      max-width: 250px;
      @media (max-width: $md2+px) {
        order: 2;
      }
    }
    &__invoice{
      &:hover{
        color: #4275D8;
        cursor: pointer;
      }
    }
    &__status{
      padding: 0 5px;

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
      padding-left: 5px;
      font-weight: 500;
      white-space: nowrap;
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
    padding-right: 5px;
    flex-basis: 55%;
    font-weight: 300;
    font-size: 14px;
    text-decoration-line: underline;
  }
  &__article{
    padding: 0 5px;
    flex-basis: 15%;
    opacity: 0.4;
    text-align: center;
  }
  &__count{
    padding:5px;
    flex-basis: 15%;
    text-align: center;
    span{
      margin-left: 5px;
    }

  }
  &__price{
    padding-left: 5px;
    flex-basis: 20%;
    text-align: right;
    white-space: nowrap;

  }
}
._open{
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
  margin-bottom: 0;

}
</style>
