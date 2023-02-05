<template>
    <div v-if = "IS_CATALOG_OPEN" class="menu-wrapper"
        @click="closeMenu"
    >
    </div>
</template>

<script>
  import { mapGetters, mapMutations } from "vuex";

  export default {
    name: "MenuWrapper",

    computed: {
      ...mapGetters("header", ["IS_CATALOG_OPEN"]),
    },

    methods: {
      ...mapMutations("header", ["UPDATE_IS_CATALOG_OPEN"]),

      closeMenu() {
        // console.log(e);
        this.UPDATE_IS_CATALOG_OPEN(false);
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
}
</style>