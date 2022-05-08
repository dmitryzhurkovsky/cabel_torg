<template lang="html">
  <div class="catalog__menu">
    <div v-if = "CATALOG_ITEM_ACTIVE === 1">first category item</div>
    <div v-if = "CATALOG_ITEM_ACTIVE === 2">second category item</div>
    <div v-if = "CATALOG_ITEM_ACTIVE === 3">third category item</div>
    БББББББББББББББББББББББББББББББББББ
  </div>
</template>

<script>

import {mapActions, mapGetters} from 'vuex'

export default {
  name: "CatalogMenu",

  computed: {
    ...mapGetters("header", ["CATALOG_ITEM_ACTIVE"]),
  },
}
</script>

<style lang="scss" scoped>
    .catalog__menu{
      width: 200px;
      height: 200px;
      background-color: pink;
    }

</style>
