import { ref } from 'vue';
import { defineStore } from 'pinia';
import { useHeaderStore } from '@/stores/header';
import { useQueryStore } from '@/stores/query';

const defaultRoute = {
    name: 'Главная',
    path: '/',
    type: 'global',
    class: '',
  }
  
export const useBreadCrumbStore = defineStore ('breadcrumbStore', () => {

  const headerStore = useHeaderStore();
  const queryStore = useQueryStore();

  const breadCrumbStack = ref([
    { ...defaultRoute }
  ]);

  const addBreadCrumb = (breadCrumb) => {
    breadCrumbStack.value.push(breadCrumb);
  }; // ADD_BREADCRUMB

  const changeBreadCrumb = (id) => {
    while (breadCrumbStack.value.length > id + 1){
      breadCrumbStack.value.splice(breadCrumbStack.value.length -1, 1);
    }
  }; // CHANGE_BREADCRUMB

  const renameLastBreadCrumb = (breadCrumb) => {
    if (breadCrumbStack.value.length - 1){
      breadCrumbStack.value[breadCrumbStack.value.length - 1].name = breadCrumb;
    }
  }; // RENAME_LAST_BREADCRUMB

  const resetAllBreadCrumbs = (breadCrumbs) => {
    const main = { ...defaultRoute };
    breadCrumbStack.value = [main, ...breadCrumbs];
  }; // RESET_ALL_BREADCRUMBS

  const moveToSelectPath = (element) => {
    const elementData = breadCrumbStack.value[element];
    if (elementData.type === 'global') {
      changeBreadCrumb(element);
    } else {
      const route = breadCrumbStack.value[element];
      if (route.level === 'root') {
        changeBreadCrumb(element);
        headerStore.setAllCurrentCategories({});
        queryStore.setCategoryID(null);
      } else if (route.level === 'top') {
        const data = { mainCategory: route.category};
        headerStore.setAllCurrentCategories(data);
        queryStore.setCategoryID(route.category);
      } else if (route.level === 'sub') {
        const data = { 
            mainCategory: breadCrumbStack.value[element - 1].category, 
            middleCategory: route.category, 
            lastCategory: null
        };
        headerStore.setAllCurrentCategories(data);
        queryStore.setCategoryID(route.category);
      } else if (route.level === 'last') {
        const data = { 
            mainCategory: breadCrumbStack.value[element - 2].category, 
            middleCategory: breadCrumbStack.value[element - 1].category, 
            lastCategory: route.category};
        headerStore.setAllCurrentCategories(data);
        queryStore.setCategoryID(route.category);
      }
    } 
  } // MOVE_TO_SELECT_PATH

  return {
    breadCrumbStack,
    addBreadCrumb,
    changeBreadCrumb,
    renameLastBreadCrumb,
    resetAllBreadCrumbs,
    moveToSelectPath,
  }  
});
