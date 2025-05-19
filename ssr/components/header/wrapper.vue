<template>
  <div v-if = "isCatalogOpen || isMenuActionsOpen" id="WRAPPER"
      :class="[isMenuActionsOpen && viewType > 1 ? 'menu-wrapper actions-wrapper' : 'menu-wrapper']" 
      @click.capture.self="closeMenu"
  >
  </div>
</template>

<script setup>
  import { watch } from 'vue';
  import { useHeaderStore } from '@/stores/header';

  const headerStore = useHeaderStore();

  const { isCatalogOpen, isMenuActionsOpen, viewType } = storeToRefs(headerStore);
  
  watch(isCatalogOpen, () => {
    const wrapper = document.getElementById('app__component');
    if (isCatalogOpen.value) {
      window.scrollTo(0, 0);
      if (viewType.value > 1) {
        wrapper.style.overflowY = 'hidden';
        wrapper.style.height = '100vh'; 
        wrapper.style.position = 'relative';
      }
    } else {
      wrapper.style.overflowY = '';
      wrapper.style.height = ''; 
      wrapper.style.position = '';
    }
  });

  watch(isMenuActionsOpen, () => {
    // console.log('Wrapper ', viewType.value);
    const wrapper = document.getElementById('app__component');
    if (isMenuActionsOpen.value) {
      window.scrollTo(0, 0);
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
      if (viewType.value === 1) document.body.style.paddingRight = '';
    }
  });

  const closeMenu = () => {
    headerStore.updateIsCatalogOpen(false);
    headerStore.updateIsMenuActionsOpen(false);
  };
</script>

<style lang='scss' scoped>

.menu-wrapper {
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  z-index: 1;
  //background: linear-gradient(180deg, rgba(66, 62, 72, 0.2) 0%, rgba(66, 62, 72, 0) 100%);
  //backdrop-filter: blur(2px);
}
.actions-wrapper {
  z-index: 20;
  background: linear-gradient(180deg, rgba(66, 62, 72, 0.2) 0%, rgba(66, 62, 72, 0) 100%);
  backdrop-filter: blur(2px);
}
</style>