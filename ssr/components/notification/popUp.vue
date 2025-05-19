<template>
    <transition-group>
      <div v-if="viewType === 1"
        @click.stop="closePopUp(false)"
        ref="popup" 
        class="popup__wrapper"
        :class="{ 'disabled' : !isPopUpOpen }"
        :key="1"
      >
        <!-- :class="[isPopUpOpen === true ? 'popup__wrapper popup__desktop': 'popup__wrapper popup__desktop disabled']" -->
        <div class="popup__body" @click.stop="">
            <div class="icon-close popup__close" @click.stop="closePopUp(false)"></div>
            <div class="popup__content" >
              <NotificationMsg v-if = "popUpAction === 'ShowCompleteMsg'" />
              <NotificationRequestCall v-if = "popUpAction === 'RequestCall'"/>
              <NotificationRequestPrice v-if = "popUpAction === 'RequestPrice'"/>
              <NotificationUserLogin v-if = "popUpAction === 'UserLogin'"/>
              <NotificationChangePass v-if = "popUpAction === 'ChangePassword'"/>
            </div>
        </div>
      </div>
      <div v-else
        @click.stop="closePopUp(false)"
        ref="popup" 
        :class="[isPopUpOpen === true ? 'popup__wrapper': 'popup__wrapper disabled']"
        :key="2"
      >
        <div class="popup__body" @click.stop="">
            <div class="icon-close popup__close" @click.stop="closePopUp(false)"></div>
            <div class="popup__content" >
              <NotificationMsg v-if = "popUpAction === 'ShowCompleteMsg'" />
              <NotificationRequestCall v-if = "popUpAction === 'RequestCall'"/>
              <NotificationRequestPrice v-if = "popUpAction === 'RequestPrice'"/>
              <NotificationUserLogin v-if = "popUpAction === 'UserLogin'"/>
              <NotificationChangePass v-if = "popUpAction === 'ChangePassword'"/>
            </div>
        </div>
      </div>
    </transition-group>
    
</template>

<script setup>
  import { ref, watch } from 'vue';
  import { useAuthStore } from '@/stores/auth';
  import { useHeaderStore } from '@/stores/header';

  const router = useRouter();
  const authStore = useAuthStore();
  const headerStore = useHeaderStore();

  const popup = ref(null);
  const { redirectAfterLogin } = storeToRefs(authStore);
  const { viewType, popUpAction, isPopUpOpen } = storeToRefs(headerStore);

  watch(isPopUpOpen, () => {
    // console.log(viewType.value);
    const wrapper = document.getElementById('app__component');
    if (isPopUpOpen.value) {
      setTimeout(() => {
        popup.value.style.top = window.pageYOffset + 'px';
        wrapper.style.overflowY = 'hidden';
        wrapper.style.height = '100vh'; 
        wrapper.style.position = 'relative';
        if (viewType.value === 1) {
          if (wrapper.scrollHeight !== window.innerHeight) document.body.style.paddingRight = '16px';              
        }
      }, 200);
      wrapper.style.overflowY = 'hidden';
      wrapper.style.height = '100vh'; 
      wrapper.style.position = 'relative';
      if (viewType.value === 1) {
        if (wrapper.scrollHeight !== window.innerHeight) document.body.style.paddingRight = '16px';              
      }
    } else {
      wrapper.style.overflowY = '';
      wrapper.style.height = ''; 
      wrapper.style.position = '';
      if (viewType.value === 1) {
        document.body.style.paddingRight = '';
      }
    }
  });

  const closePopUp = (status) => {
    headerStore.setIsPopUpOpen(status);
    headerStore.setPopUpAdditionalData({});
    if (redirectAfterLogin.value) {
      const path = redirectAfterLogin.value;
      authStore.setDestination('');
      router.push(path);
    }
  };

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
