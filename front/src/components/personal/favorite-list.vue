<template lang="html">
  <div class="catalog app__content">
    <div class="catalog__wrapper">
      <div class="catalog__content _container">
        <div class="catalog__body">

          <div class="catalog__block">

                <div class="content-block">
                    <div class="content-block__topfilter topfilter">
                        <div class="topfilter__right flex-center">
                            <ViewPanel />
                        </div>
                    </div>
                    <div class="content-block__list">
                        <div class="content-block__item product-row" v-if = "FULL_FAVORITES.length !== 0 && VIEW_TYPE === 'row'">
                            <ListItem 
                            v-for   = "item in FULL_FAVORITES"
                            :key    = "item.id"
                            :card   = item
                            />
                        </div>  
                        <div class="content-block__item product-table" v-if = "FULL_FAVORITES.length !== 0 && VIEW_TYPE === 'table'">
                            <CardItem 
                            v-for   = "item in FULL_FAVORITES"
                            :key    = "item.id"
                            :card   = item
                            />
                        </div>  
                    </div>
                    <!-- <PaginationPanel class="content-block__pagination" /> -->
                </div>
            </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>

import { mapGetters, mapMutations, mapActions } from 'vuex'

import ListItem from '@/components/catalog/list-item.vue';
import CardItem from '@/components/catalog/card-item.vue';
import ViewPanel from '@/components/catalog/view-panel.vue';
import PaginationPanel from '@/components/catalog/pagination-panel.vue';

export default {
    name: 'FavoriteList',

    components:
    {
      ListItem, CardItem, ViewPanel, PaginationPanel, 
    },

    computed: {
        ...mapGetters("favorite", ["FULL_FAVORITES", "FAVORITES"]),
        ...mapGetters("query", ["VIEW_TYPE"]),

        ChangeParameters(){
          return JSON.stringify(this.FAVORITES);
        }
    },

    methods: {
        ...mapMutations("favorite", ["CLEAR_FULL_FAVORITES"]),
        ...mapActions("favorite", ["GET_USER_FULL_FAVORITES"]),
        ...mapMutations("notification", ["SET_IS_LOADING"]),

        async getData() {
            this.SET_IS_LOADING(true);
            this.CLEAR_FULL_FAVORITES();
            await this.GET_USER_FULL_FAVORITES();
            this.SET_IS_LOADING(false);
       }
    },

    watch: {
      ChangeParameters: async function() {
        await this.getData();
      },
    },

    async mounted() {
        await this.getData();
    },

    beforeUnmount() {
        this.CLEAR_FULL_FAVORITES();
    }
}
</script>

<style lang="scss" scoped>
.catalog {

&__wrapper{

}
&__content{

}

&__body{
}



&__item{


}
&__block{
  display: flex;
  align-items: flex-start;

}
&__sidebar{
  min-width: 260px;
  width: 272px;
  padding-right: 10px;
}

}

.content-block{

&__subcategory{
  display: grid;
  gap: 10px;
  grid-template-columns: repeat(3, minmax(0, 300px));
  text-align: center;
  //padding: 24px 20px 20px 0;

  .recomendation__nav__item{
    background: #FFFFFF;
    border: 1px solid rgba(0, 0, 0, 0.05);
    border-radius: 50px;
    font-size: 14px;
    line-height: 24px;
    text-align: center;
    opacity: 0.5;
    margin-right: 10px;
    padding: 6px 20px;
    //max-width: 25%;
    text-overflow: ellipsis;
    white-space: nowrap;
    overflow: hidden;
    transition: all 0.5s ease;

    cursor: pointer;
    &:hover{
      box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.08);
      color:#4275D8;
      font-weight: 500;
      opacity: 1;
    }
  }

}
&__pagination{
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 20px 0;
}
&__item{
  display: flex;
  flex-direction: column;
  gap:16px;
}

&__topfilter{
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 0;
  font-size: 12px;
}

}

.product-table{
  display: grid;
  width: 100%;
  grid-template-columns: repeat(3, minmax(242px, 272px));
  grid-template-rows: auto;
  gap: 10px;
  @media (max-width: $md2+px) {
    grid-template-columns: repeat(2, minmax(142px, 272px));
  }
  .item-card{
    //min-width: 270px;
  }
}
</style>
