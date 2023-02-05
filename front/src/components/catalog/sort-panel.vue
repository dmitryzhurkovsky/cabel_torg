<template>
    <ul class="tools-sort icon-change">
        <li 
            :class="[item.type === SORT_TYPE.type ? 'tools-sort_item active' : 'tools-sort_item']"
            v-for = "item in sortItems"
            :key = "item.type"
        >
            <a href="" class="tools-sort_link" @click="changeSort($event, item)">{{ item.name }}</a>
        </li>
    </ul>
</template>

<script>

  import {mapGetters, mapMutations} from 'vuex'

  export default {
    name: 'SortPanel',

    computed: {
        ...mapGetters("query", ["SORT_TYPE"]),
    },

    data() {
        return {
            sortItems: [
                {name: 'По дате добавления', type: 'date'},
                {name: 'цене', type: 'price'},
                {name: 'скидке', type: 'discount'},
            ],
        };
    },

    methods: {
        ...mapMutations("query", ["SET_SORT_TYPE"]),

        changeSort(e, type) {
            e.preventDefault();
            this.SET_SORT_TYPE(type);
        }
    },
  }
</script>


<style scoped lang="scss">
.tools-sort{
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
.active{
  color: #423E48;
  font-weight: 500;
 }

</style>