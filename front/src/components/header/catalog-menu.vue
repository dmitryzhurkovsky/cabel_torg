<template lang="html">
<!--      <div v-if = "CATALOG_ITEM_ACTIVE === 1">first category item</div>-->
<!--      <div v-if = "CATALOG_ITEM_ACTIVE === 2">second category item</div>-->
<!--      <div v-if = "CATALOG_ITEM_ACTIVE === 3">third category item</div>-->
      <div class="catalog__menu menu__container">
        <div class="menu active">
          <div class="menu__scroll">
            <div class="container row">
              <ul class="menu__mass">
                <li class="menu__item active">
                  <a class="menu__link" href="">
                    Сетевое оборудование</a>
                </li>
              </ul>
            </div>
          </div>
        </div>
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
      position: absolute;
      top: 20px;
      left: 20px;
      width: 600px;
      height: 420px;
      background-color: pink;
      z-index: 3;
    }

</style>
