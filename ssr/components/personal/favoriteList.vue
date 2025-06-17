<template>
  <div class="catalog app__content">
    <div class="catalog__wrapper">
      <div class="catalog__content _container">
        <div class="catalog__body">

          <div class="catalog__block">

                <div class="content-block">
                    <div class="content-block__topfilter topfilter">
                        <div class="topfilter__right flex-center">
                            <CatalogViewPanel />
                        </div>
                    </div>
                    <div class="content-block__list">
                        <div class="content-block__item product-row" v-if = "fullFavorites.length !== 0 && catalogViewType === 'row'">
                            <CatalogListItem 
                            v-for   = "item in fullFavorites"
                            :key    = "item.id"
                            :card   = item
                            />
                        </div>  
                        <div class="content-block__item product-table" v-if = "fullFavorites.length !== 0 && catalogViewType === 'table'">
                            <CatalogCardItem 
                            v-for   = "item in fullFavorites"
                            :key    = "item.id"
                            :card   = item
                            />
                        </div>  
                    </div>
                </div>
            </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script setup>

  import { computed, onMounted, onBeforeMount, watch } from 'vue';
  import { useNotificationsStore } from '@/stores/notifications';
  import { useQueryStore } from '@/stores/query';
  import { useFavoritesStore } from '@/stores/favorites';

  const notificationsStore = useNotificationsStore();
  const queryStore = useQueryStore();
  const favoritesStore = useFavoritesStore();

  const { catalogViewType } = storeToRefs(queryStore);
  const { favorites, fullFavorites } = storeToRefs(favoritesStore);

  const ChangeParameters = computed(() => {
    return JSON.stringify(favorites.value);
  });

  const getData = async () => {
    notificationsStore.setIsLoading(true);
    favoritesStore.clearFullFavorites();
    await favoritesStore.getUserFullFavorite();
    notificationsStore.setIsLoading(false);
  };

  watch(ChangeParameters, async () => {
    await getData();
  });

  onMounted(async () => {
      await getData();
  });

  onBeforeMount(() => {
    favoritesStore.clearFullFavorites();
  });
</script>

<style lang="scss" scoped>
.catalog {

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
  @media (max-width: 1089px) {
    grid-template-columns: repeat(2, minmax(142px, 272px));
  }
}
</style>
