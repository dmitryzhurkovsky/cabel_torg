<template>
  <div class="contacts">
    <div class="contacts__wrapper">
      <div class="contacts__content _container">
        <div class="contacts__body">
          <h3>Контактная информация</h3>
          <p>Если у вас возникнут какие-либо вопросы по работе нашего интернет-магазина или понадобится консультация
            относительно ассортимента, обратитесь к нам любым удобным для вас способом. Мы обязательно поможем!</p>
          <div class="contacts__block flex-center">

            <div class="contacts__block__item">
                <div class="block__item flex-center">
                  <img  class="_icon" src="@/assets/svg/phone.svg" alt="Phone">
                  <a class="_title"  :href="'tel:' + String(SETTINGS.phone).replace(/ /g,'')">{{ SETTINGS.phone }}</a>
                </div>
                <div class="block__item flex-center">
                  <img class="_icon" src="@/assets/svg/round-place.svg" alt="Address">
                  <div>
                    <div class="_title">Наш адрес:</div>
                    <div>{{ SETTINGS.legal_address }}</div>
                  </div>
                </div>
                <div class="block__item flex-center" 
                  v-for = "address in SETTINGS.addresses" 
                  :key ="address.id"
                >
                  <img class="_icon" src="@/assets/svg/round-place.svg" alt="Address">
                  <div>
                    <div class="_title">{{ address.title }}:</div>
                    <div>{{ address.payload }}</div>
                  </div>
                </div>
            </div>
            <div class="contacts__block__item">
              <form class="contacts__form form-contacts">
                <div class="form-contacts__title mb-20 ">Напишите нам</div>
                <div class="group">
                    <input type="text" class="input mb-20" placeholder="ФИО" v-model="fullname">
                    <div class="error-message" v-if="ERRORS.fullname"> {{ ERRORS.fullname }} </div>
                </div>
                <!-- <input type="text" class="input mb-20" placeholder="ФИО" v-model="fullname"> -->
                <div class="form-contacts__row flex-center mb-20">
                  <div class="group">
                    <input type="text" class="input" placeholder="Email" v-model="email">
                    <div class="error-message" v-if="ERRORS.email"> {{ ERRORS.email }} </div>
                  </div>
                  <div class="group">
                    <input type="text" class="input" placeholder="Телефон" v-model="phone_number">
                    <div class="error-message" v-if="ERRORS.phone_number"> {{ ERRORS.phone_number }} </div>
                  </div>
                </div>
                <div class="group">
                  <textarea class="textarea mb-20" placeholder="Сообщение" v-model="message"></textarea>
                  <div class="error-message" v-if="ERRORS.message"> {{ ERRORS.message }} </div>
                </div>
                <button class="btn" @click = "sendRequest($event)">Отправить</button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters, mapMutations } from "vuex";

  definePageMeta({
    // middleware: ["auth"],
    name: 'Контакты',
  });

  export default defineNuxtComponent({
    name: 'Contacts',

    head () {
      return {
        title: 'Кабельторг | Контакты',
        meta: [{
          name: 'Контакты',
          content: 'Страница Контакты'
        }]
      }
    },

    data: function() {
      return {
          fullname: '',
          phone_number: '',
          email: '',
          message: '',
          isLoading: false,
      }
    },

    computed: {
      ...mapGetters("auth",["ERRORS"]),
      ...mapGetters("main", ["SETTINGS"]),
    },

    mounted(){
      this.$store.dispatch("breadcrumb/CHANGE_BREADCRUMB", 0);
      this.$store.commit('breadcrumb/ADD_BREADCRUMB', {
        name: this.$router.currentRoute.value.meta.name,
        path: this.$router.currentRoute.value.path,
        type: "global",
        class: ""
      });
    },

    methods: {
      ...mapMutations("auth", ["SET_ERRORS",]),
      ...mapActions("header", ["SEND_REQUEST_FEEDBACK",]),

      async sendRequest(event){
        event.preventDefault();
        if (this.isLoading) return;

        this.isLoading = true;
        const errorsInData = {};
        this.SET_ERRORS(errorsInData);

        if (!this.fullname) {
          errorsInData.fullname = 'Укажите валидное имя'
        }
        if (!this.phone_number) {
          errorsInData.phone_number = 'Укажите номер телефона'
        }
        if (!this.email) {
          errorsInData.email = 'Укажите email'
        }
        if (!this.message) {
          errorsInData.message = 'Укажите текст сообщения'
        }
        if (Object.keys(errorsInData).length) {
          this.SET_ERRORS(errorsInData);
        } else {
          const data = {
              fullname: this.fullname,
              phone_number: this.phone_number,
              email: this.email,
              message: this.message,
          };
          // Тут посылаем на бэк запрос и ждем ответа, по результатам фомируем окно с ответом
          await this.SEND_REQUEST_FEEDBACK(data);
          this.fullname = '';
          this.phone_number = '';
          this.fullnaemailme = '';
          this.message = '';
        }
        this.isLoading = false;
      }
    }

  })
</script>

<style scoped lang="scss">
  .error-message {
    position: absolute;
    left: 15px;
    bottom: -4px;
    padding: 0 8px 0 8px;
    font-size: 12px;
    background-color: #fff;
    color: #E30044;

  }

.contacts {

  &__wrapper{


  }
  &__content{

  }

  &__body{
    padding: 0 0 60px 0;
    h3{
      margin-bottom: 28px;
    }
    p{
      font-weight: 400;
      font-size: 18px;
      line-height: 140%;
    }


  }
  &__form{
    background: #FFFFFF;
    box-shadow: 0px 4px 20px rgba(51, 51, 51, 0.1);
    border-radius: 16px;
    padding: 32px 28px;
    input{
      width: 100%;
      background: #FFFFFF;
      border: 1px solid rgba(66, 62, 72, 0.2);
      box-sizing: border-box;
      border-radius: 8px;
      font-size: 16px;
      line-height: 16px;
      display: flex;
      align-items: center;
      padding: 14px 16px;
      color: #423E48;
    }


  }
  &__block{
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    margin-top: 30px;
    @media (max-width: $md2+px) {
      flex-direction: column;
    }

    &__item{
      align-items: flex-start;
      width: 100%;
      &:nth-child(1){
        flex-basis: 35%;
        padding-right: 10px;
      }

      &:nth-child(2){
        flex-basis: 65%;


      }
      .block__item{
        margin-bottom: 30px;
        align-items: flex-start;
        &:nth-child(1){
          color:#4275D8;
          cursor: pointer;


        }
      }
    }




  }
  &__paragraph{
    margin-bottom: 60px;

    &__title{
      position: relative;
      height: 20px;
      background: rgba(66, 117, 216, 0.1);
      border-radius: 4px;
      span{

        font-weight: 500;
        position: absolute;
        top: -10px;
        left: 10px;
        font-size: 20px;
        line-height: 24px;
        color: #4275D8;
      }


    }
    &__text{

      p{
        margin: 10px 0;
        font-size: 18px;
        line-height: 140%;
      }
    }
  }

}
.form-contacts{
  text-align: center;
  &__title{

  }
  .group{
    width: 100%;
  }


  &__row{
    width: 100%;
    gap: 10px;

    @media (max-width: $md2+px) {
      flex-direction: column;
    }
    .input:nth-child(1){
      margin-right: 20px;
      @media (max-width: $md2+px) {
        margin-right: 0px;
        margin-bottom: 20px;
      }
    }

  }
  textarea{
    background: #FFFFFF;
    border: 1px solid rgba(66, 62, 72, 0.2);
    box-sizing: border-box;
    border-radius: 8px;
    width: 100%;
    max-height: 400px;
    padding: 14px 16px;
    resize: vertical;
    position: relative;
    min-height: 80px;
  }
  button{

  }
}
</style>
