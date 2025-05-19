<template>
  <div class="breadcrumb__wrapper _container">
    <ul class="breadcrumb">
      <li
          v-for=" (element, index) in ELEMENTS"
          :key="element.id"
          :class="element.class"
      >
        <a class="breadcrumb__link"
            v-if="element.type !=='service'"
            :href="createHref(element)"
            @click.prevent="changePage(element)"
            :style = "[ ELEMENTS.length -1 === index ? 'color : #4275D8' : '']"
        >
          {{ element.name }}
        </a>
      </li>
    </ul>
  </div>
</template>

<script setup>
  import { computed } from 'vue';
  import { useQueryStore } from '@/stores/query';
  import { useBreadCrumbStore } from '@/stores/breadcrumb';

  const router = useRouter();
  const config = useRuntimeConfig();

  const queryStore = useQueryStore();
  const breadCrumbStore = useBreadCrumbStore();

  const { breadCrumbStack } = storeToRefs(breadCrumbStore);

  const ELEMENTS = computed(() => {
    if (breadCrumbStack.value.length > 1){
      let result = [];
      breadCrumbStack.value.forEach((item, i) => {
        let menuItem = {};
        menuItem.name = item.name;
        menuItem.path = item.path;
        menuItem.type = item.type;
        menuItem.class = item.class;
        menuItem.index = i;
        result.push(menuItem);
        if (i !== breadCrumbStack.value.length - 1){
          result.push({name: '', type: 'service', class: 'breadcrumb__separater icon-arrow-l'})
        }
      });
      return result;
    } else {
      return [];
    }
  });

  const breadcrumbList = computed(() => {
    let list = [];
    let position = 1;
    ELEMENTS.value.forEach(item => {
      if (item.type === 'global'){
        const breadcrumbItem = {};
        breadcrumbItem["@type"] = "ListItem"
        breadcrumbItem["position"] = position;
        const itemData = {};
        itemData["@id"] = config.public.NUXT_APP_DOCUMENTS.slice(0, -1) + item.path;
        itemData["name"] = item.name;
        breadcrumbItem["item"] = itemData;
        position++;
        list.push(breadcrumbItem);
      }
    });
    const data = {};
    data["@context"] = "http://schema.org";
    data["@type"] = "BreadcrumbList";
    data["itemListElement"] = list;
    // console.log('ELEMENTS ', ELEMENTS.value);
    return data;
  });

  const changePage = (item) => {
    // console.log('BreadCrumb-   ', item);
    let url = '';
    if (item.path.includes('category') || item.path.includes('catalog')) {
      // console.log('breadcrumb ', item);
      if (item.path.includes('catalog')) {
        queryStore.setCategoryID(null);
      }
      queryStore.setDefaultPrices();
      queryStore.setSearchString('');
      breadCrumbStore.moveToSelectPath(item.index);
      // console.log('Url   ', item.path + url, this);
      router.push(item.path + url);
    } else {
      queryStore.setSearchString('');
      breadCrumbStore.moveToSelectPath(item.index);
      router.push(item.path);
    }
  };

  const createHref = (item) => {
    let url = '';
    if (item.path.includes('category') || item.path.includes('catalog')) {
      url = url = item.path
    } else {
      url = url + item.path;
    }
    return url;
  };

  useHead({
    script: [{
      type: 'application/ld+json',
      children: JSON.stringify(breadcrumbList.value)
    }]
  }); 
</script>

<style lang="scss" scoped>


.active__breadcrumb {
  color: blue;
}
.breadcrumb{
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  padding: 20px 0 30px 0;
  @media (max-width: $md3+px){
    padding: 10px 0 10px 0;
  }

  &__wrapper{
    width: 100%;
    text-align: left;
  }

  li{
    white-space: nowrap;
    overflow: hidden;
    &:last-child{
      a{
        opacity: 0.5;
        cursor: auto;
        color: #423E48!important;
      }

    }
    a{
      font-weight: 300;
      font-size: 12px;
      line-height: 2;
      text-align: center;
      color: #423E48;
      cursor: pointer;
      @media (max-width: $md3+px){
        font-size: 10px;
      }
    }

  }
  .active{
    font-weight: 300;
    font-size: 12px;
    line-height: 16px;
    text-align: center;
    opacity: 0.5;

  }
  &__separater{
    font-size: 8px;
    margin: 0 12px;
  }

}
</style>
