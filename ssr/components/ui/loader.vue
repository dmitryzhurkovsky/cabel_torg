<template>
  <div 
    ref="loader"
    :class="[isLoading === false ? 'lds_wrapper': 'lds_wrapper show_wrapper']"
  >
      <div class="lds-roller"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
  </div>
</template>


<script setup>
  import { watch, ref } from 'vue';
  import { useNotificationsStore } from '@/stores/notifications';

  const notificationsStore = useNotificationsStore();
  const { isLoading } = storeToRefs(notificationsStore);

  const loader = ref(null);

  watch(isLoading, () => {
    const wrapper = document.getElementById('app__component');
    if (isLoading.value) {
      loader.style.top = window.pageYOffset + 'px';
      wrapper.style.overflowY = 'hidden';
      wrapper.style.height = '100vh'; 
      wrapper.style.position = 'relative';
      document.body.style.paddingRight = '16px';
    } else {
      wrapper.style.overflowY = '';
      wrapper.style.height = ''; 
      wrapper.style.position = '';
      document.body.style.paddingRight = '0';
    }
  });

</script>

<style lang="css">
  .lds_wrapper {
    background: linear-gradient(180deg, rgba(66, 62, 72, 0.2) 0%, rgba(66, 62, 72, 0) 100%);
    backdrop-filter: blur(2px);
    z-index: 95;
    height: 100vh;
    overflow: hidden;
    display: none;
    justify-content: center;
    align-items: center;
    position: absolute;
    left: 0;
    top: 0;
    height: 100vh;
    width: 100%;
  }

  .show_wrapper {
    display: flex;
  }

  .lds-roller {
    display: inline-block;
    position: relative;
    /* top: 50%;
    left: 50%; */
    width: 80px;
    height: 80px;
  }
  .lds-roller div {
    animation: lds-roller 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;
    transform-origin: 40px 40px;
  }
  .lds-roller div:after {
    content: " ";
    display: block;
    position: absolute;
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #fff;
    margin: -4px 0 0 -4px;
  }
  .lds-roller div:nth-child(1) {
    animation-delay: -0.036s;
  }
  .lds-roller div:nth-child(1):after {
    top: 63px;
    left: 63px;
  }
  .lds-roller div:nth-child(2) {
    animation-delay: -0.072s;
  }
  .lds-roller div:nth-child(2):after {
    top: 68px;
    left: 56px;
  }
  .lds-roller div:nth-child(3) {
    animation-delay: -0.108s;
  }
  .lds-roller div:nth-child(3):after {
    top: 71px;
    left: 48px;
  }
  .lds-roller div:nth-child(4) {
    animation-delay: -0.144s;
  }
  .lds-roller div:nth-child(4):after {
    top: 72px;
    left: 40px;
  }
  .lds-roller div:nth-child(5) {
    animation-delay: -0.18s;
  }
  .lds-roller div:nth-child(5):after {
    top: 71px;
    left: 32px;
  }
  .lds-roller div:nth-child(6) {
    animation-delay: -0.216s;
  }
  .lds-roller div:nth-child(6):after {
    top: 68px;
    left: 24px;
  }
  .lds-roller div:nth-child(7) {
    animation-delay: -0.252s;
  }
  .lds-roller div:nth-child(7):after {
    top: 63px;
    left: 17px;
  }
  .lds-roller div:nth-child(8) {
    animation-delay: -0.288s;
  }
  .lds-roller div:nth-child(8):after {
    top: 56px;
    left: 12px;
  }
  @keyframes lds-roller {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }
</style>
