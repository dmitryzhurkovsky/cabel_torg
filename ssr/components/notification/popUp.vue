<template>
    <transition-group>
      <div v-if="DEVICE_VIEW_TYPE === 1"
        @click.stop="closePopUp(false)"
        ref="popup" 
        class="popup__wrapper"
        :class="{ 'disabled' : !IS_POPUP_OPEN }"
        :key="1"
      >
        <!-- :class="[IS_POPUP_OPEN === true ? 'popup__wrapper popup__desktop': 'popup__wrapper popup__desktop disabled']" -->
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
      <div v-else
        @click.stop="closePopUp(false)"
        ref="popup" 
        :class="[IS_POPUP_OPEN === true ? 'popup__wrapper': 'popup__wrapper disabled']"
        :key="2"
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
        console.log(this.DEVICE_VIEW_TYPE);
        const wrapper = document.getElementById('app__component');
        if (this.IS_POPUP_OPEN) {
          setTimeout(() => {
            this.$refs.popup.style.top = window.pageYOffset + 'px';
            wrapper.style.overflowY = 'hidden';
            wrapper.style.height = '100vh'; 
            wrapper.style.position = 'relative';
            if (this.DEVICE_VIEW_TYPE === 1) {
              if (document.scrollHeight !== window.innerHeight) document.body.style.paddingRight = '16px';              
            }
          }, 200);
          wrapper.style.overflowY = 'hidden';
          wrapper.style.height = '100vh'; 
          wrapper.style.position = 'relative';
          if (this.DEVICE_VIEW_TYPE === 1) {
            if (document.scrollHeight !== window.innerHeight) document.body.style.paddingRight = '16px';              
          }
        } else {
          wrapper.style.overflowY = '';
          wrapper.style.height = ''; 
          wrapper.style.position = '';
          if (this.DEVICE_VIEW_TYPE === 1) {
            document.body.style.paddingRight = '';
          }
        }
      }
    },

    computed: {
      ...mapGetters("header", ["IS_POPUP_OPEN", "POPUP_ACTION", "DEVICE_VIEW_TYPE"]),
      ...mapGetters("auth", ["REDIRECT_AFTER_LOGIN"])
    },

    methods: {
      ...mapMutations("header", ["SET_IS_POPUP_OPEN", "SET_POPUP_ADDITIONAL_DATA"]),
      ...mapMutations("auth", ["SET_DESTINATION"]),

      closePopUp(status) {
        this.SET_IS_POPUP_OPEN(status);
        this.SET_POPUP_ADDITIONAL_DATA({});
        if (this.REDIRECT_AFTER_LOGIN) {
          const path = this.REDIRECT_AFTER_LOGIN;
          this.SET_DESTINATION('');
          this.$router.push(path);
        }
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

    &__desktop {
      width: calc(100% - 16px);
    }

    &__close {
      position: absolute;
      top:0;
      right: -25px;
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
      @media (max-width: $md3+px){
        width: 85%;
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
