<template>
    <transition-group>
      <div 
        @click.stop="closePopUp(false)"
        ref="popup" 
        :class="[IS_POPUP_OPEN === true ? 'popup__wrapper': 'popup__wrapper disabled']"
        :key="1"
      >
        <div class="popup__body" @click.stop="">
            <div class="icon-close popup__close" @click.stop="closePopUp(false)"></div>
            <div class="popup__content" >
              <NotificationMsg v-if = "POPUP_ACTION === 'ShowCompleteMsg'" />
              <NotificationRequestCall v-if = "POPUP_ACTION === 'RequestCall'"/>
              <NotificationUserLogin v-if = "POPUP_ACTION === 'UserLogin'"/>
              <NotificationChangePass v-if = "POPUP_ACTION === 'ChangePassword'"/>
            </div>
        </div>
      </div>
    </transition-group>
    
</template>

<script>
  import { mapGetters, mapMutations } from "vuex";

  export default {
    name: "PopUp",

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
      ...mapMutations("header", ["SET_IS_POPUP_OPEN", "SET_POPUP_ADDITIONAL_DATA"]),

      closePopUp(status) {
        this.SET_IS_POPUP_OPEN(status);
        this.SET_POPUP_ADDITIONAL_DATA({});
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
