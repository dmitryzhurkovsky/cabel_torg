<script setup lang='ts'>
  import LayoutHeader from "@/components/Layout/Header.vue";
  import LayoutSidebar from "@/components/Layout/Sidebar.vue";
  import Loader from '@/components/UI/Loader.vue';
  import { onBeforeUpdate, onMounted, ref, watch } from "vue";
  import { useStore } from './store';
  import { ActionTypes } from './store/action-types';
  import { router } from './router'

  const isOpenMenu = ref(true);
  const isLogin = ref(false)
  const store = useStore()

  const onToggleMenu = () => {
    isOpenMenu.value = !isOpenMenu.value;
  };
       
  watch(() => store.getters.isLogin,
    (curr, prev) => {
      isLogin.value = curr
    }
  )

  onBeforeUpdate(() => {
    if (!store.getters.usersList) {
      router.push('/login')
    }
  })

  onMounted( async () => {
    if (localStorage.getItem("authToken")) {
      await store.dispatch(ActionTypes.GET_USER_DATA, null)
    }
  })

</script>

<template>
  <div class="container">
    <Loader />
    <layout-header v-if="isLogin"/>
    <layout-sidebar v-if="isLogin"
      :openSidebar="isOpenMenu" 
      @onToggleMenu="onToggleMenu"
      />
    <div :class="['content', { content_full: !isOpenMenu }]">
      <router-view />
    </div>
  </div>
</template>

<style lang="scss">
@import "./styles/global.scss";

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.content {
  // max-width: 1400px;
  margin-left: 250px;
  padding: 30px;
  transition: 0.2s;
  padding-top: 92px;
  &_full {
    margin-left: 0;
  }
}

// @media screen and (max-width: 1023px) {
//   .content {
//     margin-left: 0;
//   }
// }
</style>
