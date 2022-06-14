<template lang="html">
  <ul class="breadcrumb">
    <li
        class="v-notification__body"
        v-for="element in ELEMENTS"
        :key="element.id"
        :class="element.class"
    >
      <div
          v-if="element.type !=='service'"
          @click="changePage(element)"
      >{{element.name}}</div>
    </li>
  </ul>
</template>

<script>

import { mapGetters } from "vuex";

export default {
  name: "breadcrumb",

  computed: {
    ...mapGetters("breadcrumb", ["STACK"]),

    ELEMENTS(){
      if (this.STACK.length > 1){
        let result = [];
        this.STACK.forEach((item, i) => {
          let menuItem = {};
          menuItem.name = item.name;
          menuItem.path = item.path;
          menuItem.type = item.type;
          menuItem.class = item.class;
          menuItem.index = i;
          result.push(menuItem);
          result.push({name: '', type: 'service', class: 'breadcrumb__separater icon-arrow-l'})
        });
        return result;
      } else {
        return [];
      }
    },
  },

  methods: {
    changePage(item){
      this.$store.dispatch("breadcrumb/CHANGE_BREADCRUMB", item.index);
      this.$router.push(item.path);
    }
  }
}
</script>

<style lang="scss" scoped>
.breadcrumb{
  display: flex;
  align-items: center;
  padding: 20px 0 30px 0;

  li{
    div{
      font-weight: 300;
      font-size: 12px;
      line-height: 16px;
      text-align: center;
      color: #423E48;
      cursor: pointer;
    }

  }
  .active{
    font-weight: 300;
    font-size: 12px;
    line-height: 16px;
    text-align: center;
    opacity: 0.5;

  }
  &__separater{
    font-size: 8px;
    margin: 0 12px;
  }

}
</style>
