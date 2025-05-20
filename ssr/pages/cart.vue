<template>
  <Breadcrumb/>
  <div class="cart app__content">
    <div class="cart__wrapper">
      <div class="cart__content _container">
        <div class="cart__body">


          <div class="cart__block">
            <h3>Товары в корзине: <span>{{ totalOrderQuantity }}</span></h3>

            <div v-if = "orders.length === 0" class="cart__list">
              <div class="cart__empty__item">Ваша корзина пуста</div>
              <a class="_link" @click.prevent = "openPage('/catalog')">
                <svg width="16" height="8" viewBox="0 0 16 8" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M15.5 3.99935H0.916666M0.916666 3.99935L4.25 0.666016M0.916666 3.99935L4.25 7.33268" stroke="#4275D8"/>
                </svg>
                Вернуться к покупкам
              </a>
            </div>

            <div v-if = "orders.length !== 0" class="cart__list">
              <PersonalCartItem  
                class="cart__item"
                v-for = "cartItem in orders"
                :key = "cartItem.product.id"
                :cartItem = cartItem
                :type = true
              />
            </div>
            <div v-if = "orders.length !== 0" class="cart__footer flex-center">
              <div class="group cart__promo">
                <label for="promo" class="label">Промокод</label>
                <div class="input__box">
                  <input id="promo_code" class="promo_code" type="text" v-model="promo_code" autocomplete=off>
                  <button class="btn black" @click = "checkPromoCod()">Применить</button>
                </div>
              </div>
              <div class="cart__summary">
                <div class="_footnote">* Сумма указана с учетом НДС</div>
                <div class="label flex-center ">
                  Общая стоимость:
                  <span>{{ totalOrderCost }}</span>
                   BYN
                </div>
                <div class="">
                  <button @click.stop = "openOrderRequest()" class="btn" ref="secondPartElement">Оформить заказ</button>
                </div>
              </div>
            </div>
          </div>

          <!-- Появляется если есть товар в корзине  и человек наживаем кнопку оформить заказ -->

          <div v-if = "isApplicationOpen === true && orders.length !== 0" class="cart__order">
            <h3>Оформление заказа </h3>
            <div class="about__paragraph">
              <div class="about__paragraph__title">
                <span>Доставка</span>
              </div>
              <div class="about__paragraph__box flex-center">
                <div :class="[checkPickUp() ? 'group table3x disabled' : 'group table3x']">
                  <label for="city" class="label">Город / населенный пункт</label>
                  <input id="city" type="text" :class="{ 'is-invalid': authErrors.city }" v-model="city" autocomplete=off :disabled="checkPickUp()">
                  <div class="error-message" v-if="authErrors.city"> {{ authErrors.city }} </div>
                </div>
                <div class="radio__list table3x">
                  <div class="radio" v-for = "delivery in oredersStore.deliveryTypes" :key = delivery.id>
                    <input :id = delivery.id name="radio" type="radio" :value = delivery.id v-model = "delivery_type_id" @click=onChangeDeliveryType(delivery.is_pickup)>
                    <label :for = delivery.id class="radio-label">{{ delivery.payload }}</label>
                  </div>
                </div>

                <div :class="[checkPickUp() ? 'table3x disabled' : 'table3x']">
                  <div class="group mb-20">
                    <label for="address" class="label">Улица</label>
                    <input id="address" type="text" :class="{ 'is-invalid': authErrors.address }" v-model="address" autocomplete=off :disabled="checkPickUp()">
                    <div class="error-message" v-if="authErrors.address"> {{ authErrors.address }} </div>
                  </div>
                  <div class="group__row flex-center">
                    <div class="group">
                      <label for="" class="label">Дом</label>
                      <input id="house" type="text" :class="{ 'is-invalid': authErrors.house }" v-model="house" autocomplete=off :disabled="checkPickUp()">
                      <div class="error-message" v-if="authErrors.house"> {{ authErrors.house }} </div>
                    </div>
                    <div class="group">
                      <label for="address" class="label">Квартира</label>
                      <input id="" type="text" class="input" :disabled="checkPickUp()">
                    </div>
                  </div>

                </div>
              </div>
            </div>
            <div class="about__paragraph">
              <div class="about__paragraph__title">
                <span>Контактная информация</span>
              </div>
              <div class="about__paragraph__box flex-center group__row">
                <div class="group ">
                  <label for="full_name" class="label">ФИО</label>
                  <input id="full_name" type="text" :class="{ 'is-invalid': authErrors.full_name }" v-model="full_name" autocomplete=off>
                  <div class="error-message" v-if="authErrors.full_name"> {{ authErrors.full_name }} </div>
                </div>
                <div class="group ">
                  <label for="phone_number" class="label">Номер телефона</label>
                  <input id="phone_number" type="text" :class="{ 'is-invalid': authErrors.phone_number }" v-model="phone_number" autocomplete=off>
                  <div class="error-message" v-if="authErrors.phone_number"> {{ authErrors.phone_number }} </div>
                </div>
                <div class="group ">
                  <label for="email" class="label">Email</label>
                  <input id="email" type="text" :class="{ 'is-invalid': authErrors.email }" v-model="email" autocomplete=off>
                  <div class="error-message" v-if="authErrors.email"> {{ authErrors.email }} </div>
                </div>


                </div>
              </div>
            <div class="about__paragraph">
              <div class="about__paragraph__title">
                <span>Данные оптового клиента</span>
              </div>
              <div class="about__paragraph__box ">

                  <div class="group__row flex-center">
                    <div class="group">
                      <label for="company_name" class="label">Наименование компании</label>
                      <input id="company_name" type="text" :class="{ 'is-invalid': -authErrors.company_name }" v-model="company_name" autocomplete=off>
                      <div class="error-message" v-if="authErrors.company_name"> {{ authErrors.company_name }} </div>
                    </div>
                    <div class="group">
                      <label for="IBAN" class="label">Расчетный счет IBAN</label>
                      <input id="IBAN" type="text" :class="{ 'is-invalid': authErrors.IBAN }" v-model="IBAN" autocomplete=off>
                      <div id="anim" class="icon_info input__icon">
                          <div class="tooltip flex-center" data-tooltip="Новые счета IBAN записываются в таком формате: ААВВ ССС DDDD ЕЕЕЕ ЕЕЕЕ ЕЕЕЕ ЕЕЕЕ.">!</div>
                      </div>
                      <div class="error-message" v-if="authErrors.IBAN"> {{ authErrors.IBAN }} </div>
                    </div>
                  </div>

                <div class="group__row flex-center">
                  <div class="group">
                    <label for="unp" class="label">УНП</label>
                    <input id="unp" type="text" :class="{ 'is-invalid': authErrors.unp }" v-model="unp" autocomplete=off>
                    <div class="error-message" v-if="authErrors.unp"> {{ authErrors.unp }} </div>
                  </div>
                  <div class="group">
                    <label for="BIC" class="label">БИК</label>
                    <input id="BIC" type="text" :class="{ 'is-invalid': authErrors.BIC }" v-model="BIC" autocomplete=off>
                    <div class="error-message" v-if="authErrors.BIC"> {{ authErrors.BIC }} </div>
                  </div>
                </div>
                <div class="group__row flex-center">
                  <div class="group">
                    <label for="legal_address" class="label">Юридический адрес</label>
                    <input id="legal_address" type="text" :class="{ 'is-invalid': authErrors.legal_address }" v-model="legal_address" autocomplete=off>
                    <div class="error-message" v-if="authErrors.legal_address"> {{ authErrors.legal_address }} </div>
                  </div>
                  <div class="group">
                    <label for="serving_bank" class="label">Обслуживающий банк</label>
                    <input id="serving_bank" type="text" :class="{ 'is-invalid': authErrors.serving_bank }" v-model="serving_bank" autocomplete=off>
                    <div class="error-message" v-if="authErrors.serving_bank"> {{ authErrors.serving_bank }} </div>
                  </div>
                </div>

                </div>
              </div>
            <div class="about__paragraph">
              <div class="about__paragraph__title">
                <span>Оплата</span>
              </div>
              <div class="about__paragraph__box flex-center">

                <div class="radio__list">
                  <div class="radio">
                    <input id="radio-6" name="radio-1" type="radio" checked>
                    <label for="radio-6" class="radio-label">Безналичный расчет</label>
                  </div>
                  <p>После оформления заказа мы отправим счет для оплаты на ваш адрес электронной почты. Также наш
                    специалист свяжется с вами для подтверждения заказа.</p>
                </div>
                <div class="cart__summary">
                  <div class="summary__item">Стоимость товаров: <span>{{ totalOrderCost }}</span>BYN</div>
                  <div class="summary__item">Стоимость доставки: <span>0.0</span>BYN</div>
                  <div class="summary__item">Скидка по промокоду: <span>{{ promo_price }}</span></div>
                  <div class="summary__item">Итоговая стоимость: <span><b>{{ (totalOrderCost - promo_price).toFixed(2) }}</b></span>BYN</div>
                  <div class="_footnote">* Сумма указана с учетом НДС</div>
                  <button class="btn" @click="checkRequestData()">Оформить заказ</button>

                </div>


              </div>
            </div>

          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import axios from "@/utils/api";
  import { isValidEmail } from "@/common/validation";
  import { useHead } from 'nuxt/app';
  import { ref, computed, onMounted } from 'vue';
  import { useNotificationsStore } from '@/stores/notifications';
  import { useOrdersStore } from '@/stores/orders';
  import { useAuthStore } from '@/stores/auth';
  import { useHeaderStore } from "@/stores/header";
  import { useBreadCrumbStore } from '@/stores/breadcrumb';

  const router = useRouter();

  const notificationsStore = useNotificationsStore();
  const oredersStore = useOrdersStore();
  const authStore = useAuthStore();
  const headerStore = useHeaderStore();
  const breadCrumbStore = useBreadCrumbStore();

  const { isApplicationOpen } = storeToRefs(oredersStore);
  const { userData, authErrors } = storeToRefs(authStore);
  const { orders, totalOrderCost, totalOrderQuantity } = storeToRefs(oredersStore);

  const promo_code = ref("");
  const company_name = ref("");
  const unp = ref("");
  const legal_address = ref("");
  const IBAN = ref("");
  const BIC = ref("");
  const serving_bank = ref("");
  const full_name = ref("");
  const phone_number = ref("");
  const email = ref("");
  const city = ref("");
  const address = ref("");
  const house = ref("");
  const flat = ref("-");
  const delivery_type_id = ref(1);
  const promo_price = ref(0);
  const isLoading = ref(false);
  const isEnablePickup = ref(false);

  const secondPartElement = ref(null);

  useHead({
    title: 'Корзина',
    meta: [{
      name: 'Корзина',
      content: 'Страница Корзина'
    }]
  });

  const changeParameters = computed(() => {
    return JSON.stringify(userData.value)
  });

  watch(changeParameters, () => {
    company_name.value = userData.value?.company_name;
    unp.value = userData.value?.unp;
    legal_address.value = userData.value?.legal_address;
    IBAN.value = userData.value?.IBAN;
    BIC.value = userData.value?.BIC;
    serving_bank.value = userData.value?.serving_bank;
    full_name.value = userData.value?.full_name;
    phone_number.value = userData.value?.phone_number;
    email.value = userData.value?.email;
  });

  const openPage = (page) => {
    if (router.path != page) {
        router.push(page);
    }
  };

  const checkPromoCod = () => {
    console.log('Is ' + promo_code.value + ': promo cod available');
  };

  const checkPickUp = () => {
    return !isEnablePickup.value;
  };

  const openOrderRequest = () => {
    oredersStore.setIsApplicationOpen(true);
    const scrollY = secondPartElement.value.getBoundingClientRect().bottom + window.pageYOffset;
    setTimeout(() => window.scrollTo(0, scrollY), 200);
  };

  const onChangeDeliveryType = (type) => {
    isEnablePickup.value = Boolean(type)
  };

  const checkRequestData = async () => {
    console.log('Start send order ');
    const orderProducts = [];
    orders.value.forEach(item => orderProducts.push({amount: item.amount, id: item.product.id}));
    console.log('isLoading.value ', isLoading.value);
    
    if (isLoading.value) return;

    isLoading.value = true;
    const errorsInData = {};
    authStore.setErrors(errorsInData);
    if (!company_name.value) {
        errorsInData.company_name = 'Укажите название организации'
    }
    if (!unp.value || unp.value.toString().length !== 9) {
        errorsInData.unp = 'Укажите валидный УНП'
    }
    if (!legal_address.value) {
        errorsInData.legal_address = 'Укажите адрес организации'
    }
    if (!IBAN.value || IBAN.value.toString().length !== 28) {
        errorsInData.IBAN = 'Укажите валидный IBAN счет'
    }
    if (!BIC.value || BIC.value.toString().length < 6) {
        errorsInData.BIC = 'Укажите валидный BIC банка'
    }
    if (!serving_bank.value) {
        errorsInData.serving_bank = 'Укажите название банка'
    }
    if (!full_name.value) {
        errorsInData.full_name = 'Укажите ФИО'
    }
    if (!phone_number.value) {
        errorsInData.phone_number = 'Укажите номер телефона'
    }
    if (!city.value) {
      if (!checkPickUp()) {
        errorsInData.city = 'Укажите название города'
      }
    }
    if (!address.value) {
      if (!checkPickUp()) {
        errorsInData.address = 'Укажите название улицы'
      }
    }
    if (!house.value) {
      if (!checkPickUp()) {
        errorsInData.house = 'Укажите номер дома'
      }
    }
    if (!isValidEmail(email.value)) {
        errorsInData.email = 'Укажите валидный адрес эл. почты'
    }
    if (Object.keys(errorsInData).length) {
      authStore.setErrors(errorsInData);
      isLoading.value = false;
      const scrollY = secondPartElement.value.getBoundingClientRect().bottom + window.pageYOffset;
      // window.scrollTo(0, scrollY);
      setTimeout(() => window.scrollTo(0, scrollY), 200);
    } else {
      notificationsStore.setIsLoading(true);
      const orderData = {
        promo_code: promo_code.value, 
        company_name: company_name.value,
        unp: unp.value,
        legal_address: legal_address.value,
        IBAN: IBAN.value,
        BIC: BIC.value,
        serving_bank: serving_bank.value,
        full_name: full_name.value,
        phone_number: phone_number.value,
        email: email.value,
        city: city.value,
        address: address.value,
        house: house.value,
        flat: flat.value,
        delivery_type_id: delivery_type_id.value,
        products: orderProducts
      };

      if (localStorage.getItem("authToken")) {
        authStore.setDestination('/user_profile');
        // router.push('/login');
        orderData.user = userData.value.id;
        await oredersStore.sendOrderRequest(orderData);
        ym(94113822, 'reachGoal', 'oform-zakaz');
        isLoading.value = false;
        // notificationsStore.setIsLoading(true);
        // router.push('/user_profile');
      } else {
        try {
          const response = await axios.get("users/check_email/<email>?email=" + email.value);
          if (response.data.message === 'True') {
            notificationsStore.setIsLoading(false);
            headerStore.setIsPopUpOpen(true);
            headerStore.setPopUpAction('UserLogin');
            headerStore.setPopUpAdditionalData({email: orderData.email});
          } else if (response.data.message === 'False') {
            let password = '';
            for (let i = 0; i < 8; i++){
              let rand = Math.random() * 10 - 0.5;
              password = password + String(Math.round(rand))
            }
            const userDataForRegister = {
              email: email.value,
              full_name: full_name.value,
              phone_number: phone_number.value,
              company_name: company_name.value,
              unp: unp.value,
              password: password,
              legal_address: legal_address.value,
              IBAN: IBAN.value,
              BIC: BIC.value,
              serving_bank: serving_bank.value,
              isGenerated: true,
            };

            await authStore.sendRegisterRequest(userDataForRegister);
            orderData.user = userData.value.id;
            await oredersStore.sendOrderRequest(orderData);
            ym(94113822, 'reachGoal', 'oform-zakaz');
            isLoading.value = false;
            notificationsStore.setIsLoading(false);
            router.push('/user_profile');
          }
        }
        catch (e) {
          console.log(e);
          notificationsStore.setIsLoading(false);
        };
      }
      isLoading.value = false;
      notificationsStore.setIsLoading(false);
    }
  };

  onMounted(() => {
    oredersStore.setIsApplicationOpen(false);
    breadCrumbStore.changeBreadCrumb(0);
    breadCrumbStore.addBreadCrumb({
      name: router.currentRoute.value.meta.name,
      path: router.currentRoute.value.path,
      type: "global",
      class: ""
    });
    if (userData.value) {
      company_name.value = userData.value.company_name;
      unp.value = userData.value.unp;
      legal_address.value = userData.value.legal_address;
      IBAN.value = userData.value.IBAN;
      BIC.value = userData.value.BIC;
      serving_bank.value = userData.value.serving_bank;
      full_name.value = userData.value.full_name;
      phone_number.value = userData.value.phone_number;
      email.value = userData.value.email;
      city.value = userData.value.delivery_adress;
      address.value = userData.value.address;
      house.value = userData.value.house;
      flat.value = userData.value.flat;
    }
  });
</script>

<style scoped lang="scss">

.cart {
  min-height: 400px;
  h3{
    margin-bottom: 45px;
  }
  &__content-block{
    width: 100%;
    padding: 0 16px;
  }

  &__empty__item{
    margin-bottom: 20px;
    font-size: 14px;

  }

  &__item{
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
  &__list{
      ._link{
        margin-top: 20px;
        cursor: pointer;
      }
  }
  &__footer{
    align-items: flex-start;
    justify-content: space-between;
    width: 100%;
    padding: 40px 0;
    @media (max-width: $md2 + px){
      flex-direction: column;
      align-items: flex-end;
    }

    input{
      width:241px;
      border-bottom-right-radius: 0;
      border-top-right-radius: 0;
    }
    .black{
      border-bottom-left-radius: 0;
      border-top-left-radius: 0;
    }
  }
  &__summary{
    flex-basis: 50%;
    text-align: right;
    @media (max-width: $md3+px){
      margin-top: 30px;
    }

    .label{
      justify-content: flex-end;
      margin-top: 15px;
      align-items: flex-end;
    }

    span{
      font-weight: 600;
      font-size: 20px;
      line-height: 20px;
      &:nth-child(1){
        margin: 0 10px 0 10px;
      }
    }
    .btn{
      margin-top: 20px;
    }


  }
  &__order{
    .summary__item{
      font-size: 14px!important;
      line-height: 20px;
      opacity: 1!important;
      margin-bottom: 12px;
      &:nth-child(3){
        margin-bottom: 30px;
      }

      span{
        font-size: 16px;
        margin: 0 5px 0 10px;
      }


    }

  }

  &__promo{
      .input__box{
        display: flex;
    }
      .promo_code{
        width: inherit;
      }
  }

}



.content-block{
  width: 100%;
  &__title{
    font-weight: 500;
    font-size: 20px;
    line-height: 24px;
    color: #423E48;
    margin-bottom: 40px;
  }
}

.about__paragraph {
  margin-bottom: 60px;
  @media (max-width: $md2+px) {
    margin-bottom: 30px;
    &:last-child {
      .about__paragraph__box {
        align-items: flex-end;
      }
    }
    &:nth-child(4) {
      .group__row{
        flex-direction: column;
      }
    }
  }



  &__title {
    position: relative;
    height: 20px;
    background: rgba(66, 117, 216, 0.1);
    border-radius: 4px;

    span {

      font-weight: 500;
      position: absolute;
      top: -10px;
      left: 10px;
      font-size: 20px;
      line-height: 24px;
      color: #4275D8;
    }


  }

  &__box {
    padding: 24px 0 30px 0;
    align-items: flex-start;
    @media (max-width: $md2+px) {
      flex-direction: column;

    }
    .table3x{
      @media (max-width: $md2+px) {
        width: 100%;
      }
    }
    .group{
      width: 100%;
      position: relative;
      margin-bottom: 10px;

    }
  }

  &__text {

    p {
      margin: 10px 0;
      font-size: 18px;
      line-height: 140%;
    }
  }

  .radio__list {
    padding: 0 10px;
    @media (max-width: $md2+px) {
      order: -1;
    }
    p {
      font-size: 14px;
      line-height: 16px;
      opacity: 0.4;
    }
    .radio input{
      width: auto;
    }
    label{
      opacity: 1;
    }
  }
}



</style>
<style lang="scss">
.cart__item{
  position: relative;
  @media (max-width: $md2 + px){
    flex-direction: column;
  ._label{
    @media (max-width: $md2 + px){
      display: none;
    }
    }
  }
  .icon__row .icon{
    font-size: 15px;
    white-space: nowrap;
    &:before{
      font-size: 18px;

    }
  }
  .product__img{
    min-width: 100px;
    max-width: 10%;
    img{
      object-fit: contain;
    }

  }
}

.error-message {
  position: absolute;
  left: 15px;
  bottom: -4px;
  padding: 0 8px 0 8px;
  font-size: 12px;
  background-color: #fff;
  color: #E30044;

}

// tooltip style

.tooltip {
  position: relative;
  border: 2px solid #8c8b8e;
  //padding: 5px 12px;
  width: 20px;
  height: 20px;
  margin: 5px;
  color: #8c8b8e;
  font-weight: 600;
  font-size: 15px;
  border-radius: 50%;
  opacity: 0.5;
  padding-top: 2px;
  justify-content: center;
}

.tooltip:before,
.tooltip:after {
  position: absolute;
  content: '';
  opacity: 0;
  transition: all 0.4s ease;
}

.tooltip:before {
  border-width: 10px 8px 0 8px;
  border-style: solid;
  border-color:#423E48 transparent transparent transparent;
  top: -15px;
  transform: translateY(20px);
}

.tooltip:after {
  content: attr(data-tooltip);
  background: #423E48;
  border: 1px solid #423E48;
  color: #fff;
  width: 330px;
  height: 40px;
  font-size: 12px;
  line-height: 1.3;
  font-weight: 300;
  top: -50px;
  right: 0;

  padding: 5px 10px;
  border: 1px solid #423E48;
  border-radius: 5px;
  transform: translateY(20px);
}

.tooltip:hover::before,
.tooltip:hover::after {
  opacity: 1;
  transform: translateY(-2px);
}

@keyframes shake {
  0% {
    transform: rotate(2deg);
  }
  50% {
    transform: rotate(-3deg);
  }
  70% {
    transform: rotate(3deg);
  }

  100% {
    transform: rotate(0deg);
  }
}

#anim:hover {
  animation: shake 500ms ease-in-out forwards;
}
.icon_info{
  right: 3px;
  top: 23px;
}
</style>