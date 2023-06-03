<template>
  <div v-if = "IS_CATALOG_OPEN || IS_MENU_ACTIONS_OPEN" id="WRAPPER"
      :class="[IS_MENU_ACTIONS_OPEN && DEVICE_VIEW_TYPE > 1 ? 'menu-wrapper actions-wrapper' : 'menu-wrapper']" 
      @click.capture.self="closeMenu"
  >
  </div>
</template>

<script>
import { mapGetters, mapMutations } from "vuex";

export default {
  name: "MenuWrapper",

  computed: {
    ...mapGetters("header", ["IS_CATALOG_OPEN", "IS_MENU_ACTIONS_OPEN", "DEVICE_VIEW_TYPE"]),
  },

  watch: {
    IS_CATALOG_OPEN: function(){
      if (this.IS_CATALOG_OPEN) {
        window.scrollTo(0, 0);
        if (this.DEVICE_VIEW_TYPE > 1) {
          document.body.style.overflow = 'hidden';
          // document.body.style.paddingRight = '16px';
        }
      } else {
        document.body.style.overflow = '';
        // document.body.style.paddingRight = '0';
      }
    },

    IS_MENU_ACTIONS_OPEN: function(){
      console.log(this.DEVICE_VIEW_TYPE);
      if (this.IS_MENU_ACTIONS_OPEN) {
        window.scrollTo(0, 0);
        document.body.style.overflowY = 'hidden';
        if (this.DEVICE_VIEW_TYPE === 1) document.body.style.paddingRight = '16px';
      } else {
        document.body.style.overflowY = '';
        if (this.DEVICE_VIEW_TYPE === 1) document.body.style.paddingRight = '0';
      }
    }
  },

  methods: {
    ...mapMutations("header", ["UPDATE_IS_CATALOG_OPEN", "UPDATE_IS_MENU_ACTIONS_OPEN"]),

    closeMenu() {
      this.UPDATE_IS_CATALOG_OPEN(false);
      this.UPDATE_IS_MENU_ACTIONS_OPEN(false);
    }
  }
}
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