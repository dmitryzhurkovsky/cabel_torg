<template>
  <div class='v-notification'>
    <transition-group
        name="v-transition-animate"
        class="messages_list"
    >
      <div
          class="v-notification__content"
          v-for="message in MESSAGES"
          :key="message.id"
          :class="message.icon"
      >
        <div class="content__text">
          <div class="content-message">{{message.name}}</div>
          <!-- <div class="material-icons">
          </div> -->
        </div>
        <div class="content_buttons">
          <button v-if="rightButton.length">{{rightButton}}</button>
          <button v-if="leftButton.length">{{leftButton}}</button>
          <div class="close-popup btn-close-popup" @click="closeNotification"></div>
        </div>
      </div>
    </transition-group>
  </div>
</template>

<script>

  import { mapGetters } from "vuex";

  export default {
    name: "v-notification",
    props: {
      // messages:     { type: Array,   default: () => {return []}},
      rightButton:  { type: String,  default: ''},
      leftButton:   { type: String,  default: ''},
      timeout:      { type: Number,  default: 300}
    },

    // data() {
    //   return {}
    // },
    //
    computed: {
      ...mapGetters('notification', ['MESSAGES'], { root: true }),
    },

    methods: {
      hideNotification() {
        let vm = this;
        console.log(vm);
        if (this.MESSAGES.length) {
          setTimeout(function () {
            vm.$store.commit('notification/DELETE_MESSAGE', { root: true })
          }, vm.timeout)
        }
      },

      closeNotification(){
          this.$store.commit('notification/DELETE_MESSAGE', { root: true })
      },
    },

    watch: {
      MESSAGES() {
        this.hideNotification()
      }
    },

    mounted() {
      this.hideNotification()
    }
  }
</script>

<style lang='scss' scoped>
  .v-notification {
    position: fixed;
    top: 80px;
    right: 16px;
    width: 30%;
    z-index: 99;
    &__messages_list {
      display: flex;
      flex-direction: column-reverse;
    }
    &__content {
      padding: 16px;
      border-radius: 4px;
      color: #ffffff;
      display: flex;
      justify-content: space-between;
      align-items: center;
      height: 50px;
      margin-bottom: 16px;
      background: green;
      &.error {
        background: red;
      }
      &.warning {
        background: orange;
      }
      &.check_circle {
        background: green;
      }
    }
    .content {
      &__text {
        display: flex;
        align-items: center;
        justify-content: space-between;
      }
    }
    // .material-icons {
    //   // margin-left: 16px;
    //   position: relative;
    //   cursor: pointer;
    // }
  }
  .v-transition-animate {
    &-enter {
      transform: translateX(120px);
      opacity: 0;
    }
    &-enter-active {
      transition: all .6s ease;
    }
    &-enter-to {
      opacity: 1;
    }
    &-leave {
      height: 50px;
      opacity: 1;
    }
    &-leave-active {
      transition: transform .6s ease, opacity .6s, height .6s .2s;
    }
    &-leave-to {
      height: 0;
      transform: translateX(120px);
      opacity: 0;
    }
    &-move {
      transition: transform .6s ease;
    }
  }

  /* Кнопка закрытия */
  .btn-close-popup{
    position: absolute;
    top: 15px;
    right: 17px;
    width: 23px;
    height: 23px;
    cursor: pointer;
    border: 1px solid #fff;
    border-radius: 50%;
    z-index: 1000;
  }

  .btn-close-popup:before,
  .btn-close-popup:after {
    content: "";
    position: absolute;
      top: 10px;
      left: 6px;
      width: 10px;
      height: 1px;
    background: #fff;
  }

  .btn-close-popup:before {
    transform: rotate(45deg);
  }

  .btn-close-popup:after {
    transform: rotate(-45deg);
  }


</style>
