<template lang="html">
  <div class="pop__up__menu">
    <div v-if = "MENU_ITEM_ACTIVE === 1">sdfsdfsfsdaf</div>
    <div v-if = "MENU_ITEM_ACTIVE === 2">asdfdfsdfasdfasf</div>
    <div v-if = "MENU_ITEM_ACTIVE === 3">sdfadfasdfasddf</div>
    AAAAAAAAAAAAAAAAAAAAAAAA
  </div>
</template>

<script>

import {mapActions, mapGetters} from 'vuex'

export default {
  name: "PopUpMenu",

  computed: {
    ...mapGetters("header", ["MENU_ITEM_ACTIVE"]),
  },
}
</script>

<style lang="scss" scoped>
    .pop__up__menu{
      position: absolute;
      top: 100px;
      width: 200px;
      height: 200px;
      background-color: black;
    }

</style>
