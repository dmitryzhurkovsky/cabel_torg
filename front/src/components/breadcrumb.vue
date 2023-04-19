<template lang="html">
  <div class="breadcrumb__wrapper _container" v-if = "ELEMENTS.length">
    <ul class="breadcrumb">
      <li
          v-for=" (element, index) in ELEMENTS"
          :key="element.id"
          :class="element.class"
      >
        <div
            v-if="element.type !=='service'"
            @click="changePage(element)"
            :style = "[ ELEMENTS.length -1 === index ? 'color : #4275D8' : '']"
        >
          {{ element.name }}
        </div>
      </li>
    </ul>
  </div>
</template>

<script>

import { mapActions, mapMutations, mapGetters } from "vuex";

export default {
  name: "breadcrumb",

  computed: {
    ...mapGetters("breadcrumb", ["STACK"]),

    // watch: {
    //   STACK: function() {
    //     console.log('watch');
    //     this.ELEMENTS()
    //   },
    // },

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
          if (i !== this.STACK.length - 1){
            result.push({name: '', type: 'service', class: 'breadcrumb__separater icon-arrow-l'})
          }
        });
        return result;
      } else {
        return [];
      }
    },
  },

  methods: {
    ...mapActions("breadcrumb", ["MOVE_TO_SELECT_PATH"]),
    ...mapMutations("query", ["SET_SEARCH_STRING"]),
    
    changePage(item){
      this.SET_SEARCH_STRING('');
      this.MOVE_TO_SELECT_PATH(item.index);
      this.$router.push(item.path);
    }
  }
}
</script>

<style lang="scss" scoped>


.active__breadcrumb {
  color: blue;
}
.breadcrumb{
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  padding: 20px 0 30px 0;
  @media (max-width: $md3+px){
    padding: 10px 0 10px 0;
  }

  &__wrapper{
    width: 100%;
    text-align: left;
  }

  li{
    white-space: nowrap;
    overflow: hidden;
    &:last-child{
      a{
        opacity: 0.6;
        cursor: auto;
      }

    }
    div{
      font-weight: 300;
      font-size: 12px;
      line-height: 2;
      text-align: center;
      color: #423E48;
      cursor: pointer;
      @media (max-width: $md3+px){
        font-size: 8px;
      }
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
