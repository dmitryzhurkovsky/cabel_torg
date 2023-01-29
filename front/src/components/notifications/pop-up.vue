<template>
    <transition-group class="popup__animation">
      <div 
        @click.stop="closePopUp(false)"
        ref="popup" 
        :class="[IS_POP_UP_OPEN === true ? 'popup__wrapper': 'popup__wrapper disabled']"
      >
        <div class="popup__body" @click.stop="">
            <div class="icon-close popup__close" @click.stop="closePopUp(false)"></div>
            <div class="popup__content" >
<!--              <div class="content__popup">-->
<!--                <h3>Заказать звонок</h3>-->
<!--                <div class="">-->
<!--                  <div class="group">-->
<!--                    <label class="label">Ваше имя</label>-->
<!--                    <input type="text" class="input">-->
<!--                    &lt;!&ndash;                  <div class="error-message" v-if="ERRORS.email"> {{ ERRORS.email }} </div>&ndash;&gt;-->
<!--                  </div>-->
<!--                  <div class="group">-->
<!--                    <label class="label">Контактный телефон</label>-->
<!--                    <input type="text" class="input">-->
<!--                    &lt;!&ndash;                  <div class="error-message" v-if="ERRORS.password"> {{ ERRORS.password }} </div>&ndash;&gt;-->
<!--                  </div>-->

<!--                  <div class="group__row flex-center mt-20">-->
<!--                    <div class="center-text">-->
<!--                      <button @click = "userLogin()" type="submit" class="btn black">Отмена</button>-->
<!--                    </div>-->

<!--                    <div class="center-text">-->
<!--                      <button @click = "userLogin()" type="submit" class="btn black">Заказать звонок</button>-->
<!--                    </div>-->

<!--                  </div>-->


<!--                </div>-->
<!--              </div>-->
              <div class="content__popup popup__msg">
                <svg width="80" height="80" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd" clip-rule="evenodd" d="M40 70C56.5685 70 70 56.5685 70 40C70 33.3975 67.8671 27.2932 64.2528 22.3385L38.765 50.6582C37.726 51.8127 35.9776 51.9832 34.7351 51.0513L22.1333 41.6C21.2497 40.9373 21.0706 39.6837 21.7333 38.8C22.3961 37.9163 23.6497 37.7373 24.5333 38.4L36.4035 47.3027L61.6585 19.2416C56.1982 13.546 48.5132 10 40 10C23.4315 10 10 23.4315 10 40C10 56.5685 23.4315 70 40 70Z" fill="url(#paint0_linear_2011_3)"/>
                  <defs>
                    <linearGradient id="paint0_linear_2011_3" x1="40" y1="10" x2="40" y2="70" gradientUnits="userSpaceOnUse">
                      <stop stop-color="#4275D8" stop-opacity="0.8"/>
                      <stop offset="1" stop-color="#4275D8" stop-opacity="0.6"/>
                    </linearGradient>
                  </defs>
                </svg>
                <h3>Готово!</h3>
                <p>Наш менеджер свяжется с вами в ближайшее время</p>
                <p class="mt-20"><b>Время работы: </b> Пн-Пт - 9:00 - 17:00</p>

              </div>


<!--                <div class="popup__message">Тут содежимое PopUp</div>-->
            </div>
        </div>
      </div>
    </transition-group>
    
</template>

<script>

  import { mapGetters, mapMutations } from "vuex";

  import TopMenuActions  from '@/components/header/header-actions.vue'

  export default {
    name: "PopUp",

    components: {
        TopMenuActions,
    },

    watch: {
      IS_POP_UP_OPEN: function(){
        if (this.IS_POP_UP_OPEN) {
          this.$refs.popup.style.top = window.pageYOffset + 'px';
          document.body.style.overflow = 'hidden';
          document.body.style.paddingRight = '16px';
        } else {
          document.body.style.overflow = '';
          document.body.style.paddingRight = '0';
        }
      }
    },

    computed: {
        ...mapGetters("header", ["IS_POP_UP_OPEN"]),
    },

    methods: {
        ...mapMutations("header", ["SET_IS_POP_UP_OPEN"]),

        closePopUp(status) {
            this.SET_IS_POP_UP_OPEN(status);
        }
    }

  }
</script>  

<style lang="scss" scoped>
.popup {
    &__wrapper {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        position: absolute;
        left: 0;
        top: 0;
        //height: 100%;
        // max-height:100vh;
        width: 100%;
        background: linear-gradient(180deg, rgba(66, 62, 72, 0.2) 0%, rgba(66, 62, 72, 0) 100%);
        backdrop-filter: blur(2px);
        z-index: 95;
        height: 100vh;
        overflow-y: hidden;
    }

    &__close {
      position: absolute;
      top:0;
      right: -30px;
      cursor: pointer;
    }
    &__body {
        position: relative;
        display: flex;
        justify-content: center;
        align-items: center;
        //width: 400px;
        //height: 300px;
        padding: 2% 2% ;
        background: #fff;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.08);
        border-radius: 16px;

    }
  &__msg{
    text-align: center;
    h3{
      margin: 20px 0;
    }
    p{
      font-weight: 300;
      font-size: 14px;
      line-height: 140%;
      text-align: center;
      color: #423E48;

    }
  }

}
.left-menu {
    cursor: pointer;
}

.disabled {
    display: none;
}
</style>
