import axios from "@/utils/api";
import { ref } from 'vue';
import { defineStore } from 'pinia';
import { useNotificationsStore } from "@/stores/notifications";
import { useHeaderStore } from "@/stores/header";

const min = 0
const max = 80000

export const useQueryStore = defineStore ('queryStore', () => {
  
  const notificationsStore = useNotificationsStore();
  const headerStore = useHeaderStore();

  const catalogViewType = ref('table'); //VIEW_TYPE
  const typeOfProduct = ref('all');  //TYPE_OF_PRODUCT
  const categoryId = ref(null); // CATEGORY_ID
  const offset = ref(0); // OFFSET
  const limit = ref(12); // LIMIT
  const sortType = ref('created_at'); //SORT_TYPE
  const sortDirection = ref('-'); //SORT_DIRECTION
  const minPrice = ref(min); // MIN_PRICE
  const maxPrice = ref(max); // MAX_PRICE
  const minLimit = ref(min); // MIN_LIMIT
  const maxLimit = ref(max); // MAX_LIMIT
  const searchString = ref(''); // SEARCH_STRING
  const findedElements = ref([]); // FINDED_ELEMENTS
  const allTypesOfProduct = ref( [
    {name : 'Все товары', type: 'all'},
    {name : 'Акции', type: 'with_discount'}, 
    {name : 'В наличии', type: 'available'},
    {name : 'Топ продаж', type: 'popular'},
    {name : 'Цена по запросу', type: 'with_price_on_request'},
  ]); // ALL_TYPE_OF_PRODUCTS
  const allSortsOfProduct = ref([
    {name: 'По дате добавления', type: 'created_at'},
    {name: 'цене', type: 'actual_price'},
    // {name: 'скидке', type: 'discount'},
  ]); // ALL_SORT_OF_PRODUCTS
  const limitItems = ref([12, 24, 48]); // LIMIT_ITEMS

  const setViewType = (newViewType) => {
    catalogViewType.value = newViewType;
  };

  const setTypeOfProduct = (newTypeOfProduct) => {
    if (typeOfProduct.value !== newTypeOfProduct) offset.value = 0;
    typeOfProduct.value = newTypeOfProduct;
  };

  const setCategoryID = (category) => {
    if (categoryId.value !== category) {
      offset.value = 0;
    }
    categoryId.value = category;
  };

  const setOffset = (newOffset) => {
    offset.value = newOffset;
  };

  const setLimit = (newlimit) => {
    limit.value = newlimit;
  };

  const setSortType = (newSortType) => {
    sortType.value = newSortType;
  };

  const setSortDirection = (direction) => {
    sortDirection.value = direction;
  };

  const setMinPrice = (price) => {
    // console.log('SET min ', price);
    minPrice.value = price;
  };

  const setMaxPrice = (price) => {
    // console.log('SET max ', price);
    maxPrice.value = price;
  };

  const setDefaultPrices = () => {
    // console.log('SET default');
    minPrice.value = min;
    maxPrice.value = max;
    typeOfProduct.value = 'all';
    offset.value = 0;
    limit.value = 12;
  };

  const setSearchString = (query) => {
    searchString.value = query;
  };

  const setFindedElements = (items) => {
   findedElements.value = items.data;
  };

  const findElements = async () => {
    try {
        const query = searchString.value ? '&q=' + searchString.value : '';
        const response = await axios.get( 
            'products?' + 
            '&offset=0' +  
            '&limit=12' + 
            query
        );
        setFindedElements(response.data);
    } catch (e) {
        console.log(e);
      // notificationsStore.addMessage(
      //    {name: "Не возможно загрузить искомые товары ", icon: "error", id: '1'}
      // )
    }
  };

  const createUrl = (offcet = offset.value) => {
    let url = '';
    if (!categoryId.value) {
      url = "/catalog";
    } else {
      url = "/category/";
      const link = headerStore.categories.filter(item => item.id == categoryId.value );
      url = url + link[0]?.site_link;
    }
    url += '?';
    if (offcet != 0 || limit.value != 12) {
      url = url + "offset=" + offcet + '&';
      url = url + "limit=" + limit.value + '&';
    }
    if (minPrice.value != 0 || maxPrice.value != 80000) {
      url = url + "actual_price_gte=" + minPrice.value + '&';
      url = url + "actual_price_lte=" + maxPrice.value + '&';
    }
    if (sortDirection.value !== '-' || sortType.value !== 'created_at') {
      url = url + "ordering=" + sortDirection.value + sortType.value + '&';
    }
    if (typeOfProduct.value !== 'all') {
      url = url + "type_of_product=" + typeOfProduct.value + '&';
    }
    const lastSymbol = url.slice(-1);
    if (lastSymbol === '&' || lastSymbol === '?') url = url.slice(0, -1);
    console.log('url: ', url);
    
    return url;        
  };

  return {
    catalogViewType,
    typeOfProduct,
    categoryId,
    offset,
    limit,
    sortType,
    sortDirection,
    minPrice,
    maxPrice,
    minLimit,
    maxLimit,
    searchString,
    findedElements,
    allTypesOfProduct,
    allSortsOfProduct,
    limitItems,
    setViewType,
    setTypeOfProduct,
    setCategoryID,
    setOffset,
    setLimit,
    setSortType,
    setSortDirection,
    setMinPrice,
    setMaxPrice,
    setDefaultPrices,
    setSearchString,
    setFindedElements,
    findElements,
    createUrl,
  }
});

