<template>
    <div class="tools-pages">
        <div class="tools-pages__header">Показывать по: </div>
        <ul class="tools-pages__body">
            <li class="tools-pages__item" 
                v-for = "limitItem in limitItems" 
                :key = limitItem
            >
                <a href=""  
                  :class="[limitItem === LIMIT ? 'tools-pages__link active' : 'tools-pages__link']"
                  @click="setLimit($event, limitItem)"
                >{{ limitItem }}</a>
            </li>
        </ul>
    </div>    
</template>

<script>

  import {mapGetters, mapMutations} from 'vuex'


  export default {
    name: 'LimitPanel',

    data() {
      return {
        limitItems : [10, 30, 60],
      }
    },

    computed: {
        ...mapGetters("query", ["LIMIT"]),
    },

    methods: {
      ...mapMutations("query", ["SET_LIMIT"]),

      setLimit(event, limit) {
        event.preventDefault();
        this.SET_LIMIT(limit);
      },
    },
  }

</script>

<style scoped lang="scss">
.tools-pages {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-right: 20px;
  &__item{
    .active{
      color: #423E48;
      font-weight: 500;
    }

  }
  &__header {
    margin-right: 15px;
  }
  &__body {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-right: 20px;
  }
  a{
    font-size: 12px;
    color:#000;
    opacity: 0.8;
    transition: all ease 1ms;
    &:hover{
      color: #423E48;
      opacity: 0.8;
    }
  }

}
</style>