<template>
  <div class="header__search search-wrapper ">
    <div class="search__box">
      <div class="search__field">
        <input type="text" required class="search-box" placeholder="Поиск товаров"
          v-model = "queryString" @input="onInput()" autocomplete="off"
        />
        <button class="icon-close" type="reset" v-if ="queryString" @click = "clearString"></button>
      </div>

    </div>
    
    <div class="dropdown__box" v-if = "searchString !== catalogSearchString">
      <div class="dropdown__wrapper">
        <div class="dropdown__content popup-cart">
            <div class="dropdown__content__title">Найденые товары</div>

              <div v-if="queryString && findedElements.length" class="popup-cart__list">
                <HeaderSearchItem 
                    class="row" 
                    v-for = "item in findedElements"
                    :key = "item.id"
                    :item = item
                    @click.stop = "openCardItem(item.vendor_code)"
                />
                <div class="search__footer" @click = "openFindedElementsInCatalg" autocomplete="off">
                  Показать все
                </div>
              </div>
              <div v-if="queryString && findedElements.length === 0" class="popup-cart__list">
                <div class="row">
                  По Вашему запросу ничего не найдено. Проверьте правильность написания или упростите запрос.
                </div>
              </div>
          </div>
      </div>
    </div>

  </div>
</template>

<script setup>
  import { ref, watch } from 'vue';
  import { useQueryStore } from '@/stores/query';
  import { useCatalogStore } from '@/stores/catalog';

  const router = useRouter();
  const queryStore = useQueryStore();
  const catalogStore = useCatalogStore();

  const { sortType, sortDirection, searchString, findedElements } = storeToRefs(queryStore);
  const { catalogSearchString } = storeToRefs(catalogStore);

  const queryString = ref('');

  watch(searchString, async () => {
    queryString.value = searchString.value;
    if (searchString.value) {
      await queryStore.findElements();
    } else {
      queryStore.setFindedElements({ data: [] });
    }
  });

  const onInput = () => {
    queryStore.setSearchString(queryString.value);
  };

  const openCardItem = (id) => {
    clearString();
    const URL = '/card_product/' + id;
    router.push(URL);
  };

  const clearString = () => {
    queryString.value = '';
    queryStore.setSearchString('');
    catalogStore.setCatalogSearchString('');
    // let url = "/catalog?";
    // url = url + "&ordering=" + sortDirection.value + sortType.value;
    // url = url + '&type_of_product=all';
    // router.push(url);
  };

  const openFindedElementsInCatalg = () => {
    catalogStore.setCatalogSearchString(searchString.value);
    let url = "/catalog?";
    if (catalogSearchString.value) url = url + "offset=0&limit=12";
    url = url + "&ordering=" + sortDirection.value + sortType.value;
    url = url + '&type_of_product=all';
    if (catalogSearchString.value) url = url + "&q=" + catalogSearchString.value;
    router.push(url);
  };
</script>

<style lang="scss" scoped>

.dropdown__wrapper{
display: block;
}
.header{
  &__search{
    position: relative;
    width: 100%;
    @media (max-width: $md2+px) {
      display: none;
    }
  }
}

//SEARCH
.search-box,.close-icon,.search-wrapper {
position: relative;
padding: 10px;
}
.search-wrapper {
  .dropdown__box{
    width: 100%;
    position: absolute;
    bottom: 0;
    left: 6px;

  }
  .dropdown__wrapper{
    padding: 0 16px 20px 16px;
    margin: 0 10%;
    @media (max-width: $md2+px){
      margin: 0 0;
      padding: 0 16px 10px 16px;
    }
  }
}
.search__box {
  //width: 500px;
  background: #fff;
  height: 32px;
  display: flex;
  padding: 6px 16px;
  margin: 0 10%;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.08);
  border-top-right-radius: 10px;
  border-top-left-radius: 10px;

  //# hide this style when search__result open
  border-bottom-right-radius: 10px;
  border-bottom-left-radius: 10px;
  @media (max-width: $md2+px){
    margin: 0 0;
  }


}

.search__field{
width: 100%;
height: 100%;
position: relative;

input{
  width: 100%;
  height: 100%;
  border: 0px;
  padding-right: 38px;
  font-weight: 300;
  font-size: 14px;
  opacity: 0.5;

}

button{
  position: absolute;
  top: 4px;
  right: 0;
  font-size: 16px;
  color: #423E48;


  cursor: pointer;
}
}

.search__result{
position: absolute;
top: 40px;
left: 10px;
width: 96%;
background: #fff;
min-height: 50px;
padding: 20px 20px;
border-bottom-left-radius:10px;
border-bottom-right-radius:10px;
border-top: 2px solid rgba(0, 0, 0, 0.05) ;


}
::-webkit-input-placeholder { /* Chrome/Opera/Safari */
color: #9fa3b1;
}
::-moz-placeholder { /* Firefox 19+ */
color: #9fa3b1;
}
:-ms-input-placeholder { /* IE 10+ */
color: #9fa3b1;
}

.search__footer{
background: #4275D8;
color: #fff;
padding: 8px 5px;
text-align: center;
border-radius: 6px;
transition: all 0.3s ease;
cursor: pointer;
&:hover{
  background: #6291ED;
}

}
.dropdown__content__title{

  font-size: 20px;
  line-height: 140%;
  margin-bottom: 16px;
  color: #423e48;
  font-weight: 500;
}

</style>
