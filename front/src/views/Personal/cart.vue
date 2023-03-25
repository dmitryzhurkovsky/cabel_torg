<template>
  <div class="cart">
    <div class="cart__wrapper">
      <div class="cart__content _container">
        <div class="cart__body">


          <div class="cart__block">
            <h3>Товары в корзине: <span>{{ TOTAL_ORDER_QUANTITY }}</span></h3>

            <div v-if = "ORDERS.length === 0" class="cart__list">
              <div class="cart__empty__item">Ваша корзина пуста</div>
              <a class="_link" @click.prevent = "openPage('/catalog')">
                <svg width="16" height="8" viewBox="0 0 16 8" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M15.5 3.99935H0.916666M0.916666 3.99935L4.25 0.666016M0.916666 3.99935L4.25 7.33268" stroke="#4275D8"/>
                </svg>
                Вернуться к покупкам
              </a>
            </div>

            <div v-if = "ORDERS.length !== 0" class="cart__list">
              <CartItem  
                class="cart__item"
                v-for = "cartItem in ORDERS"
                :key = "cartItem.product.id"
                :cartItem = cartItem
                :type = true
              />
            </div>
            <div v-if = "ORDERS.length !== 0" class="cart__footer flex-center">
              <div class="group cart__promo">
                <label for="promo" class="label">Промокод</label>
                <div class="input__box">
                  <input id="promo_code" type="text" v-model="promo_code" autocomplete=off>
                  <button class="btn black" @click = "checkPromoCod()">Применить</button>
                </div>
              </div>
              <div class="cart__summary">
                <div class="_footnote">* Сумма указана с учетом НДС</div>
                <div class="label flex-center ">
                  Общая стоимость:
                  <span>{{ TOTAL_ORDER_COST }}</span>
                   BYN
                </div>
                <div class="">
                  <button @click.stop = "openOrderRequest()" class="btn" ref="secondPartElement">Оформить заказ</button>
                </div>
              </div>
            </div>
          </div>

          <!-- Появляется если есть товар в корзине  и человек наживаем кнопку оформить заказ -->

          <div v-if = "IS_APPLICATION_OPEN === true" class="cart__order">
            <h3>Оформление заказа </h3>
            <div class="about__paragraph">
              <div class="about__paragraph__title">
                <span>Доставка</span>
              </div>
              <div class="about__paragraph__box flex-center">
                <div class="group table3x">
                  <label for="city" class="label">Город / населенный пункт</label>
                  <input id="city" type="text" :class="{ 'is-invalid': ERRORS.city }" v-model="city" autocomplete=off>
                  <div class="error-message" v-if="ERRORS.city"> {{ ERRORS.city }} </div>
                </div>
                <div class="radio__list table3x">
                  <div class="radio" v-for = "delivery in ORDER_DELIVERY_TYPES" :key = delivery.id>
                    <input :id = delivery.id name="radio" type="radio" :value = delivery.id v-model = "delivery_type_id">
                    <label :for = delivery.id class="radio-label">{{ delivery.payload }}</label>
                  </div>
                </div>

                <div class="table3x">
                  <div class="group mb-20">
                    <label for="address" class="label">Улица</label>
                    <input id="address" type="text" :class="{ 'is-invalid': ERRORS.address }" v-model="address" autocomplete=off>
                    <div class="error-message" v-if="ERRORS.address"> {{ ERRORS.address }} </div>
                  </div>
                  <div class="group__row flex-center">
                    <div class="group">
                      <label for="" class="label">Дом</label>
                      <input id="house" type="text" :class="{ 'is-invalid': ERRORS.house }" v-model="house" autocomplete=off>
                      <div class="error-message" v-if="ERRORS.house"> {{ ERRORS.house }} </div>
                    </div>
                    <div class="group">
                      <label for="address" class="label">Квартира</label>
                      <input id="" type="text" class="input">
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
                  <input id="full_name" type="text" :class="{ 'is-invalid': ERRORS.full_name }" v-model="full_name" autocomplete=off>
                  <div class="error-message" v-if="ERRORS.full_name"> {{ ERRORS.full_name }} </div>
                </div>
                <div class="group ">
                  <label for="phone_number" class="label">Номер телефона</label>
                  <input id="phone_number" type="text" :class="{ 'is-invalid': ERRORS.phone_number }" v-model="phone_number" autocomplete=off>
                  <div class="error-message" v-if="ERRORS.phone_number"> {{ ERRORS.phone_number }} </div>
                </div>
                <div class="group ">
                  <label for="email" class="label">Email</label>
                  <input id="email" type="text" :class="{ 'is-invalid': ERRORS.email }" v-model="email" autocomplete=off>
                  <div class="error-message" v-if="ERRORS.email"> {{ ERRORS.email }} </div>
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
                      <input id="company_name" type="text" :class="{ 'is-invalid': ERRORS.company_name }" v-model="company_name" autocomplete=off>
                      <div class="error-message" v-if="ERRORS.company_name"> {{ ERRORS.company_name }} </div>
                    </div>
                    <div class="group">
                      <label for="IBAN" class="label">Расчетный счет IBAN</label>
                      <input id="IBAN" type="text" :class="{ 'is-invalid': ERRORS.IBAN }" v-model="IBAN" autocomplete=off>
                      <div class="error-message" v-if="ERRORS.IBAN"> {{ ERRORS.IBAN }} </div>
                    </div>
                  </div>

                <div class="group__row flex-center">
                  <div class="group">
                    <label for="unp" class="label">УНП</label>
                    <input id="unp" type="text" :class="{ 'is-invalid': ERRORS.unp }" v-model="unp" autocomplete=off>
                    <div class="error-message" v-if="ERRORS.unp"> {{ ERRORS.unp }} </div>
                  </div>
                  <div class="group">
                    <label for="BIC" class="label">БИК</label>
                    <input id="BIC" type="text" :class="{ 'is-invalid': ERRORS.BIC }" v-model="BIC" autocomplete=off>
                    <div class="error-message" v-if="ERRORS.BIC"> {{ ERRORS.BIC }} </div>
                  </div>
                </div>
                <div class="group__row flex-center">
                  <div class="group">
                    <label for="legal_address" class="label">Юридический адрес</label>
                    <input id="legal_address" type="text" :class="{ 'is-invalid': ERRORS.legal_address }" v-model="legal_address" autocomplete=off>
                    <div class="error-message" v-if="ERRORS.legal_address"> {{ ERRORS.legal_address }} </div>
                  </div>
                  <div class="group">
                    <label for="serving_bank" class="label">Обслуживающий банк</label>
                    <input id="serving_bank" type="text" :class="{ 'is-invalid': ERRORS.serving_bank }" v-model="serving_bank" autocomplete=off>
                    <div class="error-message" v-if="ERRORS.serving_bank"> {{ ERRORS.serving_bank }} </div>
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
                  <div class="summary__item">Стоимость товаров: <span>{{ TOTAL_ORDER_COST }}</span>BYN</div>
                  <div class="summary__item">Стоимость доставки: <span>0.0</span>BYN</div>
                  <div class="summary__item">Скидка по промокоду: <span>{{ promo_price }}</span></div>
                  <div class="summary__item">Итоговая стоимость: <span><b>{{ (TOTAL_ORDER_COST - promo_price).toFixed(2) }}</b></span>BYN</div>
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

<script>
  import axios from "axios";
  import {mapActions, mapGetters, mapMutations} from 'vuex'
  import CartItem from '@/components/catalog/cart-item.vue';
  import { isValidEmail } from "../../common/validation";

  export default {
    name: 'cart',
  
    components: {
      CartItem
    },

    data: function(){
      return{
        promo_code: "",
        company_name: "",
        unp: "",
        legal_address: "",
        IBAN: "",
        BIC: "",
        serving_bank: "",
        full_name: "",
        phone_number: "",
        email: "",
        city: "",
        address: "",
        house: "",
        flat: "-",
        delivery_type_id: 1,
        promo_price: 0,
        isLoading: false,
      }
    },

    watch:{
      changeParameters: function() {
        this.company_name = this.USER.company_name;
        this.unp = this.USER.unp;
        this.legal_address = this.USER.legal_address;
        this.IBAN = this.USER.IBAN;
        this.BIC = this.USER.BIC;
        this.serving_bank = this.USER.serving_bank;
        this.full_name = this.USER.full_name;
        this.phone_number = this.USER.phone_number;
        this.email = this.USER.email;
      }
    },

    computed: {
      ...mapGetters("order", ["ORDERS", "TOTAL_ORDER_QUANTITY", "TOTAL_ORDER_COST", "IS_APPLICATION_OPEN", "ORDER_DELIVERY_TYPES"]),
      ...mapGetters("auth",["ERRORS", "USER"]),
      ...mapGetters("header", ["TOP_CATEGORIES_ITEM_ACTIVE", "SUB_CATEGORIES_ITEM_ACTIVE", "LAST_CATEGORIES_ITEM_ACTIVE"]),

      changeParameters(){
        return JSON.stringify(this.USER)
      }
    },

    methods: {
      ...mapActions("order", ["GET_USER_ORDER", "SEND_ORDER_REQUEST"]),
      ...mapActions("breadcrumb", ["CHANGE_BREADCRUMB"]),
      ...mapActions("auth", ["SEND_REGISTER_REQUEST"]),
      ...mapMutations("order", ["SET_IS_APPLICATION_OPEN"]),
      ...mapMutations("breadcrumb", ["ADD_BREADCRUMB"]),
      ...mapMutations("auth", ["SET_ERRORS", "SET_DESTINATION"]),
      ...mapMutations("header", ["SET_IS_POPUP_OPEN", "SET_POPUP_ACTION", "SET_POPUP_ADDITIONAL_DATA"]),

      openPage(page) {
          if (this.$router.path != page) {
              this.$router.push(page);
          }
      },

      checkPromoCod(){
        console.log('Is ' + this.promo_code + ': promo cod available');
      },

      openOrderRequest(){
        this.SET_IS_APPLICATION_OPEN(true);
        const scrollY = this.$refs.secondPartElement.getBoundingClientRect().bottom + window.pageYOffset;
        setTimeout(() => window.scrollTo(0, scrollY), 200);
      },

      async checkRequestData(){
        console.log('Start send order ');
        const orderProducts = [];
        this.ORDERS.forEach(item => orderProducts.push({amount: item.amount, id: item.product.id}));

        if (this.isLoading) return;

        this.isLoading = true;
        const errorsInData = {};
        this.SET_ERRORS(errorsInData);

        if (!this.company_name) {
            errorsInData.company_name = 'Укажите название организации'
        }
        if (!this.unp || this.unp.toString().length !== 9) {
            errorsInData.unp = 'Укажите валидный УНП'
        }
        if (!this.legal_address) {
            errorsInData.legal_address = 'Укажите адрес организации'
        }
        if (!this.IBAN || this.IBAN.toString().length !== 28) {
            errorsInData.IBAN = 'Укажите валидный IBAN счет'
        }
        if (!this.BIC || this.BIC.toString().length < 6) {
            errorsInData.BIC = 'Укажите валидный BIC банка'
        }
        if (!this.serving_bank) {
            errorsInData.serving_bank = 'Укажите название банка'
        }
        if (!this.full_name) {
            errorsInData.full_name = 'Укажите ФИО'
        }
        if (!this.phone_number) {
            errorsInData.phone_number = 'Укажите номер телефона'
        }
        if (!this.city) {
            errorsInData.city = 'Укажите название города'
        }
        if (!this.address) {
            errorsInData.address = 'Укажите название улицы'
        }
        if (!this.house) {
            errorsInData.house = 'Укажите номер дома'
        }
        if (!isValidEmail(this.email)) {
            errorsInData.email = 'Укажите валидный адрес эл. почты'
        }
        if (Object.keys(errorsInData).length) {
          this.SET_ERRORS(errorsInData);
          this.isLoading = false;
          const scrollY = this.$refs.secondPartElement.getBoundingClientRect().bottom + window.pageYOffset;
          // window.scrollTo(0, scrollY);
          setTimeout(() => window.scrollTo(0, scrollY), 200);
        } else {

          const orderData = {
            promo_code: this.promo_code, 
            company_name: this.company_name,
            unp: this.unp,
            legal_address: this.legal_address,
            IBAN: this.IBAN,
            BIC: this.BIC,
            serving_bank: this.serving_bank,
            full_name: this.full_name,
            phone_number: this.phone_number,
            email: this.email,
            city: this.city,
            address: this.address,
            house: this.house,
            flat: this.flat,
            delivery_type_id: this.delivery_type_id,
            // user_id: this.USER.id,
            products: orderProducts
          };

          if (localStorage.getItem("authToken")) {
            // this.SET_DESTINATION('/cart');
            // this.$router.push('/login');
            orderData.user = this.USER.id;
            await this.SEND_ORDER_REQUEST(orderData);
            this.isLoading = false;
            this.$router.push({name: "user-cab"});
          } else {
            console.log('Тут проверяем есть ли пользователь');
            try {
              const response = await axios.get(process.env.VUE_APP_API_URL + "users/check_email/<email>?email=" + this.email);
              console.log(response);
              console.log(response.data.message === 'True');
              if (response.data.message === 'True') {
                this.SET_IS_POPUP_OPEN(true);
                this.SET_POPUP_ACTION('UserLogin');
                this.SET_POPUP_ADDITIONAL_DATA({email: orderData.email});
                console.log('Пользователь существует. Требуем залогиниться');
              } else if (response.data.message === 'False') {
                console.log('прльзователя нет создаем с нуля');
                let password = '';
                for (let i = 0; i < 8; i++){
                  let rand = Math.random() * 10 - 0.5;
                  password = password + String(Math.round(rand))
                }
                const userData = {
                  email: this.email,
                  full_name: this.full_name,
                  phone_number: this.phone_number,
                  company_name: this.company_name,
                  unp: this.unp,
                  password: password,
                  legal_address: this.legal_address,
                  IBAN: this.IBAN,
                  BIC: this.BIC,
                  serving_bank: this.serving_bank,
                };

                await this.SEND_REGISTER_REQUEST(userData);
                orderData.user = this.USER.id;
                await this.SEND_ORDER_REQUEST(orderData);
                this.isLoading = false;
                this.$router.push({name: "user-cab"});
              }
            }
            catch (e) {
              console.log(e);
            };
          }
          this.isLoading = false;
        }
      },
    },

    async checkIsUserLogin() {
      // await 
    },

    mounted() {
      this.SET_IS_APPLICATION_OPEN(false);
      this.CHANGE_BREADCRUMB(0);
      this.ADD_BREADCRUMB({
        name: this.$router.currentRoute.value.meta.name,
        path: this.$router.currentRoute.value.path,
        type: "global",
        class: ""
      });
      if (this.USER) {
        this.company_name = this.USER.company_name;
        this.unp = this.USER.unp;
        this.legal_address = this.USER.legal_address;
        this.IBAN = this.USER.IBAN;
        this.BIC = this.USER.BIC;
        this.serving_bank = this.USER.serving_bank;
        this.full_name = this.USER.full_name;
        this.phone_number = this.USER.phone_number;
        this.email = this.USER.email;
        // this.city = this.USER.delivery_adress;
        // this.address = this.USER.address;
        // this.house = this.USER.house;
        // this.flat = this.USER.flat;
      }
    },
  }
</script>

<style scoped lang="scss">

.cart {
  min-height: 300px;
  h3{
    margin-bottom: 45px;
  }
  &__content-block{
    width: 100%;
    padding: 0 16px;
  }

  &__block{ }
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

  }

}



.content-block{
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

  }
}
</style>