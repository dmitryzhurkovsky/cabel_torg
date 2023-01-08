<template>
    <ul class="tools-view">
      <!-- list, grid -->
        <li class="tools-view__item">
            <a href="" 
              :class="['table' === VIEW_TYPE ? 'tools-view__link icon-catalog-table active' : 'tools-view__link icon-catalog-table']"
              @click="changeView($event, 'table')"
            ></a>
        </li>
        <li class="tools-view__item">
            <a href="" 
              :class="['row' === VIEW_TYPE ? 'tools-view__link icon-catalog-row active' : 'tools-view__link icon-catalog-row']"
              @click="changeView($event, 'row')"
            ></a>
        </li>
    </ul>
</template>

<script>

  import {mapGetters, mapMutations} from 'vuex'

  export default {
    name: 'ViewPanel',

    computed: {
        ...mapGetters("query", ["VIEW_TYPE"]),
    },

    methods: {
      ...mapMutations("query", ["SET_VIEW_TYPE"]),

      changeView(e, type) {
        e.preventDefault();
        this.SET_VIEW_TYPE(type);
      }
    }
}
</script>

<style lang="scss" scoped>
.tools-view{
  float: right;
  display: flex;
  align-items: center;
  gap: 10px;
  &__item{
    .active{
      color: #423E48;
    }
  }
  a{
    font-size: 20px;
    color: #ddd;
    transition: all 0.3s ease;
    &:hover{
      color: #423E48;
      opacity: 0.8;
    }
  }
}
</style>