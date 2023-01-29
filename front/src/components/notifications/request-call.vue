<template>
    <div class="content__popup">
        <h3>Заказать звонок</h3>
        <div class="">
            <div class="group">
                <label class="label">Ваше имя</label>
                <input type="text" class="input" :class="{ 'is-invalid': ERRORS.email }" v-model="email">
                <div class="error-message" v-if="ERRORS.email"> {{ ERRORS.email }} </div>
            </div>
            <div class="group">
                <label class="label">Контактный телефон</label>
                <input type="text" class="input" :class="{ 'is-invalid': ERRORS.phone }" v-model="phone">
                <div class="error-message" v-if="ERRORS.phone"> {{ ERRORS.phone }} </div>
            </div>

            <div class="group__row flex-center mt-20">
                <div class="center-text">
                    <button @click = "cancelRequest()" type="submit" class="btn black">Отмена</button>
                </div>

                <div class="center-text">
                    <button @click = "sendRequest()" type="submit" class="btn black">Заказать звонок</button>
                </div>

            </div>
        </div>
    </div>
</template>

<script>
import { createElementBlock } from '@vue/runtime-core';

  import { mapGetters, mapMutations } from "vuex";
  import { isValidEmail } from "../../common/validation";

  export default {
    name: "RequestCall",

    data: function() {
      return {
          email     : '',
          phone: '',
          isLoading: false,
      }
    },


    computed: {
        ...mapGetters("auth",["ERRORS"]),
    },

    async beforeUnmount() {
      this.SET_ERRORS({});
    },


    methods: {
        ...mapMutations("header", ["SET_IS_POPUP_OPEN", "SET_POPUP_ACTION", "SET_POPUP_MESSAGE"]),
        ...mapMutations("auth", ["SET_ERRORS"]),

        cancelRequest(){
            this.SET_IS_POPUP_OPEN(false);
            this.SET_POPUP_ACTION('');
        },

        sendRequest(){
            if (this.isLoading) return;

            this.isLoading = true;
            const errorsInData = {};
            this.SET_ERRORS(errorsInData);

            if (!isValidEmail(this.email)) {
                errorsInData.email = 'Укажите валидный адрес эл. почты'
            }
            if (!this.phone) {
                errorsInData.phone = 'Укажите номер телефона'
            }
            if (Object.keys(errorsInData).length) {
                this.SET_ERRORS(errorsInData);
            } else {
                const data = {
                    email: this.email,
                    phone_number: this.phone,
                };
                // Тут посылаем на бэк запрос и ждем ответа, по результатам фомируем окно с ответом
                // await this.SEND_REGISTER_REQUEST(data);
                this.SET_POPUP_ACTION('ShowCompleteMsg');
                const msg ={};
                msg.main = 'Наш менеджер свяжется с вами в ближайшее время.';
                msg.bolt = 'Время работы:';
                msg.sub = ' Пн-Пт - 9:00 - 17:00'
                this.SET_POPUP_MESSAGE(msg);
            }
            this.isLoading = false;
        }
    }
  }
</script>

<style lang="scss" scoped>
  .group{
    //width: 100%;
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    margin-bottom: 15px;
    text-align: center;
    justify-content: center;
  }
  input{
    width: 100%;
    background: #FFFFFF;
    border: 1px solid rgba(66, 62, 72, 0.2);
    border-radius: 8px;
    padding: 10px 16px;
  }
  .is-invalid{
    border: 1px solid #E30044;
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
</style>
