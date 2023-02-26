<template>
    <ul class="tools-sort">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <line x1="2" y1="17.1133" x2="23" y2="17.1133" stroke="#423E48" stroke-width="1.25"/>
          <line x1="23" y1="7.50391" x2="2" y2="7.5039" stroke="#423E48" stroke-width="1.25"/>
          <circle cx="16.6619" cy="16.911" r="3.08088" fill="white" stroke="#423E48" stroke-width="1.25"/>
          <circle cx="8.33806" cy="7.70623" r="3.08088" transform="rotate(-180 8.33806 7.70623)" fill="white" stroke="#423E48" stroke-width="1.25"/>
        </svg>
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