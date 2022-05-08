<template lang="html">
  <div class="burger__menu__open">
    <div v-if = "MENU_ITEM_ACTIVE === 1">first menu item</div>
    <div v-if = "MENU_ITEM_ACTIVE === 2">second menu item</div>
    <div v-if = "MENU_ITEM_ACTIVE === 3">third menu item</div>
    AAAAAAAAAAAAAAAAAAAAAAAA
  </div>
</template>

<script>

import {mapActions, mapGetters} from 'vuex'

export default {
  name: "BurgerMenu",

  computed: {
    ...mapGetters("header", ["MENU_ITEM_ACTIVE"]),
  },
}
</script>

<style lang="scss" scoped>
    .burger__menu__open{
      position: absolute;
      top: 100px;
      width: 200px;
      height: 200px;
      background-color: black;
    }

</style>
