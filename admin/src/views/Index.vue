<script setup lang='ts'>
  import { useStore } from '../store'
  import { ActionTypes } from '../store/action-types'
  import { MutationTypes } from '../store/mutation-types'
  import {ref, onMounted, watch} from 'vue'
  import BaseTable from '@/components/Table/BaseTable.vue'
  import { IDeliveryType } from '../types'
  import Select from '@/components/UI/Select.vue'
  import PopUp from '@/components/PopUp/PopUp.vue'
  import Img from '@/components/UI/Img.vue'
  import Button from '@/components/UI/Button.vue'

  const store = useStore()

  const tableHeads = [
    {db: 'id', name: 'Номер заказа'},
    {db: 'date', name: 'Дата'}, 
    {db: 'delivery_type_name', name: 'Доставка'},
    {db: 'statusName', name: 'Статус'}, 
    {db: 'total_price', name: 'Сумма'}, 
    {db: '', name: ''},
    {db: '', name: ''},
  ]

  const orederType = ref('')
  const orderID = ref(null as unknown as string)
  const newStatus = ref(null as unknown as string)
  const orderData = ref()
  const tableData = ref([] as Array<IDeliveryType>)
  const fileredData = ref([] as Array<IDeliveryType>)
  const tableSizeColumns = '100px 1fr 1fr 1fr 60px 40px 40px'

  const ordersRequest = async () => {
    await store.dispatch(ActionTypes.GET_DELIVERY_TYPE, null)
    await store.dispatch(ActionTypes.GET_ORDERS_DATA, null)
  };

  watch(() => store.getters.orders,
    () => {
      tableData.value = [...store.getters.orderList]
      onFilterData()
      store.commit(MutationTypes.SET_IS_LOADING, false)
    }
  )

  onMounted(() => {
    store.commit(MutationTypes.SET_IS_LOADING, true)
    store.commit(MutationTypes.SET_ISPOPUPOPEN, false)
    newStatus.value =null as unknown as string
    orderID.value = null as unknown as string
    orderData.value = null
    ordersRequest()
  })

  const onFilterData = () => {
    if (orederType.value) {
      fileredData.value = tableData.value.filter(item => item.status === orederType.value)
    } else {
      fileredData.value = [...tableData.value]
    }
  }

  const onChangeType = (id: string) => {
    orederType.value = id
    onFilterData()
  }

  const onEditOrder = (order: IDeliveryType) => {
    store.commit(MutationTypes.SET_ISPOPUPOPEN, true)
    orderID.value = order.idFromDB
    orderData.value = store.getters.orders.filter(item => item.id === order.idFromDB)[0];
  }

  const price = (product: IDeliveryType) => {
    return product.price_with_discount_and_tax ? product.price_with_discount_and_tax : product.price_with_tax
  }

  const statusName = (id: string) => {
    const isStatus = store.getters.orderTypes.filter(item => item.id === id)
    return isStatus.length ? isStatus[0].name : 'Не известно'
  }

  const onSetNewType = (id: string) => {
    newStatus.value = id
  }

  const onSaveNewData = async () => {
    await store.dispatch(ActionTypes.UPDATE_ORDER_STATUS, {newStatus: newStatus.value, orderId: orderID.value})
    store.commit(MutationTypes.SET_IS_LOADING, false)
    store.commit(MutationTypes.SET_ISPOPUPOPEN, false)
    newStatus.value = null as unknown as string
    orderID.value = null as unknown as string
    orderData.value = null
  }

  const onGetInvoice = () => {
    store.commit(MutationTypes.SET_IS_LOADING, true)
    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/x-www-form-urlencoded");

    const urlencoded = new URLSearchParams();

    const requestOptions = {
        method  : 'POST',
        headers : myHeaders,
    };
    fetch(import.meta.env.VITE_APP_API_URL + "orders/" + orderID.value + '/invoices', requestOptions)
    .then((response) => response.blob())
    .then((blob) => {
        const _url = window.URL.createObjectURL(blob);
        window.open(_url, '_blank');
        store.commit(MutationTypes.SET_IS_LOADING, false)
    }).catch((err) => {
        console.log(err);
        store.commit(MutationTypes.SET_IS_LOADING, false)
    });
  }

</script>

<template>
  <div class="orders-content">
    <PopUp> 
      <div v-if = "orderData">
        <div class="product__container"
          v-for="(element) of orderData.products"
          :key="element.db"
        >

          <div class="product__wrapper" v-if="element.product">
            <a class="product__img">
                <Img :image = element.product.images />
                <!-- <Img :image="srcImage" /> -->
            </a>
            <div class="product__info">
                <div class="product__article  _label mb-20">Артикул: <span>{{ element.product.vendor_code }}</span></div>
                <a  class="product__title"> {{ element.product.name }}</a>
            </div>
          </div>

          <div class="product__wrapper">
            <div class="product__count flex-center">
              <div class="_label mb-20">Количество:</div>
              <div class="flex-center">
                <span class="product__input"> {{ element.amount }}</span>
              </div>
            </div>
            <div class="product__price">
              <div class="_label mb-20">Стоимость (с учетом НДС):</div>
              <div class="old_price">
                <span>{{ (element.product.price * element.amount).toFixed(2) }}</span>BYN
                <span>/{{ element?.product?.base_unit?.full_name }}</span>
              </div>
              <div class="current_price">
                <span>{{ (price(element.product) * element.amount).toFixed(2) }}</span>
                BYN
              </div>
            </div>

          </div>

        </div>
      </div>
      <div v-if = "orderData">
        <div>Обработать заказ</div>
        <Select
          v-if="store.getters.orderTypes.length"
          :text = "statusName(orderData.status)"
          :id  = "orderData.status" 
          fieldForSearch = "name"
          :data = "store.getters.orderTypes"
          @onSelectItem="onSetNewType"
        />
        <Button label="Сохранить" color="primary" @click="onSaveNewData()"></Button>
        <Button label="Счет" color="primary" @click="onGetInvoice()"></Button>
      </div>
    </PopUp>
    <h2 class="heading-2">Список заказов</h2>

    <div class="parameters-block">
      <Select
        v-if="store.getters.orderTypes.length"
        text = "Все заказы"
        :id   = orederType
        fieldForSearch = "name"
        :data = "store.getters.orderTypes"
        @onSelectItem="onChangeType"
      />
    </div>
    <base-table
      :head="tableHeads"
      :columnTemplates="tableSizeColumns"
      :tableData="fileredData"
      :addButton=false
      :deleteButton="false"
      @editRow="onEditOrder"
    />
  </div>
</template>

<style lang="scss" scoped>

  .parameters{
    &-block{
      margin: 20px 0;
      width: 500px;
    }
  }

  .product{

  &__container {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    padding: 24px 20px;
    background: #FFFFFF;
    border: 2px solid #EEEEEE;
    border-radius: 8px;
    margin-bottom: 16px;
    ._label{
      font-weight: 300;
      font-size: 12px;
      line-height: 20px;

    }
  }

  &__img {
      width: 100%;
      flex-basis: 20%;
      text-align: center;
      img{
          max-width: 100%;
          object-fit: fill;
      }
  }
  &__info{
    width: 100%;

  .icon{
      font-size: 10px;
      line-height: 20px;
      color: #423E48;
      opacity: 0.6;
      &:before{
        margin-right: 5px;
      }
      &:nth-child(1){
        margin-right: 15px;
      }
    }
  }

  &__title{
      font-size: 14px;
      line-height: 24px;
      text-decoration-line: underline;
      color: #423E48;
  }

  &__wrapper{
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  &__count{
      flex-direction: column;
      //margin: 24px 0;
      .icon-plus, .icon-minus{
          cursor: pointer;
      }
  }
  &__input{
      width: 40px;
      height: 40px;
      padding: 9px 8px;
      background: rgba(66, 62, 72, 0.07);
      border-radius: 2px;
      border: none;
      margin: 0 10px;
      text-align: center;
  }

  &__price{
      display: flex;
      flex-direction: column;
      align-items: flex-end;

      .old_price{
          font-size: 14px;
          line-height: 20px;
          text-decoration-line: line-through;
          opacity: 0.4;
          margin-bottom: 5px;
          min-height: 20px;
      }
      .current_price{
          font-size: 20px;
          line-height: 20px;
          color: #423E48;
          font-weight: 500;
      }

  }
}

</style>
