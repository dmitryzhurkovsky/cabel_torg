<template>
    <transition-group class="popup__animation">
      <div 
        @click.stop="closePopUp(false)"
        ref="popup" 
        :class="[IS_POPUP_OPEN === true ? 'popup__wrapper': 'popup__wrapper disabled']"
      >
        <div class="popup__body" @click.stop="">
            <div class="icon-close popup__close" @click.stop="closePopUp(false)"></div>
            <div class="popup__content" >
              <PopUpMsg v-if = "POPUP_ACTION === 'ShowCompleteMsg'" />
              <RequestCall v-if = "POPUP_ACTION === 'RequestCall'"/>
              <UserLogin v-if = "POPUP_ACTION === 'UserLogin'"/>
            </div>
        </div>
      </div>
    </transition-group>
    
</template>

<script>
  import { mapGetters, mapMutations } from "vuex";

  import TopMenuActions  from '@/components/header/header-actions.vue'
  import PopUpMsg from '@/components/notifications/pop-up-msg.vue'
  import RequestCall from '@/components/notifications/request-call.vue'
  import UserLogin from '@/components/notifications/user-login.vue'

  export default {
    name: "PopUp",

    components: {
        TopMenuActions, PopUpMsg, RequestCall, UserLogin
    },

    watch: {
      IS_POPUP_OPEN: function(){
        if (this.IS_POPUP_OPEN) {
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
        ...mapGetters("header", ["IS_POPUP_OPEN", "POPUP_ACTION"]),
    },

    methods: {
        ...mapMutations("header", ["SET_IS_POPUP_OPEN"]),

        closePopUp(status) {
            this.SET_IS_POPUP_OPEN(status);
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
}
.left-menu {
    cursor: pointer;
}

.disabled {
    display: none;
}
</style>
