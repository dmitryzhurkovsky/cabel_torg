<template>
  <div class='v-notification'>
    <transition-group
        name="v-transition-animate"
        class="messages_list"
    >
      <div
          class="v-notification__body"
          v-for="message in MESSAGES"
          :key="message.id"
          :class="message.icon"
      >
        <div class="content__text">
          <div class="content__message">{{message.name}}</div>
        </div>

        <div class="content__buttons">
          <button v-if="rightButton.length">{{rightButton}}</button>
          <button v-if="leftButton.length">{{leftButton}}</button>
        </div>
        <div class="close-popup btn-close-popup" @click="closeNotification"></div>
      </div>
    </transition-group>
  </div>
</template>

<script>

  import { mapGetters, mapMutations } from "vuex";

  export default {
    name: "v-notification",
    props: {
      // messages:     { type: Array,   default: () => {return []}},
      rightButton:  { type: String,  default: ''},
      leftButton:   { type: String,  default: ''},
      timeout:      { type: Number,  default: 3000}
    },

    computed: {
      ...mapGetters("notification", ["MESSAGES", "LENGTH"]),
    },

    methods: {
      ...mapMutations("notification", ["DELETE_MESSAGE"]),

      hideNotification() {
        let vm = this;
        if (this.LENGTH) {
          setTimeout(() => {
            vm.DELETE_MESSAGE();
          }, vm.timeout)
        }
      },

      closeNotification(){
          this.DELETE_MESSAGE();
      },
    },

    watch: {
      LENGTH() {
        this.hideNotification();
      }
    },

  }
</script>

<style lang='scss' scoped>

.v-notification {
    position: fixed;
    top: 80px;
    right: 16px;
    //width: 30%;
    @include adaptiv-value("width",30%,50%,50%);
    z-index: 99;
    &__messages_list {
      display: flex;
      flex-direction: column-reverse;
    }
    &__body {
      position: relative;
      padding: 12px 8px;
      @include adaptiv-font(16, 12, 20);
      border-radius: 8px;
      color: #ffffff;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
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
          padding-right: 25px;
      }
    }

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
    top: 10px;
    right: 10px;
    width: 19px;
    height: 19px;
    border: 1px solid #fff;
    border-radius: 50%;
    z-index: 1000;
    cursor: pointer;
  }

  .btn-close-popup:before,
  .btn-close-popup:after {
    content: "";
    position: absolute;
      top: 8px;
      left: 4px;
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
