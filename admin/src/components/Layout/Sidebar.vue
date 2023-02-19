<script setup lang='ts'>
import { ref } from "vue";

const props = defineProps({
  openSidebar: {
    type: Boolean,
    required: true,
  },
});

const emit = defineEmits(['onToggleMenu']);

const toggleMenu = (): void => {
  emit('onToggleMenu');
};

const links = ref([
  { name: "Партнеры", href: "/partners" },
  { name: "Варианты доставки", href: "/delivery_types" },
]);

</script>

<template>
  <div :class="['sidebar', { sidebar_isopen: openSidebar }]">
    <router-link
      class="sidebar__link"
      v-for="link in links"
      :key="link.name"
      :to="link.href"
      >{{ link.name }}
    </router-link
    >
  </div>
  <div v-if = "!openSidebar" class="sidebar-marker" @click="toggleMenu">&#5125;</div>
  <div v-else class="sidebar-marker sidebar-marker_isopen" @click="toggleMenu">&#5130;</div>
</template>

<style lang="scss" scoped>
.sidebar {
  left: 0;
  top: 62px;
  height: 100%;
  background: #fff;
  position: fixed;
  width: 250px;
  padding: 20px;
  transition: 0.2s;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.07);
  transform: translateX(-250px);
  &_isopen {
    transform: translateX(0px);
  }
  &__link {
    display: block;
    border-radius: 12px;
    border: 2px solid #fff;
    transition: 0.2s;
    font-weight: bold;
    margin-bottom: 10px;
    &:hover {
      color: var(--primary);
    }
  }
  &-marker {
    position: fixed;
    left: 0;
    width: 15px;
    background: var(--background-content);
    height: 100%;
    top: 62px;
    z-index: 1;
    cursor: pointer;
    color: var(--primary-hover);
    display: flex;
    align-items: center;
    justify-content: center;
    &_isopen{
      left: 235px;      
      background: var(--background);
    }
  }

}
</style>
