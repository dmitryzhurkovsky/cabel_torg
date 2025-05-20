import axios from "@/utils/api";
import { ref } from 'vue';
import { defineStore } from 'pinia';
import { useBreadCrumbStore } from "@/stores/breadcrumb";
import { useNotificationsStore } from "@/stores/notifications";

const mainBreadCrumb = {
  name: 'Каталог',
  path: '/catalog',
  type: 'global',
  class: '',
  category: 1,
  level: 'root',
}

export const useHeaderStore = defineStore ('headerStore', () => {

  const breadcrumbStore = useBreadCrumbStore();
  const notificationsStore = useNotificationsStore();

  const isCatalogOpen = ref(false);
  const isMenuActionsOpen = ref(false);
  const windowWidth = ref(1280);
  const topCategoriesItemActive = ref(1);
  const subCategoriesItemActive = ref(null);
  const lastCategoriesItemActive = ref(null);
  const viewType = ref(1);
  const categories = ref([]);
  const catalog = ref([]);
  const isPopUpOpen = ref(false);
  const popUpAction = ref('');
  const popUpMessage = ref(null);
  const requestCallType = ref('U');
  const popUpAdditionalData =ref({});

  const topCategories = computed(() => {
    const top = [];
    categories.value.forEach((item) => {
      if (item.parent_category_id === null) {
        top.push(item);
      }
    });
    return top;
  });

  const subCategories = computed(() => {
    let sub = [];
    categories.value.forEach(item => {
      if (item.parent_category_id == topCategoriesItemActive.value){
        sub.push({id : item.id, name: item.name, subItems : []});
      }
    });
    for (let i = 0; i < sub.length; i++){
      categories.value.forEach(item => {
        if (item.parent_category_id == sub[i].id){
          sub[i].subItems.push({id : item.id, name : item.name});
        }
      });
      sub[i].subItems = sub[i].subItems.sort((a, b) => {
        if (a.name < b.name) return -1;
        return 1
      })
    };
    sub = sub.sort((a, b) => { 
      if (a.name - b.name) return -1
      return 1
    });
    return sub;
  });

  const updateIsCatalogOpen = (catalogSatae) => {
    isCatalogOpen.value = catalogSatae;
  };

  const updateIsMenuActionsOpen = (menuactionsSata) => {
    isMenuActionsOpen.value = menuactionsSata;
  };

  const updateViewParameters = (width) => {
    windowWidth.value = width;
    if (width > 768.5) {
      // XXXX - 768
      viewType.value = 1;
    } else if (width > 480.5) {
      // 768 - 480
      viewType.value = 2;
    } else {
      // 480 - 0
      viewType.value = 3;
    }
  };

  const setIsPopUpOpen = (status) => {
    isPopUpOpen.value = status;
  };

  const setCurrentLastCategory = (id) => {
    lastCategoriesItemActive.value = id;
  };


  const setPopUpAction = (action) => {
    popUpAction.value = action;
  };

  const setPopUpMessage = (msg) => {
    popUpMessage.value = {...msg};
  };

  const setRequestCallType = (type) => {
    requestCallType.value = type;
  };

  const setPopUpAdditionalData = (data) => {
    popUpAdditionalData.value = data;
  };

  const setCatalogStateForFilterPanelToFalse = () => {
    catalog.value.forEach(mainItem => {
      mainItem.filterPanel = false;
      const sub = mainItem.childrens;
      sub.forEach(subItem => {
        subItem.filterPanel = false;
        const last = subItem.childrens;
        last.forEach(lastItem => lastItem.filterPanel = false);
      });
    });
    if (topCategoriesItemActive.value) {
      const main = catalog.value.filter(item => item.id === topCategoriesItemActive.value)[0];
      main.filterPanel = true;
      const mianChildrens = main.childrens;
      if (subCategoriesItemActive.value) {
        const sub = mianChildrens.filter(item => item.id === subCategoriesItemActive.value)[0];
        sub.filterPanel = true;
        const subChildrens = sub.childrens;
        if (lastCategoriesItemActive.value) {
          const last = subChildrens.filter(item => item.id === lastCategoriesItemActive.value)[0];
          last.filterPanel = true
        }
      }
    }
  };

  const getCategories = async () => {
    try {
      const response = await axios.get('categories');
      const respCategories = response.data
      categories.value = respCategories;
      if (respCategories.length > 0){
        topCategoriesItemActive.value = respCategories[0].id
      } else {
        topCategoriesItemActive.value = null;
      }

      let menuItems = [];
      const mainLevel = respCategories.filter(item => item.parent_category_id === null);
      let otherItems = respCategories.filter(item => item.parent_category_id !== null);
      menuItems = [...mainLevel];
      menuItems.forEach(item => {
        item.selected = false;
        item.filterPanel = false;
        item.mobileMenu = false;
        item.childrens = [];
      });
      menuItems.forEach(mainItem => {
        const mainItemChildrens = otherItems.filter( item => item.parent_category_id === mainItem.id).sort((a, b) => {
          if (a.name < b.name) return -1
          return 1  
        });;
        otherItems = otherItems.filter(item => item.parent_category_id !== mainItem.id);
        mainItemChildrens.forEach(item => {
          item.selected = false;
          item.filterPanel = false;
          item.mobileMenu = false;
          item.childrens = [];
        });
        mainItemChildrens.forEach(middleItem => {
          const lastChildrens = otherItems.filter( item => item.parent_category_id === middleItem.id).sort((a, b) => {
            if (a.name < b.name) return -1
            return 1  
          });;
          otherItems = otherItems.filter(item => item.parent_category_id !== middleItem.id);
          lastChildrens.forEach(item => {
            item.selected = false;
            item.filterPanel = false;
            item.mobileMenu = false;
            item.childrens = [];
          });
          middleItem.childrens = [...lastChildrens];
        })
        mainItem.childrens = [...mainItemChildrens];
      });
      catalog.value = menuItems;

    } catch (e) {
      console.log(e);
      // notificationsStore.addMessage(
      //   {name: "Не возможно обновить каталог товаров", icon: "error", id: '1'}
      // )
    }
  };

  const setAllCurrentCategories = (categoryState) => {
    const { mainCategory, middleCategory, lastCategory } = categoryState;
    const breadCrumbs = [ mainBreadCrumb ];
    if (mainCategory) {
      topCategoriesItemActive.value = mainCategory;
      const currCategory = categories.value.filter(item => item.id === mainCategory)[0];
      const currBreadCrumb  = {
        name: currCategory.name,
        path: '/category/' + currCategory.site_link,
        type: 'global',
        class: '',
        category: currCategory.id,
        level: 'top',
      };
      breadCrumbs.push(currBreadCrumb);
    } else {
      topCategoriesItemActive.value = null;
    }
    if (middleCategory) {
      subCategoriesItemActive.value = middleCategory;
      const currCategory = categories.value.filter(item => item.id === middleCategory)[0];
      const currBreadCrumb  = {
        name: currCategory.name,
        path: '/category/' + currCategory.site_link,
        type: 'global',
        class: '',
        category: currCategory.id,
        level: 'sub',
      };
      breadCrumbs.push(currBreadCrumb);
    } else {
      subCategoriesItemActive.value = null;
    }
    if (lastCategory) {
      lastCategoriesItemActive.value = lastCategory;
      const currCategory = categories.value.filter(item => item.id === lastCategory)[0]
      const currBreadCrumb  = {
        name: currCategory.name,
        path: '/category/' + currCategory.site_link,
        type: 'global',
        class: '',
        category: currCategory.id,
        level: 'last',
      };
      breadCrumbs.push(currBreadCrumb);
    } else {
      lastCategoriesItemActive.value = null;
    }
    breadcrumbStore.resetAllBreadCrumbs(breadCrumbs);
    setCatalogStateForFilterPanelToFalse();
  };

  const sendRequestCall = async (data) => {
    try {
      await axios.post('service_entities/request_calls', data);
      setPopUpAction('ShowCompleteMsg');
      const msg ={};
      msg.main = 'Наш менеджер свяжется с вами в ближайшее время.';
      msg.bolt = 'Время работы:';
      msg.sub = ' Пн-Пт - 9:00 - 17:00'
      setPopUpMessage(msg);
    } catch (e) {
      console.log(e);
      // notificationsStore.addMessage(
      //   {name: "Не возможно обновить каталог товаров", icon: "error", id: '1'}
      // )
      setPopUpMessage({});
      setIsPopUpOpen(false);
      setPopUpAction('');
    }
  };
  
  const sendRequestFeedback = async (data) => {
    try {
      await axios.post('service_entities/feedbacks', data);
      setPopUpAction('ShowCompleteMsg');
      const msg ={};
      msg.main = 'Наш менеджер свяжется с вами в ближайшее время.';
      msg.bolt = 'Время работы:';
      msg.sub = ' Пн-Пт - 9:00 - 17:00'
      setPopUpMessage(msg);
      setIsPopUpOpen(true);
    } catch (e) {
      console.log(e);
      // notificationsStore.addMessage(
      //   {name: "Не возможно обновить каталог товаров", icon: "error", id: '1'}
      // )
      setPopUpMessage({});
      setIsPopUpOpen(false);
      setPopUpAction('');
    }
  };


  return {
    isCatalogOpen,
    isMenuActionsOpen,
    topCategoriesItemActive,
    subCategoriesItemActive,
    lastCategoriesItemActive,
    windowWidth,
    viewType,
    categories,
    topCategories,
    subCategories,
    catalog,
    isPopUpOpen,
    popUpAction,
    popUpMessage,
    requestCallType,
    popUpAdditionalData,
    updateIsCatalogOpen,
    updateIsMenuActionsOpen,
    updateViewParameters,
    setIsPopUpOpen,
    setCurrentLastCategory,
    setPopUpAction,
    setPopUpMessage,
    setRequestCallType,
    setPopUpAdditionalData,
    getCategories, 
    setAllCurrentCategories,
    sendRequestCall,
    sendRequestFeedback,
  }
});
