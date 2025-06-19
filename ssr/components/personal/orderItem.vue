<template>
  <div>
    <div v-if = "card"
      :class="[isOpen ? 'order__item _open' : 'order__item']"
    >
      <div class="order__num" @click = "toggleOrder()">
        Заказ #  <span>{{ card.id }}</span>
      </div>
      <div class="flex-center order__row">
        <div class="order__invoice" @click.stop = "dowwnloadInvoice"> Счет </div>
        <div class="order__date">{{ order_date }}</div>
        <div class="order__delivery">{{ delivery_type }}</div>
        <div :class="['order__status', `_status-color-${order_color}`]">{{ order_status }}</div>
        <div class="order__price">{{ order_price }}<span> BYN</span></div>
      </div>
    </div>
    <div class="order__details" v-if = "isOpen === true && card">
        <div class="details-order" v-if ="card.products.length">
          <div class="details-order__item flex-center"
              v-for   = "orderProduct in card.products"
              :key    = "String(orderProduct.id) + String(card.id)"
          >
            <div class="details-order__title long_text">{{ orderProduct.product.name }}</div>
            <div class="details-order__article"><span>{{ orderProduct.product.vendor_code }}</span></div>
            <div class="details-order__count">{{ orderProduct.amount }}<span> {{ orderProduct.product.base_unit.full_name }}</span></div>
            <div class="details-order__price">
              <b>
                {{ Number(orderProduct.amount * (orderProduct.product.price_with_discount_and_tax && orderProduct.product.price_with_discount_and_tax !== orderProduct.product.price_with_tax ? orderProduct.product.price_with_discount_and_tax : orderProduct.product.price_with_tax)).toFixed(2)}}
              </b> BYN
            </div>
                <!-- : orderProduct.product.price_with_tax).toFixed(2)  -->
            <!-- orderProduct.product.price -->
          </div>
        </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, computed } from 'vue';
  import { useOrdersStore } from '@/stores/orders';
  import { useNotificationsStore } from '@/stores/notifications';

  const ordersStore = useOrdersStore();
  const notificationsStore = useNotificationsStore();

  const { deliveryTypes } = storeToRefs(ordersStore);

  const props = defineProps({
    card:  { type: Object,  default: null},
  });

  const isOpen = ref(false);

  const order_price = computed(() => {
    let totalPrice = 0;
    props.card.products.forEach(item => {
      const price = item.product.price_with_discount_and_tax && item.product.price_with_discount_and_tax !== item.product.price_with_tax ? item.product.price_with_discount_and_tax : item.product.price_with_tax
      totalPrice = totalPrice + Number((item.amount * price));
    });
    return totalPrice.toFixed(2);
  });

  const order_status = computed(() => {
    if (props.card.status === 'P') return 'В обработке';
    if (props.card.status === 'S') return 'Отправлен';
    if (props.card.status === 'c') return 'Отменен';
    if (props.card.status === 'C') return 'Выполнен';
  });

  const order_color = computed(() => {
    if (props.card.status === 'P') return 'progress';
    if (props.card.status === 'S') return 'send';
    if (props.card.status === 'c') return 'cancel';
    if (props.card.status === 'C') return 'complete';
  });

  const order_date = computed(() => {
    const dirtyDate = props.card.created_at.slice(0, 10);
    const year = dirtyDate.slice(0, 4);
    const month = dirtyDate.slice(5, 7);
    const date = dirtyDate.slice(8);
    return date + '.' + month + '.' + year;
  });

  const delivery_type = computed(() => {
    const type = deliveryTypes.value.filter(item => item.id === props.card.delivery_type_id);
    return type.length ? type[0].payload : 'unknown';
  });

  // const productPrice = (item) => {
  //   // console.log(item);
  //   return (item.amount * item.product.price).toFixed(2)
  // };

  const toggleOrder = () => {
    isOpen.value = !isOpen.value;
  };

  const dowwnloadInvoice = () => {
    notificationsStore.setIsLoading(true);
    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/x-www-form-urlencoded");
    myHeaders.append("Authorization", "Bearer " + localStorage.getItem("authToken"));
    const urlencoded = new URLSearchParams();
    const requestOptions = {
        method  : 'POST',
        headers : myHeaders,
    };
    fetch(useRuntimeConfig().public.NUXT_APP_API_URL + "orders/" + props.card.id + '/invoices', requestOptions)
    .then((response) => response.blob())
    .then((blob) => {
        const _url = window.URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = _url;
        link.download = 'invoise' + props.card.id;
        link.click();
        // URL.revokeObjectURL(link.href);
        // window.open(_url, '_blank');
        notificationsStore.setIsLoading(false);
    }).catch((err) => {
        console.log(err);
        notificationsStore.setIsLoading(false);
    });
  };
  // }
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
      position: relative;
      padding: 30px 18px 30px 28px;
      background: #FFFFFF;
      border: 2px solid #EEEEEE;
      border-radius: 8px;
      margin-bottom: 16px;
      @media (max-width: $md2+px) {
        align-items: flex-start;
        padding: 12px 12px ;
      }
      ._status-color-complete{
        color: #32A071;
        font-weight: 500;
      }
      ._status-color-send{
        color: orange;
        font-weight: 500;
      }
      ._status-color-cancel{
        color: red;
        font-weight: 500;
      }
      ._status-color-progress{
        color: blue;
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
        text-align: right;
      }
    }
    &__invoice{
        position: absolute;
        right: 23px;
        bottom: 10px;
        font-size: 12px;
      @media (max-width: $md2+px) {
        right: auto;
        bottom: 7px;
        left: 17px;
  }

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
    border-top:none;

}



&__price{
  padding-left: 5px;
  font-weight: 500;
  white-space: nowrap;
  min-width: 110px;
  text-align: right;
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
