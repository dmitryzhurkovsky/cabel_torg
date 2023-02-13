<template>
    <ul class="tools-sort icon-change">
        <div class= "tools-sort__direction" v-if = "!SORT_DIRECTION" @click.prevent="SET_SORT_DIRECTION('-')">А-Я</div>
        <div class= "tools-sort__direction" v-if = "SORT_DIRECTION"  @click.prevent="SET_SORT_DIRECTION('')">Я-А</div>
        <li 
            :class="[item.type === SORT_TYPE ? 'tools-sort__item active' : 'tools-sort__item']"
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
        ...mapGetters("query", ["SORT_TYPE", "SORT_DIRECTION"]),
    },

    data() {
        return {
            sortItems: [
                {name: 'По дате добавления', type: 'created_at'},
                {name: 'цене', type: 'price'},
                {name: 'скидке', type: 'discount'},
            ],
        };
    },

    methods: {
        ...mapMutations("query", ["SET_SORT_TYPE", "SET_SORT_DIRECTION"]),

        changeSort(e, type) {
            e.preventDefault();
            this.SET_SORT_TYPE(type);
        },

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
  &__direction{
    cursor: pointer;
  }
}
.active{
  color: #423E48;
  font-weight: 500;
 }

</style>