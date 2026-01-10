<template>
  <div class="burger__menu__open">
      <div class="burger__menutop">
        <div class="burger__close">
          <svg @click="closeMenu" width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M1 1L15 15" stroke="#4275D8" stroke-width="2"/>
              <path d="M15 1L1 15" stroke="#4275D8" stroke-width="2"/>
          </svg>
          <!-- <HeaderActions /> -->
        </div>
        <HeaderSearchBurger/>
      </div>
    <ul class="burger__menu_list animated" v-if="catalog.length">
      <li 
        v-for   = "mainItem in catalog"
        :key    = "mainItem.id"
      >
        <div class="burger__menu_item flex-center">
          <label
              :class = "{'active' : mainItem.mobileMenu}"
              @click.stop  = "changeCategory(mainItem.id)"
          >
            {{ mainItem.name }}
          </label>
          <div
              :class = "[mainItem.mobileMenu ? 'icon-arrow-down burger__menu_active' : 'icon-arrow-down']"
              @click.stop  = "toggleCategory(mainItem)"
              v-if="mainItem.childrens.length"
          >
          </div>
        </div>

        <ul class="second" v-if = "mainItem.mobileMenu && mainItem.childrens.length">
          <li 
            v-for   = "middleItem in mainItem.childrens"
            :key    = "middleItem.id"
          >
            <div class="burger__menu_item flex-center">
              <label
                  :class = "{'active' : middleItem.mobileMenu}"

                  @click.stop  = "changeCategory(middleItem.id)"
              >
                {{ middleItem.name }}
              </label>
              <div
                  :class = "{'active' : middleItem.mobileMenu}"
                  class="icon-arrow-down"
                  @click.stop  = "toggleCategory(middleItem)"
                  v-if="middleItem.childrens.length"
              >

              </div>
            </div>

            <ul class="third" v-if = "middleItem.mobileMenu && middleItem.childrens.length">
              <li 
                class="has-children"
                v-for = "lastItem in middleItem.childrens"
                :key  = "lastItem.id"
              >
                <label for="sub-group-level-3"
                  @click.stop = "changeCategory(lastItem.id)"
                >
                  {{ lastItem.name }}
                </label>
              </li>
            </ul>
          </li>
        </ul>
      </li>
    </ul>
    <hr class="burger__menu__hr">
    <ul class="burger__menu_list animated">
      <li>
        <div class="burger__menu_item flex-center">
          <label :class = "{'active' : activeMenuItem === 'Покупателям'}"
            @click.stop  = "activeMenuItem === 'Покупателям' ? activeMenuItem = null: activeMenuItem = 'Покупателям'"
          >
            Покупателям
          </label>
          <div :class = "[activeMenuItem === 'Покупателям' ? 'icon-arrow-down burger__menu_active' : 'icon-arrow-down']"
            @click.stop  = "activeMenuItem === 'Покупателям' ? activeMenuItem = null: activeMenuItem = 'Покупателям'"
          >
          </div>
        </div>
        <ul class="second" v-if = "activeMenuItem === 'Покупателям'">
          <li><a @click.prevent="openPage('/how_to_work')">Как оформить заказ</a></li>
          <li><a @click.prevent="openPage('/shipping')">Оплата и доставка</a></li>        
          <li><a @click.prevent="openPage('/wholesale')">Оптовым клиентам</a></li>        
          <li><a @click.prevent="openPage('/warranty')">Гарантийное обслуживание</a></li>        
          <li><a @click.prevent="openPage('/offer')">Публичная оферта</a></li>
        </ul>  
      </li>
      <li>
        <div class="burger__menu_item flex-center">
          <label :class = "{'active' : activeMenuItem === 'О нас'}"
            @click.stop  = "activeMenuItem === 'О нас' ? activeMenuItem = null: activeMenuItem = 'О нас'"
          >
            О нас
          </label>
          <div :class = "[activeMenuItem === 'О нас' ? 'icon-arrow-down burger__menu_active' : 'icon-arrow-down']"
            @click.stop  = "activeMenuItem === 'О нас' ? activeMenuItem = null: activeMenuItem = 'О нас'"
          >
          </div>
        </div>
        <ul class="second" v-if = "activeMenuItem === 'О нас'">
          <li><a @click.prevent="openPage('/about')">О компании</a></li>        
          <li><a @click.prevent="openPage('/contacts')">Контактная информация</a></li>        
          <li><a @click.prevent="openPage('/news')">Новости</a></li>        
        </ul>  
      </li>
    </ul>
    <hr class="burger__menu__hr">
    <ul class="burger__menu_list">
      <li><a class="_link" href="tel:+375296889454">+375 29 6889454</a></li>
    </ul>


  </div>
</template>

<script setup>
  import { ref } from 'vue';
  import { useQueryStore } from '@/stores/query';
  import { useHeaderStore } from '@/stores/header';

  const route = useRoute();
  const router = useRouter();
  const queryStore = useQueryStore();
  const headerStore = useHeaderStore();

  const activeMenuItem = ref(null);

  const { typeOfProduct, offset, limit, sortType, sortDirection, minPrice, maxPrice } = storeToRefs(queryStore);
  const { isCatalogOpen, categories, catalog } = storeToRefs(headerStore);

  const toggleCategory = (item) => {
    item.mobileMenu = !item.mobileMenu;
  };
  
  const getCategoryUrl = (id) => {
    let url = "/category/";
    if (id) {
      const link = categories.value.filter(item => item.id == id)[0].site_link
      url = url + link;
    }
    url = url + getLastPartOfUrl();
    return url;
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

  const changeCategory = (id) => {
    headerStore.updateIsCatalogOpen(!isCatalogOpen.value);
    queryStore.setDefaultPrices();
    router.push(getCategoryUrl(id));
  };

  const openPage = (page) => {
    headerStore.updateIsCatalogOpen(false);
    if (route.path != page) {
      router.push(page);
    }
  };

  const closeMenu = () => {
    headerStore.updateIsCatalogOpen(false);
  };
</script>

<style lang="scss" scoped>

.burger__menu__open{
  position: fixed;
  overflow-y: scroll;
  top: 0;
  width: 100%;
  max-height: 100%;
  height: 100vh;

  background-color: #fff;
  z-index: 50;
}

a {
  text-decoration: none;
}

.cd-accordion-menu label {
  cursor: pointer;
}

.burger__menu{
  color: #423E48;

  &__menutop{
    display: flex;
    flex-direction: column;
  }
  &__block{
    padding: 16px 20px 16px 30px;
    border: 1px solid #F0F0F1;
    justify-content: flex-start;
    align-items: flex-start;
    flex-direction: column;
    .icon-phone{
      color: #4275D8;
      &:before{
        margin-right: 10px;
        font-size: 15px;
      }

    }
  }
  &_active{
    transform: rotate(180deg);
  }
  &__item{
    font-size: 12px;
    font-weight: bold;
    color:#423E48;

    a{
      color:#423E48;
      text-decoration: none;
    }
    
  }
  &__item {
    label .active{
      color: #4275D8;
    }
  }
  &__hr{
    height: 2px;
    background: #F0F0F1;
    width: 90%;
    margin: 0 auto;
  }

  &:last-child{
    color: #4275D8;
  }
}

.burger__menu{

  &_list{
    padding: 10px 16px;
    label, a{
      position: relative;
      display: block;
      padding: 10px 0;
      background: #fff;
      //color: #423E48;
      font-size: 12px;
      font-weight: 500;
      line-height: 12px;
      opacity: 1;
    }
    .second{
      padding-left: 16px;
    }
    .third{
      padding-left: 16px;

    }
  }
  &_item{
    justify-content: space-between;
}


}

.icon-arrow-down{
  font-size: 10px;
}

label[class="active"]{
  color: #4275D8;
}

div[class="active"]{
  transform: rotate(180deg);
}

.burger{
  &__close{
    padding: 16px 0 0 16px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    margin-bottom: 10px;
  }
}

.burger__menu__open{
   z-index: 105;
}
</style>
