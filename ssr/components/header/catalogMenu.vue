<template>
  <div class="catalog__menu menu__container">
    <div class="menu active _container">
      <div class="menu__scroll">
        <div class="container">
          <div class="left_sidebar">
            <ul class="menu__mass">
              <li 
                  class="menu__item" 
                  :class = "{ 'active' : item.id === topCategoriesItemActive }"
                  v-for   = "item in topCategories"
                  :key    = "item.id"
                  @click.stop.prevent  = "changeCategory(item)"
              >
                <a class="menu__link" :href="createHref(item)" @click.prevent>{{item.name}}</a>
              </li>
            </ul>
            <a class="_link"
              href = "/catalog"
            >
              Перейти в каталог
            </a>
          </div>

          <div class="menusub row">
            <div class="menusub__box">
              <div class="menusub__item"
                v-for   = "sub in subCategories"
                :key    = "sub.id"
                @click.stop.prevent  = "subCategoryClick(sub)"
              >
                <a :href="createHref(sub)" v-if = "sub.id" class="menu__rubric">{{sub.name}}</a>
                <ul v-if = "sub.subItems.length > 0">
                  <li
                      v-for = "subItem in sub.subItems"
                      :key  = "subItem.id"
                  >
                    <a :href="createHref(subItem)" @click.stop.prevent = "subCategoryClick(subItem)" class="menu__linksub">{{subItem.name}}</a>
                  </li>
                </ul>
              </div>

            </div>

          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script setup>
  import { useQueryStore } from '@/stores/query';
  import { useHeaderStore } from '@/stores/header';

  const router = useRouter();
  const queryStore = useQueryStore();
  const headerStore = useHeaderStore();

  const { typeOfProduct, offset, limit, sortType, sortDirection, minPrice, maxPrice } = storeToRefs(queryStore);
  const { isCatalogOpen, categories, topCategoriesItemActive, topCategories, subCategories } = storeToRefs(headerStore);

  const getCategoryUrl = (id) => {
    let url = "/category/";
    if (id) url = url + id;
    url = url + getLastPartOfUrl();
    return url;
  };

  const createHref = (category) => {
    const fullCategoryData = categories.value.filter(item => item.id == category.id)[0];
    const URL = '/category/' + fullCategoryData.site_link;
    return URL;
  };

  const getLastPartOfUrl = () => {
    let url = '?';
    if (offset.value != 0 || limit.value != 12) {
      url = url + "offset=" + offset.value + '&'
      url = url + "limit=" + limit.value + '&'
    }
    if (minPrice.value != 0 || maxPrice.value != 80000) {
      url = url + "actual_price_gte=" + minPrice.value + '&';
      url = url + "actual_price_lte=" + maxPrice.value + '&';
    }
    if (sortDirection.value !== '-' || sortType.value !== 'created_at') {
      url = url + "ordering=" + sortDirection.value + sortType.value + '&'
    }
    if (typeOfProduct.value !== 'all') {
      url = url + "type_of_product=" + typeOfProduct.value + '&'
    }
    const lastSymbol = url.slice(-1)
    if (lastSymbol === '&' || lastSymbol === '?') url = url.slice(0, -1)
    return url;        
  };

  const changeCategory = (category) => {
    queryStore.setDefaultPrices();
    router.push(getCategoryUrl(category.site_link));
  };

  const subCategoryClick = (category) => {
    headerStore.updateIsCatalogOpen(!isCatalogOpen.value);
    queryStore.setDefaultPrices();
    const menuItem = categories.value.filter(item => item.id == category.id)[0];
    router.push(getCategoryUrl(menuItem.site_link));
  };
</script>

<style scoped lang="scss">

.catalog__menu{
position: absolute;
top: 50px;
left: 0;
padding: 38px 0 20px 0;
width: 100%;
//height: 420px;
background: #FFFFFF;
box-shadow: 0px 4px 20px rgba(66, 62, 72, 0.05);
z-index: 5;
}
.menu{

.container {
display: grid;
grid-template-columns: 290px 1fr;
}


&__mass{
min-width: 250px;
max-height: 100%;
position: static;

&-lnk{
  padding-left: 15px;
  font-size: 14px;
  margin: 20px 0;
  color: #423E48;
  transition: all 0.3s ease;
  &:hover{
    color: #4275D8;
  }
}
.active .menu__link{

  color:#4275D8;
}
}

&__item{
//margin: 20px 0;
width: 100%;
padding: 10px 15px;
transition: all 0.2s ease;
&:hover{
  color:#4275D8;
  background: rgba(66, 117, 216, 0.1);
  border-radius: 6px;
  padding: 10px 15px;

}
}




&__link{
font-weight: 500;
font-size: 16px;
line-height: 24px;
color: #423E48;
width: 100%;
&:nth-child(1){
}


}

.row{
display: flex;
align-items: flex-start;

}
.left_sidebar{
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: space-between;
  height: 100%;
  ._link{
    padding-left: 15px;
  }
}


&__rubric{
  display: inline-block;
  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
  text-decoration-line: underline;
  color: #423E48;
  transition: all 0.2s ease;
    &:hover{
    color:#4275D8;
    opacity: 0.8;
}

}

&__linksub{
  display: inline-block;
  font-weight: 300;
  font-size: 14px;
  color: #423E48;
  margin-top: 8px;
  opacity: 0.5;
  &:hover{
    opacity: 0.7;
  }
}
}

.menusub{
  display: flex;
  align-items: center;
  padding: 15px;
  width: 100%;
  max-height: 100%;
  position: static;
  min-height: 350px;

&__box{
display: grid;
grid-template-columns: repeat(3, 1fr);
grid-template-rows: auto;
gap: 12px;
}

&__item{

}



}
</style>
