<script setup lang="ts">

  import { onMounted, ref, watch } from "vue"
  import { store } from "../../store"
  import { MutationTypes } from "../../store/mutation-types"

  const isPopUpOpen = ref(false)
  const popup = ref(null as unknown as HTMLElement)

  watch(() => store.getters.isPopUpOpen,
    (curr, prev) => {
      const status = store.getters.isPopUpOpen
      // console.log('cur: ', prev, ' prev: ', prev);
      
      if (status) {
        popup.value.style.top = window.pageYOffset + 'px';
        document.body.style.overflowY = 'hidden';
        document.body.style.paddingRight = '16px';
      } else {
        document.body.style.overflowY = '';
        document.body.style.paddingRight = '0';
      }
      isPopUpOpen.value = store.getters.isPopUpOpen
    }
  )

  const closePopUp = (status: boolean) => {
    store.commit(MutationTypes.SET_ISPOPUPOPEN, status)
  }

  onMounted(() => {
    popup.value = document.getElementById('popup') as HTMLElement
  })

</script>  

<template>
  <transition-group>
    <div key="popup"
      @click.stop="closePopUp(false)"
      id="popup" 
      :class="[isPopUpOpen === true ? 'popup__wrapper': 'popup__wrapper disabled']"
    >
      <div class="popup__body" @click.stop="">
        <div class="icon-close popup__close" @click.stop="closePopUp(false)"></div>
        <div class="popup__content" >
          <slot></slot>
        </div>
      </div>
    </div>
  </transition-group>
  
</template>

<style lang="scss" scoped>
.popup {
  &__wrapper {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    position: fixed;
    left: 0;
    top: 0;
    //height: 100%;
    // max-height:100vh;
    width: 100%;
    background: linear-gradient(180deg, rgba(66, 62, 72, 0.2) 0%, rgba(66, 62, 72, 0) 100%);
    backdrop-filter: blur(2px);
    z-index: 95;
    height: 100%;
    overflow-y: hidden;
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
    max-width: 60%;
    overflow-y: scroll;
    @media (max-width: 480px){
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
