import axios from "@/utils/api";
import { ref } from 'vue';
import { defineStore } from 'pinia';
import { useQueryStore } from '@/stores/query';
import { useNotificationsStore } from "@/stores/notifications";

export const useCatalogStore = defineStore ('catalogStore', () => {

  const queryStore = useQueryStore();
  const notificationsStore = useNotificationsStore();

  const { offset, limit, minLimit, maxLimit, minPrice, maxPrice, sortDirection, sortType, typeOfProduct } = storeToRefs(queryStore);

  const cartItemId = ref(null);
  const cartItemData = ref(null);
  const itemsList = ref([]); // ITEMS_LIST
  const totalPages = ref(0); // TOTAL_PAGES
  const activePage = ref(0); // ACTIVE_PAGE
  const recomendedList = ref([]); //RECOMENDED_ITEMS 
  const recomendationType = ref('new'); // RECOMENDATION_TYPE
  const recomendationOrder = ref(''); // RECOMENDATION_ORDER
  const recomendationQuantity = ref(10); //RECOMENDATION_QUANTITY
  const catalogSearchString = ref(''); // CATALOG_SEARCH_STRING
  const shownItemslist = ref([]); // SHOWN_ITEMS_LIST
  const category = ref({}); // CATEGORY

  const setShownItemsList = (data) => {
    shownItemslist.value = [...data];
  };

  const setCatalogSearchString = (searchStr) => {
    catalogSearchString.value = searchStr;
  };

  const setPageState = (data) => {
    if (!data.offset) {
      activePage.value = 1;
    } else {
      activePage.value =  Math.floor(data.offset / data.limit) + 1;
    }
    totalPages.value =  data.back.total % data.limit === 0 ? data.back.total / data.limit: Math.floor(data.back.total / data.limit) + 1;
  };

  const setRecomendationType = (type) => {
    recomendationType.value = type;
  };

  const setRecomendationOrder = (order) => {
    recomendationOrder.value = order;
  };

  const setRecomendationQuantity = (quantity) => {
    recomendationQuantity.value = quantity;
  };

  const setCategory = (category) => {
    category.value = category;
  };

  const getCatalogItems = async (category) => {
    try {
      if (category === null) {
        return;
      }
      let queryData = 'products?category_id=' + category + 
      '&offset=' + offset.value + 
      '&limit=' + limit.value;
      if (minLimit.value != minPrice.value || maxLimit.value != maxPrice.value) {
        queryData = queryData + '&actual_price_gte=' + minPrice.value;
        queryData = queryData + '&actual_price_lte=' + maxPrice.value;
      }
      queryData = queryData + '&ordering=' + sortDirection.value + sortType.value + '&q=' + catalogSearchString.value;
      if (typeOfProduct.value !== 'all') queryData = queryData + '&type_of_product=' + typeOfProduct.value;
      const response = await axios.get(queryData);
      
      const items = response.data;
      itemsList.value = items.data;

      setPageState({ back: items, offset: offset.value, limit: limit.value});
    } catch (e) {
      console.log(e);
      // notificationsStore.addMessage(
      //   {name: "Не возможно загрузить каталог категории " + data, icon: "error", id: '1'}
      // )
    }
  };

  const getAllCatalogItems = async() => {
    try {
      let queryData = 'products?' + 
      'offset=' + offset.value + 
      '&limit=' + limit.value
      if (minLimit.value != minPrice.value || maxLimit.value != maxPrice.value) {
        queryData = queryData + '&actual_price_gte=' + minPrice.value;
        queryData = queryData + '&actual_price_lte=' + maxPrice.value;
      }
      queryData = queryData + '&ordering=' + sortDirection.value + sortType.value + '&q=' + catalogSearchString.value;
      if (typeOfProduct.value !== 'all') queryData = queryData + '&type_of_product=' + typeOfProduct.value
      const response = await axios.get(queryData);

      const items = response.data;
      itemsList.value = items.data;

      setPageState({ back: items, offset: offset.value, limit: limit.value});
      // return response.data;
    } catch (e) {
      console.log(e);
      // notificationsStore.addMessage(
      //   {name: "Не возможно загрузить весь каталог ", icon: "error", id: '1'}
      // )
    }
  };

  const setCartItemId = (id) => {
    cartItemId.value = id;
  }

  const getCartItemData = async (id) => {
    cartItemData.value = null;
    try {
      const url = 'products/' + id
      const goodUrl = encodeURI(url);
      const response = await axios.get(goodUrl)
      cartItemData.value = response.data;
      console.log('Good request products/' + id);
    } catch (e) {
      console.log('Bad request products/' + id);
      // console.log(e)
      // notificationsStore.addMessage({name: "Не возможно загрузить рекомендованные товары ", icon: "error", id: '1'});
    }
  }

  const getRecomendedItems = async () => {
    try {
      let queryData = 'products?offset=0' +  
      '&limit=' + recomendationQuantity.value;

      if (recomendationType.value !== 'all') queryData = queryData + '&type_of_product=' + recomendationType.value;
      if (recomendationOrder.value) queryData = queryData + '&ordering=' + sortDirection.value + recomendationOrder.value;
      const response = await axios.get(queryData);
      const items = response.data;
      recomendedList.value = items.data;
    } catch (e) {
      console.log(e);
      // notificationsStore.addMessage(
      //   {name: "Не возможно загрузить рекомендованные товары ", icon: "error", id: '1'}
      // )
    }
  };

  return {
    cartItemId,
    cartItemData,
    itemsList,
    totalPages,
    activePage,
    recomendedList,
    recomendationType,
    recomendationOrder,
    catalogSearchString,
    shownItemslist,
    category,
    setShownItemsList,
    setCatalogSearchString,
    setRecomendationType,
    setRecomendationOrder,
    setRecomendationQuantity,
    setCategory,
    getCatalogItems,
    getAllCatalogItems,
    setCartItemId,
    getCartItemData,
    getRecomendedItems,
  }
});
